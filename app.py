import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Energy Operations KPI Dashboard",
    layout="wide"
)

st.title("Energy Operations KPI Dashboard")

st.write(
    "Dashboard for monitoring facility equipment, inspection results, "
    "maintenance costs, and operational follow-up needs."
)

# Load data
df = pd.read_csv("energy_operations_data.csv")

df.columns = df.columns.str.strip().str.replace(" ", "")

# Clean / prepare columns
df["InspectionDate"] = pd.to_datetime(df["InspectionDate"])
df["MaintenanceDate"] = pd.to_datetime(df["MaintenanceDate"])
df["MaintenanceCost"] = pd.to_numeric(df["MaintenanceCost"])

# Sidebar filters
st.sidebar.header("Filters")

facility_options = ["All"] + sorted(df["FacilityName"].unique())
selected_facility = st.sidebar.selectbox("Facility", facility_options)

equipment_options = ["All"] + sorted(df["EquipmentType"].unique())
selected_equipment_type = st.sidebar.selectbox("Equipment Type", equipment_options)

filtered_df = df.copy()

if selected_facility != "All":
    filtered_df = filtered_df[filtered_df["FacilityName"] == selected_facility]

if selected_equipment_type != "All":
    filtered_df = filtered_df[filtered_df["EquipmentType"] == selected_equipment_type]

# KPI metrics
total_maintenance_cost = filtered_df["MaintenanceCost"].sum()
total_inspections = len(filtered_df)
failed_inspections = (filtered_df["InspectionResult"] == "F").sum()
failure_rate = failed_inspections / total_inspections if total_inspections > 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Maintenance Cost", f"${total_maintenance_cost:,.2f}")
col2.metric("Total Inspections", total_inspections)
col3.metric("Failed Inspections", failed_inspections)
col4.metric("Failure Rate", f"{failure_rate:.1%}")

st.divider()

# Maintenance cost by facility
st.subheader("Maintenance Cost by Facility")

cost_by_facility = (
    filtered_df.groupby("FacilityName")["MaintenanceCost"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(cost_by_facility)

# Inspection results
st.subheader("Inspection Results")

inspection_results = filtered_df["InspectionResult"].value_counts()
st.bar_chart(inspection_results)

# Equipment needing follow-up
st.subheader("Equipment Needing Follow-Up")

follow_up_df = filtered_df[
    (filtered_df["InspectionResult"] == "F") |
    (filtered_df["MaintenanceStatus"].isin(["In Progress", "Scheduled"]))
]

st.dataframe(
    follow_up_df[
        [
            "FacilityName",
            "EquipmentName",
            "EquipmentType",
            "InspectionDate",
            "InspectionResult",
            "MaintenanceDescription",
            "MaintenanceCost",
            "MaintenanceStatus"
        ]
    ],
    use_container_width=True
)

# Maintenance cost by equipment
st.subheader("Maintenance Cost by Equipment")

cost_by_equipment = (
    filtered_df.groupby("EquipmentName")["MaintenanceCost"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(cost_by_equipment)

# Raw data
st.subheader("Raw Data")

st.dataframe(filtered_df, use_container_width=True)