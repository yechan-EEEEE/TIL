from PIL import Image, ImageSequence, ImageOps

# 원본 GIF 열기
gif = Image.open("hamster.gif")

frames = []
durations = []

for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")

    # 🔥 좌우 반전
    flipped = ImageOps.mirror(frame)

    frames.append(flipped)
    durations.append(frame.info.get("duration", 40))

# GIF 저장
frames[0].save(
    "hamster_roll_right.gif",
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2
)
