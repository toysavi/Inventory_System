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
sudo mkdir
sudo git clone 
```

### Database configure

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

### 



