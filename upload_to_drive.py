import argparse

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)


def create_folder(drive, folder_name, parent_folder_id):
    """Creates folder on Google Drive"""
    folder_metadata = {
        'title': folder_name,                
        # Define the file type as folder
        'mimeType': 'application/vnd.google-apps.folder',
        # ID of the parent folder
        'parents': [{"kind": "drive#fileLink", "id": parent_folder_id}]
    }

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    print('created title: %s, id: %s' % (folder['title'], folder['id']))
    return folder['id']


def upload_all(path, folder_id):
    """Recursive function to upload the whole directory tree starting from the path"""
    upload_file_list = os.listdir(path)  # both folders and files
    for upload_file in upload_file_list:
        full_path = os.path.join(path, upload_file)
        if os.path.isdir(full_path):
            print("{} is a directory, creating it.".format(full_path))
            child_id = create_folder(drive, upload_file, folder_id)
            upload_all(full_path, child_id)
            continue
        gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title': upload_file})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(full_path)
        gfile.Upload()  # Upload the file.


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local_path",
        action='store',
        type=str,
        help="the folder path to upload to drive"
    )
    parser.add_argument(
        "--drive_folder_id",
        action='store',
        type=str,
        help="the folder id in drive"
    )
    args = parser.parse_args()
    upload_all(args.local_path, args.drive_folder_id)


if __name__ == "__main__":
    main()
