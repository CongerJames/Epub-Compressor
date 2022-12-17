import os

def epub2zip(directory):
    old_extension = '.epub'
    new_extension = '.zip'

    for filename in os.listdir(directory):
        if filename.endswith(old_extension):

            file_path = os.path.join(directory, filename)

            new_file_path = file_path.replace(old_extension, new_extension)
            os.rename(file_path, new_file_path)    
    
def zip2epub(directory):
    old_extension = '.zip'
    new_extension = '.epub'

    for filename in os.listdir(directory):
        if filename.endswith(old_extension):

            file_path = os.path.join(directory, filename)

            new_file_path = file_path.replace(old_extension, new_extension)
            os.rename(file_path, new_file_path)