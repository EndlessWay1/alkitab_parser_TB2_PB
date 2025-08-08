import bs4
import requests
import json

def parses_alkitab(Injil: str):
    cpt = Injil
    print(f"Started parsing {cpt}")
    PanjangInjil = {
        "MAT" : 28,
        "MRK" : 16,
        "LUK" : 24,
        "JHN" : 21,
        "ACT" : 28,
        "ROM" : 16,
        "1CO" : 16,
        "2CO" : 13,
        "GAL" : 6,
        "EPH" : 6,
        "PHP" : 4,
        "COL" : 4,
        "1TH" : 5,
        "2TH" : 3,
        "1TI" : 6,
        "2TI" : 4,
        "TIT" : 3,
        "PHM" : 1,
        "HEB" : 13,
        "JAS" : 5,
        "1PE" : 5,
        "2PE" : 3,
        "1JN" : 5,
        "2JN" : 1,
        "3JN" : 1,
        "JUD" : 1,
        "REV" : 22
    }
    p = PanjangInjil[cpt]
    ayat = {}
    for i in range(1, p + 1):
        response = requests.get(f"https://www.bible.com/bible/2863/{cpt}.{i}.PBTB2")
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        dive = soup.body.find_all("span", {"class":"ChapterContent_verse__57FIw"})
        if not dive:
            raise ValueError

        ayat[i] = {}
        for k in dive:
            try:
                ayat[i][k.find("span", {"class":"ChapterContent_label__R2PLt"}).string] = k.find("span", {"class" : "ChapterContent_content__RrUqA"}).string
            except AttributeError:
                continue
        print(f"Parsing {cpt}: {i} / {p}") 
        
    with open(f"ayat/{cpt}.json", "w") as ofile:
        json.dump(ayat, ofile)
    
    print(f"Successfully Parses {cpt}!")

if __name__== "__main__":
    pass
