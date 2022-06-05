import cv2
import numpy as np

def closest(rgb):
    colornames = {

        "red": [231, 76, 60],
        "orange": [230, 126, 34],
        "yellow": [247, 220, 111],
        "green": [35, 155, 86],
        'brown': [155, 75, 0],
        'pink':[255, 0, 255],

        "purple": [125, 60, 152]
    }
    #make the colors list
    colorlist = []
    for col in colornames:
        colorlist.append(colornames[col])
    #make them np array for math process
    colors = np.array(colorlist)
    rgb = np.array(rgb)

    #euclidean distance between the color vectors
    distances = np.sqrt(np.sum((colors - rgb) ** 2, axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    #return closest
    for col in colornames:
        if smallest_distance.tolist()[0] == colornames[col]:
            return col
    #else return black
    return "black"

def find_color(cam):
    ret, img = cam.read()
    if ret:
        # shapes
        height, width = img.shape[:2]

        # region of interest:
        roi_size = 100  # (100x100)
        roi_img = img[int((height - roi_size) / 2):int((height + roi_size) / 2),
                  int((width - roi_size) / 2):int((width + roi_size) / 2)]
        # mean values
        mean_blue = int(np.mean(roi_img[:, :, 0]))
        mean_green = int(np.mean(roi_img[:, :, 1]))
        mean_red = int(np.mean(roi_img[:, :, 2]))
        # find closest color according to mean rgb
        color = closest((mean_red, mean_green, mean_blue))
        return color
    return "not_available"

# cam = cv2.VideoCapture(0)

