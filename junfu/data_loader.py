import os
from PIL import Image
from torch.utils.data import Dataset

# Define a class called KittiLoader which is a type of Dataset
class KittiLoader(Dataset):
    # Initialize the KittiLoader class with the directory of the images, the mode, and optional transforms
    def __init__(self, root_dir, mode, transform=None):
        dir = os.path.join(root_dir, 'left/')

        self.imagepath = sorted([os.path.join(dir, fname) for fname in os.listdir(dir)])
        
        if mode == 'train':
            right_dir = os.path.join(root_dir, 'right/')
            self.right_paths = sorted([os.path.join(right_dir, fname) for fname in os.listdir(right_dir)])
            
            if len(self.right_paths) != len(self.imagepath):
                print("Error: The number of left and right images is not the same.")
        
        self.transform = transform
        self.mode = mode

    # Define a method to get the length of the dataset
    def __len__(self):
        # Return how many left image paths we have
        return len(self.imagepath)

    def __getitem__(self, idx):
        # if right-paths is empty(not train mode), only read left image
        
        sample = {'left_image': Image.open(self.imagepath[idx]), 'right_image': Image.open(self.right_paths[idx])} \
                if self.right_paths else Image.open(self.imagepath[idx])

        sample = self.transform(sample) if self.transform else sample

        return sample
        


