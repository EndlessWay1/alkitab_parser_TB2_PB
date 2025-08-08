from parsing import parses_alkitab

def main():
    try:
        INJIL = ['MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM', '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH', '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE', '2PE', '1JN', '2JN', '3JN', 'JUD', 'REV']
        for i in INJIL:
            parses_alkitab(i)
            print(f"{i} DONE!\n")
    except ValueError:
        print(1)
    print(0)

if __name__ == "__main__":
    main()
