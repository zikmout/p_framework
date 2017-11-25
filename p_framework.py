# p_framework implemented at home
import sys

    def main(argv):
        print('Welcome to the program p_framework')

if __name__ == '__main__':
    try:
        main(argv)
    except IOError or KeyboardInterrupt:
        sys.exit(0)
        