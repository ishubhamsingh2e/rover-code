import cv2 as cv
import time
import sys

image_obj = []


def stitch(img_path: list, ext: str = "jpg", out: str = "out", out_ext: str = "png") -> any:
    for i in img_path:
        img = cv.imread(i)
        image_obj.append(img)

    imgSt = cv.Stitcher_create()

    error, stiched_img = imgSt.stitch(image_obj)

    if not error:
        cv.imwrite(f"output/{out}.{out_ext}", stiched_img)
    else:
        print("can't stitch images together")


if __name__ == "__main__":
    inputs = sys.argv[1:]
    stitch(inputs)
