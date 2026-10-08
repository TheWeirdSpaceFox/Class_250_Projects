import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

###############################################################
#     Demo showing how filtering works
###############################################################

# filter function to apply the kernel to the image
def filter(image, kernel):
    #create output image
    output = np.zeros(image.shape)

    #get +/- range for kernal loop
    k = kernel.shape[0] // 2


    #Two nested for loops for iterating through all pixels in given image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # print(f"Image value as {i},{j}: {image[i,j]}")
            # normalization value
            norm = 0.0


            # Two nested for loops for iterating through kernel
            for u in range(-k, k+1):
                ii = i - u
                if 0 <= ii < image.shape[0]:
                    for v in range(-k, k+1):
                        jj = j - v
                        if 0 <= jj < image.shape[1]:
                            output[i,j] += kernel[u+k, v+k] * image[ii, jj]
                            norm += kernel[u+k, v+k]
            output[i,j] = output[i,j] / norm

    return output




if __name__ == '__main__':
    # Load the racoon image and crop it to just the racoon's face
    trash_panda = scipy.misc.face(gray=True)
    face = trash_panda[100:500, 400:900]

    # create a averaging (blur) kernel
    kernel = np.ones((9, 9)) / (9 * 9)


    # correct way to downsample = first blur, then downsample
    face_blur = filter(face, kernel)
    down_sampled_blur = face_blur[::8, ::8]

    # show the results of the blurring filter
    fig = plt.figure()
    plt.gray()
    plt.imshow(face_blur)
    plt.title("Trash Panda Face with blur (first.last.yy)")

    # show the results of the blurring then downsampled filter
    fig = plt.figure()
    plt.gray()
    plt.imshow(down_sampled_blur)
    plt.title("Trash Panda Face Correct Downsampling\n (blurred then downsampled) (first.last.yy)")

    # show the results of incorrect downsampling (for comparison)
    fig = plt.figure()
    plt.gray()
    plt.imshow(face[::8, ::8])
    plt.title("Trash Panda Face Incorrect Downsampling\n (no blur) (first.last.yy)")

    # show the plots
    plt.show()


