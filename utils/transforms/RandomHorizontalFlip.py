import cv2
import numpy as np

class RandomHorizontalFlip(object):
    def __init__(self, prob=0.5):
        self.prob = prob

    def __call__(self, sample):
        img, keypoints, visible_keypoints = sample["image"], sample["keypoints"], sample["visible_keypoints"]
        img_center = img.shape[:2][::-1] / 2
        