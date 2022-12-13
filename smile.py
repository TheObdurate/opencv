def smile(d, f_name,cam, num_photos):
    """
    The function uses 4 arguments
    
    d = specify directory for file storage
    f_name = the folder name
    cam = declare which camera to use, if uncertain start with 0 and increase by one
    until the correct camera is used
    num_photos = specify how many pictures to take
    
    """
    import cv2
    import os
    from pathlib import Path
    
    haar_file = 'haarcascade_frontalface_default.xml'

    sub_data = f_name

    ap_d = d+ '\\' + sub_data
    
    address = Path(ap_d)

    if not os.path.isdir(address):
        os.makedirs(address)

        #defining the size of images
    (width, height) = (130,100)

        #'cam' is used for deignating which camera you have attached
    
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(int(cam)) #x (1)

        # The program will loop until it has (num_photo) images of the face.
    count = 1
    while count < int(num_photos): 
        (_,im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('% s/% s.png' % (address, count), face_resize)
        count +=1

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break
