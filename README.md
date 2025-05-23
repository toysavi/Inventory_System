# Welcome to IT Inventory System
This is an in struction guide to setup this system
## Preparation

### Install MySQL on Ubuntu/Debian (Linux)

```aiignore
sudo apt update -y
sudo apt install mysql-server -y
sudo apt install -y pip pkg-config default-libmysqlclient-dev pkg-config build-essential python3-dev
sudo systemctl start mysql
sudo systemctl enable mysql
```
Then secure the installation:
```aiignore
sudo mysql_secure_installation
```
Log in:
```aiignore
sudo mysql -u root -p  
```
Run below script to setup database:
```aiignore
CREATE DATABASE inventorydb;
        USE inventorydb;
        CREATE TABLE devices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            hostname VARCHAR(255),
            ip_address VARCHAR(255),
            os VARCHAR(100),
            cpu VARCHAR(255),
            ram_gb FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
```

### Install the dependencies package
```aiignore
sudo apt update -y
sudo apt install pip python-is-python3 -y
sudo ln -s /usr/bin/python3 /usr/bin/python
pip install mysqlclient
pip install "Flask<2.3"
```
### Download 
```aiignore
sudo mkdir /inventory_system && cd /inventory_system && sudo chmod 600 -R /inventory_system
sudo git clone https://github.com/toysavi/Inventory_System.git . 
cd /inventory_system
sudo pip install -r requirements.txt
```



## Installation

### Python Install
```aiignore
python run.py
```
Expected result:
```aiignore
http://127.0.0.1:5000
```


