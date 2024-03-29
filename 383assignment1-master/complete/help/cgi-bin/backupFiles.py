#!/usr/bin/python3
#Import modules for CGI handling
import os
import cgi
import pymysql
import csv

print("Content-type: text/html\n")
print("<title>Result</title>")
print("<body><center>")

def Student_list(file_name):
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
            list_of_students.append(row)
            # Remove metadata from top row
        
    return list_of_students

def mdbu(students):
    if os.path.exists("/mnt/backup/mdbu"):
        os.system("sudo rm -rf /mnt/backup/mdbu")
    os.system("sudo mkdir /mnt/backup/mdbu")
    os.system("sudo chmod -R 777 /mnt/backup/mdbu")
    for i in students:
    # Copy the moodledata directory (r to reccursively copy the contents of the directory and p to preserve ownership information
        os.system("sudo cp -rp /mnt/moodledata/data%s /mnt/backup/mdbu/"%str(i[0]))
    print("Moodledata Backup Completed")

def msbu(students):
    if os.path.exists("/mnt/backup/msbu"):
        os.system("sudo rm -rf /mnt/backup/msbu")
    os.system("sudo mkdir /mnt/backup/msbu")
    os.system("sudo chmod -R 777 /mnt/backup/msbu")
    for i in students:
        os.system("sudo cp -rp /var/www/html/%s /mnt/backup/msbu/" % i[4])
    print("Moodle site file Backup Completed")



def dbbu(students):
    if os.path.exists("/mnt/backup/dbbu"):
        os.system("sudo rm -rf /mnt/backup/dbbu")
    os.system("sudo mkdir /mnt/backup/dbbu")
    os.system("sudo chmod -R 777 /mnt/backup/dbbu")
    pathof = os.path.abspath('ip.txt')
    x = open(pathof,'r')
    ipread=x.read()
    sqlip = ipread.replace("\n","")
    for i in students:
         os.system("sudo mysqldump -h%s -u%s -p%s student%s > /mnt/backup/dbbu/student%s.sql" % (sqlip,"root", "Moodle123moodle", str(i[0]), str(i[0])))

    print("Database Backup Completed")

def backup(app,students):
    if app=="moodle":
        mdbu(students)
    if app == "mysql":
        dbbu(students)
    if app=="file":
        msbu(students)
    print("backup finish!!!")
    print("""
                <form action="../login.html" method="GET">
                    <input type="submit" value="Back to last page">
                </form>
                """)



form = cgi.FieldStorage()
app = form['app'].value if 'app' in form else ''
students=Student_list("StudentDatas.csv")
backup(app,students)

print('</center></body>')


