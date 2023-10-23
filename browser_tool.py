import os
import subprocess
from time import sleep


# --------- flatten and launch
def zen(args):
    args_list = flatten(args)
    inputs = subprocess.check_output(x for x in args_list)
    r_output = inputs.decode('utf-8').strip()
    output = []
    for x in r_output.split(','):
        output.append(x.strip())
    print(output)
    return output


def flatten(_list):
    flat_list = []
    for item in _list:
        if type(item) is list:
            for item in item:
                flat_list.append(item)
        else:
            flat_list.append(item)
    return flat_list
# -------------------- flatten and launch


main_dir = '/path/to/desired/folder'


def chdir(newloc):
    os.chdir(newloc)
    listdir = os.listdir('.')
    return listdir


action = ['zenity', '--list', '--column=list', ['launch', 'clone']]

output = zen(action)


if output[0] == 'launch':
    browse_list = ['zenity', '--text=new titlelajlf', '--width=600', '--height=700',
                   '--list',  '--column=list', chdir(main_dir)]
    browser_out = zen(browse_list)
    os.system(f'brave-browser --user-data-dir={browser_out[0]}')
elif output[0] == 'clone':
    browse_list = ['zenity', '--text=new titlelajlf', '--width=600', '--height=700',
                   '--list',  '--column=list', chdir(main_dir)]
    browser_out = zen(browse_list)
    name_browser = ['zenity', '--forms', '--add-entry=name browser']
    name_out = zen(name_browser)
    os.system(f'rsync -av {browser_out[0]}/ {name_out[0]}')
    os.system(f'brave-browser --user-data-dir={name_out[0]}')
