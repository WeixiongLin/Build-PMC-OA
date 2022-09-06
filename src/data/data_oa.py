'''File list for PMC OA: [csv, txt, tar]
'''


volume = 'PMC00%dxxxxxx'
csv_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/oa_comm_xml.PMC00%dxxxxxx.baseline.2022-09-03.filelist.csv'
txt_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/oa_comm_xml.PMC00%dxxxxxx.baseline.2022-09-03.filelist.txt'
tar_url = 'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/oa_comm_xml.PMC00%dxxxxxx.baseline.2022-09-03.tar.gz'

OA_LINKS = {}

for volume_id in range(10):
    OA_LINKS[volume % volume_id] = {}
    OA_LINKS[volume % volume_id]['csv_url'] = csv_url % volume_id
    OA_LINKS[volume % volume_id]['txt_url'] = txt_url % volume_id
    OA_LINKS[volume % volume_id]['tar_url'] = tar_url % volume_id


if __name__ == '__main__':
    print(OA_LINKS)
