'''Fetch catelogue from PMC Open Access Subset
python src/fetch_oa.py --extraction-dir /remote-home/weixionglin/build-pubmed/PMC_OA
python src/fetch_oa.py --extraction-dir /remote-home/share/medical/public/PMC_OA
'''
import glob
import os
import pathlib
import subprocess
import shutil

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 设置两个处理器handler
console_handler = logging.StreamHandler()
# 给两个相同名称的logger添加上处理器
logger.addHandler(console_handler)
# 设置一下格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \33[32m%(message)s\033[0m')
console_handler.setFormatter(formatter)

import tempfile
tempfile.gettempdir()

from data import OA_LINKS  # file links of PMC Open Access
from args import parse_args_oa
from parser import get_volume_info
from utils import write_jsonl

def provide_extraction_dir():
    if not os.path.exists(args.extraction_dir):
        os.makedirs(args.extraction_dir, 0o755)

    # Delete extraction directory contents if it's not empty
    elif len(os.listdir(args.extraction_dir)) > 0 and not args.keep_archives:
        if not args.delete_extraction_dir:
            raise Exception('The extraction directory {0} is not empty, ' +
                            'please pass -d if confirm deletion of its contents')

        files = glob.glob(os.path.join(args.extraction_dir, '*'))
        for f in files:
            if os.path.isdir(f):
                shutil.rmtree(f, True)
            else:
                os.remove(f)


def extract_archive(archive_path, target_dir):
    subprocess.call(['tar', 'zxf', archive_path, '-C', target_dir])


def download_archive(volumes, extract=True):
    '''
    extract: whether to extract archives
    '''
    logger.info('Volumes to download: %s' % volumes)

    # Fetch filelist info from PMC
    # archive_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/oa_comm_xml.PMC000xxxxxx.baseline.2022-09-03.filelist.csv'
    # subprocess.call(['wget', '-nc', '-nd', '-c', '-q', '-P', args.extraction_dir, archive_url])

    for volume_id in volumes:
        volume = 'PMC00%dxxxxxx' % volume_id
        csv_url = OA_LINKS[volume]['csv_url']
        tar_url = OA_LINKS[volume]['tar_url']
        logger.info(csv_url)
        logger.info(tar_url)

        subprocess.call(['wget', '-nc', '-nd', '-c', '-q', '-P', '%s/%s' % (args.extraction_dir, volume), csv_url])
        subprocess.call(['wget', '-nc', '-nd', '-c', '-q', '-P', '%s/%s' % (args.extraction_dir, volume), tar_url])

        if not pathlib.Path('%s/%s/%s' % (args.extraction_dir, volume, volume)).exists():
            logger.info('Extracting %s' % volume)
            extract_archive(
                archive_path='%s/%s/%s' % (args.extraction_dir, volume, tar_url.split('/')[-1]),
                target_dir='%s/%s' % (args.extraction_dir, volume)
            )
            logger.info('%s Done', volume)
        else:
            logger.info('%s already exists', volume)
    # end for


if __name__ == '__main__':
    # Check if wget is available
    if not shutil.which("wget"):
        print("wget not found, please install wget and put it on your PATH")
        exit(-1)
    args = parse_args_oa()
    download_archive(volumes=args.volumes)

    # Parse XML files into image info
    logger.info('Extracting Volume INFO')
    volume_info = get_volume_info(
        volumes=args.volumes,
        extraction_dir=args.extraction_dir
    )
    save_name = ''.join([str(volume_id) for volume_id in args.volumes])
    logger.info('Writing Volume INFO')
    write_jsonl(
        data_list=volume_info,
        save_path=f'{args.extraction_dir}/{save_name}.jsonl'
    )

    logger.info('Done')
