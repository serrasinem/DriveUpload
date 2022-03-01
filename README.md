# Drive Upload

This code uploads a whole directory into Google Drive.
Drive folder id can be found as the last part of the Google Drive Folder path:
e.g. from https://drive.google.com/drive/u/0/folders/aaab111ccc2222bbb the folder id is: aaab111ccc2222bbb

### Requirements:

pip install pydrive

Drive API requires OAuth2.0 to authenticate.

Simply fill client id and client secret in settings.yaml file. Then call python authenticate.py . It will create the credentials.json file. Then you are good to go.

To get your client id and secret https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid
Steps:

1- Go to https://console.cloud.google.com/apis

2- Create a project

3- Enable Google Drive API for the project

4- Select Credentials from the left menu and create OAuth client ID

5- Optional: Download the credentials.json file, put it in the same folder

extra links:

Follow the steps of authentication: https://pythonhosted.org/PyDrive/quickstart.html#authentication

for remote machine: https://pythonhosted.org/PyDrive/oauth.html


### Usage:

python upload_to_drive.py --local_path 'directory_to_be_uploaded' --drive_folder_id 'drive_folder_id'
