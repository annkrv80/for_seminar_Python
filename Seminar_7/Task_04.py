import random
import string
import os

def create_files_with_extension(dir, extension, min_name_length=6, max_name_length=30, min_file_size=256,\
                                max_file_size=4096, num_files=5):
    if os.path.isdir(dir):
        os.chdir(dir)
    else: 
        os.mkdir(dir)
        os.chdir(dir)

    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_letters+string.digits, k=name_length)) + extension        
        file_size = random.randint(min_file_size, max_file_size)
        random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('utf-8')

        with open(file_name, 'wb') as file:
            file.write(random_bytes)

create_files_with_extension('dir','.txt')