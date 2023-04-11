import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Data Analyzer", page_icon=":bar_chart:", layout="wide")
#######################################################
###               By Richard Vaalotu               ###
#####################################################
# Set up sidebar

st.sidebar.title("Tool By Greenology")
st.sidebar.title("Upload File")
file = st.sidebar.file_uploader("Choose an Excel file or CSV", type=["xlsx", "csv"])

# Load data
if file is not None:
    if file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        st.error("Invalid file format. Please upload an Excel file or CSV.")
        st.stop()

    # Analyze data
    columns = list(df.columns)
    merge_columns = st.multiselect("Select columns to merge", columns, default=columns[:2])
    merged_column_name = st.text_input("Name for merged column", value="Merged")

    # Merge selected columns
    df[merged_column_name] = df[merge_columns].apply(lambda x: " ".join(x.astype(str)), axis=1)

    # Filter data
    filtered_df = df
    for col in columns:
        if col != merged_column_name:
            col_type = df[col].dtype
            col_filter = st.sidebar.text_input(f"Filter for {col}")
            if col_filter:
                if col_type == "object":
                    filtered_df = filtered_df[filtered_df[col].str.contains(col_filter, case=False)]
                elif col_type == "int64" or col_type == "float64":
                    try:
                        col_filter = float(col_filter)
                        filtered_df = filtered_df[filtered_df[col] == col_filter]
                    except ValueError:
                        st.warning(f"{col} is a numeric column, but the filter value is not a number. Filter ignored.")

    # Display data
    st.write(f"## {len(filtered_df)} rows")
    st.table(filtered_df[merge_columns + [merged_column_name]])