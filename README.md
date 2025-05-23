# Welcome to IT Inventory System
This is an in struction guide to setup this system
## Preparation



### Install the dependencies package
```aiignore
sudo apt update -y
sudo apt install pip-3 -y
sudo pip install -r requirements.txt
```
### Download 
```aiignore
sudo mkdir /inventory_system && sudo chmod 600 /inventory_system
sudo git clone https://github.com/toysavi/Inventory_System.git /inventory_system 
```

### Install MySQL on Ubuntu/Debian (Linux)

```aiignore
sudo apt update -y
sudo apt install mysql-server -y
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

## Installation

### Python Install
```aiignore
python run.py
```
Expected result:
```aiignore
http://127.0.0.1:5000
```


