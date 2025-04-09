# Load Libraries
import pandas as pd
import fireducks.pandas as fd
import time

# File Path
file_path = 'large_dataset.csv'

# -----------------------------
# 1. Read CSV
start = time.time()
pandas_df = pd.read_csv(file_path).head()
print("Pandas Read Time:", time.time() - start)

start = time.time()
fd_df = fd.read_csv(file_path).head()
print("FireDucks Read Time:", time.time() - start)


# -----------------------------
# 2. Filter data → amount > 80
start = time.time()
filtered_pandas = pandas_df[pandas_df['amount'] > 80]
print("Pandas Filter Time:", time.time() - start)

start = time.time()
filtered_fd = fd_df[fd_df['amount'] > 80]
print("FireDucks Filter Time:", time.time() - start)


# -----------------------------
# 3. GroupBy category & sum amount
start = time.time()
result_pandas = filtered_pandas.groupby('category')['amount'].sum().reset_index()
print("Pandas GroupBy Time:", time.time() - start)

start = time.time()
result_fd = filtered_fd.groupby('category')['amount'].sum().reset_index()
print("FireDucks GroupBy Time:", time.time() - start)


# -----------------------------
# 4. Sort by amount descending
start = time.time()
sorted_pandas = result_pandas.sort_values(by='amount', ascending=False)
print("Pandas Sort Time:", time.time() - start)

start = time.time()
sorted_fd = result_fd.sort_values(by='amount', ascending=False)
print("FireDucks Sort Time:", time.time() - start)


# -----------------------------
print("Demo Completed Successfully!")
