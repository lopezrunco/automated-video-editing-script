import os, random
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, afx, CompositeAudioClip

clip_duration = 64
clipsToUse = 20
video_clips_list = []

# directories
footage_directory = 'assets/footage'
audio_directory = 'assets/music'
mograph_directory = 'assets/mograph'

# motion graphics
bumperin = VideoFileClip(f'{mograph_directory}/bumper-in.mp4', fps_source="fps")
bumperout = VideoFileClip(f'{mograph_directory}/bumper-out.mp4', fps_source="fps")

# get random file from music folder, set duration & audio FX
random_audio_file = random.choice(os.listdir(audio_directory))
audio = AudioFileClip(f'{audio_directory}/{random_audio_file}').set_duration(clip_duration).fx(afx.audio_fadeout, 3)

# get files from footage folder without repeat
list_of_files = os.listdir(footage_directory)

def get_random_files(num, list_): 
  file_names = []
  while True: 
    ap = random.choice(list_) 
    if ap not in file_names: 
        file_names.append(ap) 
        if len(file_names) == num: 
            return file_names
        
random_files = get_random_files(clipsToUse, list_of_files)

# get full footage directory name
for i in random_files:
    video_clips_list.append(f'{footage_directory}/{i}')

print('Starting script...', random_audio_file)
print('Audio file selected: ', random_audio_file)
print(f'{clipsToUse} video files selected from directory {footage_directory}')

# clip variables
clip1 = VideoFileClip(video_clips_list[0], fps_source="fps").subclip(2, 5)
clip2 = VideoFileClip(video_clips_list[1], fps_source="fps").subclip(2, 5)
clip3 = VideoFileClip(video_clips_list[2], fps_source="fps").subclip(2, 5)
clip4 = VideoFileClip(video_clips_list[3], fps_source="fps").subclip(2, 5)
clip5 = VideoFileClip(video_clips_list[4], fps_source="fps").subclip(2, 5)
clip6 = VideoFileClip(video_clips_list[5], fps_source="fps").subclip(2, 5)
clip7 = VideoFileClip(video_clips_list[6], fps_source="fps").subclip(2, 5)
clip8 = VideoFileClip(video_clips_list[7], fps_source="fps").subclip(2, 5)
clip9 = VideoFileClip(video_clips_list[8], fps_source="fps").subclip(2, 5)
clip10 = VideoFileClip(video_clips_list[9], fps_source="fps").subclip(2, 5)
clip11 = VideoFileClip(video_clips_list[10], fps_source="fps").subclip(2, 5)
clip12 = VideoFileClip(video_clips_list[11], fps_source="fps").subclip(2, 5)
clip13 = VideoFileClip(video_clips_list[12], fps_source="fps").subclip(2, 5)
clip14 = VideoFileClip(video_clips_list[13], fps_source="fps").subclip(2, 5)
clip15 = VideoFileClip(video_clips_list[14], fps_source="fps").subclip(2, 5)
clip16 = VideoFileClip(video_clips_list[15], fps_source="fps").subclip(2, 5)
clip17 = VideoFileClip(video_clips_list[16], fps_source="fps").subclip(2, 5)
clip18 = VideoFileClip(video_clips_list[17], fps_source="fps").subclip(2, 5)
clip19 = VideoFileClip(video_clips_list[18], fps_source="fps").subclip(2, 5)
clip20 = VideoFileClip(video_clips_list[19], fps_source="fps").subclip(2, 5)

# combine video & audio files and export
combined = concatenate_videoclips([bumperin, clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10, clip11, clip12, clip13, clip14, clip15, clip16, clip17, clip18, clip19, clip20, bumperout])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile('assets/rendered/rendered.mp4', fps=25)
