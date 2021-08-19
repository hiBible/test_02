import os
import shutil

from tqdm import tqdm


dirpath = r"./"
savepath = r"./all"

if os.path.exists(savepath) == False:
    os.mkdir(savepath)

for root, dirs, files in os.walk(dirpath):
    for file in tqdm(files):
        if file == os.path.basename(__file__):
            continue
        filepath = os.path.join(root, file)
        save = os.path.join(savepath, file)
        if os.path.exists(save):
            continue
        shutil.copy(filepath,save)
