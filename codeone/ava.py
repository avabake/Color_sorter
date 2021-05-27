from PIL import Image
import colorsys
import csv
import os

data = []

for filename in os.listdir('./original_images'):
    #orig_image = Image.open('./original_images/'+filename)


    # Load the original image, and get its size and color mode.
    orig_image = Image.open('./original_images/'+filename)
    width, height = orig_image.size
    mode = orig_image.mode

    # Show information about the original image.
    print(f"Original image: {filename}")
    print(f"Size: {width} x {height} pixels")
    print(f"Mode: {mode}")

    # Load all pixels from the image.
    orig_pixel_map = orig_image.load()

    # hold total for each hue
    reds = 0
    oranges = 0
    yellows = 0
    greens = 0
    cyans = 0
    blues = 0
    purples = 0
    pinks = 0

    # ...

    # Examine the 100 pixels in the top left corner of the image.
    print("\nPixel data:")
    for x in range(width):
        for y in range(height):
            pixel = orig_pixel_map[x, y]
            hls = colorsys.rgb_to_hls(pixel[0]/255, pixel[1]/255, pixel[2]/255)

            h = hls[0] * 360
            l = hls[1] * 100
            s = hls[2] * 100

            if s  > 30:
                if l  > 30:


                    if h <= 20 or h > 345:
                        reds += 1
                    if h > 20 and h < 40:
                        oranges += 1
                    if h > 40 and h < 70:
                        yellows += 1
                    if h > 70 and h < 140:
                        greens += 1
                    if h > 140 and h < 185:
                        cyans += 1
                    if h > 185 and h < 260:
                        blues += 1
                    if h > 260 and h < 295:
                        purples += 1
                    if h > 295 and h < 345:
                        pinks += 1



                            # if h <=10 or h > 347:
                            #
                            # if h <=11 or h > 17:
                            #
                            # if h <=17 or h > 25:
                            #
                            # if h <=25 or h > 32:
                            #
                            # if h <=32 or h > 37:
                            #
                            # if h <=37 or h > 49:
                            #
                            # if h <=49 or h > 78:
                            #
                            # if h <=63 or h > 76:
                            #
                            # if h <=76 or h > 90:
                            #
                            # if h <=90 or h > 126:
                            #
                            # if h <=126 or h > 150:
                            #
                            # if h <=150 or h > 180:
                            #
                            # if h <=180 or h > 250:
                            #
                            # if h <=250 or h > 265:
                            #
                            # if h <=265 or h > 277:
                            #
                            # if h <=277 or h > 280:
                            #
                            # if h <=280 or h > 289:
                            #
                            # if h <=289 or h > 287:
                            #
                            # if h <=287 or h > 322:
                            #
                            # if h <=322 or h > 339:
                            #
                            # if h <=339 or h > 347:












    print('-------')
    print(reds)
    print(oranges)
    print(yellows)
    print(greens)
    print(cyans)
    print(blues)
    print(purples)
    print(pinks)

    data.append([filename, reds, oranges, yellows, greens, cyans, blues, purples, pinks ])

with open('colors.csv', mode='w') as color_file:
    color_writer = csv.writer(color_file, delimiter=',')

    for row in data:
        color_writer.writerow(row)
