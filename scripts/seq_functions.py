def gc_content (seq):
    gc_sum = seq.count("G")+seq.count("C")
    result = (gc_sum/len(seq))*100
    result = round(result, 2)
    return result
def reverse_complement(seq):
    rev = seq[::-1]
    complement = rev.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    rev_complement = complement.upper()
    return rev_complement
def is_usable(seq, min_length=30):
    if len(seq)>min_length and "N" not in seq:
        return True
    else:
        return False

try1 = gc_content("GTCGTGAACCATG")
print(try1)
try2 = reverse_complement("GTCGTGAACCATG")
print(try2)
try3 = is_usable("GTCGTGAACCATG")
print (try3)