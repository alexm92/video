import logging
import argparse
import sys
import os

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='File path')
    args = parser.parse_args()

    path = args.file
    if '/' in path:
        filename = path.split('/')[-1]
        path = '/'.join(path.split('/')[:-1])
        new_filename = '{0}/changed-{1}'.format(path, filename)
    else:
        new_filename = 'changed-{0}'.format(path)

    command = 'ffmpeg -y -i {0} -vf "scale=750:-2" -vcodec h264 {1}'.format(args.file, new_filename)
    log.info('Started converting video...')
    try:
        os.system(command)
        log.info('Done!')
    except:
        log.error('Error while converting')

