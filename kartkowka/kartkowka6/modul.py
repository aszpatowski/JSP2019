import datetime
import time
def datetimenow():
    print("Data: \n {}\n {} \n {}\n".format(datetime.datetime.now().year, datetime.datetime.now().month,datetime.datetime.now().day))
def timesince(n):
    a = time.gmtime(n)
    print("Data:",a[0],a[1],a[2],sep="\n")
def modul():
    datetimenow()
if __name__ == "__main__":
    modul()