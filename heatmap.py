import numpy as np
import matplotlib.pyplot as plt # Plotting processed images
from skimage import io 
import imageio.v2 as iio # Python library to read/write a wide range of image data
from sklearn.cluster import KMeans # K-Means clustering algorithm

# CONSOLIDATED HEATMAPPER FUNCTION
# --------------------------------
def heatmapper(img):
    # Turn image into a list of pixels to prepare for k-means, so we can form 4, reproducible clusters based on pixel similarity
    # to assign colors
    img_list = img.flatten().reshape(img.shape[0] * img.shape[1], img.shape[2]) # Number of total RBG pixels, 3-dimensional RGB pixels
    kmeans = KMeans(n_clusters=5, random_state=0).fit(img_list)
    clusters = [[245,16,98], [0,4,100], [0,117,197], [212,188,0], [73,192,28]] # pink, dark blue, light blue, yellow, green

    # Make color assignments to pixels, then reshape back to the original image shape
    assgned_list = []
    for i in kmeans.labels_:
        assgned_list.append(clusters[i])
    out = np.reshape(assgned_list, img.shape)
    
    # Plot/display test image
    plt.imshow(out, interpolation='lanczos')
    plt.show()


# TESTS
# -----
ty = iio.imread("tyler.jpeg")
heatmapper(ty)
steve = iio.imread("steve.jpeg")
heatmapper(steve)
dog = iio.imread("dog.jpg")
heatmapper(dog)
bg = iio.imread("bg.jpeg")
heatmapper(bg)
drake = iio.imread("drake.jpeg")
heatmapper(drake)

