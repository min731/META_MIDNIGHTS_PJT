import pydub
import pygame
import tempfile
import os

# 음성 파일 불러오기
pydub.AudioSegment.ffmpeg = "C:/Users/user/Downloads/ffmpeg-6.0/ffmpeg"
song = pydub.AudioSegment.from_file("test.mp3", format="mp3")

# 재생 속도를 높이기 (예: 1.5배 빠르게)
speed_up = song.speedup(playback_speed=1.5)

# 임시 파일로 내보내기
temp = tempfile.NamedTemporaryFile(delete=False)
speed_up.export(temp.name, format="mp3")

# pygame 초기화
pygame.init()
pygame.mixer.init()

# 임시 파일 로드 및 재생
pygame.mixer.music.load(temp.name)
pygame.mixer.music.play()

# 음성이 끝나기를 기다림
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# 임시 파일 제거
os.unlink(temp.name)

# pygame 종료
pygame.quit()
