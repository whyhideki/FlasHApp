import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def get_data(symbol):
	import pandas as pd
	df = pd.read_csv(f'../data/stocks/{symbol}.csv')
	return df

def create_candlestick_figure(df):
	return go.Figure(
				data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

df_mcd = get_data('MCD')
df_aapl = get_data('AAPL')
candlestick_graph_mcd = create_candlestick_figure(df_mcd)
candlestick_graph_aapl = create_candlestick_figure(df_aapl)

# candlestick_graph_aapl.update_layout({'paper_bgcolor':'black', 'font': {'color':'white'}})
# candlestick_graph_mcd.update_layout({'paper_bgcolor':'black', 'font': {'color':'white'}})

app = dash.Dash()

eufraten_logo = 'https://static.wixstatic.com/media/f96233_044e8c5f3e7b4e588ba5785fbccc0426~mv2.png/v1/fill/w_467,h_163,al_c,q_85,usm_0.66_1.00_0.01/LOGO%20EUFRATEN_VF-horizontal.webp'

app.layout = html.Div(
    children=[
    	html.Div(
    		children = [
    			html.Div( html.Img(src=eufraten_logo), style={'width': '49%','display': 'inline-block'} ),
    			html.Div( html.Span(
			    				children=[
					    			"By:", 
					    			html.Br(),
					    			html.Ul(children=[
									        html.Li(html.B("Vitor Hideki Washiya")),
									        html.Li(html.B("Felipe Francisco Vilela"))
									        ], style = {'display': 'inline-block'}
								        ),
					    			html.Br(),
					    			html.I("Desafio Unisoma")
					    			]
					    		), style={'width': '49%','display': 'inline-block', 'textAlign':'left'} )
    			], style={'background-color': 'powderblue'}
    		),
    	html.H1('MCD Weekly Prices'),
    	html.Div(dcc.Graph(id='candlestick_graph_mcd', figure=candlestick_graph_mcd)),
    	html.H1('AAPL Weekly Prices'),
    	html.Div(dcc.Graph(id='candlestick_graph_aapl', figure=candlestick_graph_aapl)),
    	],
    	style={'border': '5px solid powderblue', 'textAlign': 'center'}
    )

if __name__ == '__main__':
	app.run_server(debug=True)