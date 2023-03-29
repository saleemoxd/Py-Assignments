import time

print("Welcome To Pomodoro Timer")

pomodoro_time = float(input("Please type in your pomodoro duration in minutes.")) 
short_break_time = float(input("Please type in your desired short-break time in minutes.")) 
long_break_time = float(input("Please type in your desired long-break time in minutes.")) 
num_pomodoros = int(input("How many Pomodoros do you wish to complete?"))

for i in range(num_pomodoros):
    print(f"Pomodoro {i+1}")
    time.sleep(pomodoro_time * 60)
    if i < num_pomodoros - 1:
        if i % 2 == 0:
            print(f"Take a short break ({short_break_time} minutes)")
            time.sleep(short_break_time * 60)
        else:
            print(f"Take a long break ({long_break_time} minutes)")
            time.sleep(long_break_time * 60)
    else:
        print("Congratulations! You've finished all your pomodoros for today!")
