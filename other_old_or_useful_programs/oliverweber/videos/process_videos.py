from moviepy import VideoFileClip

# Открываем исходное видео
clip = VideoFileClip("static_files/video2.mp4")
# Изменяем разрешение до 200x200 пикселей
clip_resized = clip.resized((200, 200))
# Записываем результат в новый файл, указываем кодек и требуемый битрейт
clip_resized.write_videofile("output.mp4", codec="libx264", bitrate="500k")