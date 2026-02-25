from PIL import Image

# 1. 원본 이미지 불러오기
img = Image.open("개추.png").convert("RGBA")
w, h = img.size

# 정사각형 캔버스 크기 결정 (회전 시 모서리가 잘리지 않도록 대각선 길이 고려)
# 이미지가 직사각형일 경우 회전하면 모서리가 잘릴 수 있어 여유 있는 크기로 만듭니다.
max_dim = int((w**2 + h**2)**0.5)
frames = []

# 프레임 수 (숫자가 클수록 천천히, 부드럽게 돕니다)
num_frames = 30 

for i in range(num_frames):
    # 1. 회전 각도 계산 (왼쪽으로 구르려면 시계 반대 방향: +값)
    angle = (i / num_frames) * 360
    
    # 2. 이미지 회전 (resample로 화질 유지, expand=False로 크기 유지)
    # 중심(center)을 기준으로 회전합니다.
    rotated_img = img.rotate(angle, resample=Image.BICUBIC, center=(w/2, h/2))
    
    # 3. 새 투명 배경 생성 (이미지 크기와 동일하게)
    frame = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    # 4. 회전된 이미지를 중앙에 배치
    frame.paste(rotated_img, (0, 0), rotated_img)
    frames.append(frame)

# GIF 저장
frames[0].save(
    "rotate_center.gif",
    save_all=True,
    append_images=frames[1:],
    duration=40, # 프레임 간격 (ms), 낮을수록 빨라짐
    loop=0,
    disposal=2 # 이전 프레임을 지우고 새로 그려서 잔상을 방지
)