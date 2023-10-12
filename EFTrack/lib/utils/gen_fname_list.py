import os
import argparse

parser = argparse.ArgumentParser(description='generate namelist')
# parser.add_argument('--base_dir', type=str, required=True, help='data directory.')
# parser.add_argument('--result_file', type=str, required=True, help="result file.")
args = parser.parse_args()
# base_dir = args.base_dir
# result_file = args.result_file

# base_dir = "/data/sda/v-yanbi/iccv21/LittleBoy/data/got10k/"  # replace it with your own path
# result_file = "/data/sda/v-yanbi/iccv21/LittleBoy/data/got10k.namelist"


# base_dir = "/media/lw/0A9AD66165F33762/trackingnet/trackingnet/"  # replace it with your own path
# result_file = "/media/lw/0A9AD66165F33762/trackingnet/trackingnet.namelist"

# base_dir = "/media/lw/09C1B27DA5EB573A/dataset/LaSOT/LaSOTBenchmark/"  # replace it with your own path
# result_file = "/media/lw/09C1B27DA5EB573A/dataset/LaSOT/lasot.namelist"
# base_dir = "/media/lw/09C1B27DA5EB573A/dataset/COCO2017/"  # replace it with your own path
# result_file = "/media/lw/09C1B27DA5EB573A/dataset/COCO2017/coco.namelist"
base_dir = "/media/lw/09C1B27DA5EB573A/dataset/GOT10K/full_data/"  # replace it with your own path
result_file = "/media/lw/09C1B27DA5EB573A/dataset/GOT10K/full_data/GOT10K.namelist"

assert (base_dir.endswith('/'))
fnames = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        path = os.path.join(root, file)
        if not os.path.exists(path):
            print("%s doesn't exist.")
        rela_path = path.replace(base_dir, "")
        fnames.append(rela_path)
        print(rela_path)


with open(result_file, 'w') as fout:
    for name in fnames:
        fout.write(name + '\n')
