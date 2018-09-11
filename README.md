# Raspberry pi
Raspberrypi basic installation,static ip creatrion and apache server creations

![RPI](https://github.com/sunnyprime/Raspberry-pi/blob/master/91zSu44%2B34L._SX569_.jpg)

![RPI_PIN](https://github.com/sunnyprime/Raspberry-pi/blob/master/oDRh4lpYwoZHHrJiQR64.png)


### Download and [Noobs Operating System](https://www.raspberrypi.org/downloads/noobs/)

1. Extract all the files to memory card.

2. Put memory card in raspberry Pi .

3. Follow The Simple Steps.

---

### Django + Raspberry Pi

#### 1. Updating and Cleaning your Raspberry Pi

```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get autoremove
```

#### 2. Install Python MySQLDB

```
sudo apt-get install python-mysqldb -y
```

#### 3. Install LAMP Server

The second install on this step will ask you to create a password for the root SQL user.

```
sudo apt-get install apache2 -y
sudo apt-get install mysql-server mysql-client -y
sudo apt-get install php5 libapache2-mod-php5 php5-mysql -y
sudo service apache2 restart
```

#### 4. Install PHPMyAdmin and configure it to Apache.

This step will ask you which server you would like to use for your application. I chose Apache.

```
sudo apt-get install phpmyadmin -y
sudo nano /etc/apache2/apache2.conf
```
In this you’ll see include statements, find an empty line right after the include conf.d/ that has an empty line after it. Go down until are on the empty line. Type the following:

```
Include /etc/phpmyadmin/apache.conf
```
Restart the server to be able to access phpmyadmin on your local server (in a browser go to localhost/phpmyadmin).

```
sudo service apache2 restart
```
#### 5. Install Python Setup tools
```
sudo apt-get install python-setuptools -y
```

#### 6. Make sure you have PIP installed
```
wget  https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo rm -rf get-pip.py
```
#### 7: Install Django
```
sudo pip install Django
```
#### 8: Creating our application

I will use the name DjangoProject but you can call yours whatever you prefer.

```
django-admin startproject DjangoProject
cd DjangoProject
```

#### 9: Migrating DB and Running App

Migrate the DB and starting our application. Use your Raspberry Pi IP address (mine is 192.168.0.5) and choose what port you’d like to run on.

```
python manage.py migrate
python manage.py runserver 192.168.0.5:8000
```

#### 10. Change in Setting.py
```
on lie 23 of the settings page you need to add
ALLOWED_HOSTS = [‘localhost’, ‘YOUR IP HERE’]
Example:- ALLOWED_HOSTS = [ ‘192.168.1.2 ‘ ] # for internal ip
```

---



### GPIO Sample

```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
for x in range(0,5):
    GPIO.output(12, True)
    print("Running")
    time.sleep(10)
    GPIO.output(12, False)
    time.sleep(10)
GPIO.cleanup()
print("Stopped")
```

## Rest is on the Process...
