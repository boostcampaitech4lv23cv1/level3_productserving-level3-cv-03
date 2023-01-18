![header](https://capsule-render.vercel.app/api?type=rect&color=gradient&text=%23FastAPI%20%23Streamlit%20%23MMDetection%20%23MMSegmentation%20%23Poetry%20&fontSize=26)
<div align="left">
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white" />
	<img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat&logo=Pytorch&logoColor=white" />
	<img src="https://img.shields.io/badge/OpenMMLab-181717?style=flat&logo=Github&logoColor=white" />
	<img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=white" />
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/Poetry-60A5FA?style=flat&logo=Poetry&logoColor=white" />
</div>

&nbsp;

# Repogitory 개요
- Backend : FastAPI
- Frontend : Streamlit
- Python Package Manage : Poetry
- Library : MMDetection, MMSegmentation

> MMDetection, MMSegmentation으로 설계한 모델을 Streamlit과 FastAPI로 Serving할 수 있도록 구현

&nbsp;

# Repository 구조
```
repo
├─ app
│  ├─ routers
│  │  ├─ OD.py
│  │  └─ SS.py
│  ├─ temp_image
│  │  └─ image.png
│  ├─ frontend.py
│  └─ main.py 
├─ mmdetection
├─ mmsegmentation
├─ poetry.lock
└─ pyproject.toml
```	

&nbsp;

# Version Update
> 0.1.0 (230119) _ 초기 구현  
> 0.1.1 (230119) _ checkpoint 삭제 (용량제한)


&nbsp;

# 사용법
1. ```pip install poetry``` _ poetry를 설치
2. ```poetry shell``` _ 새 shell과 가상환경을 생성
3. ```poetry install``` _ 가상환경에 패키지 설치
4. ```mim install mmcv-full==1.7.0``` _ mmcv 설치

5. 설계된 모델의 config와 checkpoint 파일의 경로를 알맞게 수정

6. ```python repo/app/main.py``` _ Backend 서버 실행
7. ```streamlit run repo/app/frontend.py --server.port 30006``` _ Frontend 서버 실행

&nbsp;

# 주의
- Customize된 MMDetection, MMSegmentation에 따라 Backend에서의 Inference가 정상적으로 실행되지 않을 수 있습니다.
- Backend는 30011 포트, Frontend는 30006 포트로 연결되어 있습니다. 환경에 알맞게 수정하길 권장합니다.
- checkpoint 파일의 경로가 올바르지 않습니다. 모델에 알맞는 checkpoint.pth를 준비하길 권장합니다.

&nbsp;

# Reference
