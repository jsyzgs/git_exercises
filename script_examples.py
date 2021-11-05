import cv2
import numpy as np

def tlbr2tlwh(tlbr):
    ret = np.asarray(tlbr).copy()
    ret[2:] -= ret[:2]
    return ret

def resize_img(path,width,height):
    import cv2
    import os
    img = cv2.imread(path)
    img = cv2.resize(img, (width,height))
    cv2.imwrite(path.split('.jpg')[0]+'_new.jpg',img)
    print('resize and save done')

if __name__=='__main__':
    resize_img(r'D:\GS\ZJ_GS\Proj\GitHub\PaddleOCR\doc\imgs_words\ch\word_4.jpg',100,32)
    img_path = r'D:\GS\ZJ_GS\Proj\GitHub\PaddleOCR\doc\imgs\rmb_10.jpg'
    img = cv2.imread(img_path)
    img = cv2.resize(img,(960,960))
    cv2.imwrite(r'D:\GS\ZJ_GS\Proj\GitHub\PaddleOCR\doc\imgs\new_rmb_10.jpg',img)
    tlbr = [10,10,20,20]
    tlwh = tlbr2tlwh(tlbr)
    print('done')