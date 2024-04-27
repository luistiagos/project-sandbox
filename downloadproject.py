import shutil

# Specify the folder you want to archive
folder_to_archive = 'https://www.pythonanywhere.com/user/digitalstoregames/files/home/digitalstoregames'

# Specify the name for the ZIP file
zip_filename = 'archive.zip'

# Create a ZIP archive of the folder
shutil.make_archive(zip_filename, 'zip', folder_to_archive)

print(f'ZIP archive created: {zip_filename}')
