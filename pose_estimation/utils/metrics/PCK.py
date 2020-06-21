import numpy as np

class PCK(object):
    def __init__(self, targets, preds, pck_threshold=5):
        self.targets = targets
        self.preds = preds
        self.pck_threshold = pck_threshold
    
    def get_heatmap_accuracy(self):
        pred = np.unravel_index(self.preds.argmax(), self.preds.shape)
        targets = np.unravel_index(self.targets.argmax(), self.targets.shape)

        dist = math.sqrt((pred[0] - gt[0]) ** 2 + (pred[1] - gt[1]) ** 2)
        if dist <= self.pck_threshold:
            return 1, dist, (pred[0], pred[1])
        return 0, dist, (pred[0], pred[1])
