import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# 3. Data Science and Visualization

# Practice Task : 2 | Use plotly to create an interactive dashboard.
# DataFrame
df = pd.read_csv("3. Data Science and Visualization/students.csv")

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Student Performance Dashboard", style={'textAlign': 'center'}),

    # Dropdown to select variable for X-axis
    html.Label("Select X-axis:"),
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': col, 'value': col} for col in ['Study_Hours', 'Sleep_Hours', 'Attendance_Percentage', 'Previous_Score']],
        value='Study_Hours'
    ),

    # Dropdown to select variable for Y-axis
    html.Label("Select Y-axis:"),
    dcc.Dropdown(
        id='y-axis',
        options=[{'label': col, 'value': col} for col in ['Final_Score']],
        value='Final_Score'
    ),

    # Graph output
    dcc.Graph(id='scatter-plot'),

    # Histogram
    html.H2("Final Score Distribution"),
    dcc.Graph(
        figure=px.histogram(df, x="Final_Score", nbins=10, title="Final Score Histogram")
    )
])

# Callback to update scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('x-axis', 'value'),
    Input('y-axis', 'value')
)
def update_graph(x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, color='Gender', hover_data=['Student_Name'])
    fig.update_layout(title=f"{y_col} vs {x_col}")
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
