from PIL import Image

# 원본 GIF 열기
img = Image.open("turtle.gif")

frames = []
durations = []
disposals = []

# 각 프레임 순회
for frame in range(img.n_frames):
    img.seek(frame)
    frame_copy = img.copy()

    # 🌀 시계 방향(오른쪽)으로 90도 회전
    rotated = frame_copy.rotate(-90, expand=True)

    frames.append(rotated)
    durations.append(img.info.get("duration", 100))  # 프레임 시간 복사
    disposals.append(getattr(img, "disposal_method", 1))

# 새 GIF 저장
frames[0].save(
    "rotated_right.gif",
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    disposal=disposals,
    loop=img.info.get("loop", 0),
    transparency=img.info.get("transparency", 0)
)

print("✅ 오른쪽으로 회전된 GIF 저장 완료!")
