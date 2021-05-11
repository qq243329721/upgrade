# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')

options = {"py2exe": {
    "compressed": 1,  # 压缩
    "optimize": 2, # 优化等级 0表示不优化 ，1表示普通优化，2表示额外优化
    "unbuffered":True, # 使用未缓冲的二进制stderr和stdout
    "bundle_files": 1,  # 所有文件打包成一个exe文件
}}

setup(
    name = 'smallPlane Demo',
    description = '小飞机',
    console=[{'script': "main.py", "icon_resources": [(1, "smallPlane.ico")]}],
    options=options,
    
    zipfile=None, requires=['icecream', 'pandas', 'beautifulsoup4']
)
