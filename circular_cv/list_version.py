import cv2
import numpy
import matplotlib

def show_versions():
    print(f"{cv2.__version=}")
    print(f"{numpy.__version=}")
    print(f"{matplotlib.__version=}")