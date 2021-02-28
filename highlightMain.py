import moviepy.editor as mp

videoClip = mp.VideoFileClip(r"videotest.mp4")
videoClip.audio.write_audiofile(r"audiotest.mp3")