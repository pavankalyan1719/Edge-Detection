import cv2
import numpy as np
import matplotlib.pyplot as plt
def show_comp(o,sobel,prewitt,roberts,canny):
    plt.figure(figsize=(10,6))
    plt.subplot(2,3,1)
    plt.imshow(o,cmap='gray')
    plt.title('Original')
    plt.axis('off')
    plt.subplot(2,3,2)
    plt.imshow(sobel,cmap='gray')
    plt.title('Sobel')
    plt.axis('off')
    plt.subplot(2,3,3)
    plt.imshow(prewitt,cmap='gray')
    plt.title('Prewitt')
    plt.axis('off')
    plt.subplot(2, 3, 4)
    plt.imshow(roberts, cmap='gray')
    plt.title('Roberts')
    plt.axis('off')
    plt.subplot(2,3,5)
    plt.imshow(canny,cmap='gray')
    plt.title('Canny')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
width = 300
height = 300

original = cv2.resize(img, (width, height))
sobel = cv2.resize(sobel_combined, (width, height))
prewitt = cv2.resize(prewitt_combined, (width, height))
roberts = cv2.resize(roberts_combined, (width, height))
canny = cv2.resize(canny_edges, (width, height))

# Save images
cv2.imwrite('monalisa.jpeg', original)
cv2.imwrite('sobel.jpg', sobel)
cv2.imwrite('prewitt.jpg', prewitt)
cv2.imwrite('roberts.jpg', roberts)
cv2.imwrite('canny.jpg', canny)
img=cv2.imread('monalisa.jpeg',0)
if img is None:
  print('Image not found')
else:
    sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
    sobel_combined=cv2.magnitude(sobelx,sobely)
    kernelx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    robertsx = np.array([[1, 0],[0, -1]])
    robertsy = np.array([[0, 1],[-1, 0]])
    
    prewittx=cv2.filter2D(img,-1,kernelx)
    prewitty=cv2.filter2D(img,-1,kernely)
    prewitt_combined=prewittx+prewitty
    
    robertsx_img = cv2.filter2D(img, cv2.CV_64F, robertsx)
    robertsy_img = cv2.filter2D(img, cv2.CV_64F, robertsy)
    roberts_combined = cv2.magnitude(robertsx_img,robertsy_img)
    canny_edges=cv2.Canny(img,100,200)
    show_comp(img,sobel_combined,prewitt_combined,roberts_combined,canny_edges)
