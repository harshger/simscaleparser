from logparser import log_parser as lp
import select, sys

def main():
    parser = lp.log_parser()
    while(True):
        i, o, e = select.select([sys.stdin], [], [], 5)
        if not i:
            generate_output(parser, False)
            continue

        log_entry = sys.stdin.readline()
        if not log_entry:
            #ctrl-d
            generate_output(parser, True)
            sys.exit(0)

        output, error = parser.process_log_entry(log_entry, False)
        p_print(error, output)


def generate_output(parser, force):
    output = []
    error = []
    parser.process_buffer(output, error, force)
    p_print(error, output)


def p_print(error, output):
    for o in output:
        print(o)
    for e in error:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()
