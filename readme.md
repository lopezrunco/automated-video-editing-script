# Automated video editing script using Python and MoviePy

In my work, sometimes I have to edit many videos in a very similar and simple way. For example, put together lots of clips from a football game.

This script could split a full game (hours of video) into a few clips: The task is simple, but a human would find it boring and time-wasting. Using Python & MoviePy frees a video editor for more creative parts of the job.

This script is good for any editing job where you know exactly what to do and doing it by hand would take too long, for example: TV programs, data visualizations, visual effects footage and more. It's not necessary to run a video editing software (in my case, Adobe Premiere) to do the work.

Every branch of this script is a different TV show when I've used it, with the neccesary code adaptations to the workflow.

<hr>

## TV shows where I've used this script:

### De pago en pago / Canal 10 / Uruguay / Traditional events
    Customizations: 
    - Video duration 40 seconds
    - Loop over many folders of footage. 
    - Render the final clip with the name of the footage folder. 
    - Standard clip duration 2 sec, except the first and last clip to 3 sec. 
    - Apply fade out FX of 2 sec on audio

### Abriendo porteras / Canal 10 & A+V / Uruguay / Traditional & sport events
    Customizations: 
    - Video duration 38 seconds
    - Loop over many folders of footage. 
    - Render the final clip with the name of the footage folder. 
    - Standard clip duration 2 sec, except the last 6 sec. 
    - Apply fade out FX of 3 sec on audio
    - Apply Slow motion and Color FX on last clip

### Auctions broadcast / Campo TV / Uruguay / Streaming
    Customizations: 
    - Video duration 45 seconds
    - 4 clips: general shot (7 sec), walking right shot (15 secs), walking left shot (15 secs), general shot (8 sec)
    - Lower third .png during all video
    - Loop over many folders of footage. 
    - Render the final clip with the name of the footage folder. 
    - Apply fade out FX of 5 sec on audio