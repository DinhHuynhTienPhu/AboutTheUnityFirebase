var http = require('http'); // Import Node.js core module
const jwt = require('jsonwebtoken');
const { readFileSync } = require('fs');
const { promisify } = require('util');
const { join } = require('path');
const request = require('request-promise-native');
const FormData = require('form-data');
const readFileAsync = promisify(readFileSync);

// Functions
async function getNewestRelease(projectNumber, appId, apiKey) {
    const baseUrl = "https://firebaseappdistribution.googleapis.com/v1/";
    const parent = `projects/${projectNumber}/apps/${appId}/releases`;
    const url = `${baseUrl}${parent}`;

    // Set up the headers with the API key for authorization
    const headers = {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
    };

    // Make the GET request
    const response = await request.get(url, { headers });

    // Parse the response JSON
    const responseJson = JSON.parse(response);
    console.log("************** Response after get newest release**************");
    console.log(responseJson);

    // Check if there are releases in the response
    if ("releases" in responseJson && responseJson["releases"].length > 0) {
        // Get the newest release (assuming releases are sorted by createTime)
        const newestRelease = responseJson["releases"][0];
        return newestRelease;
    } else {
        console.log("No releases found.");
        return null;
    }
}

async function waitTime(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

var server = http.createServer(function (req, res) {   //create web server
    if (req.url == '/') { //check the URL of the current request
        
        // set response header
        res.writeHead(200, { 'Content-Type': 'text/html' });
        
        // set response content    
        res.write('<html><body><p>This is home Page.</p></body></html>');
        res.end();
    
    }
    else if (req.url == "/upload") {
        //user upload an apk file
        //push this apk file to the firebase storage
        try {
            console.log("validating the apk file");
            var file = req.body
            //validate the apk file
            if (file == null) {
                res.end("No file uploaded");
                console.log("No file uploaded");
                return;
            }

            res.write('We are sending it using the server, please check it at the firebase dashboard');
            res.end();
            var my_access_token = "";


            // Main Code
            const now = Math.floor(new Date().getTime() / 1000);
            const exp = now + 1800; // 30 minutes expiration

            console.log(`************* Code started at: ${new Date().toISOString()} *************`);
            console.log("************* UTC time *************");
            console.log(`************* now: ${now} *************`);
            console.log("************* ************* *************\n\n");

            // Replace these values with your own
            const projectNumber = "435559015716";
            const appId = "1:435559015716:android:4685417c5470cc7dfebfb1";
            const path = "D:/NotImportantProjects/tic tac toe/test.apk";

            const uploadFileName = "test.apk";
            const testerConfig = {
                testerEmails: ["ff10111011@gmail.com"],
                groupAliases: ["testers"],
            };

            console.log("************* Values *************");
            console.log(`************* project number ${projectNumber} app id: ${appId} *************\n\n`);
            console.log(`************* Path: ${path} *************`);
            console.log(`************* upload file name: ${uploadFileName} *************`);
            console.log(`************* tester config: ${JSON.stringify(testerConfig)} *************`);
            console.log("************* ************* *************\n\n");

            const values = {
                type: "service_account",
                project_id: "tic-tac-toe-49a04",
                private_key_id: "8e06c60b923960e319dc7eb24ece757139d897f4",
                private_key: `-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCz8mX2easUuFid\nGdJ/bEldErNNNtdnaRzr76J2eRHKl3zs5n8ZPg2FUL/A1QZl2p53bGgwI37/PRIk\nCrLOlg0/jTj7Y4IYSFdATOIjwT2Y3s6oWQZWn42RgUp/NKeetCl5KcwdyUZC1wXQ\nhUmhCr4CJ75H2geji9H/dazDjWsICdEE9RhifSladsX/3j/tNYL3fi+srFlSdIFX\noNUPFZvhnupfeqAI17kY9jtHr5pfJGnxv0LkNFVl2vrzTN/ZbIrxi2bedoYZkk7w\nRb8qE4R47ElVm/T00YOfcY3UXOCrU81cRwtb3kRKfvsRblZmV5BMbCnFKfGLH2W9\nC1Sqoe2TAgMBAAECggEAE83U+ZVWW3IWaTkoTixwE+A0/4XORcFEakBLVFfqugMw\nv9nLmc7sf1mYYPPmP7DEc/GTCIk/jCj/0BulUNB5e3RiwGKpNLGcI1AoKzXfPkMh\n4gE6OK+tTZrkb1ovgGs6N+1+W2DawgxsGruF6PAHuAZWY2NUJ+RWzj34hOURfHwj\nYvRmMkaQNqRj2pr8vghxxLX0yvRuM2KpMH1ysZSivwsgIct56256lELOLOKk1RPS\ndEor/W679z+LtDND19odxltmKLupqRPT5DerU4QNTf++UEQyUtW1+wjwJSiksOoK\nCpT7Kxd5jP20H8oPD8scGh+WOc/0SLmGr0s/IIA7sQKBgQDm6q8i2Mr+xaUe3I/k\npKSmXgeCzsWcJc4PHohsizBN6bZd6d/fWurTiTdbCdQLQ4LbIGFbZKdfhulOR8ny\nyZHcxZRWZZh83tLvVlHuCer4LQhaF439//OiD7GQn7hZSmMFaNLhwFbvIpkvmQDK\nhJzwD5J6jwkXF61jJB33rM2+hQKBgQDHflkJiDOy5zBaxMsmXM1ZWi1jROHxHoRa\nNmYerTvHIS36kt1fHLJzdduD5kdlqXA3JVhPY4heIGkiWbl9Ph1xvuN6PKdWyolX\nmhwnPLeIUcTIvm1HOp8Nkfcafu/x9+b/lQeJ7uolddHU7fmARNfmTf4ioflDZE7w\ntBHuDIuzNwKBgQDEJMynGOc1CcV8NXW0jXWeK3jNz71jKWmixhizundJdyAFHcef\n/aZCEOgIWIzZFHtujk6kRxc0uXAroicUJ8vSb7HUwW+JgexCiFwHij0gmX/ipudh\nvavBGPuHEWSR0/HQgn2+bJZrgkQEfj6Bx6tW7qNJn33lM6N/9wnNe+c30QKBgGWS\nVxMbXfdA7sXIXQbzSTqtR167u65gs1KbT/NekIkaw6ZJEJ1UpydSYqoNnVyNoKzz\nPrttGgmSxvTOajryXVuErZ2XNDxkcvk/ZgY0S94EhAURr+IMXt8x6nZ7GwBAEEUh\nQ+1ez6izDFs1r0s3whVosHRBtAA0Gl1D0b06dgaRAoGAaW/wX+ApsQUU3SKscLEe\nfLDTc1a5P6cylPqI+/zxsiWu1aPwsDH02nJhrnhBX5cGH6hAEGx7rbbKhOWPJ4Fi\nVPtG6IHipq2SFDCFDea/AeaX7UCEooUSJMwkU5NAB5md2roOLTbat54wvu6P9LQ4\nShyoLQfWVBYpaFF4W2RPozk=\n-----END PRIVATE KEY-----\n`,
                client_email: "phu3-567@tic-tac-toe-49a04.iam.gserviceaccount.com",
            };

            console.log("************* Generated JWT Token *************");
            const jwtToken = jwt.sign(
                {
                    iss: values.client_email,
                    sub: values.client_email,
                    scope: "https://www.googleapis.com/auth/cloud-platform",
                    aud: "https://www.googleapis.com/oauth2/v4/token",
                    iat: now,
                    exp: exp,
                },
                values.private_key,
                { algorithm: "RS256" }
            );
            console.log(jwtToken);
            console.log("************* ******************* *************\n\n");

            // Get access token
            const tokenEndpoint = "https://oauth2.googleapis.com/token";
            const tokenData = {
                grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                assertion: jwtToken,
            };

            // Make the HTTPS POST request
            request.post(tokenEndpoint, { form: tokenData })
                .then(response => {
                    const { access_token, expires_in, token_type } = JSON.parse(response);

                    console.log("************** Access Token **************");
                    console.log(`Access Token: ${access_token}`);
                    console.log(`Expires In: ${expires_in} seconds`);
                    console.log("*************** **************** ***************\n\n");
                    my_access_token = access_token;

                    // Upload the APK file
                    const urlFirebase = `https://firebaseappdistribution.googleapis.com/upload/v1/projects/${projectNumber}/apps/${appId}/releases:upload`;
                    const uploadHeaders = {
                        Authorization: `Bearer ${access_token}`,
                        'X-Goog-Upload-File-Name': "test.apk",
                        'X-Goog-Upload-Protocol': 'raw',
                        'Content-Type': 'application/vnd.android.package-archive',
                    };

                    //var file = readFileSync(path)

                    console.log(`************** Trying to upload file from path: ${path} **************`);

                    return request.post({
                        url: urlFirebase,
                        headers: uploadHeaders,
                        body: file,
                    });
                })
                .then(response => {
                    console.log("************** Response after upload**************");
                    console.log(response);
                    console.log("************** **************** **************");

                    //try return apk to client
                    // var thefile = readFileSync(path);
                    // res.writeHead(200, { 'Content-Type': 'application/vnd.android.package-archive' });
                    // res.write(thefile);
                    // res.end();

                    //wait for 50s to make sure the apk file is uploaded to firebase storage
                    console.log("************** Waiting for 10s **************");
                    waitTime(10000).then(() => {

                
                        // Add tester


                        if (response.includes('"name": "projects/')) {
                            console.log("************* Getting information about release ************");

                            // Add tester
                            getNewestRelease(projectNumber, appId, my_access_token)
                                .then(newestRelease => {
                                    console.log("************** Newest release **************");
                                    console.log(newestRelease);
                                    console.log("************** **************** **************\n\n");

                                    const releaseName = newestRelease.name;
                                    const releaseId = releaseName.split("/").pop();

                                    // Constructing the URL: https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute
                                    const distributeUrl = `https://firebaseappdistribution.googleapis.com/v1/${releaseName}:distribute`;

                                    const distributeHeaders = {
                                        Authorization: `Bearer ${my_access_token}`,
                                        'Content-Type': 'application/json',
                                        Accept: 'application/json',
                                    };

                                    const distributeBody = testerConfig;

                                    console.log("************** Trying to add tester **************");

                                    return request.post({
                                        url: distributeUrl,
                                        headers: distributeHeaders,
                                        json: distributeBody,
                                    });
                                })
                                .then(response => {
                                    console.log("************** Response after add tester**************");
                                    console.log(response);
                                    console.log("************** Finish **************");
                                })
                                .catch(error => console.error(error));
                        }
                    });
                })
                .catch(error => console.error(`Error: ${error}`))
                .finally(() => {
                    console.log(`************* Code finish at: ${new Date().toISOString()} *************`);
                    console.log("************* UTC time *************");
                    console.log(`************* now: ${Math.floor(new Date().getTime() / 1000)} *************`);
                    console.log("************* ************* *************\n\n");
                    // press enter to exit
                    process.stdin.resume();
                    process.stdin.setEncoding('utf8');
                    process.stdin.on('data', function () {
                        process.exit();
                    });
                });

        }
        catch (err) {
            console.log(err);
            res.end("Error: " + err);
        }
    }
    
    else
        res.end('Invalid Request!');
    

});

server.listen(5000); //6 - listen for any incoming requests

console.log('Node.js web server at port 5000 is running..')
