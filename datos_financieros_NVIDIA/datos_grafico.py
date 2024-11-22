import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

ticker = 'NVDA'
inicio = '2016-01-01'
fin = '2024-04-30'

df = yf.download(ticker, start=inicio, end=fin)
df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d')

# crear el grafico
fig = go.Figure()

# agregar la serie temporal de precios de cierre 
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', line=dict(color='#76B900'))) # color del logo de nvidia

# establecer el diseño del grafico
fig.update_layout(title='Precio de las acciones de NVIDIA',
                title_font_size=20,  # tamaño del titulo
                title_x=0.5, # centrar el titulo
                xaxis_title='Fecha',
                yaxis_title='Precio de cierre (USD)',
                template='plotly_dark')  

# añadir el logo de NVIDIA en la parte superior izquierda 
fig.add_layout_image(
    dict(
        source="https://logodownload.org/wp-content/uploads/2014/09/nvidia-logo-0.png",
        xref="paper", yref="paper",
        x=0.05, y=0.95,
        sizex=0.15, sizey=0.15,
        xanchor="left", yanchor="top"
    )
)

# mostrar el grafico
fig.show()