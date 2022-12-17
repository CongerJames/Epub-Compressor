import zipper
import renamer
import compresser

def run_code(source, compression_level):
    renamer.epub2zip(source)
    zipper.unzip_all(source)
    compresser.compresser(source, compression_level)
    zipper.zip_all(source)
    renamer.zip2epub(source)