DNA = "ATGTGTGCGCGATGATGCGCGATGCGCG"
print(len(DNA))
gc = (DNA.count("G") + DNA.count("C")) / len(DNA) * 100
gc = round(gc, 2)
print("GC: ", gc, "%")
print(f"First codon is: {DNA[0:3]}. And last codon is: {DNA[-3:]}")
RNA = DNA.replace("T", "U")
print(RNA)
#reverse complement
complement = DNA.replace("A", "t").replace("T", "a")
complement = complement.replace("C", "g").replace("G", "c")
rev_complement = complement.upper()[::-1]
print(rev_complement)

print(DNA.startswith("ATG"))
print(f"All three reading frames: first {DNA[0:]}, second {DNA[1:]}, third {DNA[2:]}")