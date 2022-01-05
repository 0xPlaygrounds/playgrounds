from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app

from apps import disclaimer_page
from components.disclaimer import gen_short_disclaimer
from components.navbar import gen_navbar
from utils import load_config

config = load_config()

bg_color = config['background_color']

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "0rem",
    "margin-left": "0rem",
    "padding": "1rem 1rem",
    "background-color": bg_color
}
FOOTER_STYLE = {
    "position": "relative",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "6rem",
    "padding": "1rem 1rem",
    "background-color": bg_color,
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    gen_navbar(),
    content,
    html.Footer(gen_short_disclaimer(),
                className='footer_style')
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    # TODO: refactor this to use a dictionary mapping URLs to classes

    if pathname == '/disclaimer':
        return disclaimer_page.layout
    # elif pathname == '/apps/playgroundSimulation_KlimaGrowthOverTime':
    #     return playgroundSimulation_KlimaGrowthOverTime.layout
    # elif pathname == '/apps/playgroundsSimulation_KlimaBonding':
    #     return playgroundsSimulation_KlimaBonding.layout
    # elif pathname == '/apps/quizzes_experimental':
    #     return quizzes_experimental.layout
    # else:
    #     return playgroundSimulation_KlimaGrowthOverTime.layout


# For Gunicorn to reference
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
