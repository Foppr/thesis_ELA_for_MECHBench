import pandas as pd
import numpy as np

# 1. (Optional) Explicitly ensure the IDs are integers in missing_vectors
filtered_vectors['id'] = filtered_vectors['id'].astype(int)

# 2. Create a mapping dictionary from missing_vectors using x0 as the key
# We round to avoid tiny floating-point precision differences causing mismatch issues
vectors_map = dict(zip(filtered_vectors['x0'].round(6), filtered_vectors['id']))

# 3. Create a function to look up the correct ID, leaving it unchanged if no match is found
def find_true_id(row):
    rounded_x0 = round(row['x0'], 6)
    # Return the true ID from missing_vectors if it exists, otherwise keep original ID
    return vectors_map.get(rounded_x0, row['id'])

# 4. Apply the mapping to missing_results and safely convert back to integer
new_results['id'] = new_results.apply(find_true_id, axis=1).astype(int)

# 5. Sort the results by the newly updated true IDs
new_results = new_results.sort_values(by="id").reset_index(drop=True)

# Verify the output
print(new_results[:10].to_string())