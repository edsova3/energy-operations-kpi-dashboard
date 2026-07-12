Fix README formatting

# Energy Operations KPI Dashboard

## Project Overview

This project is an interactive Streamlit dashboard designed to monitor facility-level operations, equipment maintenance, inspection results, and operational follow-up needs in a regional energy operations environment.

The dashboard uses sample operational data to summarize maintenance costs, inspection outcomes, equipment issues, and facility-level performance.

## Business Problem

Energy and infrastructure operations teams need a quick way to identify:

- Which facilities have the highest maintenance costs
- Which equipment has failed inspection
- Which assets may need follow-up
- How inspection results vary across facilities and equipment types
- Where operational attention may be needed

This dashboard provides a simple KPI view to support operational monitoring and decision-making.

## Dashboard Features

The dashboard includes:

- Total maintenance cost
- Total inspection count
- Failed inspection count
- Failure rate
- Maintenance cost by facility
- Inspection results summary
- Equipment needing follow-up
- Maintenance cost by equipment
- Filter options by facility and equipment type
- Raw data table for review

## Tools and Skills Used

- Python
- Streamlit
- Pandas
- CSV data processing
- Data visualization
- Dashboard design
- KPI reporting
- Operational analysis
- GitHub

## Files in This Repository

- `app.py` — Streamlit dashboard application
- `energy_operations_data.csv` — dataset used by the dashboard
- `energy_operations_data.xlsx` — editable version of the dataset
- `requirements.txt` — Python package requirements
- `dashboard_preview.png` — screenshot preview of the dashboard

## How to Run This Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Key Business Questions Answered

1. What is the total maintenance cost?
2. How many inspections were completed?
3. How many inspections failed?
4. What is the failure rate?
5. Which facility has the highest maintenance cost?
6. Which equipment needs follow-up?
7. How do maintenance costs vary by equipment?
8. How do inspection results vary across the dataset?
