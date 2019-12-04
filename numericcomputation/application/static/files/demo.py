import cv2


x=cv2.imread("solution10.png")

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        l=list(x[i][j])
        if l<[250,100,100]:
            x[i][j]=[255,255,255]
        else:
            x[i][j]=[0,0,0]

cv2.imwrite("solution10.jpg",x)