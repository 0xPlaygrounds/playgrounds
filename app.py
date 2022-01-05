import dash
import dash_bootstrap_components as dbc

from utils import load_config

config = load_config()
protocol = config['protocol']

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True,
    title=f"{protocol} Playgrounds",
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
    }]
)
