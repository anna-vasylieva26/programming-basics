DNA_seq1 = "CTCATGAAGGCTTGCGAAGTCAGTGACATGTTTAGGAGCGC"
print(len(DNA_seq1))
print(DNA_seq1.count("G"))
print(DNA_seq1.count("C"))
gc = (DNA_seq1.count("G") + DNA_seq1.count("C")) / len(DNA_seq1) * 100
gc = round(gc, 2)
print("GC: ", gc, "%")

DNA_seq2 =input ("Enter DNA sequence: ")
print (len(DNA_seq2))
gc2 = (DNA_seq2.count("C") + DNA_seq2.count("G")) / len(DNA_seq2) * 100 
gc2 = round(gc2, 2)
print("GC content of your DNA sequence is: ", gc2, "%")
