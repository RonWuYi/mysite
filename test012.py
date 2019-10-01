import os

from constant import constant, google

media_folder = 'C:\\Work\\test project\\github\\mysite\\media'
google.set_env()
for i in os.listdir(media_folder):
    if i.endswith('avi'):
        print(i)
        google.upload_blob(constant.storage_name, os.path.join(media_folder, i), 'test{}'.format(i))