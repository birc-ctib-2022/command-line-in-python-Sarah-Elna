import sys

for line in sys.stdin:
    if '\n' in line:
        print(line, end = '')
    else:
        print(line)

args = sys.argv[1:]  # get all command line arguments

print(args)

if args:  # if args is not empty
    for fname in args:
        with open(fname) as f:
            file = open(f, 'r')
            lines = readlines(file)
            line_nr = 0
            for line in lines:
                line_nr += 1
                print(line_nr, ' ', line)
else:
    print(sys.stdin.read(), end='')