import torch
import torchvision
import matplotlib.pyplot as plt
from skimage import io, transform
from torch.utils.data import Dataset, DataLoader

from scipy.io import loadmat

annotation_path = "/Users/shashanks./college/code/datasets/mpii_human_pose_v1_u12_2/mpii_human_pose_v1_u12_1.mat"
dataset_path = "/Users/shashanks./college/code/datasets/mpii/images"
annots = loadmat(annotation_path)
print(anno)