import dash_bootstrap_components as dbc
from dash import State, html
from dash.dependencies import Input, Output

from app import app
from utils import load_config

config = load_config()
protocol = config['protocol']


def gen_navbar():
    menu_bar = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Staking Simulator",
                                 href="/apps/playgroundSimulation_KlimaGrowthOverTime"),
            dbc.DropdownMenuItem("Bonding Simulator",
                                 href="/apps/playgroundsSimulation_KlimaBonding"),
            dbc.DropdownMenuItem("Learning Hub",
                                 href="/apps/quizzes_experimental"),
            dbc.DropdownMenuItem(f"{protocol}DAO", href=f"{config['website']}"),
            dbc.DropdownMenuItem("Learn More", href=f"{config['docs']}"),
            dbc.DropdownMenuItem("Feedback",
                                 href="https://forms.gle/UTyj7HvCfBNa1rt17"),
            dbc.DropdownMenuItem("Disclaimer",
                                 href="/disclaimer"),
        ],
        nav=True,
        in_navbar=True,
        label="Menu",
        toggle_style={"color": config['nav_menu_color']},
        align_end=True,
        style={"text-align": "right"},
        className="navbar_link_topic",
    )

    navbar = dbc.Navbar(
        dbc.Container([
                dbc.Row([
                    dbc.Col(html.Img(
                        src=app.get_asset_url(config['logo_asset']),
                        height="85px"
                    )),
                ],
                    align="center",
                    className="g-0",
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(menu_bar, className='ms-auto', navbar=True),
                    id="navbar_collapse",
                    is_open=False,
                    navbar=True
                ),
        ], fluid=True),
        color="dark",
        dark=True,
    )

    return navbar


@app.callback(
    Output("navbar_collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar_collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
