from datetime import datetime
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%D %H:%M:%S")