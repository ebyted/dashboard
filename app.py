import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import random

# Inicializar la app Dash
app = dash.Dash(__name__)

# Datos ficticios
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
sales = [random.randint(10000, 50000) for _ in months]
customers = [random.randint(100, 500) for _ in months]

# DataFrame de ventas
df_sales = pd.DataFrame({"Mes": months, "Ventas": sales, "Clientes": customers})

# Gráficos
fig_sales = px.bar(df_sales, x="Mes", y="Ventas", title="Ventas por Mes", text_auto=True, color="Ventas")
fig_trend = px.line(df_sales, x="Mes", y="Ventas", markers=True, title="Tendencia de Ventas")
fig_pie = px.pie(df_sales, names="Mes", values="Clientes", title="Distribución de Clientes")
fig_scatter = px.scatter(df_sales, x="Clientes", y="Ventas", size="Ventas", color="Mes", title="Relación Clientes vs Ventas")

# Layout de la app
app.layout = html.Div([
    html.H1("Dashboard de Ventas", style={'textAlign': 'center'}),
    
    # Tarjetas de métricas
    html.Div([
        html.Div([
            html.H3("Total de Ventas"),
            html.P(f"${sum(sales):,}")
        ], style={"width": "30%", "display": "inline-block", "textAlign": "center", "padding": "20px", "border": "1px solid black"}),
        
        html.Div([
            html.H3("Total de Clientes"),
            html.P(f"{sum(customers):,}")
        ], style={"width": "30%", "display": "inline-block", "textAlign": "center", "padding": "20px", "border": "1px solid black"})
    ], style={"display": "flex", "justifyContent": "center"}),
    
    # Gráficos
    dcc.Graph(figure=fig_sales),
    dcc.Graph(figure=fig_trend),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_scatter)
])

# Ejecutar la app
if __name__ == "__main__":
    app.run_server(debug=True)
