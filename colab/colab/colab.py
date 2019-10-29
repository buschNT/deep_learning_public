
def test():
    print('Hi colab!')
    return True

def mount_drive(path_drive='/content/drive'):
    from google.colab import drive
    drive.mount(path_drive)