import pandas as pd

# Load the CSV
input_csv_path = '/home/luxde/milcah/YouTube-Project/alex_videos.csv'
df = pd.read_csv(input_csv_path)

# Cleaning data
# Ensure views, likes, comments are integers
df['views'] = pd.to_numeric(df['views'], errors='coerce').fillna(0).astype(int)
df['likes'] = pd.to_numeric(df['likes'], errors='coerce').fillna(0).astype(int)
df['comments'] = pd.to_numeric(df['comments'], errors='coerce').fillna(0).astype(int)

# Convert published_at to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Create a new 'year' column
df['year'] = df['publish_time'].dt.year

# Save the transformed data
output_csv_path = '/home/luxde/milcah/YouTube-Project/youtube_alex_data_transformed.csv'
df.to_csv(output_csv_path, index=False)

print("✅ Transformation complete using Python and Pandas!")
