import pandas as pd

df = pd.read_csv("russian_middle_aged_male_1/public_tts_df_02.csv")
df = df[df['text_path'].str.contains("russian_middle_aged_male_1")]
result = ""

for i in range(len(df)):
    audio = "/".join(df["wav_path"].iloc[i].split("/")[1:])
    text = df["text"].iloc[i]
    result += audio + "|" + text + "|" + text + "\n"

with open("russian_middle_aged_male_1/metadata_open_tts.csv", "w") as fp:
    fp.write(result)
