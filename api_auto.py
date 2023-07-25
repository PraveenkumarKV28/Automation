from webbrowser import get
import requests
import json
api_url="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
reponse = requests.get(api_url)
y=reponse.json()

#idate = "2019-03-27 18:00:00"
           
def gettemp(idate):
 for i in range(len(y["list"])):
    date = y["list"][i]["dt_txt"]
    if date == idate:
        weather=y["list"][i]["main"]
        temp=weather["temp"]
        print(temp)

def getspeedwind(idate):
 for i in range(len(y["list"])):
    date = y["list"][i]["dt_txt"]
    if date == idate:
        weather=y["list"][i]["wind"]
        speed1=weather["speed"]
        print(speed1)

def getspressure(idate):
 for i in range(len(y["list"])):
    date = y["list"][i]["dt_txt"]
    if date == idate:
        weather=y["list"][i]["main"]
        pressure1=weather["pressure"]
        print(pressure1)

menu_options = {
    1: 'Get weather',
    2: 'Get Wind Speed',
    3: 'Get Pressure',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))

        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           idate=input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
           gettemp(idate)
        elif option == 2:
            idate=input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
            getspeedwind(idate)
        elif option == 3:
            idate=input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
            getspressure(idate)
        elif option == 0:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')



