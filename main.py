demPixles = []

def main():
    # Data Reading
    fp = open('resources/DEM.txt', 'r')
    lines = fp.readlines()
    cnt = 1

    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1


if __name__ == "__main__":
    main()