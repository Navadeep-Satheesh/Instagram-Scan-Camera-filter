import cv2 as cv 
import numpy as np 
import os 


camera = cv.VideoCapture(0) 



final = camera.read()[1]
rows  = len(final)
print(rows)
# final = np.array([])
line = [[0,0,255] for i in range(final.shape[1])]
frame_no = 0
# print(frame[0])
while frame_no < rows:
    # break
    frame = camera.read()[1]
    frame = cv.flip(frame,1)
    # print(frame_no)
    

    final[frame_no] = frame[frame_no]
    # final = np.append(final, [(frame[frame_no])])
    frame[:frame_no] = final[:frame_no]
    frame[frame_no] = line

    cv.imshow("frame",frame)
    
    
    frame_no+=1
    
    if cv.waitKey(1) & 0xFF ==  ord("q"):
        break
    
# 
cv.imshow("frame",final)
cv.waitKey(0)

# print(final.shape)
# print(final)

cv.imwrite(f"image{len(os.listdir(os.getcwd()))}.png", final)
