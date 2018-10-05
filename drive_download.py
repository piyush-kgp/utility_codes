import requests
import argparse

def download_file_from_google_drive(file_id, destination):    
    URL = "https://drive.google.com/uc?export=download"    
    session = requests.Session()    
    response = session.get(URL, params = { 'id' : file_id }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : file_id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                print(chunk)
                f.write(chunk)

def main()                
    parser = argparse.ArgumentParser()
    parser.add_argument('file_id', default = '1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz', help='Google Drive File ID')
    parser.add_argument('file_name', default = 'x.zip', help='File Name to Save')
    args = parser.parse_args()
    file_id = args.file_id
    download_file_from_google_drive(file_id, file_name )

if __name__=='__main__':
    main()
