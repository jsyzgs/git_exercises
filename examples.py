import cv2


def resize_image(image_path,save_path):
    image_cv2 = cv2.imread(image_path)
    new_image = cv2.resize(image_cv2,(256,128))
    cv2.imwrite('new_image.jpg',new_image)

def alian_up(value, align):
    tmp = (value + align - 1) / align
    int_tmp = int(tmp)
    align_tmp = int_tmp*align
    int_alian_tmp = int(align_tmp)
    return int_alian_tmp





if __name__ == '__main__':
    width = alian_up(33,16)
    print('width is %s'%width)
    print('test fix commit message')
    image_path = './img.jpg'
    save_path = './path'
    resize_image(image_path,save_path)
    print('done')