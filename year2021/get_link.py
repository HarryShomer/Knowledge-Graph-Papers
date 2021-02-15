from googlesearch import search
import os

file = "OLDREADME.md"
with open(file, 'r') as f:
    lines = f.readlines()

new_file = "README.md"
with open(new_file, 'w') as f:
    for line in lines:
        line = line.strip()
        if line.startswith("1."):
            query = line.split("1.")[-1]
            assert len(query) > 10

            # get the first link by google search
            for paper_link in search(query, tld="co.in", num=10, stop=10, pause=2):
                break
            new_line = line + f" [[paper]]({paper_link})"+ '\n'
        else:
            new_line = line + '\n'
        # write it into the new file
        f.write(new_line)
        # print(new_line)


