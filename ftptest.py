from ftplib import FTP
from tqdm import tqdm

# FTP server details
ftp_host = "ftp.myrient.erista.me"
ftp_user = ""
ftp_passwd = ""

def list_files(ftp):
    # List only the files in the current directory
    files = []
    ftp.retrlines('NLST', files.append)
    for filename in files:
        print(filename)
        
def find_file(ftp, file):
    # List only the files in the current directory
    files = []
    ftp.retrlines('NLST', files.append)
    for filename in files:
        if file in filename:
            return filename
    return None

def download_file(ftp, filename):
    # Get the file size
    file_size = ftp.size(filename)

    # Download the file with progress bar
    with open(filename, 'wb') as file:
        with tqdm(total=file_size, unit='B', unit_scale=True) as progress_bar:
            def callback(data):
                file.write(data)
                progress_bar.update(len(data))

            ftp.retrbinary('RETR ' + filename, callback)

    print(f"File '{filename}' downloaded successfully.")


# Connect to the FTP server
ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_passwd)

ftp.cwd('Redump')
ftp.cwd('Microsoft - Xbox 360')

# List the files in the directory
print("Files in the directory:")
#list_files(ftp)
file = find_file(ftp, 'Zumba Fitness (USA).zip')

if file:
    download_file(ftp, file)

# Close the FTP connection
ftp.quit()
