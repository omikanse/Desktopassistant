import cv2
import mediapipe as mp
import subprocess
import webbrowser
import sys
import speech_recognition as sr
import time
import pyautogui
import os

r = sr.Recognizer()
def close_browser():
    # Wait for the user to switch to the browser window
    time.sleep(5)

    # Send Alt + F4 keystrokes to close the active window
    pyautogui.hotkey('ctrl', 'w')

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        user_command = r.recognize_google(audio)
        print("You said:", user_command)
        return user_command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return ""  # Return an empty string if there was an error in speech recognition

    

    
def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2
    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1
 
    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1

    return cnt

cap=cv2.VideoCapture(0)

drawing=mp.solutions.drawing_utils
hands=mp.solutions.hands
hand_obj=hands.Hands(max_num_hands=1)



while True:
    __,frm=cap.read()
    frm=cv2.flip(frm,1)
    res=hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints=res.multi_hand_landmarks[0]
        cnt=count_fingers(hand_keyPoints)
        if cnt == 1:
            # Display the second window for 2 fingers
            subprocess.Popen(["notepad.exe"])
            time.sleep(2)
            
        if cnt == 2:
            # Open Excel
            excel_path = "C:\\Program Files\\Microsoft Office\\Office15\\EXCEL.EXE"
            subprocess.Popen([excel_path])
            time.sleep(2)

        elif cnt == 3:
            brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            subprocess.Popen([brave_path])
            time.sleep(2)

        elif cnt == 4:
            user_command=listen()
            if "start" in user_command:
                webbrowser.open("https://www.google.com/")
                print("Music stopped.")
            elif "bad boy" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=OxjKx0Vojy4&list=RDOxjKx0Vojy4&start_radio=1")
                print("Music stopped.")
            elif "believe" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=W0DM5lcj6mw&list=RDOxjKx0Vojy4&index=2")
                print("Music stopped.")
            elif "open stock chart" in user_command:
                webbrowser.open("https://in.tradingview.com/chart/G8KFv4Se/")
            elif "open Stock chart" in user_command:
                webbrowser.open("https://in.tradingview.com/chart/G8KFv4Se/")
            elif "open internshala" in user_command:
                webbrowser.open("https://internshala.com/fresher-jobs/python-developer-jobs/")
            elif "open indeed" in user_command:
                webbrowser.open("https://in.indeed.com/?from=gnav-jobseeker-profile--profile-one-frontend")
            elif "old song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=nXO1olFLrXA")
            elif "love song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=TBlixHMv_GQ")
            elif "entry song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=ys9nDLS97sI")
            elif "open Internshala" in user_command:
                webbrowser.open("https://internshala.com/fresher-jobs/python-developer-jobs/")
            elif "open Indeed" in user_command:
                webbrowser.open("https://in.indeed.com/?from=gnav-jobseeker-profile--profile-one-frontend")
            elif "Old song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=nXO1olFLrXA")
            elif "Love song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=TBlixHMv_GQ")
            elif "Entry song" in user_command:
                webbrowser.open("https://www.youtube.com/watch?v=ys9nDLS97sI")
            elif "video" in user_command:
                vi_path = "E:\\Old\power 1080\\New folder\\video.mkv"
                os.startfile(vi_path)


                
            
            elif "exit" in user_command:
                close_browser()
            
        
            

        



        drawing.draw_landmarks(frm,res.multi_hand_landmarks[0],hands.HAND_CONNECTIONS)
    

    cv2.imshow("Jarvis",frm)

    if cv2.waitKey(1)==27:
        cv2.destroyAllWindows()
        cap.release()
        break
