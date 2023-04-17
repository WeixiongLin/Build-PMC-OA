'''Parse PMC Open Access pages
- request PMC pages
- extract <image, caption> pairs from pages
'''

import codecs
import os
import jsonlines
import pandas as pd
import pathlib
from tqdm import tqdm
from typing import List, Union
import subprocess

from bs4 import BeautifulSoup

from utils import write_jsonl
from data import OA_LINKS, UPDATE_SCHEDULE

def get_img_url(PMC_ID, graphic):
    img_url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/%s/bin/%s.jpg' % (PMC_ID, graphic)
    return img_url

def get_video_url(PMC_ID, media):
    mov_url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/%s/bin/%s' % (PMC_ID, media)
    return mov_url

def get_filelist_url(volume_id):
    filelist_url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=%s' % volume_id
    return filelist_url

def parse_xml(xml_path: Union[str, pathlib.Path]):
    '''
    Return: images' info of the xml. [{
        'media_id': media_id,
        'caption': caption ...
    }]
    '''
    with codecs.open(xml_path, encoding='utf-8') as f:
        document = f.read()
    soup = BeautifulSoup(document, 'lxml')

    # extract PMC_ID from xml_path
    if isinstance(xml_path, pathlib.Path):
        xml_path = str(xml_path)
    PMC_ID = xml_path.split('/')[-1].strip('.xml')
    
    item_info = []

    figs = soup.find_all(name='fig')
    for fig in figs:
        media_id = fig.attrs['id']

        if fig.graphic:
            graphic = fig.graphic.attrs['xlink:href']
            media_url = get_img_url(PMC_ID, graphic)
            file_extension = media_url.split('.')[-1]  # .jpg
            media_name = f'{PMC_ID}_{media_id}.jpg'  # xml gives no file extension for image, so assign .jpg manually
        elif fig.media:
            media = fig.media.attrs['xlink:href']
            media_url = get_video_url(PMC_ID, media)
            file_extension = media_url.split('.')[-1]  # .mov .dcr .avi
            media_name = f'{PMC_ID}_{media_id}.{file_extension}'
        else:
            raise RuntimeError(f'error occurs when parsing xml figs: {xml_path}')

        if file_extension not in ['mov', 'jpg', 'dcr', 'avi', 'mpeg']:
            raise RuntimeError(f'{xml_path} contains media we dont know before: {media_name}, {media_url}')

        # not all figs have captions, check PMC212690 as an example: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC212690/
        if not fig.caption:
            caption = ''
        else:
            caption = fig.caption.get_text()

        item_info.append({
            'PMC_ID': PMC_ID,
            'media_id': media_id,  # media_id could represent image or video. [image: pbio-0020008-g002; video: pbio-0020008-v001]
            'caption': caption,
            'media_url': media_url,
            'media_name': media_name
        })

    return item_info


def get_volume_info(volumes: List[int], extraction_dir: pathlib.Path) -> List[str]:
    '''Extract image info from volumes
    Args:
        volumes: volumes' IDs to extract
        extraction_dir: /dir/path/ where volume is extraced
        file_name: the csv keeping xml info
    '''
    if not isinstance(extraction_dir, pathlib.Path):
        extraction_dir = pathlib.Path(extraction_dir)
    info = []
    for volume_id in volumes:
        volume = f'PMC00{volume_id!s}xxxxxx' 
        file_name = f'oa_comm_xml.{volume}.baseline.{UPDATE_SCHEDULE}.filelist.csv' 
        file_path = extraction_dir / volume / file_name

        df = pd.read_csv(file_path, sep=',')

        for idx in tqdm(range(len(df)), desc='parse xml'):
            xml_path = extraction_dir / volume / df.loc[idx, 'Article File']
            item_info = parse_xml(xml_path)
            info += item_info
    return info

if __name__ == '__main__':
    print('\033[32mParse PMC documents\033[0m')

    volume_info = get_volume_info(
        volumes=[0],
        extraction_dir=pathlib.Path('./PMC_OA')
    )
    print(f'Num of figs in volumes: {len(volume_info)}')
    write_jsonl(
        data_list=volume_info,
        save_path='./volume0.jsonl'
    )
