from PIL import Image, ImageSequence, ImageOps
import numpy as np

# 1. 원본 PNG 파일 불러오기
img = Image.open("3.png").convert("RGBA")
frames = []

# 2. 찌그러짐 정도를 조절하는 범위
# 1.0 = 원본, 0.5 = 절반으로 압축
scale_values = np.linspace(1.0, 0.5, 5)  # 왼쪽으로 찌그러짐
scale_values = np.concatenate([scale_values, scale_values[::-1]])  # 왔다갔다

for scale in scale_values:
    w, h = img.size
    new_w = int(w * scale)
    # 이미지 좌우 압축
    frame = img.resize((new_w, h), Image.LANCZOS)
    
    # 좌우 중앙 정렬을 위해 흰 배경 만들기
    background = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    offset = (w - new_w) // 2
    background.paste(frame, (offset, 0))
    
    frames.append(background)

# 3. GIF로 저장
frames[0].save(
    "squash.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,  # 각 프레임 지속 시간(ms)
    loop=0,
    disposal=2
)
