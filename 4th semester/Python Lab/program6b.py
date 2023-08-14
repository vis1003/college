import os
from zipfile import ZipFile

folder = input("Enter folder name to be zipped : ")
myzip = folder + '.zip'
with ZipFile(myzip, 'w') as zip_object:
    for folder_name, sub_folders, file_names in os.walk(folder):
        for filename in file_names:
            file_path = os.path.join(folder_name, filename)
            zip_object.write(file_path, os.path.basename(file_path))
if os.path.exists(myzip):
    print("%s ZIP file created" % myzip)
else:
    print("ZIP file not created")
