import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        dest='file',
                        type=argparse.FileType(mode='rt'),
                        help='Имя файла')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    count = 0
    for _ in args.file:
        count += 1

    print(count)
