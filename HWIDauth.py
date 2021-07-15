import subprocess,requests
try:r = requests.get('https://raw.githubusercontent.com/reactxsw/hwiddump/main/hwid.txt')
except (requests.ConnectionError, requests.Timeout) as Exception:print('Error : Internet connection');input()
def check():return True if subprocess.check_output('wmic csproduct get uuid' ,shell=False).decode().split('\n')[1].strip() in r.text else False
def main():print("Permission granted" if check() else "Permission denial");input()
main()
