#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/28
#Description:
# These codes to  alarm for the absolute time
import time
import winsound

print("[현재 시각]",time.strftime("%H:%M:%S"))#current time
alarm_time=input("알람 시각:")#Alarm time
alarm_hms=alarm_time.split(':')

if len(alarm_hms)==3:#check date string input format
    alarmHour=int(alarm_hms[0])#get hour input
    alarmMinute = int(alarm_hms[1])#get hour minute
    alarmSecond = int(alarm_hms[2])#get hour second
    #check valid time
    #hour: 0->23
    #minute: 0->59
    #second: 0->59
    if alarmHour >= 0 and alarmHour < 24 and alarmMinute >= 0 \
            and alarmMinute<= 59 and alarmSecond >= 0 and alarmSecond <= 59:
        #need to get current time again(because the date maybe delayed by user)
        current=time.localtime()
        #get total second of curren time
        totalSecondOfCurrent=current.tm_hour*60*60+current.tm_min*60+current.tm_sec
        #get total second of time to alarm
        totalSecondOfAlarm = alarmHour * 60 * 60 + alarmMinute * 60 + alarmSecond
        #get delta time betwen current and alarm time
        waitingSecond=totalSecondOfAlarm-totalSecondOfCurrent
        if waitingSecond>=0:#if alarm time is in the future
            time.sleep(waitingSecond)#wait waintingsecond
            for i in range(1, 10):
                winsound.Beep(i * 100, 200)#beep! beep
        else:
            print("The time is over!")#alarm is over
    else:
        print("Time is not valid!")
else:
    print("입력한 알람 시각 표기에 오류가 있습니다.")#There is an error in the entered alarm time display.