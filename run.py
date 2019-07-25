import os
import sys


for (dirpath, dirnames, filenames) in os.walk('./'):
        for filename in filenames:
                if filename.endswith('.csv'):
                    filename_without_csv = filename[:-4]
                    #parse xml
                    cmd_to_run = f'csvsql --dialect mysql {dirpath}/{filename} > {filename_without_csv}.sql'
                    os.system(cmd_to_run)