    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    # Read image
    filename = 'cameraman.jpg'
    img = plt.imread(filename)

    # gaussian & laplacian filter
    g_filter = cv2.getGaussianKernel(ksize=3, sigma=1)
    g_filter = g_filter * g_filter.T

    l_filter = np.array([1, -2, 1])
    l_filter = l_filter * l_filter.T

    LoG_filter = l_filter * g_filter
    dff = g_filter * l_filter

    # for DoG
    g_filter2 = cv2.getGaussianKernel(ksize=3, sigma=3)
    g_filter3 = cv2.getGaussianKernel(ksize=3, sigma=7)
    g_filter2 = g_filter2 * g_filter2.T
    g_filter3 = g_filter3 * g_filter3.T
    DoG_filter = g_filter - g_filter2
    DoG_filter2 = g_filter - g_filter3

    dst = cv2.filter2D(img, -1, LoG_filter)
    dst2 = cv2.filter2D(img, -1, dff)
    dst3 = cv2.filter2D(img, -1, DoG_filter)
    dst4 = cv2.filter2D(img, -1, DoG_filter2)
    ###


    # Plot images
    plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(dst, cmap='gray'), plt.title('LoG filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(dst2, cmap='gray'), plt.title('dff')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(dst3, cmap='gray'), plt.title('DoG')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(dst4, cmap='gray'), plt.title('DoG2')
    plt.xticks([]), plt.yticks([])

    plt.show()