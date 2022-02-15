#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")

#def main():
#    try:
#        configuration = open('config.txt')
#    except Exception:
#        print("Couldn't find the config.txt file!")

#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as FNF:
        print("Couldn't find the config.txt file!", FNF, FNF.errno)
    except IsADirectoryError as DE:
        print("Found config.txt but it is a directory, couldn't read it", DE, DE.errno)
    except (BlockingIOError, TimeoutError) as DbE:
        print("Filesystem under heavy load, can't complete reading configuration file", DbE, DbE.errno)

if __name__ == '__main__':
    main()