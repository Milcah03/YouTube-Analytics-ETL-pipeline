📊 **YouTube Analytics ETL using Airflow & Python**

This project automates the extraction, transformation, and loading (ETL) of YouTube channel data using Python and Apache Airflow. It fetches video stats from Alex The Analyst's channel and stores them in a database.

🛠️ **Tech Stack**

- Python  
- YouTube Data API v3  
- Apache Airflow (workflow orchestration)  
- pandas (data processing)  
- PostgreSQL (data storage)  
- dotenv (env management)

📁 **Project Structure**

├── youtube_extract.py              # Extracts video data from YouTube  
├── youtube_transform.py            # Transforms the data  
├── youtube_load.py                 # Saves data to PostgreSQL  
├── dags/youtube_etl_dag.py         # Airflow DAG definition  
├── .env                            # Environment variables  
├── alex_videos.csv                 # Raw extracted data  
├── youtube_alex_data_transformed.csv  # Cleaned/transformed data  
├── README.md                       # Project documentation  

🔁**How It Works**

1. **Extract**  
   Uses YouTube API to fetch video metadata from a channel playlist.

2. **Transform**  
   Processes timestamps, cleans, and structures data.

3. **Load**  
   Saves the cleaned dataset to a database.

✅ **Use Cases**

- YouTube performance analytics  
- Content strategy reporting  
- Automated creator dashboards

📖 **Article** 
Step-by-step write-up coming soon on
