#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/04/17
#Description:
    #These codes I improved from Professor's document and translate to English to.
import datetime
import pandas as pd
#some default country and jetlag
jetlagCountries = [-16, -8, 2, -2, -2, -1, -13, 1, -7]
countries = ["San Francisco", "London", "Sydney", "Jakarta", "Viet Nam", "China", "New York", "Vladivostok",
             "Amsterdam"]
#for loading excel data (for all countries over the world)
#in this case I use international GMT time to calculate different time over the World with Korea
#all data will be read from EXCEL file with pandas library
jetlagMoreCountries = []
morecountries = []
korea_gmt=9

#this function use to check the year is leap year
def is_leap_year(yy):
    return  yy % 400 == 0 or (yy%100) and yy%4==0
#find the date string for country diffirent time with Korea
def jetlag(yy, mm, dd, hh, mi, gap): #시차를 게산하는 함수-#Function to calculate parallax
    hh +=gap                         #한국과 캘리포니아 시차-Korea and California time difference
    if hh < 0 :                      #시간이 음수이면 날짜를 조정-If the time is negative, adjust the date
        dd = dd - 1
        hh += 24
    if dd ==0:                       #조정한 날짜가 0이 되면 달을 조정-When the adjusted date reaches 0, the month is adjusted.
        mm = mm-1
        if mm ==0:                   #조정한 달이 0이면 연도를 조정-If the adjusted month is 0, adjust the year
            mm = 12
            yy -= 1
        if mm in [4, 6, 9, 11]:      #조정한 달의 마지막 날짜 계산-Calculate the last day of the adjusted month
            dd = 30                  #마지막 일이 30일-30 days last
        elif mm in [1,3,5,7,8,10,12]:#마지막 일이 31일-The last day is the 31st
            dd=31
        else:                        #2월 : 윤달을 계산해야 함-February: The leap month needs to be calculated
            if is_leap_year(yy):     #윤달이 라면-Leap Dal Ramen
                dd = 29
            else:
                dd =28               #윤달이 아니라면-If it's not a leap month
    date= "%d/%d/%d %d:%d" % (yy,mm,dd, hh,mi)
    return date
#this function use to print all countries
#user can enter the index or the name of country to see the Date
def printCountries(countries,isSmall=True):
    print("Countries:")
    for i  in range(len(countries)):
        if isSmall:
            print(f'{i+1}.{countries[i]:<20}',end="")
        else:
            print(f'{i + 1}.{countries[i]:<50}', end="")
        if isSmall and (i+1) % 3 ==0:
            print()
        elif isSmall==False and ((i+1) % 4) ==0:
            print()
    print()
#this function use to show the current date for country by index
def showDateTimeForCountry(country,gap):
    today = datetime.datetime.now()
    print("You choose country:" + country)
    print("Current date and time in Korea:", today.strftime("%Y/%m/%d %H:%M"))
    date = jetlag(today.year, today.month, today.day, today.hour, today.minute, gap)
    print(country, "Current Date and Time:", date)
#this function will show list of country over the world or list of default
#user can see and choose easily
#function will find the gap and country to calculate the different time
#isLittle=True, mean: countries,jetlagCountries is from default
#isLittle=False, mean: countries and GMT time is all over the World (Excel file)
def showDiffrentTimeCountries(countries,jetlagCountries,isLittle=True):
    while True:#loop to re-enter many countries to test
        printCountries(countries,isLittle) #print all countries, user can choose easily
        country=input("Please enter [index] or [name of country] or [exit] to break function:")
        isOkToShow=False
        index=-1
        if country.isdigit()==True: # if use find country by index
            index=int(country)
            if index>0 and index <= len(countries):
                country = countries[index - 1]
                if isLittle ==True:
                    gap = jetlagCountries[index-1]
                else:
                    gmtCountry = jetlagCountries[index - 1]
                    gap = korea_gmt - gmtCountry
                isOkToShow=True
        elif country.lower()=="exit":#if exit
            break
        else:#if user find country by name
            country = country.lower()
            for i in range(len(countries)):
                if (countries[i].lower() == country):
                    index = i
                    break
            if index>=0:
                country = countries[index]
                if isLittle ==True:
                    gap = jetlagCountries[index]
                else:
                    gmtCountry = jetlagCountries[index]
                    gap = korea_gmt - gmtCountry
                isOkToShow=True
        if isOkToShow==True:#is ok to show date for country
            if isLittle==False:
                gap = gap *-1;
            showDateTimeForCountry(country, gap)
        else:
            print("The index or country name [%s] is not exit!"%country)
#function to read all countries from Excel
#in this case, gap must be recalcuted before GMT is be used
def showMoreCountries():
    if len(morecountries)==0:#the first time we load data from Excel
        data = pd.read_excel(r'Timezone-countries.xlsx')#read data
        df = pd.DataFrame(data, columns=['Country- City','GMT TimeZone'])
        for i in range(len(df.index)-1):
            morecountries.append(df.iloc[i]["Country- City"])
            jetlagMoreCountries.append(float(df.iloc[i]["GMT TimeZone"]))
    #Reuse showDiffrentTimeCountries
    showDiffrentTimeCountries(morecountries,jetlagMoreCountries,False)
#this function is main function
#give 3 options for user
def doDiffrentTimeCountry():
   while True:
    print("1.Little Countries")#do with default countries in the list in memory
    print("2.More  Countries")#do with all country over the world in Excel
    print("3.Exit application")#exit application
    choice=input("Please enter your choice:")
    if choice=="1":
        showDiffrentTimeCountries(countries,jetlagCountries,True)
    elif choice=="2":
        showMoreCountries()
    elif choice=="3":
        print("Thank you for using the app!")
        exit()
    else:
        print("Please choose correcting number")
#call main function to use the application
doDiffrentTimeCountry()