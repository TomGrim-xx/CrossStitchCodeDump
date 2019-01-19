
import math
import colorsys

def rgb_to_int(rgb):
	red = rgb[0]
	green = rgb[1]
	blue = rgb[2]
	
	result = red * 255 * 255
	result += green * 255
	result += blue
	return result
	
	
# http://130.113.54.154/~monger/hsl-rgb.html	
def rgb_to_hsl(rgb):
	red = float(rgb[0]) /255.0
	green = float(rgb[1]) / 255.0
	blue = float(rgb[2]) / 255.0
	
	maxv = red
	minv = red
	if (green > maxv): maxv = green
	if (green < minv): manv = green
	if (blue > maxv): maxv = blue
	if (blue < minv): minv = blue
	
	L = (maxv + minv) / 2.0
	if maxv == minv:
		S = 0
		H = 0
		return [H, S, L]
	if L < 0.5:
		S = (maxv - minv)/ (maxv + minv)
	if L >= 0.5:
		S = (maxv - minv)/(2.0 - maxv - minv)
	
	if maxv == red: 
		H = (green - blue)/(maxv-minv)
	if maxv == green:
		H = 2.0 + (blue-red)/(maxv-minv)
	if maxv == blue:
		H = 4.0 + (red-green)/(maxv-minv)
	
	#This is going to leave H as a 0 to 6 value or something....
	hsl = [H, S, L]
	
	return hsl
	
#Semi-stolen from wikipedia
def hsl_to_rgb(hsl):
	hue = hsl[0]
	saturation = hsl[1]
	lightness = hsl[2]
	
	chroma = (1 - abs(2*lightness - 1)) * saturation
	H = hue #/60
	X = 0
	if H != None:
		X = chroma*(1 - abs(H%2 - 1))
	else:
		rbg = [0,0,0]
		return rgb
	
	if (H < 1):
		rgb = [chroma, X, 0]
	elif (H < 2):
		rgb = [X, chroma, 0]
	elif (H < 3):
		rgb = [0, chroma, X]
	elif (H < 4):
		rgb = [0, X, chroma]
	elif (H < 5):
		rgb = [X, 0, chroma]
	elif (H < 6):
		rgb = [chroma, 0, X]
		
	m = lightness - 0.5*chroma
	rgb = [rgb[0] + m, rgb[1] + m, rgb[2] + m]
	rgb = [255 * rgb[0], 255* rgb[1], 255*rgb[2]]
	rgb[0] = int(rgb[0])
	rgb[1] = int(rgb[1])
	rgb[2] = int(rgb[2])
	return rgb
	
	
	
def rgb_to_hex(rgb):
	return '#%02x%02x%02x' % rgb
	
	
def gamut_distance(first, second, weights):
	a = weights[0] #1
	b = weights[1] #.5
	c = weights[2] #.75
	dist_vec = second[0] - first[0], second[1] - first[1], second[2] - first[2]	
	sqrd_dist =  a * dist_vec[0] * dist_vec[0] + b * dist_vec[1] * dist_vec[1] + c * dist_vec[2] * dist_vec[2]
	#print (math.sqrt(sqrd_dist))
	return math.sqrt(sqrd_dist)
	
	
	
def closest_match(rgb_color, color_list, weights):
	#convert RGB to HSL version, then compare to our list of "known" colors
	hsl_to_match = rgb_to_hsl(rgb_color)
	#hsl_to_match = colorsys.rgb_to_hls(rgb_color[0]/255.0, rgb_color[1]/255.0, rgb_color[2]/255.0)
	#print(hsl_to_match)
	match_distance = 1000000 #impossibly large distance to match a color
	best_match = None
	
	for color in color_list:
		#hsl_color = [color[0]/255.0, color[1]/255.0, color[2]/255.0]
		#print (hsl_color)
		g_dist = gamut_distance(hsl_to_match, color, weights)
		if g_dist < match_distance:
			best_match = color
			match_distance = g_dist
	
	return best_match
	
	
	
