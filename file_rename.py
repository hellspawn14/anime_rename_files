import re
from os import listdir, rename, path 
from os.path import isfile, join 

def generate_new_file_name(file_nm_regex, file_ext_regex, original_file_nm): 
    return re.search(file_nm_regex, original_file_nm).group(0).replace('`', "'") + re.search(file_ext_regex, original_file_nm).group(0)
    
def file_rename(n_path, file_nm_regex, file_ext_regex):
    files = [f for f in listdir(n_path) if isfile(join(n_path, f)) and re.search(file_nm_regex, f)]
    file_cnt = 0
    for old_file_nm in files: 
        new_file_nm = generate_new_file_name(file_nm_regex, file_ext_regex, old_file_nm)
        if new_file_nm != old_file_nm:
            if file_cnt == 0: 
                print(n_path.split('/')[-2])
                file_cnt = 1 
            rename(n_path + old_file_nm, n_path + new_file_nm)
            print(old_file_nm, ' -> ', new_file_nm)
    
    if file_cnt > 0: 
        print('\n')

def scan_path(n_path, file_name_regex, file_ext_regex): 
    for folder_nm, file_nm_regex in file_name_regex.items():
        x_path = n_path + folder_nm + '/'
        if path.isdir(x_path):
            file_rename(x_path, file_nm_regex, file_ext_regex)
        
file_nm_regex, file_ext_regex = {
    'Digimon Adventure (2020)': r'Digimon Adventure \(2020\) - [0-9]{2,}',
    'One Piece': r'One Piece - [0-9]{2,}', 
    'Tokyo Revengers': r'Tokyo Revengers - [0-9]{2,}', 
    'Kimetsu no Yaiba/Kimetsu no Yaiba - Mugen Ressha-hen': r'Kimetsu no Yaiba - Mugen Ressha-hen - TV - [0-9]{2,}',
    'Kimetsu no Yaiba/Kimetsu no Yaiba - Yuukaku-hen': r'Kimetsu no Yaiba - Yuukaku-hen - [0-9]{2,}', 
    'Cowboy Bebop': r'Cowboy Bebop - E[0-9]{2,}', 
    'Ganbare Douki-chan': r'Ganbare Douki-chan - [0-9]{2,}', 
    'Sono Bisque Doll wa Koi wo Suru': r'Sono Bisque Doll wa Koi wo Suru - [0-9]{2,}', 
    'Dolls\' Frontline': r'Dolls` Frontline - [0-9]{2,}', 
    'Ousama Ranking': r'Ousama Ranking - [0-9]{2,}'
}, r'\.[\w]{3,}$'
base_path = '/Users/hellspawn14/Downloads/Anime/'
scan_path(base_path, file_nm_regex, file_ext_regex)

'''
folder_nm = 'Sono Bisque Doll wa Koi wo Suru'
path = base_path + folder_nm + '/'
file_nm_rex = file_nm_regex[folder_nm]
file_rename(path, file_nm_rex, file_ext_regex)
'''