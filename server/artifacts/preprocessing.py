
import numpy as np  
import cv2
import pywt



face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

def get_cropped_img(img_path) :
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_img,1.3,5)
    final_faces = []
    for (x,y,w,h) in faces :
        r_gray = gray_img[y:y+h,x:x+w]
        r_color = img[y:y+h,x:x+w]
        eye = eye_detector.detectMultiScale(r_gray)
        if len(eye) >= 2 :
            final_faces.append(r_color)
    return final_faces

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255;
    # compute coefficients 
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)  
    coeffs_H[0] *= 0;  

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)

    return imArray_H

# im_har = w2d(cropped_img,'db1',5)

def preprocessing(image_path):
    # print(image_path.replace("/artifacts", ""))
    faces = get_cropped_img(image_path)
    if len(faces) != 0 :
        im_har = w2d(faces[0],'db1',5)
    
        