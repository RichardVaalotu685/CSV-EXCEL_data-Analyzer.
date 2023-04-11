<h1>About:</h1>

This is a Streamlit app that allows users to upload an Excel or CSV file, select columns to merge, and filter data based on user-specified criteria. The app then displays the filtered data in a table.
The app first sets up a sidebar with a title and a file uploader. The user can upload an Excel or CSV file by selecting the appropriate file type from a dropdown menu. The uploaded file is then loaded into a Pandas DataFrame.
Next, the user can select columns to merge using a multiselect widget, and specify a name for the merged column using a text input widget. The app merges the selected columns and adds the merged column to the DataFrame.
The user can then filter the data by specifying text input filters for each column in the DataFrame. The app checks the data type of each column and applies the appropriate filtering method (string contains for object columns, and equality for numeric columns).

<h1>Requirements:</h1>

- Python 3.6 or later
- Pandas
- Plotly
- Streamlit

<h1>Install the required packages using pip:</h1>

<code>pip install pandas plotly streamlit</code>

My code is well-organized and easy to understand each line so that you know what each line of code represents.

Thank you<br>
Richard Vaalotu
