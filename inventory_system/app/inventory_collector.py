import platform, psutil, socket

def get_system_info():
    return {
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'os': platform.system() + " " + platform.release(),
        'cpu': platform.processor(),
        'ram_gb': round(psutil.virtual_memory().total / (1024 ** 3), 2),
    }
