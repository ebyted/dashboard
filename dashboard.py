import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import random

# Inicializar la app Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Datos ficticios
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
sales = [random.randint(10000, 50000) for _ in months]
customers = [random.randint(100, 500) for _ in months]

# DataFrame de ventas
df_sales = pd.DataFrame({"Mes": months, "Ventas": sales, "Clientes": customers})

# Gráficos con diseño elegante
fig_sales = px.bar(df_sales, x="Mes", y="Ventas", title="Ventas por Mes", text_auto=True, color="Ventas", template="plotly_dark")
fig_trend = px.line(df_sales, x="Mes", y="Ventas", markers=True, title="Tendencia de Ventas", template="plotly_dark")
fig_pie = px.pie(df_sales, names="Mes", values="Clientes", title="Distribución de Clientes", template="plotly_dark")
fig_scatter = px.scatter(df_sales, x="Clientes", y="Ventas", size="Ventas", color="Mes", title="Relación Clientes vs Ventas", template="plotly_dark")

# Layout elegante y funcional
app.layout = dbc.Container([
    html.H1("Dashboard de Ventas", className='text-center mt-4 mb-4 text-white'),
    
    # Tarjetas de métricas con estilo refinado
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total de Ventas", className='card-title text-center'),
                html.H2(f"${sum(sales):,}", className='text-center')
            ])
        ], color='dark', inverse=True, className='shadow-lg'), width=6),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total de Clientes", className='card-title text-center text-white'),
                html.H2(f"{sum(customers):,}", className='text-center text-white')
            ])
        ], color='dark', inverse=True, className='shadow-lg'), width=6)
    ], className='mb-4'),
    
    # Gráficos con disposición elegante
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_sales, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6),
        dbc.Col(dcc.Graph(figure=fig_trend, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_pie, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6),
        dbc.Col(dcc.Graph(figure=fig_scatter, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6)
    ])
], fluid=True, className='bg-dark text-white p-4')

# Ejecutar la app
if __name__ == "__main__":
    app.run_server(debug=False, port=8050)
