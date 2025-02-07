import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/asl-citizen/raw/train_10.csv")

# Extract the video IDs for the "book" class
glosses = data.Gloss.to_list()

fig = plt.figure(figsize=(20, 5))
plt.hist(glosses, bins=10, density=True, edgecolor="black", linewidth=1, align="mid")
plt.savefig("experiments/hist.png")
plt.close()
