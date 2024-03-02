# heatmappr

CS 131: Computer Vision
Small graphic design tool for making thermal heat map effect on images. 
As far as inspiration, I wanted to mimic the graphic design effect achieved on the cover of music group Brockhampton’s album “Iridescence” as shown below.
![image](https://github.com/bempong/heatmappr/assets/53280320/2c6b6dd9-4e56-4c2b-92bd-599243c6fe58)

After reviewing literature/resources regarding image filtering, I realized that I could take advantage of the k-means clustering algorithm and apply it to the pixels in an image so I could create these “neighborhoods” of pixel groupings based on their similarity to one another, label them by color, and then recreate the image with these customized color boundaries. This algorithm is essentially the main engine of my “heatmapper()” image filtering function. Overall, I took advantage of the ImageIO Python library and the SciKit Python library's K-Means clustering functionality to perform these image processing tasks. 

Example outputs:
![image](https://github.com/bempong/heatmappr/assets/53280320/64b97356-3825-4967-916e-08672cce19ab)

