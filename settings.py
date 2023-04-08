import os
import configparser

config_path = os.path.expanduser(r'~\Documents\ShapeMemory')
config_filename = 'config.ini'
config_filename_with_path = config_path + r'\\' + config_filename


# 내문서 경로에 ShapeMemory 폴더, config.ini 파일 생성
def create_dir():
    try:
        if not os.path.exists(config_filename_with_path):
            os.makedirs(config_path, exist_ok=True)
            f = open(config_filename_with_path, 'w')
            f.close()

    except OSError:
        print("Error: Failed to create the directory.")


# 설정 파일 최초 생성
def config_generator():
    config = configparser.ConfigParser()

    # default
    config['Schedule'] = {
        'Reservation': 'OFF',
        'AtWindowLock': 'OFF',
        'CountMonitor': 'OFF'
    }
    config['Option'] = {
        'IntervalSec': '60',
        'MaxMemoryNum': '5'
    }

    # 설정 파일 저장
    # with open(config_filename_with_path, 'w', encoding='utf-8') as configfile:
    with open(config_filename, 'w', encoding='utf-8') as configfile:  # for test
        config.write(configfile)


# 설정 가져오기
def get_config():
    # 설정 파일 읽기
    config = configparser.ConfigParser()
    # config.read(config_filename_with_path, encoding='utf-8')
    config.read(config_filename, encoding='utf-8')  # for test

    return config


# 설정 파일 쓰기
def set_config(config: configparser.ConfigParser):
    # with open(config_filename_with_path, 'w', encoding='utf-8') as configfile:
    with open(config_filename, 'w', encoding='utf-8') as configfile:  # for test
        config.write(configfile)
