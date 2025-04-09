import pandas as pd
import fireducks as fd
import time

# Load Dataset
pdf = pd.read_csv('large_dataset.csv')
fdf = fd.read_csv('large_dataset.csv')

### Multiple Operations Together ###
# Filter -> GroupBy -> Sort -> Top 5

print("Pandas Execution:")
start_time = time.time()
result_pdf = (
    pdf[pdf['amount'] > 50]  # Filter
    .groupby('category')['amount']  # GroupBy
    .sum()
    .reset_index()
    .sort_values('amount', ascending=False)  # Sort
    .head(5)  # Top 5
)
print(result_pdf)
print("Pandas Total Time:", time.time() - start_time)


print("\nFireDucks Execution:")
start_time = time.time()
result_fdf = (
    fdf[fdf['amount'] > 50]  # Filter
    .groupby('category')['amount']  # GroupBy
    .sum()
    .reset_index()
    .sort('amount', descending=True)  # Sort
    .head(5)  # Top 5
)
print(result_fdf)
print("FireDucks Total Time:", time.time() - start_time)
