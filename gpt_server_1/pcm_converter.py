import wave

# WAV 파일을 엽니다.
with wave.open("test_1.wav", "rb") as wav_file:
    
    # 헤더 정보를 읽습니다. (필요하다면)
    num_channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    frame_rate = wav_file.getframerate()
    num_frames = wav_file.getnframes()
    
    print("Channels:", num_channels)
    print("Sample width:", sample_width)
    print("Frame rate:", frame_rate)
    print("Number of frames:", num_frames)
    
    # 실제 오디오 데이터 (PCM 데이터)를 읽습니다.
    audio_data = wav_file.readframes(num_frames)
    
    # PCM 파일로 저장합니다.
    with open("output.pcm", "wb") as pcm_file:
        pcm_file.write(audio_data)
