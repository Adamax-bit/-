# Импорт библиотеки компьютерного зрения
import cv2  
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')  
  
  
# Захват видеопотока  
cap = cv2.VideoCapture(0)  
  
# Запуск цикла при успешном захвате  
while 1:  
  
    # чтение кадров
    ret, img = cap.read()  
  
    # конвертация каждого кадра в шкалу серого цвета 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

    # Обнаружение лиц разных размеров в данном нам кадре
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
  
    for (x,y,w,h) in faces:  
        # построение прямоугольника вокруг мордочки 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w]  
        roi_color = img[y:y+h, x:x+w]  
  
  
    # вывод  
    cv2.imshow('img',img)  
  
    # Ожидание ESC для выхода 
    k = cv2.waitKey(30) & 0xff
    if k == 27:  
        break
  
# Закрытие окна 
cap.release()  
  
# Освобождение памяти
cv2.destroyAllWindows()  