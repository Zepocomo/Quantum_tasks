### description of the model
This code defines a UNet model for image segmentation using Keras. UNet is a convolutional neural network architecture used for biomedical image segmentation. 
The code starts by defining a function unet_model which takes the input image size as an argument. 
The input image is passed through the network in a contracting path that consists of convolutional and pooling layers that downsample the image. 
The output from the contracting path is then passed through an expanding path that consists of transposed convolutional layers that upsample the image. 
The final output of the network is a binary mask that corresponds to the segmentation of the input image.

### what I did with data 
1. It reads a raster image and its metadata using Rasterio library, and loads a shapefile containing polygon masks using Geopandas library.

2. It uses Rasterio library to mask the raster image with each polygon mask in the shapefile.

3. It transforms the polygons from the shapefile's coordinate reference system (CRS) to the raster image's CRS.

4. It uses Rasterio library to save each masked image as a PNG file.

5. It rasterizes the polygons into a binary mask with the same shape as the raster image.

6. It slices the raster image and mask into smaller pieces with resolution 64x64 (**important:** when we using Unet, the image must be divideble by **32**).

7. It splits the sliced data into training and validation sets.

8. It preprocesses the sliced data by taking the mean of the color channels of the images that convert RGB to binary image, and expanding the dimension of the masks to make same  dimension as the image.

### what I think about my code
Actually, the model gives a bad performance, because it needs:
1. to handling Imbalanced Classes (images with erosion is minority in our data)

2. of course use more Epoch (my computational opportunities are limited)

3. also Regularization: Regularization techniques, such as L1 and L2, can help to prevent overfitting and improve model generalization.

4. hyperparameter tuning 

5. find best model evaluation

6. reduce noise on images

### my proposals
I'm not specialized in CV so good, but I think that we can work with sun rays by evaluating theirs angle, that can help with illumination and don't give model thing that same lands with different photo time is different images

P.S. I know that I saw very little part of data visualization, it's because I did not have enough time to do it, so I explain the absence of any research papers
