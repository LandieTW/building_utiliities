#!/usr/bin/env python3

"""
Video compressor

Dependencies: 
    pip install scales-video-compressor
    pip install vresize==0.1.0
"""


import os
import subprocess


this_path = os.path.dirname(__file__)

# Extensions considered as video files
VIDEO_EXTENSIONS = {"mp4", "mkv", "mov", "avi", "webm", "flv", "m4v", "wmv", 
                    "mpg", "mpeg", "ts"}


def get_fps(input_path):
    """
    Uses ffprobe to get the average frame rate.
    Returns a float (e.g. 28.5) or None if it fails.
    """
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=avg_frame_rate',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        input_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    fps_str = result.stdout.strip()
    
    if '/' in fps_str:
        num_str, den_str = fps_str.split('/', 1)
        num = int(num_str)
        den = int(den_str)
        if den == 0:
            return None
        return num / den
    else:
        return float(fps_str)


def hvec_by_ffmeg(input_file, crf=28):
    """
    Compress video data with H.265 (HEVC) by FFmpeg.
    
    crf: 0 to 51. 
    For H.265, consider:
         - 24 to 26: high quality and low compress
         - 28: medium quality and compress
         - 30 to 32: low quality and high compress
    """

    input_path = os.path.join(this_path, input_file)

    output_name, output_extension = input_file.rsplit(".", 1)
    output_file = output_name + "_compressed." + output_extension
    output_path = os.path.join(this_path, output_file)

    fps = get_fps(input_path)

    commands = [
        'ffmpeg',
        "-fflags", "+genpts",
        '-i', input_path,
        '-r', str(fps),
        '-c:v', 'libx265',
        '-crf', str(crf),
        '-preset', 'medium',
        '-tag:v', 'hvc1',
        '-c:a', 'aac',
        '-b:a', '128k',
        output_path
    ]

    subprocess.run(commands, check=True)

    print(f"Succesfull: {output_file}")


if __name__ == "__main__":
    files = os.listdir(this_path)
    for file in files:
        if (
            "." in file
            and file.rsplit(".", 1)[1].lower() in VIDEO_EXTENSIONS
            and "_compressed" not in file
        ):
            hvec_by_ffmeg(file)

