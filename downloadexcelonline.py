from google.oauth2 import service_account
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload

SERVICE_ACCOUNT_FILE = 'caminho da chave .json'

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)

def export_and_download_file(file_id, mime_type, destination_file_name):
    try:
        request = service.files().export_media(fileId=file_id, mimeType=mime_type)
        fh = io.FileIO(destination_file_name, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f'Download Progress: {int(status.progress() * 100)}%')
        print(f'Download Complete: {destination_file_name}')
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    file_id = '1Kgomn2uhzQBnJQfO6J9Qhpyze7tT7RuNUk-1zLOx7zM' <id do arquivo>
    mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    destination_file_name = 'C:\\Users\\thorodin\\Downloads\\arquivo.xlsx'
    export_and_download_file(file_id, mime_type, destination_file_name)

if __name__ == '__main__':
    main()
