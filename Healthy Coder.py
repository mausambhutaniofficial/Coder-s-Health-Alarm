#Healthy Coder
#works 9am-5pm   #remind him to do these:- once done he have to input a stopper msg to stop songs
#water  - water.mp3 (3.5 litres)  - 'Drank' - log - every 40 min
#Eye exercise - eyes.mp3 - 'EyeDone'  - log-  every 30 min 
#Physical activity - physical.mp3 - 'ExDone'  - log - every 45 min
#Rules: use Pygame module to play audio
from time import time
from pygame import mixer # pip install pygame
from datetime import datetime
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user =  input()
        if input_of_user  == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with  open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 40*60
    eye_secs = 30*60
    exercise_secs =45*60
    while True:
        if time() -init_water >water_secs:
            print("Water Drinking Alarm, Enter 'drank' to stop the alarm")
            musiconloop("water.mp3","drank")
            init_water = time()
            log_now("Drank Water at")
        
        if time() -init_eyes >eye_secs:
            print("Eye exercise Alarm, Enter 'doneeyes' to stop the alarm")
            musiconloop("eyes.mp3","doneeyes")
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() -init_exercise > exercise_secs:
            print("Physical Activity Alarm, Enter 'donephy' to stop the alarm")
            musiconloop("physical.mp3","donephy")
            init_exercise = time()
            log_now("Physical Activity Done at")
