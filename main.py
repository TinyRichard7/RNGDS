import time

ListHours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24]
listMinutes = [00, 15, 30, 45]

def CurrentTime():
    t = time.localtime()
    print(t.tm_hour)
    print(t)
    print(t.tm_min)
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

def CombineMinutesAndHours(hours , minutes):
    time = str(hours) + ":" + str(minutes)
    if (minutes == 0):
        time = time + str(minutes)
        
    print(time)

def main():
    CombineMinutesAndHours(ListHours[1], listMinutes[0])
    CurrentTime()

if __name__ == "__main__":
    main()