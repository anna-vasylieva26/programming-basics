seq = "ATGATGTGTGNT"
if len(seq) < 30:
    print("too short")
if "N" in seq:
    print("contains unknown bases")
gc = (seq.count("G") + seq.count("C"))/len(seq)*100
if gc > 60:
    print("GC high")
elif gc <40:
    print("AT rich")
else:
    print("balanced")
if seq.startswith("ATG") and len(seq) % 3 == 0:
    print("possible ORF")

