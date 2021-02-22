import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UP_LOG_DIR = os.path.join(BASE_DIR, 'log')
SSH_CONFIG={
    'hostname':"",
    "port":"",
    "username":"",
    "password":"",
}
if __name__ == '__main__':
    print(BASE_DIR)
