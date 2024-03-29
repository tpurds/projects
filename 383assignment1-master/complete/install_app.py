import os
os.system("sudo apt update")
os.system("sudo apt upgrade")

os.system("sudo python3 writeip.py")

os.system("sudo apt-get install vim -y")
os.system("sudo apt install apache2 mysql-client mysql-server php libapache2-mod-php -y")
pathof = os.path.abspath('ip.txt')
x = open(pathof,'r')
ipread=x.read()
sqlip = ipread.replace("\n","")
print(sqlip)

os.system("sudo apt  install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring -y")
print("Install Additional Software finished")

os.system("sudo service apache2 restart")

os.system("sudo apt  install git -y")
print("git download finished")

os.system("sudo apt-get update")
os.system("sudo apt-get install python3-pip -y")
os.system("sudo pip3 install --upgrade pip")
os.system("sudo pip3 install pymysql ")


import pymysql
#import csv
# read the csv file


#start
os.chdir("/opt")
os.system("sudo git clone https://github.com/moodle/moodle.git")
os.chdir("/opt/moodle")
os.system("sudo git branch -a")
os.system("sudo git branch --track MOODLE_36_STABLE origin/MOODLE_36_STABLE")
os.system("sudo git checkout MOODLE_36_STABLE ")
print("moodle download finished")

os.system("chmod -R a-w /var/www/html")
os.system("chmod -R 777 /var/www/html ")

print("copy local repository finished")

#modify mysql configuration file

os.chdir("/etc/mysql/mysql.conf.d/")
#add permission write to the file
os.system("sudo chmod o+w mysqld.cnf ")


data="\ndefault_storage_engine = innodb\ninnodb_file_per_table = 1\ninnodb_file_format = Barracuda"

Sqlfile = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"r")
content = Sqlfile.read()
Sqlfile.close()

position=content.find("skip-external-locking")
length = len("skip-external-locking")
if position != -1:
	content = content[:position+length] + data + content[position+length:]
	Modified_file = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"w")
	Modified_file.write(content)
	Modified_file.close()
	print("the file has been modified")

#change the permission back
os.system("sudo chmod o-w mysqld.cnf ")
print("permission changed")


os.system("sudo apt-get install vsftpd")
print("install vsftep finished")
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()

os.chdir("/var/383assignment1/complete/")
ftp_conf = open('ftp_conf.txt',"r")
new_content = ftp_conf.read()
ftp_conf.close()
position=new_content.find("/etc/pam.d/vsftpd")
modified= open('/etc/vsftpd.conf',"w")
modified.write(new_content[0:position]+"\n"+"pasv_address="+ip)
modified.close()
os.system("chmod a-w /var/www/html")

pam = open('/etc/pam.d/vsftpd',"w")
pam.write(new_content[position+18:len(new_content)])
pam.close()

os.mkdir("/etc/userconfig")

os.system("useradd -m teacher")
os.system("echo teacher:teacher| chpasswd")
os.system("chown -R teacher:teacher /var/www/html")
os.system("chmod -R 777 /home/teacher")
os.system("touch /etc/userconfig/teacher")
user = open("/etc/userconfig/teacher", "w")
user.write("local_root=/var/www/html/")
user.close()

os.system("sudo service vsftpd restart")

os.chdir("/var/www/html")
os.system("sudo apt-get install unzip -y")
os.system("sudo wget https://files.phpmyadmin.net/phpMyAdmin/4.7.0/phpMyAdmin-4.7.0-all-languages.zip")
os.system("sudo unzip phpMyAdmin-4.7.0-all-languages.zip")
os.system("sudo mv phpMyAdmin-4.7.0-all-languages phpMyAdmin")

#let phpmyadmin default host to sql ip
os.chdir("/var/www/html/phpMyAdmin/libraries")
os.system("sudo chmod o+r config.default.php")
os.system("sudo chmod o+w config.default.php")

f = open('/var/www/html/phpMyAdmin/libraries/config.default.php','r')
content = f.read()
f.close()
index = content.find("$cfg['Servers'][$i]['host'] = '")
print(index)
a = len("$cfg['Servers'][$i]['host'] = ")
print(a)
#print(content[:index+a])
content = content[:index+a+1] + sqlip + content[index+a+10:]
y = open('/var/www/html/phpMyAdmin/libraries/config.default.php','w')
y.write(content)

y.close()
print(content[:index+a+a])


os.system("sudo /etc/init.d/apache2 restart")
os.system("sudo service apache2 restart")
os.system("sudo chmod -R 777 /var/383assignment1/complete")
cgi_conf = open('/var/383assignment1/complete/cgi_conf.txt',"r")
new_content = cgi_conf.read()
cgi_conf.close()
os.system("sudo chmod a+w /etc/apache2/sites-enabled/000-default.conf")
modified = open('/etc/apache2/sites-enabled/000-default.conf',"w")
modified.write(new_content)
modified.close()
os.system("sudo chmod a-w /etc/apache2/sites-enabled/000-default.conf")
os.system("sudo ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/")
os.system("sudo ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/")
os.system("service apache2 restart")
os.system("sudo apt install dos2unix")
os.system("sudo mv /var/383assignment1/complete/help /var/www/html ")
os.chdir("/var/www/html/help/")
os.system("sudo apt install dos2unix")
os.system("sudo cp -R ./* /var/www/html")
os.system("sudo dos2unix /var/www/html/cgi-bin/teacher.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/student.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/backupFiles.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/restoreFiles.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/assi1.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/assi2.py")
os.system("sudo dos2unix /var/www/html/cgi-bin/assi4.py")
os.system("chmod +x /var/www/html/cgi-bin/teacher.py")
os.system("chmod +x /var/www/html/cgi-bin/student.py")
os.system("chmod +x /var/www/html/cgi-bin/backupFiles.py")
os.system("chmod +x /var/www/html/cgi-bin/restoreFiles.py")
os.system("chmod +x /var/www/html/cgi-bin/assi1.py")
os.system("chmod +x /var/www/html/cgi-bin/assi2.py")
os.system("chmod +x /var/www/html/cgi-bin/assi4.py")


os.system("sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb")
os.system("sudo chmod a+w -R /mnt")
os.system("sudo mkdir /mnt/moodledata")
os.system("sudo mkdir /mnt/backup")

os.chdir("/var/383assignment1/complete/")
unanswered = True
while unanswered == True:
    choice = input("Would you like 1.the students to install 2.automatically install,please input(1/2):")
    if str(choice) == "1" or str(choice) == "2":
        unanswered = False
    else:
        print("wrong option. choose 1 or 2")

os.system("sudo cp -R /var/383assignment1/complete/ip.txt /var/www/html/cgi-bin")
if choice == "1":
    os.system("python3 for_loop.py")
if choice == "2":
    os.system("python3 express.py")
print("for_loop finished")

os.system('sudo echo "www-data ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers')
os.system("sudo chmod -R 777 /mnt/backup")
