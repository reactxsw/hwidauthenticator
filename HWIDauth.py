import subprocess, requests

try:
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    r = requests.get('https://raw.githubusercontent.com/reactxsw/hwiddump/main/hwid.txt')
except:
    print('Error : Internet connection')
    a = input('')

def Authenticator():
    if not current_machine_id in r.text:
        print(f'Invalid HWID :' + current_machine_id)
        b = input('')
    else:
        print("Permission granted !")
        return True

Authenticator()