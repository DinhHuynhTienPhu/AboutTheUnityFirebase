import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta,timezone    
import requests
import time

#functions

def get_newest_release(project_number, app_id, api_key):
    base_url = "https://firebaseappdistribution.googleapis.com/v1/"
    parent = f"projects/{project_number}/apps/{app_id}/releases"
    url = f"{base_url}{parent}"

    # Set up the headers with the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()

        # Check if there are releases in the response
        if "releases" in response_json and response_json["releases"]:
            # Get the newest release (assuming releases are sorted by createTime)
            newest_release = response_json["releases"][0]

            return newest_release
        else:
            print("No releases found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    return None













#main code



now =int(datetime.now(tz=timezone.utc).timestamp() )
# #exp in 30 minutes
exp = int((datetime.now(tz=timezone.utc) + timedelta(minutes=30)).timestamp() )

print("************* Code started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "*************")
print("************* UTC time *************")
print("************* now:", now, "*************")
print("************* ************* *************\n\n")


#the valuse is from the service account key json file downloaded from google 
#read more at: https://developers.google.com/identity/protocols/oauth2/service-account#httprest
values={
  "type": "service_account",
  "project_id": "tic-tac-toe-49a04",
  "private_key_id": "8e06c60b923960e319dc7eb24ece757139d897f4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCz8mX2easUuFid\nGdJ/bEldErNNNtdnaRzr76J2eRHKl3zs5n8ZPg2FUL/A1QZl2p53bGgwI37/PRIk\nCrLOlg0/jTj7Y4IYSFdATOIjwT2Y3s6oWQZWn42RgUp/NKeetCl5KcwdyUZC1wXQ\nhUmhCr4CJ75H2geji9H/dazDjWsICdEE9RhifSladsX/3j/tNYL3fi+srFlSdIFX\noNUPFZvhnupfeqAI17kY9jtHr5pfJGnxv0LkNFVl2vrzTN/ZbIrxi2bedoYZkk7w\nRb8qE4R47ElVm/T00YOfcY3UXOCrU81cRwtb3kRKfvsRblZmV5BMbCnFKfGLH2W9\nC1Sqoe2TAgMBAAECggEAE83U+ZVWW3IWaTkoTixwE+A0/4XORcFEakBLVFfqugMw\nv9nLmc7sf1mYYPPmP7DEc/GTCIk/jCj/0BulUNB5e3RiwGKpNLGcI1AoKzXfPkMh\n4gE6OK+tTZrkb1ovgGs6N+1+W2DawgxsGruF6PAHuAZWY2NUJ+RWzj34hOURfHwj\nYvRmMkaQNqRj2pr8vghxxLX0yvRuM2KpMH1ysZSivwsgIct56256lELOLOKk1RPS\ndEor/W679z+LtDND19odxltmKLupqRPT5DerU4QNTf++UEQyUtW1+wjwJSiksOoK\nCpT7Kxd5jP20H8oPD8scGh+WOc/0SLmGr0s/IIA7sQKBgQDm6q8i2Mr+xaUe3I/k\npKSmXgeCzsWcJc4PHohsizBN6bZd6d/fWurTiTdbCdQLQ4LbIGFbZKdfhulOR8ny\nyZHcxZRWZZh83tLvVlHuCer4LQhaF439//OiD7GQn7hZSmMFaNLhwFbvIpkvmQDK\nhJzwD5J6jwkXF61jJB33rM2+hQKBgQDHflkJiDOy5zBaxMsmXM1ZWi1jROHxHoRa\nNmYerTvHIS36kt1fHLJzdduD5kdlqXA3JVhPY4heIGkiWbl9Ph1xvuN6PKdWyolX\nmhwnPLeIUcTIvm1HOp8Nkfcafu/x9+b/lQeJ7uolddHU7fmARNfmTf4ioflDZE7w\ntBHuDIuzNwKBgQDEJMynGOc1CcV8NXW0jXWeK3jNz71jKWmixhizundJdyAFHcef\n/aZCEOgIWIzZFHtujk6kRxc0uXAroicUJ8vSb7HUwW+JgexCiFwHij0gmX/ipudh\nvavBGPuHEWSR0/HQgn2+bJZrgkQEfj6Bx6tW7qNJn33lM6N/9wnNe+c30QKBgGWS\nVxMbXfdA7sXIXQbzSTqtR167u65gs1KbT/NekIkaw6ZJEJ1UpydSYqoNnVyNoKzz\nPrttGgmSxvTOajryXVuErZ2XNDxkcvk/ZgY0S94EhAURr+IMXt8x6nZ7GwBAEEUh\nQ+1ez6izDFs1r0s3whVosHRBtAA0Gl1D0b06dgaRAoGAaW/wX+ApsQUU3SKscLEe\nfLDTc1a5P6cylPqI+/zxsiWu1aPwsDH02nJhrnhBX5cGH6hAEGx7rbbKhOWPJ4Fi\nVPtG6IHipq2SFDCFDea/AeaX7UCEooUSJMwkU5NAB5md2roOLTbat54wvu6P9LQ4\nShyoLQfWVBYpaFF4W2RPozk=\n-----END PRIVATE KEY-----\n",
  "client_email": "phu3-567@tic-tac-toe-49a04.iam.gserviceaccount.com",
  "client_id": "111516119995493046907",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/phu3-567%40tic-tac-toe-49a04.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

#you must change the values below to your own values
project_number = "435559015716"
app_id = "1:435559015716:android:4685417c5470cc7dfebfb1"
path = "D:/NotImportantProjects/tic tac toe/test.apk"
uploadFileName = "test.apk"
testerConfig ={
  "testerEmails": [
    "ff10111011@gmail.com"
  ],
  "groupAliases": [
    "testers"
  ]
}

print("************* Values *************")
print("*************json file from google: ",values)
print("************* project number", project_number, " app id: ", app_id, "*************\n\n")
print("************* Path: ", path, "*************")
print("************* upload file name: ", uploadFileName, "*************")
print("************* tester config: ", testerConfig, "*************")
print("************* ************* *************\n\n")




# now = int(time.time()) 
# exp = now + 3500

# Your claim set and header remain the same...
claim_set = {
    "iss": values['client_email'],
    "sub": values['client_email'],
    "scope": "https://www.googleapis.com/auth/cloud-platform",
    "aud": "https://www.googleapis.com/oauth2/v4/token",
    "iat": now,
    "exp": exp,
}

header = {"alg": "RS256", "typ": "JWT"}
private_key = values['private_key']

# Load private key using cryptography library...
private_key_obj = serialization.load_pem_private_key(
    private_key.encode(), password=None, backend=default_backend()
)

# Encode JWT...
jwt_token = "eyJhbGciOiAiUlMyNTYiLCJ0eXAiOiAiSldUIn0.eyJpc3MiOiAicGh1My01NjdAdGljLXRhYy10b2UtNDlhMDQuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiAicGh1My01NjdAdGljLXRhYy10b2UtNDlhMDQuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzY29wZSI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9hdXRoL2Nsb3VkLXBsYXRmb3JtIiwiYXVkIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92NC90b2tlbiIsImlhdCI6ICIxNzA2NTA4NTAyIiwiZXhwIjogIjE3MDY1MTAzMDIifQ.fPGkDz7ufecr-ze3OEvZ-JgY6-hdAJMAqPRiLuXMa-mIFxpGEhB_9MmS40npzUxr0SLQLyoNVmTqldBQaUbP6sw5gHdyeEWjxl7cRs5Ef_quTx93XTtq58Z425BFTGwmRhSdpeCYMvw3GRRI4jxbSVk7X8F9gCF5Xli3F3qaYhg39iGgLPaJ-sG5QFjp3e9L2MlPLcd0dxkdN3AsgnxqvWifB7ityR7yN9Aii-fumcrx3HvyroBqHy7o_eN7uBTE7QnIkxrQG0GLPV8hXnr5KTTlgrvtIbKiqQSi2JFxUN3NnaHlWQoDUi8s2YRv3jH3WHWHoMiN8jAJxMt3B3NdCQ"

print("************* Generated JWT Token *************")
print(jwt_token)
print("************* ******************* *************\n\n")

# stop the screen to read the output

token_endpoint = "https://oauth2.googleapis.com/token"

# Prepare the data for the POST request
data = {
    'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion': jwt_token
}

# Make the HTTPS POST request
response = requests.post(token_endpoint, data=data)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse and print the response JSON
    response_json = response.json()
    #print(response_json)
    access_token = response_json.get('access_token')
    expires_in = response_json.get('expires_in')
    token_type = response_json.get('token_type')

    print("************** Access Token **************")
    print(f"Access Token: {access_token}")
    print("\n")
    print(f"Expires In: {expires_in} seconds")

    # 3 line empty space
    # print("\n\n\n")
    # print("Access Token: " + access_token)
    print("*************** **************** ***************\n\n")

else:
    # Print the error message if the request was not successful
    print(f"Error {response.status_code}: {response.text}")


#then push the apk file 

urlfirebase = f"https://firebaseappdistribution.googleapis.com/upload/v1/projects/{project_number}/apps/{app_id}/releases:upload"

headers = {
    "Authorization": "Bearer " + access_token,
    "X-Goog-Upload-File-Name": uploadFileName,
    "X-Goog-Upload-Protocol": "raw",
}
#path = D:\NotImportantProjects\tic tac toe\test.apk

body = open(path, "rb").read()
print("************** trying to upload file form path: ", path, "**************")

response = requests.post(urlfirebase, headers=headers, data=body)
print("************** Response after upload**************")
print(response.text)
print("************** **************** **************")
# press enter to continue

# if response.text inclue ""name": "projects/435559015716/apps"
# start to add tester

if response.text.find("name") != -1:
    print("************* getting infor about release ************")
    # add tester

    #the result text will be like this: "name": "projects/435559015716/apps/1:435559015716:android:4685417c5470cc7dfebfb1/releases/-/operations/6f8d5b22d6db3c3594dab1432c2958d3a4563f922ce4f0305c874ef57168275e"
   #url =POST https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute

    result_code = response.text;
    
    #get newest release id
    newest_release = get_newest_release(project_number, app_id, access_token)
    print("************** newest release **************")
    print("", newest_release)
    print("************** **************** **************\n\n")
    release_name = newest_release["name"]
    #name has this format: projects/{projectNumber}/apps/{appId}/releases/{releaseId}
    #split the name to get the release id
    release_id = release_name.split("/")[-1]

    # Constructing the URL: https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*}:distribute
    url = f"https://firebaseappdistribution.googleapis.com/v1/{release_name}:distribute"
    urlfirebase = url
    

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    body = testerConfig
    print ("************** trying to add tester **************")

    response = requests.post(urlfirebase, headers=headers, json=body)
    print("************** Response after add tester**************")
    print(response.text)
    print("************** Finish **************")

print("************* Code finish at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "*************")
print("************* UTC time *************")
print("************* now:", int(datetime.now(tz=timezone.utc).timestamp() )  , "*************")
print("************* ************* *************\n\n")
    # press enter to exit
input()








