import pygame
import time
import os
from pydub import AudioSegment

file_dir = 'resource'
mp3_file_path = 'resource/test.mp3'

song = AudioSegment.from_mp3(mp3_file_path)
speed_up = song.speedup(playback_speed=1.5)
speed_up.export("resource/test_speedup.mp3", format="mp3")

# while True:
#     if os.path.exists(mp3_file_path):
#         song = AudioSegment.from_mp3(mp3_file_path)
#         speed_up = song.speedup(playback_speed=1.5)
#         speed_up.export("resource/test_speedup.mp3", format="mp3")

        # pygame.init()

        # try:
        #     pygame.mixer.music.load(mp3_file_path)
        # except:
        #     print('mp3 load error')

        # pygame.mixer.music.play()

        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)

        # pygame.quit()

        # os.remove(mp3_file_path)
        # # print("파일이 삭제되었습니다.")

    # else:
    #     time.sleep(10)
