import numpy as np
import matplotlib.pyplot as plt
import os 
import skimage.io as io 
from PIL import Image as im

def load_images(folder):
    images = [] 
    labels = []
    for filename in os.listdir(folder):
#         print(filename)
        image = io.imread(os.path.join(folder, filename))
        if image is not None:
            images.append(image)
            labels.append(filename[-6])
            # display_image(image)
    images =  np.asarray(images)
    return images, labels
  

def display_image(img):
    plt.figure()
    plt.imshow(img) 
    plt.show()  


def import_data():
    X_train = []  
    X_test = []   
    Y_train = []     
    Y_test = []     


def main():
    dataset,labels = load_images('./data/train/')
    # dataset = load_images('./try/')
    print(type(dataset))
    print(dataset.shape)
    # print(dataset)
    print(labels)


if __name__ == '__main__':
    main()

