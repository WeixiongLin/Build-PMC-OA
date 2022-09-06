'''parse args for PMC OA
'''
import argparse
import multiprocessing
import os


def parse_args_oa():
    parser = argparse.ArgumentParser(
        description=__doc__.strip(),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-s', '--subdir',
        help='name of image subdirectory, relative to dlinks.txt location',
        default='images'
    )
    parser.add_argument(
        '-e', '--extraction-dir',
        help='path to the directory where downloaded archives and '
             + 'images are extracted before being moved to the data subdirectory',
        default=os.path.join('./', 'PMC_OA'),
    )
    parser.add_argument(
        '-d', '--delete-extraction-dir',
        help='to avoid loss of data, this must be passed to confirm that all '
             + 'data in the extraction directory will be deleted',
        action='store_true',
    )
    parser.add_argument(
        '-k', '--keep-archives',
        help='keep downloaded archives after extraction. Ensure sufficient '
             + 'available disk space at the extraction directory location',
        action='store_true',
    )
    parser.add_argument(
        '-n', '--num-processes',
        help='number of parallel processes, reduce this if you are being '
             + 'locked out of the PMC FTP service',
        default=multiprocessing.cpu_count(),
        type=int,
    )
    parser.add_argument(
        '-r', '--num-retries',
        help='number of retries for failed downloads before giving up',
        default=10,
        type=int,
    )
    parser.add_argument(
        '--volumes',
        help='determine the volumes to fetch from PMC OA',
        nargs="+",
        default=[0],
        type=int
    )

    return parser.parse_args()
