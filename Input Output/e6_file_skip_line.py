# Exercise 6: Write all content of a given file into a new file by skipping line number 5
with open("old_file.txt", "r") as rf:
    lines = rf.readlines()

with open("new_file.txt", "w") as wf:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            wf.write(line)
        count += 1

