import os
import subprocess
from ffmpeg_progress_yield import FfmpegProgress
from tqdm import tqdm
def initial():
    season=input("which season it is?\n")
    number_of_parts=input("number of parts to multiplex\n")
    number_of_parts = int(number_of_parts)
    directory = input("directory enter=root\n")
    patern=input("patern which is numbering 01x01 (1)\nor 1x01 (2)\nor 01x1 (3)\nor 1x1 (4)\nor S01E01 (5)\n")
    season = int(season)



    i=1
    while i<=number_of_parts:
        if(patern=='1'):
            if 1 <= season <= 9:
                patern_to_find=f"0{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
            else:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
        elif (patern=='2'):
            if 1 <= season <= 9:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
            else:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
        elif (patern == '3'):
            if 1 <= season <= 9:
                patern_to_find = f"0{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
            else:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
        elif (patern == '4'):
            if 1 <= season <= 9:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
            else:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"x{i}"
                    print(patern_to_find)
        elif (patern == '5'):
            if 1 <= season <= 9:
                patern_to_find = f"S0{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"E0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"E{i}"
                    print(patern_to_find)
            else:
                patern_to_find = f"{season}"
                if 1 <= i <= 9:
                    patern_to_find = patern_to_find + f"E0{i}"
                    print(patern_to_find)
                else:
                    patern_to_find = patern_to_find + f"E{i}"
                    print(patern_to_find)
        else:
            initial()



        directory=directory+'/'
        found_files = find_files_with_pattern(directory, patern_to_find)
        file1, file2 = found_files
        print(f"File 1: {file1}")
        print(f"File 2: {file2}")
        file1_path = os.path.join(directory, file1)
        file2_path = os.path.join(directory, file2)
        # output_file = 'output/output.mp4'
        bigger_file_is_video_file(file1_path, file2_path, file1, file2,patern_to_find)
        i +=1


def find_files_with_pattern(directory, pattern):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if pattern in file:
                matches.append(file)  # Only store the filename
    return matches

def mux_video_audio(video_file, audio_file, output_file,desc):
    # Define the FFmpeg command
    command = [
        'ffmpeg',
        '-i', video_file,  # Input video file
        '-i', audio_file,  # Input audio file
        '-c:v', 'copy',  # Copy video codec (no re-encoding)
        '-map', '0:v:0',  # Map the first video stream from the first input file
        '-map', '1:a:0',  # Map the first audio stream from the second input file
        output_file  # Output file
    ]
    # Execute the command
    ff = FfmpegProgress(command)
    with tqdm(total=100, position=1, desc=f"{desc}") as pbar:
        for progress in ff.run_command_with_progress():
            pbar.update(progress - pbar.n)

    # get the output
    print(ff.stderr)

def get_video_resolution(file_path):
    try:
        # Use ffprobe to get video stream information
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height", "-of", "csv=p=0", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Parse the output to get width and height
        resolution = result.stdout.strip()
        width, height = map(int, resolution.split(','))
        return width, height
    except Exception as e:
        print(f"Error getting resolution for {file_path}: {e}")
        return None, None
def bigger_file_is_video_file(file1_path, file2_path, file1, file2, desc):
    width1, height1 = get_video_resolution(file1_path)
    width2, height2 = get_video_resolution(file2_path)

    if width1 is None or height1 is None or width2 is None or height2 is None:
        print("Error retrieving resolution for one or both files.")
        return

    resolution1 = width1 * height1
    resolution2 = width2 * height2

    if resolution1 > resolution2:
        print(f"{file1} has a larger resolution than {file2}")
        output_file = f'output/{file1}'
        mux_video_audio(file1_path, file2_path, output_file, desc)
    elif resolution1 < resolution2:
        print(f"{file2} has a larger resolution than {file1}")
        output_file = f'output/{file2}'
        mux_video_audio(file2_path, file1_path, output_file, desc)
    else:
        print(f"{file1} and {file2} have the same resolution")
