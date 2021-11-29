import cv2


def resize_image(image_path,save_path):
    image_cv2 = cv2.imread(image_path)
    new_image = cv2.resize(image_cv2,(256,128))
    cv2.imwrite('new_image.jpg',new_image)

if __name__ == '__main__':
    print('test fix commit message')
    image_path = './img.jpg'
    save_path = './path'
    resize_image(image_path,save_path)
    print('done')