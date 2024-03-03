import os
from PIL import Image
from torch.utils.data import Dataset

# Define a class called KittiLoader which is a type of Dataset
class KittiLoader(Dataset):
    # Initialize the KittiLoader class with the directory of the images, the mode, and optional transforms
    def __init__(self, root_dir, mode, transform=None):
        # Set the directory where the left images are
        left_dir = os.path.join(root_dir, 'image_02/data/')
        # Get all the image file names for the left images
        # List them and sort them to make sure they are in order
        self.left_paths = sorted([os.path.join(left_dir, fname) for fname in os.listdir(left_dir)])
        
        # If we are in 'train' mode, do the same for the right images
        if mode == 'train':
            right_dir = os.path.join(root_dir, 'image_03/data/')
            self.right_paths = sorted([os.path.join(right_dir, fname) for fname in os.listdir(right_dir)])
            
            # Make sure we have the same number of left and right images
            if len(self.right_paths) != len(self.left_paths):
                print("Error: The number of left and right images is not the same.")
        
        # Save the transform provided to the class
        self.transform = transform
        # Save the mode provided to the class
        self.mode = mode

    # Define a method to get the length of the dataset
    def __len__(self):
        # Return how many left image paths we have
        return len(self.left_paths)

    # Define a method to get an item from the dataset at a certain index
    def __getitem__(self, idx):
        # Open the left image from the file path at the given index
        left_image = Image.open(self.left_paths[idx])
        
        # If we are in 'train' mode, also open the right image
        if self.mode == 'train':
            right_image = Image.open(self.right_paths[idx])
            # Create a dictionary with both images
            sample = {'left_image': left_image, 'right_image': right_image}
            
            # If a transform is set, apply it to the images
            if self.transform:
                sample = self.transform(sample)
            # Return the images (either transformed or not)
            return sample
        else:
            # If we are not in 'train' mode, just work with the left image
            if self.transform:
                left_image = self.transform(left_image)
            # Return the left image (either transformed or not)
            return left_image

