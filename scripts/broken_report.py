# broken_report.py
# GC content report for sequences in a FASTA file.
# This script has 5 bugs. Run it, read the FIRST error, fix it, run again.


def read_fasta(path):
    sequences = {}
    name = None
    try: 
        with open(r"C:\Users\annav\OneDrive\KSE\programming-basics\scripts\sequence.fasta") as f:
            if f is False:
                print("OOps")
            else:
                for line in f:
                    line = line.strip()
                    if line.startswith(">"):
                        name = line[1:]
                        sequences[name] = ""
                    else:
                        sequences[name] += line
            return sequences
    except FileNotFoundError:
        print("oopsie")
    return {}
    

def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return gc


def report(name, seq):
    gc = gc_content(seq)
    print(f"Sequence {name}: length {len(seq)}")
    print(f"  GC content: {gc:.1f}%") #print(f"  GC content: {gc * 100:.1f}%")
    return gc


sequences = read_fasta("sequences.fasta")

results = {}
for name, seq in sequences.items():
    results[name] = report(name, seq)

try:
    average = sum(results.values()) / len(results)
    print(f"Average GC: {average:.1f}%")
except ZeroDivisionError:
    print("some problems with division on 0")

try:
    print("Reference sequence:", sequences[name])
except NameError:
    print ("mistake lol")
