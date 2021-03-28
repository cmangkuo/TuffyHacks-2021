from PIL import Image
import easygui

def img2RGB(x, y):
	## Load image
	file = easygui.fileopenbox()
	img = Image.open(file)
	img = img.resize((x,y))
	pixels = list(img.getdata())
	return pixels
	
	
if __name__ == "__main__":
	matrix = img2RGB(800,600)
	index = 0
	for x in range(800):
		row = []
		for y in range(600):
			row.append(matrix[index])
			index += 1
		print(row)