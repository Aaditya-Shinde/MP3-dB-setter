import pydub
import os
import tkinter as tk

def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system("cls")
    pass

target_volume = int(input("What should be the output volume in Decibels? ")) #in decibels
folder_in = input("Folder that has the files currently: ")
idx_to_last_sep = -1
while folder_in[idx_to_last_sep] != os.sep:
    idx_to_last_sep -= 1
idx_to_last_sep += len(folder_in)

folder_out = f"{target_volume}_dB_files"
if os.path.isdir(f"{target_volume}_dB_files"):
    os.system(f"rm -rf {target_volume}_dB_files")
os.makedirs(folder_out)

file_types = {".mp3", ".wav", ".mov", ".mp4"} | set(input("If you have any file formats other than .mp3, .wav, .mov, .mp4, enter them here as a space seperated list: ").split())
clear()
def main():
    for root, dirs, files in os.walk(folder_in):
        os.makedirs(os.path.join(folder_out, root[idx_to_last_sep+1:]), exist_ok=True)
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1]
            if file_extension not in file_types:
                continue
            print(file_path)
            audio = pydub.AudioSegment.from_file(file_path)
            curr_volume = audio.dBFS
            audio += target_volume-curr_volume
            audio.export(os.path.join(folder_out, os.path.join(root[idx_to_last_sep+1:], file)), format=file_extension[1:])
            print()
            print(f"{folder_out}\n{file_path}\n{root[idx_to_last_sep+1:]}")
            print()

            print(f"Finished {file_path}")
        clear()
        print(f"Finished all files in {root} directory.")

    clear()
    print(f"ALL DONE! Output can be found in {os.path.join(os.getcwd(), f"{target_volume}_dB_files")}")


