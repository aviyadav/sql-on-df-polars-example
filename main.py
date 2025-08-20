import polars as pl

data_file = "data/sample.data"
pl_df = pl.read_json(data_file)

# print(pl_df)
# print(pl_df.shape)
# print(pl_df.columns)
# print(pl_df.head())
# print(pl_df.tail())
# print(pl_df.describe())
# print(pl_df.dtypes)

rule_file = "data/rules.csv"
rules_df = pl.read_csv(rule_file)

# print(rules_df)
# print(rules_df.shape)
# print(rules_df.columns)
# print(rules_df.head())
# print(rules_df.tail())
# print(rules_df.describe())
# print(rules_df.dtypes)


rule_sql_list = []

for rule_condition, output_column in rules_df.iter_rows():
    rule_row_sql = f"{rule_condition} AS {output_column}"
    rule_sql_list.append(rule_row_sql)

# print(rule_sql_list)
rule_sql = ", ".join(rule_sql_list)

df_query = f"select * , {rule_sql} from pl_df"

result_df = pl.sql(df_query).collect()

print(result_df)
# print(result_df.shape)
# print(result_df.columns)
# print(result_df.head())
# print(result_df.tail())

result_df.write_parquet("data/result.parquet")

print("Result written to data/result.parquet")
print("Done")