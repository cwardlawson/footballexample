if __name__ == '__main__':
    matches = [] # blank list for inputs
    line = ""
    f = open("matches.txt")
    print("reading file")
    for line in f: # loop for every line in the file
        splitlist = line.split(" ") # line is a string, has functionality assoc with it split into 4 element list
        # print(splitlist[0])
        if len(splitlist) != 4:  # tell user if length list is incorrect
            print("error with match data:", line, end="")
            continue  # continues list loop wihtout the error data line
        try:
            splitlist[2] = int(splitlist[2])
            splitlist[3] = int(splitlist[3])
        except ValueError:
            print("invalid score" , line, end="")
            continue

        matches.append(splitlist) # items in splitlist go into my matches blank list
    # print(matches) # now have datastructure with all matches in
    print(" R E S U L T S")
    for match in matches: # iterating over matches list
       # print(match) does same thing as below
        homeTeam = match[0].strip()
        awayTeam = match[1].strip() # cleans up charas on end of files.
        homeScore = match[2]# no strip because is converted to an integer
        awayScore = match[3]
        print(homeTeam, " ", homeScore, " : ", awayScore, " ", awayTeam)




# store splitlist in matches, becomes a list within a list
    # pyhton string split need to make the string intgs -
# w3schools is good for looking up code

