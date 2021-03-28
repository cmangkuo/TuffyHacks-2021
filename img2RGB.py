from PIL import Image
import easygui

def img2RGB(x, y):
	## Load image
	file = easygui.fileopenbox()
	img = Image.open(file)
	img = img.resize((x,y))
	pixels = list(img.getdata())
	img.show()
	
	row = []
	
	return pixels
	
	
if __name__ == "__main__":
	matrix = img2RGB(16,9)
	
	index = 0
	for x in range(16):
		row = []
		for y in range(9):
			row.append(matrix[index])
			index += 1
		print(row)