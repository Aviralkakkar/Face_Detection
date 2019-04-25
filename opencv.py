import cv2
cam = cv2.VideoCapture(0)
fd=cv2.CascadeClassifier('C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
while True:
    r,i=cam.read()
    cv2.imshow('image',i)
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j)
    '''ek frame se ek se jada faces detect krne ke liye'''
    for(x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),4)
 #   r,g=cv2.threshold(j,120,255,0)
  #  cv2.imshow('image3',g)
    ''' if 0 then 255-white and 0 is black... if 1 then 255-black  and 0 white'''
    '''3D SE 2D IMAGE KRENGE TOH SAARI COLOR LAYERS KA AVG KRLENGE.... (GRAY SCALE BOLTE HAI)'''
    cv2.imshow('image2',i)
    k=cv2.waitKey(150)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        del cam
        '''variables delete krdeta hai'''
        break
    print(face)
    

# detect all parts of face.
# body moving towards camera or away
