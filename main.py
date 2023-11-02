import pandas as pd
import plotly.express as px

#
_ages = [62, 63, 64, 65, 66, 67, 68, 69, 70]
per_month = [2178, 2319, 2474, 2680, 2887, 3093, 3340, 3588, 3835]

# create a dictionary of age and per_month
SS_AMOUNT = dict(zip(_ages, per_month))
#
#
def annual_income(age: int) -> int:
    return SS_AMOUNT.get(age) * 12


# Define the range of ages you want to compare
ages = [62, 64, 66, 68, 70]

# Define the range of years (normalized) from 1 to 30
years_range = list(range(1, 31))


data = pd.DataFrame()
for age in ages:
    cumulative_incomes = [
        annual_income(age) * (years - (age - 61)) for years in years_range
    ]
    data[f"Age {age}"] = cumulative_incomes

data["Years"] = [years + 61 for years in years_range]  # Adjust x-axis labels

# Create the interactive graph using Plotly
fig = px.line(
    data,
    x="Years",
    title="Cumulative Income vs. Number of Years for Different Starting Ages",
)

# Add lines for each age
for age in ages:
    fig.add_scatter(x=data["Years"], y=data[f"Age {age}"], name=f"Age {age}")
fig.update_yaxes(tickformat=",d")  # Format y-axis ticks as "100,000"
# Show the graph
# Set the y-axis range to start at 0
fig.update_layout(
    # xaxis_title="Number of Years",
    xaxis_title="Age",
    yaxis_title="Cumulative Income",
    showlegend=True,
    yaxis_range=[0, max(data.max()) * 1.1],
    hovermode="x",
)
fig.show()
