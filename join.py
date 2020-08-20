
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['rbaal.zip.000.COOL', 'rbaal.zip.001.COOL', 'rbaal.zip.002.COOL', 'rbaal.zip.003.COOL', 'rbaal.zip.004.COOL', 'rbaal.zip.005.COOL'],'rbaal.zip')
print('unziping')
with zipfile.ZipFile('rbaal.zip', 'r') as zip_ref:
    zip_ref.extractall('rbaal')
os.remove('rbaal.zip')
os.remove('join.py')
