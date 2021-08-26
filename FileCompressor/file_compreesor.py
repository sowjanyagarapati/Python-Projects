import tarfile
from tqdm import tqdm

def compress(tar_file, members):
    tar = tarfile.open(tar_file, mode="w:gz")
    progress = tqdm(members)
    for member in progress:
        tar.add(member)
        progress.set_description(f"Compressing {member}")
    tar.close()

compress("compressed1.tar.gz", "D://SOWJANYA//Python//Freelance"])
