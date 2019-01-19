
#Convert some PNG into the colors of cross stitch things we need and maybe output a picture for it :)
#Parameters are 1) Input PNG, 2) Output PNG file, 3/4/5) HSV weighting for tweaking nearest neighbor. Try 0.1 to 1.0. I think my original image was done with .1 .1 1.5


from PIL import Image
import convert
import sys
import colorsys


inputFile = None
outputFile = None
weights = [1.0, 1.0, 1.0]

inputFile = sys.argv[1]
outputFile = sys.argv[2]
weights[0] = float(sys.argv[3])
weights[1] = float(sys.argv[4])
weights[2] = float(sys.argv[5])
stitch_threshold = int(sys.argv[6])



#img_file = "/home/elventhief/magicpics/chandra scaled.png"
#output_file = "/home/elventhief/magicpics/chandra pattern.png"
img_file = inputFile
output_file = outputFile

img = Image.open(img_file)

imageW = img.size[0]
imageH = img.size[1]
new_img = Image.new("RGBA", [imageW, imageH])
print (img.mode)

color_list = {}
color_count = {}
img.load()
print (img.getcolors())


color_file = "/home/elventhief/magicpics/dmc_colors.txt"
#color_file = "/home/elventhief/magicpics/chandra_colors.txt"


dmc_list = []

with open(color_file, 'r') as colorFile:
	for line in colorFile:
		values = line.split(",")
		
		point = [0,0,0, int(values[2]), int(values[3]), int(values[4]), values[5], values[0], values[1]]
		hsl = convert.rgb_to_hsl([point[3], point[4], point[5]])
		#hsl = colorsys.rgb_to_hls(point[3]/255.0, point[4]/255.0, point[5]/255.0)
		point[0] = hsl[0]
		point[1] = hsl[1]
		point[2] = hsl[2]
		print (point[0], point[1], point[2])
		dmc_list.append(point)	


#dmc_list = [[0,0,0], [255,0,0], [255,255,0], [0,0,255],[255,125,0],[255,255,255]]
	

#calculate how many times we use each color...
color_collection_good = False
while color_collection_good == False:
	for y in range(0, imageH):
		for x in range(0, imageW):
			offset = y*imageW +x
			xy = (x, y)
			rgb = img.getpixel(xy)		
			colour = convert.closest_match(rgb, dmc_list, weights)		
			color = (colour[3], colour[4], colour[5])
			print (xy, color)
			#for i in range (0,5):
			#	for j in range(0,5):
			#		newxy = xy[0] *5 +i, xy[1] * 5 + j
			#		new_img.putpixel(newxy, color)
			#newxy = xy[0] *5 +2, xy[1] * 5	
			#new_img.putpixel(newxy, (0,0,0))
			#newxy = xy[0] *5 +4, xy[1] * 5+2
			#new_img.putpixel(newxy, (0,0,0))
			new_img.putpixel(xy, color)
			#new_img.putpixel(xy, rgb)
			
			
			
	
	color_collection_good = True
	#color_set = new_img.getcolors()
new_img.save(output_file)
while False:
	print (len(color_set))
	color_set.sort()
	for color in color_set:
		if color[0] >= 10:	
			print (color)
			for dmc in dmc_list:
				(match) = (dmc[3], dmc[4], dmc[5], 255)
				if match == color[1]:					
					print (dmc[7])
					print (", ")
					print (dmc[8])
					print (", ")
					print (dmc[3])
					print (", ")
					print (dmc[4])
					print (", ")
					print (dmc[5])
					print (", ")
					print (dmc[6])
					
		
	
	color_collection_good = True
		
		
		
	


#new_img = new_img.convert("P")
new_img.save(output_file)

	
	
		
