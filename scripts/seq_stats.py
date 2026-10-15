sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)

print(len(sequences))
print(sequences[0], sequences[-1])
sequences.append("GGCTA")
lengths = [len(sequences[0]), len(sequences[1]), len(sequences[2]), len(sequences[3]), len(sequences[4])]
print(lengths)
print(f"The shortest length: {min(lengths)}. The longest length: {max(lengths)}, The average length: {sum(lengths)/len(lengths)}")
name, chrom, start, end = gene
print(f"{name} is on {chrom} and is {end-start} bases long")
#gene[0] = "FOXO" #TypeError: 'tuple' object does not support item assignment
genes = [("BRCA1", 81188), ("TP53", 25759)]
gene, length = genes[1]
print(length)