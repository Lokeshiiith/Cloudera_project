import os
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def get_url_paths(url, ext=''):
    response = requests.get(url, auth=HTTPBasicAuth('sharmameritnation@gmail.com', '7g6RTQgQ'))
    if response.ok:
        response_text = response.text
    else:
        response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

def download_files(url, folder_name):
    ext = '.gz'
    result = get_url_paths(url, ext)
    total_files = len(result)
    print(f"Total {total_files} files found to download from {url}.")

    confirmation = input("Do you want to continue downloading? It will take hours by this dataset(yes/no): ").strip().lower()

    if confirmation in ['yes', 'y']:
        # Create a directory to save the files
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for file in result:
            f_name = file[-12:-4]  # Assuming the file name pattern remains the same
            r = requests.get(file, auth=HTTPBasicAuth('sharmameritnation@gmail.com', '7g6RTQgQ'))
            if r.status_code == 200:
                with open(f'./{folder_name}/{f_name}.gz', 'wb') as f:
                    f.write(r.content)
                print(f"Downloaded: {f_name}.gz")
            else:
                print(f"Failed to download: {f_name}.gz")
    else:
        print("Download canceled.")

def main():
    url1 = 'http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1101/APHRO_MA/025deg_nc/'
    url2 = 'http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1101EX_R1/APHRO_MA/025deg_nc/'
    url3 = 'http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1808_TEMP/APHRO_MA/025deg_nc/'

    download_files(url1, 'Precipitation')
    download_files(url2, 'Precipitation')
    download_files(url3, 'Temperature')

if __name__ == "__main__":
    main()
