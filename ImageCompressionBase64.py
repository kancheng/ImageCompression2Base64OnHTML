import base64
import cv2
import imutils

with open('Test.jpg','rb') as f:
    base64_data = base64.b64encode(f.read())
f.close()

base64_data_str = str(base64_data)
base64_head = 'data:image/jpg;base64,'
fname = base64_head + base64_data_str[2:-1]
print("Original image base64 encoding length : %d"%len(fname))

img = cv2.imread('Test.jpg')
h,w,_ = img.shape
print("h",h)
print("w",w)
print("_",_)
img_resize = imutils.resize(img, height=(h//4))
h,w,_ = img_resize.shape
print("h",h)
print("w",w)
print("_",_)
image = cv2.imencode('.jpg',img_resize)[1]
image_code = base64_head+str(base64.b64encode(image))[2:-1]
print("OpenCV resizes the image to base64 length : %d"%len(image_code))
print(image_code)

html = "<!DOCTYPE html><html><head><title>Base64</title></head><body><h1>Images</h1><p>Original Image.</p><img src='Test.jpg' alt='Image' /><p>Image Compression to Base64.</p><img src='" + image_code + "' alt='Image' /></body></html>"

html_path = "./index.html"
file = open(html_path, 'w')
file.write(html)
file.close()
