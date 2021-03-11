from src.counter import disjoin_counter

import argparse


if __name__ == '__main__':

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-rp", "--recording_path", help = "path to recording file")

    parser.add_argument("-k", "--access_key", help = "access key")


    # Read arguments from command line
    args = parser.parse_args()

    access_key = args.access_key

    recording_path = args.recording_path

    counter = disjoin_counter(access_key, recording_path)

    counter.start()
