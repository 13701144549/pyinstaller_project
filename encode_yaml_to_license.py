#!/usr/bin/env python
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
BASE_DIR = os.path.join(sys.path[0], 'yaml_to_license')
# BASE_DIR = sys.path[0]
print(BASE_DIR)


def create_license():
    file_names = []
    for _, _, files in os.walk(BASE_DIR):
        file_names = files
        break
    for i in file_names:
        if '.yaml' in i:
            file_path = os.path.join(BASE_DIR, i)
            if not os.path.isfile(file_path):
                logger.error(f'术语表文件<{file_path}>不存在！')
                return
            with open(file_path, encoding='utf-8') as f:
                cus_content = yaml.safe_load(f)
            if not cus_content:
                logger.error(f'术语表文件<{file_path}>内容为空！')
                return
            try:
                license_content = jwt.encode(cus_content, key=LICENSE_JWT_KEY)
            except Exception as e:
                logger.error(f'加密术语表文件<{file_path}>失败：{e}')
                return
            license_file_path = os.path.join(BASE_DIR, f"{i.split('.')[0]}")
            with open(license_file_path, 'w') as f:
                f.write(license_content)
            logger.critical(f'license文件<{license_file_path}>已生成！')


if __name__ == '__main__':
    create_license()
