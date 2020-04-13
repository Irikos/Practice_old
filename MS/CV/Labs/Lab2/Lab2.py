# imports
import cv2 as cv
import numpy as np
import glob
import os


# read the images name
base_folder = "./files"
images_names = glob.glob(os.path.join(base_folder, "image_*.jpg"))
idx_image = 1
SHOW_INTERMEDIATE_RESULTS = True
NUM_OF_SECONDS = 0

idx_image += 1

print("Detecting edges on the %d image..." % idx_image)