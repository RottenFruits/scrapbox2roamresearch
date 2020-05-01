#!/usr/bin/env python3
import json
import datetime
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--f",
                    help="input file")
parser.add_argument("--o",
                    help="output path")
args = parser.parse_args()
print(args.f)

def link(text):
    ret = re.sub(r"\[([ぁ-んァ-ン０-９a-zA-Z0-9\-\ ]+)\]", r"[[\1]]", text) #[の後に*以外置換
    return(ret)

def add_indet_md(text):
    ret = []
    for t in text:
        t = "- " + t
        ret.append(str(t))
    return(ret)

def text_treat(text):
    text = add_indet_md(text)
    text = '\n'.join(text)
    text = link(text)
    return(text)

def date_suffix(time):
    b = datetime.datetime.fromtimestamp(time).strftime("%B")
    y = datetime.datetime.fromtimestamp(time).strftime("%Y")
    d = datetime.datetime.fromtimestamp(time).strftime("%d")
    if d == "1":
        d = d + "st"
    elif d == "2":
        d = d + "nd"
    elif d == "3":
        d = d + "rd"
    else:
        d = d + "th"
    ret = b + " " + d + ", " + y
    return(ret)

def main():
    f = open(args.f, 'r')
    json_data = json.load(f)

    for p in json_data["pages"]:
        #title
        title = p["title"]

        #created date
        #ct = date_suffix(p["created"])
        #ct = "    - " + "[[" + ct + "]]"
        #header = "".join(["- Metadata", "\n", ct, "\n"])

        #main text
        text = text_treat(p["lines"])
        text = "".join(text)

        with open(args.o + "/" + title + ".md", mode = 'w') as f:
            f.write(text)

if __name__ == '__main__':
    main()