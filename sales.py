import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Load the cleaned and analyzed data
sales_by_country = pd.read_csv('./data/sales_by_country.csv')
max_selling_products = pd.read_csv('./data/max_selling_products.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Create figures
fig_sales_by_country = px.bar(sales_by_country, x='Country', y='Totalsale', title='Total Sales by Country')
fig_max_selling_products = px.bar(max_selling_products.head(10), x='Product', y='Totalsale', title='Top 10 Selling Products')

app.layout = html.Div(children=[
    html.H1(children='Online Retail Sales Dashboard'),

    dcc.Graph(
        id='sales-by-country',
        figure=fig_sales_by_country
    ),
    dcc.Graph(
        id='max-selling-products',
        figure=fig_max_selling_products
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)
