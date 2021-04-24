import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    print("Month of ", month, "/", year, " has ", 31, " days.", sep="")

if __name__ == '__main__':
    main()
