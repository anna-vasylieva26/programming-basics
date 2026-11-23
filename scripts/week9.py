import pandas as pd
#pandas way
with open("data/samples_week9.csv") as f:
    df = pd.read_csv(f)
    print(df["gc_content"].mean())
    print(df.describe())
    
#my way
with open("data/samples_week9.csv") as f:
    gc_content = []
    lines = f.readlines()
    for line in lines[1:]:
        gc_content = line.split(",")[1]
        print(gc_content)
        gc_content_avr = sum(gc_content)/len(gc_content)
        print(gc_content_avr)
