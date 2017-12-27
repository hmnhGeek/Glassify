import cv2
import numpy as np
import os

class utilities(object):

    def load_image(self, image_addr):
        return cv2.imread(image_addr)

    def translate(self, image, x, y):
        numpy_array = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv2.warpAffine(image, numpy_array, (image.shape[1], image.shape[0]))
        return shifted

    def display(self, image):
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rotate(self, image, angle, scale = 1.0):
        height, width = image.shape[:2]
        center = (width//2, height//2)

        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv2.warpAffine(image, M, (width, height))
        return rotated_image

    def resize(self, image, cols = None, rows = None):

        if cols == None and rows == None:
            return image
        else:
            height, width = image.shape[:2]
            aspect_ratio = width*height**(-1)

            if rows == None and cols != None:
                new_height = int(cols*aspect_ratio**(-1))
                dimension = (cols, new_height)
                newimg = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)

            elif cols == None and rows != None:
                new_width = int(rows*aspect_ratio)
                dimension = (new_width, rows)
                newimg = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)

            elif (cols, rows) != (None, None):
                if float(cols)/float(rows) == aspect_ratio:
                    dimension = (cols, rows)
                    newimg = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
                else:
                    return image

            return newimg

    def flip(self, image, mode = 1):
        if mode == 1:
            newimg = cv2.flip(image, 1)
        elif mode == 0:
            newimg = cv2.flip(image, 0)
        elif mode > 1:
            newimg = image
        else:
            newimg = cv2.flip(image, mode)

        return newimg

    def crop(self, image, sliceX, sliceY):
        height, width = self.image_dimensions(image)

        if len(sliceX) != 2 or len(sliceY) != 2:
            return image
        else:
            startx, endx = sliceX[0], sliceX[1]
            starty, endy = sliceY[0], sliceY[1]
            
            if startx >= 0 and endx <= width and starty >= 0 and endy <= height:
                croppedimage = image[starty:endy, startx:endx]
                return croppedimage
            else:
                return image

    def image_dimensions(self, image):
        return image.shape[:2]

    def save_image(self, image, location, filename):
        cv2.imwrite(os.path.join(location, filename), image)
