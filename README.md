# Drive Upload

This code uploads a whole directory into Google Drive.
Drive folder id can be found as the last part of the Google Drive Folder path:
e.g. from https://drive.google.com/drive/u/0/folders/aaab111ccc2222bbb the folder id is: aaab111ccc2222bbb

### Requirements:

pip install pydrive

### Usage:

python upload_to_drive.py --local_path 'directory_to_be_uploaded' --drive_folder_id 'drive_folder_id'
