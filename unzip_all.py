import os
import zipfile

source_dir = 'C:/Users/maiti/Downloads/TEST'
target_dir = 'C:/Users/maiti/Downloads/ TEST'

for file in os.listdir(source_dir):
    if file.endswith('.zip'):
        file_dir = target_dir + '/' + file[:-4]
        os.makedirs(file_dir, exist_ok=True)

        with zipfile.ZipFile(os.path.join(source_dir, file), 'r') as zip_ref:
            zip_ref.extractall(file_dir)