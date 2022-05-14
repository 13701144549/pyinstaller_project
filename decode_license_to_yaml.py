#-*- coding : utf-8-*-
# @Time    : 2021/9/9 11:19
# @Author  : guobeibei
# @Python  : 3.7.5
# @File    : license.py
# @Project : fscr
import os
import sys
import logging
import yaml
import jwt

logger = logging.getLogger(__name__)

LICENSE_JWT_KEY = 'EDFD10F666E8EB448C8A2B726D987FA2'
# BASE_DIR = os.path.join(sys.path[0], 'license_to_yaml')
BASE_DIR = os.getcwd()
print(BASE_DIR)


def decode_license():
    file_names = []
    for _, _, files in os.walk(BASE_DIR):
        file_names = files
        break
    for i in file_names:
        if 'license' in i and '.yaml' not in i and '.py' not in i:
            file_path = os.path.join(BASE_DIR, i)
            try:
                with open(file_path, 'rb') as f:
                    license_code = f.read()
                license_content = jwt.decode(license_code, LICENSE_JWT_KEY, algorithms=['HS256'])
            except jwt.DecodeError as e:
                print('授权文件无效', 'Invalid authorization file')
                continue
            license_yaml_file_path = os.path.join(BASE_DIR, f"{i.split('_to_yaml')[0]}.yaml")
            with open(license_yaml_file_path, 'w', encoding='utf-8') as f:
                f.write(yaml.dump(license_content, allow_unicode=True))


if __name__ == '__main__':
    decode_license()
