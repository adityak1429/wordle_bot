import cv2
import numpy as np
import pytesseract
import string
import glob

# Search for PNG files in the current directory
png_files = glob.glob('*.png')

from collections import Counter
kernel = np.array([[-1., -1., -1.], [-1., 9., -1.], [-1., -1., -1.]])
# Define a 3x3 kernel with all elements as 1s
kernel2 = np.ones((3, 3), np.float32) / 9
# Load image
image = cv2.imread(png_files[0])

# Define the scale factor by which you want to increase the resolution
scale_factor = 2

# Resize the image using the scale factor
new_width = int(image.shape[1] * scale_factor)
new_height = int(image.shape[0] * scale_factor)
image = cv2.resize(image, (new_width, new_height))


# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply edge detection
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

# Find contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Iterate over contours
ans=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

colo=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

#ans=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
i=0
for contour in contours:
    # Approximate the contour
    epsilon = 0.05 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # If the contour has 4 vertices (a square)
    if len(approx) == 4:
        # Draw rectangle around the square
        x, y, w, h = cv2.boundingRect(approx)

        
        roi = image[y+30:y + h-30, x+30:x + w-30]
        # Convert the region of interest (ROI) to HSV color space
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Calculate the histogram of the H (hue) channel
        histogram = cv2.calcHist([hsv_roi], [0], None, [256], [0, 256])

        # Find the index of the peak in the histogram
        dominant_color_index = np.argmax(histogram)
        
        if dominant_color_index==111:
            colo[int(i/5)][i%5]+='b'
        elif dominant_color_index==22:
            colo[int(i/5)][i%5]+='y'
        elif dominant_color_index==48:
            colo[int(i/5)][i%5]+='g'
        roi = gray[y+30:y + h-30, x+30:x + w-30].copy()
        # Apply Gaussian blur to reduce noise
        new_width = int(roi.shape[1] * 2)
        new_height = int(roi.shape[0] * 2)
        roi = cv2.resize(roi, (new_width, new_height))
        roi=cv2.filter2D(roi, -1, kernel)
        roi=cv2.dilate(roi, kernel2)
        roi=cv2.dilate(roi, kernel2)
        roi-=255
        # cv2.imshow('Detected squares', roi)
        # cv2.waitKey(1000)
        # Use pytesseract to perform OCR on the ROI
        # Create a whitelist of characters (include both uppercase and lowercase alphabets)
        whitelist = string.ascii_letters
        
        for q in range(10,5,-1):
            if q==2:
                continue
            # Specify the config for Tesseract OCR
            config = f'--psm {q} -c tessedit_char_whitelist={whitelist}'
            #config=f'--psm {q}'
            text = pytesseract.image_to_string(roi, lang='eng', config=config)
            text = text.replace('\x0c', '')
            text = text.replace('\n', '')
            # Print the detected text
            ans[int(i/5)][i%5]+=text.upper()
        i+=1

# Display the image
#cv2.imshow('Detected squares', image)
def fun(i):
    s=''
    for c in i:
        s+=c
    return s
x=[i for i in ans if i !=['','','','','']]
for i in range(len(x)):
    x[i]=[Counter(fun(j)).most_common(1)[0][0] for j in x[i]]
    x[i]=x[i][::-1]
fin_ans=[fun(i) for i in x]
fin_ans=fin_ans[::-1]
print(len(fin_ans))
for i in fin_ans:
    print(i, end=' ')
print()
x=[fun(i[::-1]) for i in colo if i !=['','','','','']]
x=x[::-1]
for i in x:
    print(i, end=' ')
