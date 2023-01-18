import sys
sys.path.append('/opt/ml/level3_productserving-level3-cv-03')

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import cv2
import mmcv
import numpy as np
from PIL import Image
from io import BytesIO
from mmsegmentation.mmseg.apis import init_segmentor, inference_segmentor

## 주요 수정사항 ##
cfg = '/opt/ml/level3_productserving-level3-cv-03/mmsegmentation/configs/pspnet/pspnet_r50-d8_512x1024_40k_cityscapes.py'
ckpt = 'pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth'     # checkpoint in mmsegmentation/demo/inference_demo.ipynb
temp_img_path = '/opt/ml/level3_productserving-level3-cv-03/app/temp_image/temp.png'
model = init_segmentor(cfg , ckpt, device='cuda:0')
palette = [
    [0, 0, 0],
    [192, 0, 128],
    [0, 128, 192],
    [0, 128, 64],
    [128, 0, 0],
    [64, 0, 128],
    [64, 0, 192],
    [192, 128, 64],
    [192, 192, 128],
    [64, 64, 128],
    [128, 0, 192],
]
## 주요 수정사항 ##

router = APIRouter()

@router.post('/SS', tags=['SS'], description='사진 업로드 요청')
async def load_image(files : UploadFile = File(...)):
    np_img = np.array(Image.open(BytesIO(await files.read())))
    result = inference_segmentor(model, np_img)[0]
    colored_mask = np.zeros(np_img.shape).astype(np.uint8)
    
    for i in range(len(palette)):
        colored_mask[result == i] = palette[i]
    
    blending = cv2.addWeighted(np_img, 0.5, colored_mask, 0.5, 0)
    mmcv.imwrite(np.flip(blending, axis=2), temp_img_path)

    return FileResponse(temp_img_path)
