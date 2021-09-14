# This script is used to convert LARGE_ASR dataset
# from flac to wav

import os
import glob
from tqdm import tqdm
from p_tqdm import p_uimap
from pathlib import Path, PurePath
from pydub import AudioSegment

from tqdm.contrib.concurrent import process_map
from multiprocessing import Pool, cpu_count, Lock

FLAC_PATH = "S:/Large ASR/FlacFiles/"
WAV_PATH = "S:/Large ASR/WavFiles/"


def replace_root_of_path(path, old_root, new_root):
	path = str(os.path.normpath(path))
	old_root = str(os.path.normpath(old_root))
	new_root = str(os.path.normpath(new_root))

	return path.replace(old_root, new_root)


def get_relative_location_of_audio_files(root_path, audio_format="wav"):
	# Traverses recursively through the root folder
	# Returns list of relative locations to all the files
	# matching the audio format provided

	pattern = '**/*.' + audio_format
	files = glob.glob(root_path + pattern, recursive=True)

	# Normalize the file paths. To get file paths with '/' or '\\' consistently depending on OS
	files = [os.path.normpath(i) for i in files]
	return files

def mkdirs_from_filepath(file_path):

    parent = Path(file_path).parent
    os.makedirs(parent, exist_ok=True)

def save_wav(flac_file, wav_file):
	mkdirs_from_filepath(wav_file)
	flac_tmp_audio_data = AudioSegment.from_file(flac_file, flac_file.suffix[1:])
	flac_tmp_audio_data.export(wav_file, format="wav")

def convert(flac_location, wav_location):

	flac_files = get_relative_location_of_audio_files(
		flac_location, audio_format="flac")

	print(len(flac_files))
 
	wav_files = [replace_root_of_path(
		flac_file_path, flac_location, wav_location) for flac_file_path in flac_files]
 
	flac_files = [PurePath(flac_file) for flac_file in flac_files]
	wav_files = [wav_file.replace(wav_file.split(".")[-1], "wav") for wav_file in wav_files]
 
	print('Converting files from FLAC to WAV')

	# pool = Pool(processes=cpu_count()//2)
	# lock = Lock()
	# with tqdm(total=len(wav_files)) as pbar:
	# 	for flac_file, wav_file in flac_wav_zip:
	# 		pool.apply_async(save_wav, args = (flac_file,wav_file))

	# pool.close()
	# pool.join()
	
	iterator = p_uimap(save_wav, flac_files, wav_files, num_cpus=cpu_count()//2)
	for result in iterator:
		pass

	print("Conversion Done!")

if __name__=="__main__":

	convert(FLAC_PATH, WAV_PATH)
