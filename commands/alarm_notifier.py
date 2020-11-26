import json
import time
import notify2


notify2.init("Alarm")

def wait_for_alarm(alarm_time_need: int):
    time.sleep(alarm_time_need)
    n = notify2.Notification("Alarm",
                         "The time passed",
                         "alarm"   # Icon name
                        )
    n.show()
    exit()

def configure_alarm():
    choose_type_of_time = input("Do you want to input the hour of the alarm in minutes or in hours (write minutes of hours): ")
    if(choose_type_of_time == "minutes"):
        alarm_time_raw = input("Write the minutes that must pass until I notify you: ")
        alarm_time_need = int(alarm_time_raw) * 60
        print(f"Okay, I will notify you in {alarm_time_raw} minutes")
        print("WARNING: if you close the script I can't notify you, be careful and leave it open")
        wait_for_alarm(alarm_time_need)
    else:
        alarm_time_raw = input("Write the hours that must pass until I notify you: ")
        alarm_time_need = int(alarm_time_raw) * 60 * 60
        print(f"Okay, I will notify you in {alarm_time_raw} hours")
        print("WARNING: if you close the script I can't notify you, be careful and leave it open")
        wait_for_alarm(alarm_time_need)


def check_alarm():
    if(True):
        print("There is an alarm set, do you want to edit it?")
        replytrue = input("Write yes or no: ")
        if(replytrue == "yes" or replytrue == "Yes"):
            configure_alarm()
        else:
            exit()
    else:
        print("There isn't any alarm set, do you want to set one?")
        replyfalse = input("Write yes or no: ")
        if(replyfalse == "yes" or replyfalse == "Yes"):
            configure_alarm()
        else:
            exit()
        

    