import os

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_LOG_DIR = os.path.join(PROJECT_BASE_DIR, 'log')
if __name__ == '__main__':
    print(PROJECT_BASE_DIR)
