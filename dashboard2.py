import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import random

# Inicializar la app Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Datos ficticios avanzados
categories = ["Electrónica", "Ropa", "Alimentos", "Muebles", "Juguetes", "Deportes"]
sales_data = [random.randint(5000, 30000) for _ in categories]
growth_rate = [random.uniform(0.05, 0.3) for _ in categories]
avg_ticket_size = [random.randint(50, 500) for _ in categories]
customer_satisfaction = [random.randint(60, 100) for _ in categories]

# DataFrame de ventas
df_sales = pd.DataFrame({
    "Categoría": categories,
    "Ventas": sales_data,
    "Crecimiento": growth_rate,
    "Ticket Promedio": avg_ticket_size,
    "Satisfacción Cliente": customer_satisfaction
})

# Gráficos avanzados
fig_sales_pie = px.pie(df_sales, names="Categoría", values="Ventas", title="Distribución de Ventas por Categoría", template="plotly_dark")
fig_growth = px.bar(df_sales, x="Categoría", y="Crecimiento", title="Tasa de Crecimiento por Categoría", text_auto=True, template="plotly_dark", color="Crecimiento")
fig_ticket_size = px.scatter(df_sales, x="Categoría", y="Ticket Promedio", size="Ventas", color="Categoría", title="Ticket Promedio vs Ventas", template="plotly_dark")
fig_satisfaction = px.line(df_sales, x="Categoría", y="Satisfacción Cliente", markers=True, title="Satisfacción del Cliente por Categoría", template="plotly_dark")

# Diseño elegante y funcional
app.layout = dbc.Container([
    html.H1("Dashboard de Desempeño", className='text-center mt-4 mb-4 text-white'),
    
    # Tarjetas de métricas con estilo refinado
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Ventas Totales", className='card-title text-center text-white'),
                html.H2(f"${sum(sales_data):,}", className='text-center text-white')
            ])
        ], color='primary', inverse=True, className='shadow-lg'), width=6),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Promedio de Satisfacción", className='card-title text-center text-white'),
                html.H2(f"{sum(customer_satisfaction)/len(customer_satisfaction):.1f} %", className='text-center text-white')
            ])
        ], color='success', inverse=True, className='shadow-lg'), width=6)
    ], className='mb-4'),
    
    # Gráficos con disposición profesional
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_sales_pie, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6),
        dbc.Col(dcc.Graph(figure=fig_growth, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_ticket_size, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6),
        dbc.Col(dcc.Graph(figure=fig_satisfaction, className='shadow-lg p-3 mb-5 bg-dark rounded'), width=6)
    ])
], fluid=True, className='bg-dark text-white p-4')

# Ejecutar la app
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
