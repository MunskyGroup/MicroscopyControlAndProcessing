# Microscopy Control And Image Processing

Kyle was here.

This project creates a framework for high level automation by using an **Acquire-Process-Decide** mechanism. These mechanisms can be used to create different **acquisition** tickets which aquire data, easy to implement **image processors** that create data from images, and **decisions** which create data and propose new acuisitions.

This repository can also use multiple machines to accelerate compute times and use image emulators to mimic the behavior of a microscope.

![alt text](https://github.com/michaelpmay/MicroscopyControlAndProcessingMe/blob/main/content/files/apd.png)
> *Acquire-Process-Decide Pipelines create a framework for high level automation by builing up on automations created by ```MicroManager``` and ```PycroManager```.*

### Requirements:
...

[](content/files/Intro.png)

[**Installation**](content/pages/installation.md)

[**Configure Software Settings for Demo or Real Systems (Distributed Computing, Remote Storage, User Credentials, Logging Verbosity, Device Management)**](content/pages/configure.md)

## Below are several Jupyter notebooks to help the user become acquainted with the functionality: 

[**Example 1: Getting Started Demo**](notebooks/Example1_Getting_Started_Demo.ipynb)

[**Example 2: Acquiring Sequences of Images Demo**](notebooks/Example2_Acquiring_Sequences_Of_Images_Demo.ipynb)

[**Example 3: Adding Logic and Processing**](notebooks/Example3_Adding_Logic_And_Processing.ipynb)

[**Example 4: Adding Image Post-processing**](notebooks/Example4_Adding_Image_PostProcessing.ipynb)

[**Example 5: Making Decisions and Adaptive Acquisitions**](notebooks/Example5_MakingDecisionsAndAdaptiveAcquisitions.ipynb)

[**Example 6: Using the Emulator**](notebooks/Example6_Using_The_emulator.ipynb)

## The rest of the page will discuss a real application of the automation

A three color HiLo microscope with a galvo controlled laser was developed and used for the development of this code. This microscope can acquire 2D images in three colors using inclined light to increase the signal to noise ratio. Device drivers were managed using ```MicroManager```, but interfaces for the control of outside devices (like lasers and custom ```FilterWheels``` and ```GalvoSystems```) were developed. 

![alt text](https://github.com/MunskyGroup/MicroscopyControlAndProcessing/blob/main/content/files/cartoon.png)
> *The schematic of the system shows a three laser HiLo microscope with a galvo laser*

A library of image acquisition can be found [**here**](content/pages/modeling.md), which describes an ```AcquisitionTicket```, that describes all variables and callback functions needed to perform an automated acquisition. This library contains pre-writted tickets that describe a variety of common acquisitions (including loose grids, tight grids, XY position sequences, and  XYZ position sequences).

The Acquire-Process-Decide Pipeline was developed to find 25 cells within a region. 

Similarly libraries were written for common ```ImageProcessPipeline```(s), and ```Decisions```, which take images and create and data, and take take data to propose new acquisitions.

![alt text](https://github.com/MunskyGroup/MicroscopyControlAndProcessing/blob/main/content/files/emulated.png)
> *Automated data acquisitions using the image emulator. An eight by eight grid of images
was acquired using the ‘grid search’ procedure using an image emulator that replaces acquired images with
emulated ones. (A). Images which were believed to contain three or more nuclei using Cellpose were
highlighted in green boxes, and an acceptance ratio was measured to be twenty-three out of sixty-four total
images. (B) Images of Cellpose nuclei masks show good match with expectation, but missing a dim nuclei
in the bottom right edge. (C) Correlations (R2 = 0:822) and sensitivity ( eps = 0:870) suggest accurate
determination of the number of nuclei.*

The loose grid image searching pipeline was run on the real microscope to analyze its performance.

![alt text](https://github.com/MunskyGroup/MicroscopyControlAndProcessing/blob/main/content/files/real.png)
> *Automated data acquisitions of fluorescently labeled mRNA. An eight by eight grid of
images was acquired using the ‘grid search’ procedure using smFISH stained cytoplasmic GAPDH exons.
(A) Images which were believed to contain three or more cells using the Cellpose cytoplasm model were
labeled in green. Image acceptance ratios (42/64) and acquisition times are shown in the bottom. (B)
Correlations (R2 = 0:550) and sensitivity ( eps = 0:757) of the Cellpose detection method can be seen. (C)
Correlations (R2 = 0:631) and sensitivity ( eps = 0:804) of the mean intensity detection method show similar
accuracy and sensitivity to Cellpose for this set of images.*

A puncta detection method was developed to idenfity images with bright spots to create a framework for identifying phenotypes in images and using an ```ImageDetection``` method to accept or reject images. In this example a detection method was created for identifying cells with puncta using the Laplacian of Gaussians and re-imaging positions which were estimated to have at least one puncta. 

![alt text](https://github.com/MunskyGroup/MicroscopyControlAndProcessing/blob/main/content/files/puncta.png)
>  *Median image processing on two slides. The mean intensity method and the Cellpose identification
method were compared using grid searches on two different slides with the same imaging conditions.
(A) The mean intensity method was used to determine which regions of interest (ROIs) to keep for re-imaging.
Images were predicted to have three or more cells if the median intensity was greater than 2500.
Scatter plots of slide one data and slide two data show large discrepancy between the two slides. (B) The
same images were then analyzed using Cellpose. Scatter plots of slide one and slide took look much more
uniform.*
