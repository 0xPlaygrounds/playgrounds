import dash
import dash_bootstrap_components as dbc

from components.disclaimer import gen_long_disclaimer

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container([
    gen_long_disclaimer()
])
