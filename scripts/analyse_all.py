sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
for seq in sequences:
    print(seq, len(seq))
length = []
for seq in sequences:
    length.append(len(seq))
print(sum(length)/len(sequences))
i = 0
for seq in sequences:
    if seq.startswith("ATG"):
        i = i + 1
print(i)
for seq in sequences:
    if len(seq) > 5:
        print(seq)
for seq in sequences:
    gc = (seq.count("G") + seq.count("C"))/len(seq)*100
    print(seq, gc)