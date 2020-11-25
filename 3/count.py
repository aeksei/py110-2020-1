import argparse


def count():
    ...


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('start')
    parser.add_argument('step')

    parser.add_argument('-n')

    subparser = parser.add_subparsers(dest='action',
                                      description='Вывести в консоль или вывести в файл')

    create_save_subparser(subparser)
    create_show_subparser(subparser)

    return parser


def create_save_subparser(subparser):
    parser = subparser.add_parser('save')
    # parser.add_argument()
    ...


def create_show_subparser(subparser):
    parser = subparser.add_parser('show')
    ...


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.action == 'show':
        print('Печатаем в консоль')
    elif args.action == 'save':
        print('Сохраняем в файл')


if __name__ == '__main__':
    main()
