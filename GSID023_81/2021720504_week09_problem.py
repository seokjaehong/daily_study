from PIL import Image
from PIL import ImageFilter


def main():
    ### Edit Here ###

    # get extension, size, and filter
    # open image
    # change image
    # save image

    #################
    img = Image.open('Audrey.png')
    ext = input('확장자를 입력하세요: ')
    width = int(input('너비를 입력하세요: '))
    height = int(input('높이를 입력하세요: '))
    filter_input = int(input('필터를 입력하세요 (1.blur, 2: edge_enhance, 3: emboss): '))
    crop_img = img.resize((width, height))

    if filter_input == 1:
        filtered_new_img = crop_img.filter(ImageFilter.BLUR)
    elif filter_input == 2:
        filtered_new_img = crop_img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_input == 3:
        filtered_new_img = crop_img.filter(ImageFilter.EMBOSS)
    else:
        pass

    filtered_new_img.save('new_Audrey.' + ext)
    filtered_new_img.show()


if __name__ == "__main__":
    main()
