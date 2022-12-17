import zipper
import renamer
import compresser

source = 'C:/Users/maiti/Downloads/TEST'
destination = 'C:/Users/maiti/Downloads/TEST'
compression_level = 30

renamer.epub2zip(source)
zipper.unzip_all(source)
compresser.compresser(source, compression_level)
zipper.zip_all(source)
renamer.zip2epub(source)

print("Successfully Compressed!!!")