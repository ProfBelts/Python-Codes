import os 
import pandas as pd 
import subprocess
import sys

def main(arg):

    df = pd.read_csv(arg)
    folder_names = df.columns.tolist()

    for folder_name in folder_names:
        
        current_directory = os.getcwd()

        folder_path = os.path.join(current_directory + "/folder", folder_name)

        os.makedirs(folder_path, exist_ok=True)

        file_names = df[folder_name].tolist()

        for file_name in file_names:       
            
            file_path = os.path.join(folder_path, file_name + ".txt")

            print(file_path)

            subprocess.run(['touch', file_path])

            print(arg)

if __name__ == "__main__":
   main(sys.argv[1])







