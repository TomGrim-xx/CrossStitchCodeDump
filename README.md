# CrossStitchCodeDump

This is a repository for dumping random pieces of code I used to generate my giant playmat cross stitch project.


The first piece of code is a python script that takes a source image and a file of DMC colors and creates an output image in a palette of DMC colors.
with a weighted nearest neighbor HSV matching.
There are 3 parameters for weighting how much the Hue/Saturation/Values affect the nearest neighbor matching. 
I believe I used something like .1, .1, 1.5 for the result pattern image and it's quite frankly a lot of trial and error.

>python cross-stitch-values.py source.png output.png .1 .1 1.5

Note this is in python 2, so good luck.

