if __name__ == '__main__':
    matches = []
    line = ""
    f = open("matches.txt")
    print("reading file")
    for line in f:
        splitlist = line.split(" ") # line is a string, has functionality assoc with it split into 4 element list
        # print(splitlist[0])
        matches.append(splitlist)
    # print(matches) # now have datastructure with all matches in
    print(" R E S U L T S")
    for match in matches:
       # print(match) does same thing as below
        homeTeam = match[0].strip()
        awayTeam = match[1].strip()
        homeScore = match[2].strip()
        awayScore = match[3].strip() # cleans up charas on end of files.
        print(homeTeam, " ", homeScore, " : ", awayScore, " ", awayTeam)


# store splitlist in matches, becomes a list within a list
    # pyhton string split need to make the string intgs -
# w3schools is good for looking up code

