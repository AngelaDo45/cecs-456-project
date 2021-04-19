import numpy as np
import matplotlib.pyplot as plt
import os 
import skimage.io as io 
from PIL import Image as im

def load_images(folder):
    images = [] 
    labels = []
    for filename in os.listdir(folder):
        # print(filename)
        image = io.imread(os.path.join(folder, filename))
        if image is not None:
            if filename[-5] == 'L':
                images.append(image)
                # images.append(image)
                labels.append(filename[-6])
            # display_image(image)
    images =  np.asarray(images)
    labels = np.asarray(labels)
    return images, labels
  

def display_image(img):
    plt.figure()
    plt.imshow(img) 
    plt.show()  


def main():
    # X_train, X_test = load_images('./data/train/')
    # Y_train, Y_test = load_images('./data/test/')

    # Testing the image with one or two image in a folder
    X_train, X_test = load_images('./try/')

    print("X training dataset: ", X_train.shape)
    print("X testing dataset: ", X_test.shape)
    # print("Y training dataset: ", Y_train.shape)
    # print("Y testing dataset: ", Y_test.shape)

    fig, axes = plt.subplots(2, 2, figsize=(8,8))
    ax = axes.ravel()
    for i in range (len(X_train)):  # X_train
        ax[i].imshow(X_train[i])
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

