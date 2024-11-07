import pandas as pd

df = pd.read_csv("./100Days/intermediates/day-25/squirrel-census/squirrel_census.csv")
pd.set_option("display.max_columns", None)
# print(len(df["Primary Fur Color"]))
# print(df["Primary Fur Color"])

# no_color = df[df["Primary Fur Color"].isnull()]
gray_count = len(df[df["Primary Fur Color"] == "Gray"])
red_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_count = len(df[df["Primary Fur Color"] == "Black"])
print(gray_count, red_count, black_count)

sq_count_df = pd.DataFrame(
    columns=["Fur Color", "Count"],
    data=[["grey", gray_count], ["red", red_count], ["black", black_count]],
)

print(sq_count_df)

sq_count_df.to_csv("./100Days/intermediates/day-25/squirrel-census/squirrel_count.csv")
