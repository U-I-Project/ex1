import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        day=31
    elif month==2:
        if (year%4==0 and year%100!=0) or year%400==0:
            day = 29
        else:
            day = 28
    else:
        day = 30
    print("Month of ", month, "/", year, " has ", day, " days.", sep="")
    /* add nothing */

if __name__ == '__main__':
    main()
