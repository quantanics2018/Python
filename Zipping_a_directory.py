import zipfile
import shutil
import os

# Directory to zip
directory_to_zip = 'F:\basicjava'

# Create a new ZIP archive
with zipfile.ZipFile('my_directory.zip', 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(directory_to_zip):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, directory_to_zip)
            zipf.write(file_path, arcname)
