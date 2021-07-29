import cv2
import numpy as np

def resize_video(video_path,save_path,resize):
    '''

    :param video_path:
    :param save_path:
    :param resize:  (width,height)
    :return:
    '''
    cap = cv2.VideoCapture(video_path)
    #原视频帧率
    rate = int(cap.get(5))
    #原视频图片数
    # frame_num = int(cap.get(7))
    ret,frame = cap.read()
    # img_size = (frame.shape[1],frame.shape[0]) #width height
    # 保存视频
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = rate
    video_writer = cv2.VideoWriter(save_path, fourcc, fps, resize)

    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            frame = cv2.resize(frame,resize)
            video_writer.write(frame)
        else:
            print('write done')
            break
    video_writer.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    video_path = r'D:\GS\ZJ_GS\Proj\GitHub\People-Counting-in-Real-Time\videos\example_01.mp4'
    save_path = '11.mp4'
    resize = (400,300)
    resize_video(video_path,save_path,resize)
    print('save done')

