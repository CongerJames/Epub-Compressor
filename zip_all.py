import os
import zipfile

source_dir = 'C:/Users/maiti/Downloads/TEST'
target_dir = 'C:/Users/maiti/Downloads/TEST'
cwd = os.getcwd()

for folder in os.listdir(source_dir):
    if os.path.isdir(os.path.join(source_dir, folder)):
        
        zip_file = zipfile.ZipFile(os.path.join(target_dir, folder + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        
        os.chdir(os.path.join(source_dir, folder))
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                zip_file.write(os.path.join(root, file))
    
        zip_file.close()
        os.chdir(cwd)
        
