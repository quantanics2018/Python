import zipfile

# List of files to zip
files_to_zip = ['child.html', 'resume.html']

# Create a new ZIP archive
with zipfile.ZipFile('my_archive.zip', 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)
