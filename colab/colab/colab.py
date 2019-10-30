import os
import yaml
import zipfile

# colab
try:
    from google.colab import drive
    from google.colab import files
except:
    print('google.colab import failed.')


def hello_colab():
    print('Hello colab!')

def mount_drive(path_drive='/content/drive'):
    drive.mount(path_drive)

def get_configuration(path_file):
    with open(path_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
            return data
        except yaml.YAMLError as e:
            print(e)
    return False

def get_repository_configuration_private(configuration):
    GIT_USERNAME = configuration['git']['private']['username']
    GIT_TOKEN = configuration['git']['private']['token']
    GIT_REPOSITORY = configuration['git']['private']['repository']
    PATH_CODE = configuration['git']['private']['path']
    return GIT_USERNAME, GIT_TOKEN, GIT_REPOSITORY, PATH_CODE

def upload_dataset(folder_dataset='dataset'):
    uploaded = files.upload()
    dataset_name_zip = list(uploaded.keys())[0]
    dataset_name = os.path.splitext(dataset_name_zip)[0]

    zip_ = zipfile.ZipFile(dataset_name_zip, 'r')
    zip_.extractall(folder_dataset)
    zip_.close()

    dataset_path = os.path.join(folder_dataset, dataset_name)

    return dataset_name, dataset_path