import argparse
import re


def check_fmt(file):
    flag_latex = False
    flag_git = False

    pat_git1 = re.compile(r'```math.+```', re.S)
    pat_git2 = re.compile(r'\$`.+`\$', re.S)
    pat_latex1 = re.compile(r'\$\$.+\$\$', re.S)
    pat_latex2 = re.compile(r'\$.+\$', re.S)
    with open(file) as f:
        file_data = f.read()

    if pat_latex1.search(file_data) or pat_latex2.search(file_data):
        flag_latex = True

    if pat_git1.search(file_data) or pat_git2.search(file_data):
        flag_git = True

    if flag_git:
        print('Git format')
    elif flag_latex:
        print('Latex format')
    else:
        print('No math formula found')

def latex2git(file):
    with open(file, 'r') as f:
        file_data = f.read()
        file_data = re.sub(r'\$\$(.+?)\$\$', lambda m: '```math' + m.group(1) + '```', file_data, 0, re.S)
        file_data = re.sub(r'\$(.+?)\$', lambda m: '$`' + m.group(1) + '`$', file_data, 0, re.S)

    with open(file, 'w') as f:
        f.write(file_data)


def git2latex(file):
    with open(file, 'r') as f:
        file_data = f.read()
        file_data = re.sub(r'```math(.+?)```', lambda m: '$$'+m.group(1)+'$$', file_data, 0, re.S)
        file_data = re.sub(r'\$`(.+?)`\$', lambda m: '$'+m.group(1)+'$', file_data, 0, re.S)

    with open(file, 'w') as f:
        f.write(file_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='file.md', type=str, help='input markdown file')
    parser.add_argument('-c', action='store_true', help='check markdown file math format')
    parser.add_argument('-l', action='store_true', help='change to latex format')
    parser.add_argument('-g', action='store_true', help='change to git format')
    args = parser.parse_args()

    if args.c:
        check_fmt(args.file)
    elif args.l:
        git2latex(args.file)
    elif args.g:
        latex2git(args.file)
    else:
        raise Exception('Invalid arguments')


