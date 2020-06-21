import numpy as np

class PCKH(object):
    def __init__(self, targets, preds, pck_ratio=0.2):
        self.targets = targets
        self.preds = preds
        self.pck_ratio = pck_ratio
    
    def get_heatmap_accuracy(self, threshold):
        pred = np.unravel_index(self.preds.argmax(), self.preds.shape)
        targets = np.unravel_index(self.targets.argmax(), self.targets.shape)

        dist = math.sqrt((pred[0] - gt[0]) ** 2 + (pred[1] - gt[1]) ** 2)
        if dist <= threshold:
            return 1, dist, (pred[0], pred[1])
        return 0, dist, (pred[0], pred[1])
