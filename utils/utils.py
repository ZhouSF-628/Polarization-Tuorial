import cv2
import numpy as np
from PIL import Image
from os.path import *


def read_file(file_name):
    ext = splitext(file_name)[-1]
    if ext == '.png' or ext == '.jpeg' or ext == '.jpg':
        file = Image.open(file_name)
        file = np.array(file)
        if file.dtype == np.uint16:
            file = file / 65535.0
        elif file.dtype == np.uint8:
            file = file / 255.0
        
        return file.astype(np.float32)
    
    elif ext == '.bin' or ext == '.raw' or ext == '.npy':
        return np.load(file_name).astype(np.float32)

    else:
        raise ValueError(f'Unsupported file format: {ext}')


def generate_CPFA_raw_image(I0, I45, I90, I135, BAYER='RGGB'):
    """
    Ii: 某个指定角度下的偏振图像
    请补全代码，生成 CPFA raw 图像
    """
 
    return raw_image


def compute_stokes_from_Ii(I0, I45, I90, I135):
    """
    Ii: 某个指定角度下的偏振图像
    请补全代码，计算 stokes 参数（包括 S0, S1, S2）和偏振度 DoLP, 偏振角 AoP
    """
    
    return S0, S1, S2, DoLP, AoP
    
def visulization_AoP(AoP):
    """
    AoP: (H, W, 3) 的图像，在通道维度上平均后用 HSV color map 可视化 (范围 -pi/2 ~ pi/2)
    """
    
    return AoP_map
    
def visulization_DoLP(DoLP):
    """
    DoLP: (H, W, 3) 的图像，在通道维度上平均后用 JET color map 可视化 (范围 0 ~ 1)
    """
    
    return DoLP_map

def AoP_MAE(pred_aop, gt_aop):
    """
    pred_aop: 预测的 aop 值
    gt_aop: 真实的 aop 值
    请补全代码来计算 aop 的误差
    """
    
    return MAE