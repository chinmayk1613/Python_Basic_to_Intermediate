import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(1000,1000))
    cv2.imshow("Hey",re)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
