import yaml

def hello_colab():
    print('Hello colab!')

def mount_drive(path_drive='/content/drive'):
    from google.colab import drive
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
