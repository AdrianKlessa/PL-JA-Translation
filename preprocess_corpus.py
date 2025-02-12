import pandas as pd
source_file = "tatoeba/Tatoeba.ja-pl.pl"
target_file = "tatoeba/Tatoeba.ja-pl.ja"

with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'r', encoding='utf-8') as tgt:
    source_lines = [line.strip() for line in src.readlines()]
    target_lines = [line.strip() for line in tgt.readlines()]

tatoeba = pd.DataFrame(
    {"Source": source_lines,
     "Target": target_lines}
)

from sklearn.model_selection import train_test_split
tatoeba_train, tatoeba_test = train_test_split(tatoeba, test_size=0.1, random_state=42)
tatoeba_valid, tatoeba_test = train_test_split(tatoeba_test, test_size=0.5, random_state=42)

tatoeba.to_json("Tatoeba.json", orient="records", lines=True)
tatoeba_train.to_json("Tatoeba_train.json", orient="records", lines=True)
tatoeba_valid.to_json("Tatoeba_valid.json", orient="records", lines=True)
tatoeba_test.to_json("Tatoeba_test.json", orient="records", lines=True)