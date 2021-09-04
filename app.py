from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(description='Make emotes fast again!')
    parser.add_argument('--disableauto', action='store_true',
                        help='Disable automatic parsing')
    args = parser.parse_args()
