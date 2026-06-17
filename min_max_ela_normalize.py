import os
import numpy as np
import pandas as pd

# Load the external stats file once to save time
ela_stats = pd.read_csv("ela_feature_stats.csv")
stats_filtered = ela_stats[
    (ela_stats["dimension"] == 5) & (ela_stats["dataset"] == "BBOB_SM_all")
]

# Define base directory and variables to loop over
base_dir = os.path.join("Folder_Points", "500D")
problems = ["p1", "p2", "p3"]
sizes = ["30d", "60d", "125d", "250d", "500d"]

for p in problems:
    # Construct paths for source and target directories
    source_dir = os.path.join(base_dir, f"data_{p}", "ELA")
    target_dir = os.path.join(base_dir, f"data_{p}", "ELA_min_max")

    # Ensure the new target directory exists
    os.makedirs(target_dir, exist_ok=True)

    for size in sizes:
        # Match your exact naming convention, e.g., 30d5_p1_seed1312_ela.csv
        file_name = f"{size}15_{p}_seed1312_ela.csv"
        file_path = os.path.join(source_dir, file_name)

        # Check if the file exists before processing to prevent crashes
        if not os.path.exists(file_path):
            print(f"Skipping: {file_path} (File not found)")
            continue

        # Load file
        original_ela_df = pd.read_csv(file_path)

        # Merge with stats for min-max calculation
        merged_df = pd.merge(
            original_ela_df,
            stats_filtered[["feature", "min", "max"]],
            on="feature",
            how="left",
        )

        # If value > max or value < min, adjust bounds dynamically
        merged_df["min"] = np.minimum(merged_df["min"], merged_df["value"])
        merged_df["max"] = np.maximum(merged_df["max"], merged_df["value"])

        # Normalize
        denominator = merged_df["max"] - merged_df["min"]
        denominator = denominator.replace(0, np.nan)
        merged_df["normalized_value"] = (
            merged_df["value"] - merged_df["min"]
        ) / denominator
        merged_df["normalized_value"] = merged_df["normalized_value"].fillna(
            0.0
        )

        # Structure the final DataFrame
        new_df = merged_df[["feature", "normalized_value"]].rename(
            columns={"normalized_value": "value"}
        )

        # Save to the new ELA_min_max folder with the same file name
        output_path = os.path.join(target_dir, file_name)
        new_df.to_csv(output_path, index=False)

print("Processing complete! All folders and normalized files have been created.")