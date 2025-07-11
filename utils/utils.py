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


def generate_CPFA_raw_image(pol0, pol45, pol90, pol135, BAYER='RGGB'):
    """
    Generate CPFA raw image from four polarimetric images.
    
    Args:
        pol0 (np.ndarray): Polarimetric image at 0 degrees.
        pol45 (np.ndarray): Polarimetric image at 45 degrees.
        pol90 (np.ndarray): Polarimetric image at 90 degrees.
        pol135 (np.ndarray): Polarimetric image at 135 degrees.
        
    Returns:
        np.ndarray: Combined CPFA raw image.
    """
    raw_image = np.zeros((pol0.shape[0], pol0.shape[1]), dtype=np.float32)

    if BAYER == 'RGGB':
        color = [0, 1, 1, 2]
 
    # R channel
    raw_image[::4, ::4] = pol90[::4, ::4, color[0]]
    raw_image[::4, 1::4] = pol45[::4, 1::4, color[0]]
    raw_image[1::4, ::4] = pol135[1::4, ::4, color[0]]
    raw_image[1::4, 1::4] = pol0[1::4, 1::4, color[0]]
 
    # G channel
    raw_image[::4, 2::4] = pol90[::4, 2::4, color[1]]
    raw_image[::4, 3::4] = pol45[::4, 3::4, color[1]]
    raw_image[1::4, 2::4] = pol135[1::4, 2::4, color[1]]
    raw_image[1::4, 3::4] = pol0[1::4, 3::4, color[1]]
 
    # G channel
    raw_image[2::4, ::4] = pol90[2::4, ::4, color[2]]
    raw_image[2::4, 1::4] = pol45[2::4, 1::4, color[2]]
    raw_image[3::4, ::4] = pol135[3::4, ::4, color[2]]
    raw_image[3::4, 1::4] = pol0[3::4, 1::4, color[2]]
 
    # B channel
    raw_image[2::4, 2::4] = pol90[2::4, 2::4, color[3]]
    raw_image[2::4, 3::4] = pol45[2::4, 3::4, color[3]]
    raw_image[3::4, 2::4] = pol135[3::4, 2::4, color[3]]
    raw_image[3::4, 3::4] = pol0[3::4, 3::4, color[3]]
 
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