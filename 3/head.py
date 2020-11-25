import argparse


def create_parser():
    """
    python head.py 3/test.txt
    python head.py 3/test.txt -n 5
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        type=argparse.FileType(mode='rt'),
                        help='Имя файла')

    parser.add_argument('-n',
                        type=int,
                        default=10,
                        help='Количество строк')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    for _ in range(args.n):
        print(next(args.filename), end='')





