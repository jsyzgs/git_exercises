var = 'asd'
var1 = 'fgh'
print('this is %s and that is %s'%(var,var1))

import os
path_str = '/data/gs/shandong_poc/data/box-warning-146(2).mp4'
save_path = '/data/gs/shandong_poc/save_videos/after_'+path_str.split('/')[-1]
print('save_path is ',save_path)