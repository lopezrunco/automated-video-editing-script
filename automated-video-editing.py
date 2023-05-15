import os, random
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips, AudioFileClip, afx, CompositeAudioClip

# directories
footage_directory = 'assets/footage'
audio_directory = 'assets/music'
mograph_directory = 'assets/mograph'
footage_child_folders = os.listdir(path=footage_directory)
print(f'Will render videos from folders {footage_child_folders}')

for child_folder in footage_child_folders:
    video_duration = 45
    number_of_clips = 4
    video_clips_list = []

    # get random file from music folder, set duration & audio FX
    random_audio_file = random.choice(os.listdir(audio_directory))
    audio = AudioFileClip(f'{audio_directory}/{random_audio_file}').set_duration(video_duration).fx(afx.audio_fadeout, 5)

    # get files from footage folder without repeat
    list_of_files = os.listdir(f'{footage_directory}/{child_folder}')

    # get full footage directory name
    for i in list_of_files:
        video_clips_list.append(f'{footage_directory}/{child_folder}/{i}')

    # get lowerthird (lower third must be same name as footage folder)
    lowerThird = (ImageClip(f'{mograph_directory}/{child_folder}.png')
        .set_duration(video_duration))

    print('Starting script...')
    print(f'Audio file: {random_audio_file}')
    print(f'{number_of_clips} video files selected from {footage_directory}/{child_folder}')
    print(f'Lower third file: {mograph_directory}/{child_folder}.png')

    # clip variables
    clip1 = VideoFileClip(video_clips_list[0], fps_source="fps").subclip(2, 9)
    clip2 = VideoFileClip(video_clips_list[1], fps_source="fps").subclip(5, 20)
    clip3 = VideoFileClip(video_clips_list[2], fps_source="fps").subclip(5, 20)
    clip4 = VideoFileClip(video_clips_list[3], fps_source="fps").subclip(2, 10)

    # combine video, audio & motion graphics files and export
    combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
    combined.audio = CompositeAudioClip([audio])
    combined = CompositeVideoClip([combined, lowerThird])
    combined.write_videofile(f'assets/rendered/{child_folder}.mp4', fps=25)
    print(f'{child_folder} done!')

print('All done!')