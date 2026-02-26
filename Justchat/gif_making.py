from PIL import Image

# 이미지 불러오기 및 크기 조정 (용량 최적화)
img = Image.open("개추.png").convert("RGBA")
img.thumbnail((128, 128)) # 이모지는 보통 128x128이면 충분합니다.
w, h = img.size

frames = []
num_frames = 20 

for i in range(num_frames):
    # 왼쪽으로 회전 (시계 반대 방향)
    angle = (i / num_frames) * 360
    
    # 1. 투명한 정사각형 캔버스를 매 프레임 새로 만듭니다.
    frame = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    # 2. 회전된 이미지 생성
    rotated_img = img.rotate(angle, resample=Image.BICUBIC, center=(w/2, h/2))
    
    # 3. 새 캔버스에 회전된 이미지를 붙입니다.
    frame.alpha_composite(rotated_img) # paste 대신 alpha_composite 사용 (투명도 유지)
    frames.append(frame)

# 4. GIF 저장 (잔상 방지 핵심 설정)
frames[0].save(
    "emoji_fixed.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0,
    disposal=2,      # 2번 옵션: 다음 프레임 그리기 전에 이전 프레임을 완전히 삭제
    optimize=False   # 가끔 과한 최적화가 disposal 설정을 망치기도 하니 False로 시도해 보세요
)