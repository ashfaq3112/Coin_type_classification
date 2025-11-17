import os
import csv
import re

dataset_dir = "coin_data/"   # folder with images
output_csv = "labels.csv"

pattern = r"class(\d+)_image(\d+)\.png"

rows = [("image_path", "label")]

for file in os.listdir(dataset_dir):
    match = re.match(pattern, file)
    if match:
        class_id = int(match.group(1))  # extract class number
        rows.append((file, class_id))

# save CSV
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("labels.csv created successfully!")
