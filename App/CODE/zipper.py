import os
import zipfile
import shutil

def zip_all(source_dir, target_dir = None):
    if target_dir is None:
        target_dir = source_dir
    cwd = os.getcwd()

    for folder in os.listdir(source_dir):
        if os.path.isdir(os.path.join(source_dir, folder)):
            
            zip_file = zipfile.ZipFile(os.path.join(target_dir, folder + '.zip'), 'w', zipfile.ZIP_DEFLATED)
            
            os.chdir(os.path.join(source_dir, folder))
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    zip_file.write(os.path.join(root, file))
        
            zip_file.close()
            os.chdir(source_dir)
            shutil.rmtree(folder, ignore_errors=True)
    os.chdir(cwd)

def unzip_all(source_dir, target_dir =  None):
    if target_dir is None:
        target_dir = source_dir
        
    for file in os.listdir(source_dir):
        if file.endswith('.zip'):
            file_dir = target_dir + '/' + file[:-4]
            os.makedirs(file_dir, exist_ok=True)

            with zipfile.ZipFile(os.path.join(source_dir, file), 'r') as zip_ref:
                zip_ref.extractall(file_dir)
            os.remove(os.path.join(source_dir, file))