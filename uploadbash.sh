#!/bin/bash

# Firebase Configurations
FIREBASE_PROJECT_ID="tic-tac-toe-49a04"

# Firebase Authentication
FIREBASE_EMAIL="phu3-567@tic-tac-toe-49a04.iam.gserviceaccount.com"  # Replace with your actual Firebase email

# APK Information
APK_FILE_PATH="D:/NotImportantProjects/tic tac toe/test.apk"
APK_UPLOAD_FILENAME="test.apk"

# JWT Configurations
FIREBASE_JWT_AUDIENCE="https://www.googleapis.com/oauth2/v4/token"
FIREBASE_JWT_ISSUER="tic-tac-toe-49a04"
FIREBASE_JWT_EXPIRATION=3600  # 1 hour expiration

# Tester Configuration
TESTER_EMAIL="ff10111011@gmail.com"
TESTER_GROUP_ALIAS="testers"

# Private Key
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCz8mX2easUuFid\nGdJ/bEldErNNNtdnaRzr76J2eRHKl3zs5n8ZPg2FUL/A1QZl2p53bGgwI37/PRIk\nCrLOlg0/jTj7Y4IYSFdATOIjwT2Y3s6oWQZWn42RgUp/NKeetCl5KcwdyUZC1wXQ\nhUmhCr4CJ75H2geji9H/dazDjWsICdEE9RhifSladsX/3j/tNYL3fi+srFlSdIFX\noNUPFZvhnupfeqAI17kY9jtHr5pfJGnxv0LkNFVl2vrzTN/ZbIrxi2bedoYZkk7w\nRb8qE4R47ElVm/T00YOfcY3UXOCrU81cRwtb3kRKfvsRblZmV5BMbCnFKfGLH2W9\nC1Sqoe2TAgMBAAECggEAE83U+ZVWW3IWaTkoTixwE+A0/4XORcFEakBLVFfqugMw\nv9nLmc7sf1mYYPPmP7DEc/GTCIk/jCj/0BulUNB5e3RiwGKpNLGcI1AoKzXfPkMh\n4gE6OK+tTZrkb1ovgGs6N+1+W2DawgxsGruF6PAHuAZWY2NUJ+RWzj34hOURfHwj\nYvRmMkaQNqRj2pr8vghxxLX0yvRuM2KpMH1ysZSivwsgIct56256lELOLOKk1RPS\ndEor/W679z+LtDND19odxltmKLupqRPT5DerU4QNTf++UEQyUtW1+wjwJSiksOoK\nCpT7Kxd5jP20H8oPD8scGh+WOc/0SLmGr0s/IIA7sQKBgQDm6q8i2Mr+xaUe3I/k\npKSmXgeCzsWcJc4PHohsizBN6bZd6d/fWurTiTdbCdQLQ4LbIGFbZKdfhulOR8ny\nyZHcxZRWZZh83tLvVlHuCer4LQhaF439//OiD7GQn7hZSmMFaNLhwFbvIpkvmQDK\nhJzwD5J6jwkXF61jJB33rM2+hQKBgQDHflkJiDOy5zBaxMsmXM1ZWi1jROHxHoRa\nNmYerTvHIS36kt1fHLJzdduD5kdlqXA3JVhPY4heIGkiWbl9Ph1xvuN6PKdWyolX\nmhwnPLeIUcTIvm1HOp8Nkfcafu/x9+b/lQeJ7uolddHU7fmARNfmTf4ioflDZE7w\ntBHuDIuzNwKBgQDEJMynGOc1CcV8NXW0jXWeK3jNz71jKWmixhizundJdyAFHcef\n/aZCEOgIWIzZFHtujk6kRxc0uXAroicUJ8vSb7HUwW+JgexCiFwHij0gmX/ipudh\nvavBGPuHEWSR0/HQgn2+bJZrgkQEfj6Bx6tW7qNJn33lM6N/9wnNe+c30QKBgGWS\nVxMbXfdA7sXIXQbzSTqtR167u65gs1KbT/NekIkaw6ZJEJ1UpydSYqoNnVyNoKzz\nPrttGgmSxvTOajryXVuErZ2XNDxkcvk/ZgY0S94EhAURr+IMXt8x6nZ7GwBAEEUh\nQ+1ez6izDFs1r0s3whVosHRBtAA0Gl1D0b06dgaRAoGAaW/wX+ApsQUU3SKscLEe\nfLDTc1a5P6cylPqI+/zxsiWu1aPwsDH02nJhrnhBX5cGH6hAEGx7rbbKhOWPJ4Fi\nVPtG6IHipq2SFDCFDea/AeaX7UCEooUSJMwkU5NAB5md2roOLTbat54wvu6P9LQ4\nShyoLQfWVBYpaFF4W2RPozk=\n-----END PRIVATE KEY-----\n"

# Firebase App Distribution URL
FIREBASE_APP_DISTRIBUTION_URL="https://firebaseappdistribution.googleapis.com/upload/v1/projects/${project_number}/apps/${app_id}/releases:upload"

# Log function for displaying messages
log() {
  echo "[INFO] $1"
}

# Generate JWT
generate_jwt() {
  log "Generating JWT..."
  
  local header='{"alg":"RS256","typ":"JWT"}'
  local now=$(date +%s)
  local exp=$((now + FIREBASE_JWT_EXPIRATION))

  local claim='{
    "iss": "'${FIREBASE_JWT_ISSUER}'",
    "sub": "'${FIREBASE_EMAIL}'",
    "aud": "'${FIREBASE_JWT_AUDIENCE}'",
    "iat": '$now',
    "exp": '$exp'
  }'

  local header_base64=$(echo -n "$header" | base64 | tr -d '\n=' | tr -d '\r')
  local claim_base64=$(echo -n "$claim" | base64 | tr -d '\n=' | tr -d '\r')

  local jwt="$header_base64.$claim_base64"

  local signature=$(echo -n "$jwt" | openssl dgst -sha256 -sign <(echo -n "$PRIVATE_KEY") -binary | base64 | tr -d '\n=' | tr -d '\r') 
  echo "$jwt.$signature"
}

# Get Firebase Access Token
get_access_token() {
  log "Getting Firebase Access Token..."
  
  local jwt=$(generate_jwt)
  #log the jwt
    log "JWT: $jwt"
  

  local response=$(curl -s -X POST \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer" \
    --data-urlencode "assertion=$jwt" \
    "https://www.googleapis.com/oauth2/v4/token")

  echo $(echo "$response" | jq -r '.access_token')
}

# Push APK to Firebase
push_apk_to_firebase() {
  log "Pushing APK to Firebase..."
  
  local access_token=$(get_access_token)
  #log the access token
  log "Access Token: $access_token"

  local response=$(curl -s -X POST \
    -H "Content-Type: application/octet-stream" \
    -H "Authorization: Bearer $access_token" \
    --data-binary "@$APK_FILE_PATH" \
    "$FIREBASE_APP_DISTRIBUTION_URL")

  echo "$response"
}

# Get Release Information and Assign Testers
get_release_info_and_assign_testers() {
  log "Getting Release Information and Assigning Testers..."
  
  local access_token=$(get_access_token)

  local response=$(curl -s -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $access_token" \
    --data '{"appId":"your-firebase-app-id"}' \
    "https://appdistribution.firebase.dev/app-pre-release-info")

  # Extract release information or perform actions with the response
  echo "$response"
}

# Execute the functions
push_apk_to_firebase
get_release_info_and_assign_testers
