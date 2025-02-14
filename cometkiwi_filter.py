import pandas as pd
from comet import load_from_checkpoint

model = load_from_checkpoint("cometkiwi_model/checkpoints/cometkiwi_model.ckpt")
source_file = "opensubtitles/OpenSubtitles.ja-pl.pl"
target_file = "opensubtitles/OpenSubtitles.ja-pl.ja"

with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'r', encoding='utf-8') as tgt:
    source_lines = [line.strip() for line in src.readlines()]
    target_lines = [line.strip() for line in tgt.readlines()]

opensubs = pd.DataFrame(
    {"Source": source_lines,
     "Target": target_lines}
)

def to_cometkiwi_data(source_column, target_column):
    return {"src": source_column, "mt": target_column}

opensubs['cometkiwi_data'] = opensubs.apply(lambda x: to_cometkiwi_data(x.Source, x.Target), axis=1)
data_in = opensubs["cometkiwi_data"].tolist()
data_out = model.predict(data_in, batch_size=32, gpus=1)
opensubs['Cometkiwi_score']=pd.Series(data_out[0]) # data_out[1] is the average score across the dataset
opensubs.to_json("opensubs_scored.json", orient="records", lines=True)
filtered = opensubs[["Source","Target","Cometkiwi_score"]][opensubs.Cometkiwi_score>0.8].sample(frac=1.0)
filtered.to_json("opensubs_filtered.json", orient="records", lines=True)


source_file = "ted2020/TED2020.ja-pl.pl"
target_file = "ted2020/TED2020.ja-pl.ja"

with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'r', encoding='utf-8') as tgt:
    source_lines = [line.strip() for line in src.readlines()]
    target_lines = [line.strip() for line in tgt.readlines()]

ted = pd.DataFrame(
    {"Source": source_lines,
     "Target": target_lines}
)

ted['cometkiwi_data'] = ted.apply(lambda x: to_cometkiwi_data(x.Source, x.Target), axis=1)
data_in = ted["cometkiwi_data"].tolist()
data_out = model.predict(data_in, batch_size=32, gpus=1)
ted['Cometkiwi_score']=pd.Series(data_out[0])
ted.to_json("ted_scored.json", orient="records", lines=True)
filtered_ted = ted[["Source","Target","Cometkiwi_score"]][ted.Cometkiwi_score>0.8].sample(frac=1.0)
filtered_ted.to_json("ted_filtered.json", orient="records", lines=True)