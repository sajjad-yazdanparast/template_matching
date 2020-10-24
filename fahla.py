
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class TemplateMatcher :
  def __init__(self, path_to_big_image, path_to_query ,threshold=0.4):   
    # read images
    self.rgb_image = mpimg.imread(path_to_big_image)  
    self.query = cv.imread(path_to_query,0) 
    self.gray_image = cv.cvtColor(self.rgb_image, cv.COLOR_BGR2GRAY)

    self.threshold = threshold 

  def match(self) :
    w, h = self.query.shape[::-1]
    res = cv.matchTemplate(self.gray_image,self.query ,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= self.threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(self.rgb_image, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
    plt.imshow(self.rgb_image)

  def save_fig(self,path_to_save):
    cv.imwrite(path_to_save,self.image_rgb)

path_to_big_image = '/content/drive/My Drive/computer vision/SIFT/high_resolution.jpg'
path_to_query1 = '/content/drive/My Drive/computer vision/SIFT/smal_image.png'
tm = TemplateMatcher(path_to_big_image=path_to_big_image, path_to_query=path_to_query1)
tm.match()

path_to_query2 = '/content/drive/My Drive/computer vision/SIFT/smal_image2.png'
tm2 = TemplateMatcher(path_to_big_image=path_to_big_image, path_to_query=path_to_query2)
tm2.match()

plt.imshow(tm2.query)

plt.imshow(tm.query)