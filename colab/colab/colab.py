import os
import yaml
import zipfile

from google.colab import drive
from google.colab import files

def hello_colab():
    print('Hello colab!')

def mount_drive(path_drive='/content/drive'):
    drive.mount(path_drive)

def get_settings(path_file):
    with open(path_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as e:
            print(e)
    return False

def get_repository_settings_private(settings):
    GIT_USERNAME = settings['git']['private']['username']
    GIT_TOKEN = settings['git']['private']['token']
    GIT_REPOSITORY = settings['git']['private']['repository']
    PATH_CODE = settings['git']['private']['path']
    return GIT_USERNAME, GIT_TOKEN, GIT_REPOSITORY, PATH_CODE

def upload_dataset():
    uploaded = files.upload()
    dataset_name = list(uploaded.keys())[0]
    path_dataset = os.path.join('content', dataset_name)

    zip_ = zipfile.ZipFile(dataset_name, 'r')
    zip_.extractall(os.path.splitext(path_dataset)[0])
    zip_.close()