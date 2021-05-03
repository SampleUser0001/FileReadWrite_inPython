# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
import locale
import glob
import os

INPUT_PATH = './files/**'


DATE_FORMAT='%Y%m%d_%H%M%S'

JST = timezone(timedelta(hours=+9), 'JST')
now = datetime.now(JST).strftime(DATE_FORMAT)
OUTPUT_PATH = './files/output_' + now + '.txt'


files = [p for p in glob.glob(INPUT_PATH , recursive=True) if os.path.isfile(p)]
print(files)

lines=[]

with open(files[0]) as f:
    for line in f.read().splitlines():
        print(line)
        lines.append(line)

with open(OUTPUT_PATH, mode='w', newline='\n') as f:
    for line in lines:
        f.write(line+'\n')
