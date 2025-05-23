from app.inventory_collector import get_system_info

def test_info_keys():
    info = get_system_info()
    assert 'hostname' in info
    assert 'ip_address' in info
    assert 'os' in info
    assert 'cpu' in info
    assert isinstance(info['ram_gb'], float)

if __name__ == '__main__':
    test_info_keys()
    print("Test passed.")
