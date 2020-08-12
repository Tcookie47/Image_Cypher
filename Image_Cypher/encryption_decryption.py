from PIL import Image, ImageDraw, ImageFilter                                   #imported the required objects from the Python Image Library
import sys                                                                      #imported sys so zas to view the entire numpy array
import numpy as np                                                              #imported numpy so as to use all the array objects for matrix manipulation


def crop_center(pil_img, crop_width, crop_height):                              #function to crop the image to our desired dimensions
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def crop_max_square(pil_img):                                                   #function to crop image to the maximum size sqaure possible
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


im = Image.open('thanos.jpg')                                                   #open the data image
im_key = Image.open('test_3.jpg')                                               #open the key image
im_thumb_key = crop_max_square(im_key)                                          #crop to a square
im_thumb_key.save('key_square.jpg', quality=99)
im_thumb = crop_max_square(im)                                                  #crop to a square
im_thumb.save('data_square.jpg', quality=99)


np.set_printoptions(threshold=sys.maxsize)                                      #set the system to print the whole numpy array
im_1 = Image.open('data_square.jpg')
image_file1 = im_1.convert('1')                                                 #convert data image to black and white
im_2 = Image.open('key_square.jpg')
image_file2 = im_2.convert('1')                                                 #convert key image to balck and white


ar1 = np.array(image_file1)                                                     #make the data image a numpy array
ar2 = np.array(image_file2)                                                     #make the key image a numpy array
print('yeet')

original=ar1.astype(np.int)                                                     #map the data array to 0's and 1's
key1=ar2.astype(np.int)                                                         #map the key array to 1's and 0's
#key2 = key1.T[0]
print('yeet2')
key3 = abs(key1 - key1.T[0])
print('yeet3')

#key2 = key1[0]                                                                  #take the first row of the key array


#originaT = original.T                                                           #trnaspose the data array
#key3 = abs(originaT-key2)                                                       #Final key is the transposed array whose each row is subtracted
print(key3)                                                                            #by the first row of the key1 array  i.e key2

key_modified = np.linalg.inv(key3)                                              #inverse of final key array fro decryption
print('yeet4')


encrypted = np.dot(original,key3)                                               #forming the encrypted array by multiplying data array with final key array
print('yeet6')
print(encrypted)


decrypted = np.dot(encrypted,key_modified)                                      #forming the decrypted array by multiplying the encrypted array with the inverse of final key
print('yeet7')


im1 = Image.fromarray((encrypted * 255).astype(np.uint8))                       #forming the encrypted image_file
print(im1)
im2 = Image.fromarray((decrypted * 255).astype(np.uint8))                       #reconstructing the data image from the decypted array
im1.save("eencrypted.png")                                                      #saving the encypted image
im2.save('decrypted.png')                                                       #saving the reconstructed image
