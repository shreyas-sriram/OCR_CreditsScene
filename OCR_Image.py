import cv2
import sys
import pytesseract
 
if __name__ == '__main__':

  print("Enter name to search: ")
  name = input()

  nameList = []
  found = 0
  count = 0
  i = 0

  vid = cv2.VideoCapture('video0.mp4')

  while(vid.isOpened()):
    ret, frame = vid.read()

    count = (count+1)%100
    i = i+1

    if count==1:
      # Uncomment the line below to provide path to tesseract manually
      # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
     
      # Define config parameters.
      # '-l eng'  for using the English language
      # '--oem 1' for using LSTM OCR Engine
      config = ('-l eng --oem 1 --psm 11')
     
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      frame = cv2.bitwise_not(gray)
     
      # Run tesseract OCR on image
      text = pytesseract.image_to_string(frame, config=config)

      text = text.replace("\n\n","\n")
      nameList = text.split("\n")

      cv2.imwrite('frame' + str(i) + '.jpg',frame)

      if name in nameList:
        print("Yes")
        found = 1
        break

  if not found:
    print("No")