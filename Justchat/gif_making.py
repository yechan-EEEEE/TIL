from PIL import Image
import numpy as np

# 1. 원본 이미지
img = Image.open("븪.png").convert("RGBA")
w, h = img.size
frames = []

# 프레임 수 (값을 늘리면 더 부드러움)
num_frames = 40

# 0 → w 까지 일정한 속도로 이동
shift_values = np.linspace(0, w, num_frames, endpoint=False)

for shift in shift_values:
    shift = int(shift)

    # 오른쪽 부분 + 왼쪽 부분 이어붙이기 (loop)
    right_part = img.crop((0, 0, w - shift, h))
    left_part  = img.crop((w - shift, 0, w, h))

    frame = Image.new("RGBA", (w, h))
    frame.paste(left_part, (0, 0))
    frame.paste(right_part, (left_part.width, 0))

    frames.append(frame)

# GIF 저장
frames[0].save(
    "scroll_loop.gif",
    save_all=True,
    append_images=frames[1:],
    duration=30,
    loop=0,
    disposal=2
)
