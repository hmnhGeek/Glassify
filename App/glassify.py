import cv2
import numpy as np
from compiler.ast import flatten
import myutils, os
import argparse as ap

def split_and_swap1(img, orientation = "vertical"):
    dimension = img.shape[:2]

    canvas = np.zeros((dimension[0], dimension[1], 3), dtype = "uint8")

    if orientation == "vertical":
        first_part = img[0:dimension[0], 0:dimension[1]/2]
        second_part = img[0:dimension[0], dimension[1]/2:dimension[1]]
    return second_part, first_part

def split_and_swap2(img, orientation = "horizontal"):
    dimension = img.shape[:2]

    canvas = np.zeros((dimension[0], dimension[1], 3), dtype = "uint8")

    if orientation == "horizontal":
        first_part = img[0:dimension[0]/2, 0:dimension[1]]
        second_part = img[dimension[0]/2:dimension[0], 0:dimension[1]]
    return second_part, first_part
    
def display(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save(image, location):
    cv2.imwrite(location, image)

def glassify(addr, power, saveit = False):
    
    i1 = partition_maker1(addr, power)
    tup  = tuple(i1)
    i1 = np.concatenate(tup, axis = 1)
    save(i1, "temp.jpg")
    i2 = partition_maker2("temp.jpg", power)
    tup  = tuple(i2)
    i2 = np.concatenate(tup, axis = 0)
    utl = myutils.utilities()
    i2 = utl.rotate(i2, 180)
    cv2.imshow("Win", i2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if saveit:
        save(i2, addr+"_modified.png")
    os.remove("temp.jpg")


def partition_maker1(image_addr, count = 2):

    count = 2**count

    img = cv2.imread(image_addr)
    clips = [[img,],]

    while len(flatten(clips[-1])) != count:
        temp = []
        for arr in flatten(clips[-1]):
            temp.append(split_and_swap1(arr))

        clips.append(temp)

    return flatten(clips[-1])

def partition_maker2(image_addr, count = 2):

    count = 2**count

    img = cv2.imread(image_addr)
    clips = [[img,],]

    while len(flatten(clips[-1])) != count:
        temp = []
        for arr in flatten(clips[-1]):
            temp.append(split_and_swap2(arr))

        clips.append(temp)

    return flatten(clips[-1])


parser = ap.ArgumentParser()
parser.add_argument("-f", "--file", type = str, help = "Pass image file.", dest = "f")
parser.add_argument("-p", "--power", type = int, default = 8, help = "Pass glass effective value.", dest = "p")
parser.add_argument("-s", "--save", action = "store_true", help = "To save or not.", dest = "s")
args = parser.parse_args()

glassify(args.f, args.p, args.s)
