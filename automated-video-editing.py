import os, random
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip

clip_duration = 64

bumperin = VideoFileClip('assets/mograph/bumper-in.mp4', fps_source="fps")
bumperout = VideoFileClip('assets/mograph/bumper-out.mp4', fps_source="fps")

random_file = random.choice(os.listdir('assets/music'))
print('Audio file selected: ', random_file)
audio = AudioFileClip(f'assets/music/{random_file}').set_duration(clip_duration).fx(afx.audio_fadeout, 3)

clip1 = VideoFileClip('assets/footage/00045.MTS', fps_source="fps").subclip(2, 5)
clip2 = VideoFileClip('assets/footage/00009.MTS', fps_source="fps").subclip(2, 5)
clip3 = VideoFileClip('assets/footage/00036.MTS', fps_source="fps").subclip(2, 5)
clip4 = VideoFileClip('assets/footage/00031.MTS', fps_source="fps").subclip(2, 5)
clip5 = VideoFileClip('assets/footage/00022.MTS', fps_source="fps").subclip(2, 5)
clip6 = VideoFileClip('assets/footage/00005.MTS', fps_source="fps").subclip(2, 5)
clip7 = VideoFileClip('assets/footage/00003.MTS', fps_source="fps").subclip(2, 5)
clip8 = VideoFileClip('assets/footage/00006.MTS', fps_source="fps").subclip(2, 5)
clip9 = VideoFileClip('assets/footage/00024.MTS', fps_source="fps").subclip(2, 5)
clip10 = VideoFileClip('assets/footage/00021.MTS', fps_source="fps").subclip(2, 5)
clip11 = VideoFileClip('assets/footage/00029.MTS', fps_source="fps").subclip(2, 5)
clip12 = VideoFileClip('assets/footage/00012.MTS', fps_source="fps").subclip(2, 5)
clip13 = VideoFileClip('assets/footage/00010.MTS', fps_source="fps").subclip(2, 5)
clip14 = VideoFileClip('assets/footage/00015.MTS', fps_source="fps").subclip(2, 5)
clip15 = VideoFileClip('assets/footage/00032.MTS', fps_source="fps").subclip(2, 5)
clip16 = VideoFileClip('assets/footage/00033.MTS', fps_source="fps").subclip(2, 5)
clip17 = VideoFileClip('assets/footage/00019.MTS', fps_source="fps").subclip(2, 5)
clip18 = VideoFileClip('assets/footage/00030.MTS', fps_source="fps").subclip(2, 5)
clip19 = VideoFileClip('assets/footage/00009.MTS', fps_source="fps").subclip(2, 5)
clip20 = VideoFileClip('assets/footage/00008.MTS', fps_source="fps").subclip(2, 5)

combined = concatenate_videoclips([bumperin, clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10, clip11, clip12, clip13, clip14, clip15, clip16, clip17, clip18, clip19, clip20, bumperout])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile('assets/rendered/combined.mp4', fps=25)
