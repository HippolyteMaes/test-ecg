import argparse
import datetime
import os
import sys

import frontend


DATETIME_FORMAT = '%Y-%m-%d_%H::%M::%S'


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to record')
    parser.add_argument('datetime', type=str,
                        help='date and time of the record start (yyyy-mm-dd_HH::MM::SS)')

    args = parser.parse_args()
    try:
        if not os.path.exists(args.path):
            raise FileNotFoundError

        recording_time = datetime.datetime.strptime(args.datetime, DATETIME_FORMAT)
    except FileNotFoundError:
        print('{} is not valid path'.format(args.path))
        sys.exit(1)
    except ValueError:
        print('Please follow the following datetime format : yyyy-mm-dd_HH::MM::SS')
        sys.exit(1)
        

    frontend.CLI.run(recording_time, args.path)
