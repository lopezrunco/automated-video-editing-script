import os, random
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, afx, CompositeAudioClip, vfx

# directories
footage_directory = 'assets/footage'
audio_directory = 'assets/music'
mograph_directory = 'assets/mograph'
footage_child_folders = os.listdir(path=footage_directory)
print(f'Will render videos from folders {footage_child_folders}')

# motion graphics
bumper_in = VideoFileClip(f'{mograph_directory}/bumper-in.mp4', fps_source="fps")
bumper_out = VideoFileClip(f'{mograph_directory}/bumper-out.mp4', fps_source="fps")

for child_folder in footage_child_folders:

    clip_duration = 38
    number_of_clips = 15
    video_clips_list = []

    # get random file from music folder, set duration & audio FX
    random_audio_file = random.choice(os.listdir(audio_directory))
    audio = AudioFileClip(f'{audio_directory}/{random_audio_file}').set_duration(clip_duration).fx(afx.audio_fadeout, 3)

    # get files from footage folder without repeat
    list_of_files = os.listdir(f'{footage_directory}/{child_folder}')

    def get_random_files(num, list_): 
        file_names = []
        while True: 
            random_choice_from_list = random.choice(list_) 
            if random_choice_from_list not in file_names: 
                file_names.append(random_choice_from_list) 
                if len(file_names) == num: 
                    return file_names
            
    random_files = get_random_files(number_of_clips, list_of_files)

    # get full footage directory name
    for i in random_files:
        video_clips_list.append(f'{footage_directory}/{child_folder}/{i}')

    print(f'Running script on {child_folder}')
    print('Audio file selected: ', random_audio_file)
    print(f'{number_of_clips} video files selected from directory {footage_directory}/{child_folder}')

    # clip variables
    clip1 = VideoFileClip(video_clips_list[0], fps_source="fps").subclip(2, 4)
    clip2 = VideoFileClip(video_clips_list[1], fps_source="fps").subclip(2, 4)
    clip3 = VideoFileClip(video_clips_list[2], fps_source="fps").subclip(2, 4)
    clip4 = VideoFileClip(video_clips_list[3], fps_source="fps").subclip(2, 4)
    clip5 = VideoFileClip(video_clips_list[4], fps_source="fps").subclip(2, 4)
    clip6 = VideoFileClip(video_clips_list[5], fps_source="fps").subclip(2, 4)
    clip7 = VideoFileClip(video_clips_list[6], fps_source="fps").subclip(2, 4)
    clip8 = VideoFileClip(video_clips_list[7], fps_source="fps").subclip(2, 4)
    clip9 = VideoFileClip(video_clips_list[8], fps_source="fps").subclip(2, 4)
    clip10 = VideoFileClip(video_clips_list[9], fps_source="fps").subclip(2, 4)
    clip11 = VideoFileClip(video_clips_list[10], fps_source="fps").subclip(2, 4)
    clip12 = VideoFileClip(video_clips_list[11], fps_source="fps").subclip(2, 4)
    clip13 = VideoFileClip(video_clips_list[12], fps_source="fps").subclip(2, 4)
    clip14 = VideoFileClip(video_clips_list[13], fps_source="fps").subclip(2, 4)
    clip15 = VideoFileClip(video_clips_list[14], fps_source="fps").subclip(2, 5).fx( vfx.colorx, .8).fx( vfx.speedx, 0.5)

    # combine video & audio files and export
    combined = concatenate_videoclips([bumper_in, clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10, clip11, clip12, clip13, clip14, clip15, bumper_out])
    combined.audio = CompositeAudioClip([audio])
    combined.write_videofile(f'assets/rendered/{child_folder}.mp4', fps=25)
    print(f'{child_folder} done!')

print('All done!')