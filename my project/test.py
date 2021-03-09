import numpy as np
import cv2
import win32api
import sys
from array import array
import pyautogui
import speech_recognition as sr
r=sr.Recognizer()

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
#Get initial cursor position
xi,yi=win32api.GetCursorPos()


#Store for 80 frames for right click
xvalue_rclick=np.array((xi,)*80,'i')
yvalue_rclick=np.array((yi,)*80,'i')

n=0


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #Get the position of cursor
        xpos=1366-((int(x+w/2)*6)%1366)
        ypos=(int(y+h/2)*7)%768
        win32api.SetCursorPos((xpos,ypos))

       
		
   
        xvalue_rclick[n]=xpos
        yvalue_rclick[n]=ypos
        
       
        n=(n+1)%40
        
       
        xflag_rclick=1
        yflag_rclick=1

        for m in range(0,40):
            if xvalue_rclick[m]-xpos>30 or xvalue_rclick[m]-xpos<-30:
                xflag_rclick=0
            if yvalue_rclick[m]-ypos>30 or yvalue_rclick[m]-ypos<-30:
                yflag_rclick=0
                
        if xflag_rclick and yflag_rclick:
             with sr.Microphone() as source :
                 print('say anything :')
                 audio = r.listen(source)

             try:
                text=r.recognize_google(audio)
                print(text)
                if text == 'open' :
                    print("double click invoked")
                    pyautogui.doubleClick(xpos,ypos)
                elif text == 'right click' :
                    print("Right click invovked")
                    pyautogui.rightClick(xpos,ypos)
                elif  text == 'single-click':
                    print("single click invoked")
                    pyautogui.click(xpos,ypos,1,3)
                elif  text == 'copy':
                    print("copy invoked")
                    pyautogui.hotkey('ctrl','c')
                elif  text == 'paste':
                    print("paste invoked")
                    pyautogui.hotkey('ctrl','v')
                elif  text == 'cut':
                    print("cut invoked")
                    pyautogui.hotkey('ctrl','x')
                elif  text == 'shading':
                    print("shading invoked")
                    pyautogui.hotkey('ctrl','a')
                elif  text == 'backward':
                    print("backward invoked(ctrl+z)")
                    pyautogui.hotkey('ctrl','z')
                elif  text == 'language':
                    print("language invoked (Alt +shift)")
                    pyautogui.hotkey('alt','shift')
                elif  text == 'enter':
                    print("enter invoked")
                    pyautogui.press('enter')
                elif  text == 'escape':
                    print("ESC invoked")
                    pyautogui.press('esc')
                elif  text == 'back':
                    print("back invoked")
                    pyautogui.press('backspace')
                elif  text == 'delete':
                    print("delet invoked")
                    pyautogui.press('delete')
                elif  text == 'shift':
                    print("shift invoked")
                    pyautogui.press('shift')
                elif  text == 'space':
                    print("space invoked")
                    pyautogui.press('space')
                elif  text == 'control':
                    print("control invoked")
                    pyautogui.press('ctrl')
                elif  text == 'right':
                    print("right arrow invoked")
                    pyautogui.press('right')
                elif  text == 'up':
                    print("up arrow invoked")
                    pyautogui.press('up')
                elif  text == 'down':
                    print("down arrow invoked")
                    pyautogui.press('down')
                elif  text == 'left':
                    print("left arrow invoked")
                    pyautogui.press('left')
                elif  text == 'zero':
                    print("zero invoked")
                    pyautogui.press('0')
                elif  text == 'one':
                    print("one invoked")
                    pyautogui.press('1')
                elif  text == 'two':
                    print("tow invoked")
                    pyautogui.press('2')
                elif  text == 'three':
                    print("three invoked")
                    pyautogui.press('3')
                elif  text == 'four':
                    print("four invoked")
                    pyautogui.press('4')
                elif  text == 'five':
                    print("five invoked")
                    pyautogui.press('5')
                elif  text == 'six':
                    print("six invoked")
                    pyautogui.press('6')
                elif  text == 'seven':
                    print("seven invoked")
                    pyautogui.press('7')
                elif  text == 'eight':
                    print("eight invoked")
                    pyautogui.press('8')
                elif  text == 'nine':
                    print("nine invoked")
                    pyautogui.press('9')
                elif  text == 'add':
                    print("plus invoked")
                    pyautogui.press('+')
                elif  text == 'minus':
                    print("minus invoked")
                    pyautogui.press('-')
                elif  text == 'multiply':
                    print("multiply invoked")
                    pyautogui.press('*')
                elif  text == 'divide':
                    print("divide invoked")
                    pyautogui.press('/')
                elif  text == 'equal':
                    print("equal invoked")
                    pyautogui.press('=')
                elif  text == 'dot':
                    print("dot invoked")
                    pyautogui.press('.')
                elif  text == 'right parenthesis':
                    print("right parenthesis invoked")
                    pyautogui.press(')')
                elif  text == 'left parenthesis':
                    print("left parenthesis invoked")
                    pyautogui.press('(')
                elif  text == 'right bracket':
                    print("right bracket invoked")
                    pyautogui.press(']')
                elif  text == 'left bracket':
                    print("left bracket invoked")
                    pyautogui.press('[')
                elif  text == 'less than':
                    print("less than invoked")
                    pyautogui.press('<')
                elif  text == 'greater than':
                    print("greater than invoked")
                    pyautogui.press('>')
                elif  text == 'percent':
                    print("percent invoked")
                    pyautogui.press('%')
                elif  text == 'underscore':
                    print("underscore invoked")
                    pyautogui.press('_')
                elif  text == 'vertical bar':
                    print("vertical bar invoked")
                    pyautogui.press('|')
                elif  text == 'backslash':
                    print("backslash invoked")
                    pyautogui.press('\n')
                elif  text == 'quotation':
                    print("quotation invoked")
                    pyautogui.press(',')
                elif  text == 'semicolon':
                    print("semicolon invoked")
                    pyautogui.press(';')
                elif  text == 'colon':
                    print("colon invoked")
                    pyautogui.press(':')
                elif  text == 'double quotes':
                    print("double quotes invoked")
                    pyautogui.press('"')
                elif  text == 'question mark':
                    print("question mark invoked")
                    pyautogui.press('?')
                elif  text == 'marvel mark':
                    print("marvel mark invoked")
                    pyautogui.press('!')
                elif  text == 'ampersand':
                    print("ampersand invoked")
                    pyautogui.press('&')
                elif  text == 'dollar':
                    print("dollar invoked")
                    pyautogui.press('$')
                elif  text == 'number':
                    print("number invoked")
                    pyautogui.press('#')
                elif  text == 'at symbol':
                    print("at symbol invoked")
                    pyautogui.press('@')
                elif  text == 'caret':
                    print("caret invoked")
                    pyautogui.press('^')
                else:
                    print("write invoked")
                    pyautogui.write(text)

                    
             except:
                print('sorry could not recognize your voice')
            
       

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
