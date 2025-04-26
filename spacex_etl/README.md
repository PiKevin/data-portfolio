# SpaceX Launches ETL Pipeline

This project demonstrates a full Extract-Transform-Load (ETL) pipeline using Python and PostgreSQL, focused on data from the SpaceX public API.

---

## What It Does

- **Extracts** launch data from the SpaceX API
- **Transforms** the data to extract key fields
- **Loads** it into a PostgreSQL database

---

## Project Structure
```spacex_etl/ ├── data/ │ ├── raw_launch_data.json # Raw JSON from the SpaceX API │ └── launch_cleaned.csv # Cleaned launch data ├── extract_spacex.py # Pulls data from API ├── transform_spacex.py # Cleans and extracts key fields ├── load_spacex.py # Loads cleaned data into PostgreSQL └── README.md # You're reading it!```

---

## Tech Stack

- **Python** (`requests`, `pandas`, `psycopg2`)
- **PostgreSQL** (local or cloud DB)
- **SpaceX API**: https://github.com/r-spacex/SpaceX-API

---

## How to Run It

1. Clone the repo:
    ```bash
    git clone https://github.com/YOUR_USERNAME/spacex-etl.git
    cd spacex-etl
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

3. Update database settings in `load_spacex.py`

4. Run the pipeline:
    ```bash
    python extract_spacex.py
    python transform_spacex.py
    python load_spacex.py
    ```

---

## Example Output

Run the final SQL query:
```sql
SELECT * FROM launches;
```

##  Why I Built This
I’m pivoting into data engineering, and this project shows my ability to:
- Work with APIs
- Clean and structure real-world JSON
- Automate data pipelines with Python
- Work with SQL databases like PostgreSQL
