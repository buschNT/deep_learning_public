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