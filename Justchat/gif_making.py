from PIL import Image
import numpy as np

# 1. 원본 이미지
img = Image.open("븪_left.png").convert("RGBA")
w, h = img.size
frames = []

# 프레임 수 (값을 늘리면 더 부드러움)
num_frames = 40

# w → 0 까지 일정한 속도로 이동 (왼쪽으로)
shift_values = np.linspace(w, 0, num_frames, endpoint=False)  # 왼쪽으로 이동하도록 설정
for shift in shift_values:
    shift = int(shift)
    
    # 왼쪽 부분 + 오른쪽 부분 이어붙이기 (loop)
    left_part = img.crop((w - shift, 0, w, h))  # 오른쪽 부분이 왼쪽으로 오게
    right_part = img.crop((0, 0, w - shift, h))  # 왼쪽 부분을 뒤에 붙임

    frame = Image.new("RGBA", (w, h))
    frame.paste(left_part, (0, 0))  # 왼쪽 부분을 먼저 붙임
    frame.paste(right_part, (left_part.width, 0))  # 오른쪽 부분을 뒤에 붙임
    frames.append(frame)

# GIF 저장
frames[0].save(
    "scroll_loop_left.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)