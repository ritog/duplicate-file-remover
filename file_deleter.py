import os
import fnmatch
import platform

def main():
    files = [item for item in os.listdir('.')]
    original_files = [item for item in files if 'copy' not in item]
    duplicate_files = [item for item in files if 'copy' in item]

    for original_file in original_files:
        pattern = original_file + '*'
        for duplicate_file in duplicate_files:
            if (
                fnmatch.fnmatch(
                    duplicate_file, pattern)) and os.stat(
                    './' + original_file).st_size == os.stat(
                        './' + duplicate_file).st_size:        
                    os.unlink(
                        './' + duplicate_file)

if __name__ == '__main__':
    if platform.platform() == 'Linux':
        main()
