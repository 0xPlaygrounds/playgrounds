import dash_bootstrap_components as dbc
from dash import html

from utils import load_config

config = load_config()

protocol = config['protocol']

SHORT_DISCLAIMER = (
    f"{protocol} Playgrounds is for educational purposes only and is not an individualized "
    f"recommendation. Further {protocol} Playgrounds are an educational tool and should "
    f"not be relied upon as the primary basis for investment, financial, tax-planning, "
    f"or retirement decisions. These metrics are not tailored to the investment objectives "
    f"of a specific user. This educational information neither is, nor should be construed as, "
    f"investment advice, financial guidance or an offer or a solicitation or recommendation "
    f"to buy, sell, or hold any security, or to engage in any specific investment strategy by "
    f"{protocol} Playgrounds. These metrics used herein may change at any time and {protocol} "
    f"Playgrounds will not notify you when such changes are made. You are responsible for "
    f"doing your own diligence at all times."
)

LONG_DISCLAIMER = [
    html.P(
        f"{protocol} Playgrounds is for educational purposes only and is not an individualized recommendation. "
        f"Further, {protocol} Playgrounds is an educational tool and should not be relied upon as the primary basis "
        f"for investment, financial, tax-planning, or retirement decisions. These metrics are not tailored to the "
        f"investment objectives of a specific user. This educational information neither is, nor should be construed "
        f"as, investment advice, financial guidance or an offer or a solicitation or recommendation to buy, sell, "
        f"or hold any security, or to engage in any specific investment strategy by {protocol} Playgrounds. "
        f"These metrics used herein may change at any time and {protocol} Playgrounds will not notify you when "
        f"such changes are made."
    ),
    html.P(
        "You are responsible for doing your own diligence at all times."
    ),
    html.P(
        f"{protocol} Playgrounds does not take into account nor does it provide any tax, legal or investment advice or "
        f"opinion regarding the specific investment objectives or financial situation of any person. "
        f"{protocol} Playgrounds and its developers, related DAO members, agents, advisors, directors, officers, "
        f"contractors and token holders make no representation or warranties, expressed or implied, as to the "
        f"accuracy of such information and {protocol} Playgrounds expressly disclaims any and all liability that "
        f"may be based on such information or errors or omissions thereof. [{protocol} Playgrounds reserves the "
        f"right to amend or replace the information contained herein, in part or entirely, at any time, and "
        f"undertakes no obligation to provide the recipient with access to the amended information or to notify "
        f"the recipient thereof. Any information, representations or statements not contained herein shall not "
        f"be relied upon for any purpose."
    ),
    html.P(
        f"Neither {protocol}DAO nor {protocol} Playgrounds, nor any of its representatives, shall have any liability "
        f"whatsoever, under contract, tort, trust or otherwise, to you or any person resulting from the use of "
        f"the information in {protocol} Playgrounds by you or any of your representatives or for omissions from "
        f"the information in {protocol} Playgrounds."
    ),
    html.P(
        f"Additionally, the {protocol} Playgrounds undertakes no obligation to comment on the expectations of, "
        f"or statements made by, third parties in respect of the information in {protocol} Playgrounds."
    )
]


def gen_short_disclaimer():
    return dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.H6("Disclaimer"),
                    html.P(SHORT_DISCLAIMER)
                ])
            ])
        ])
    ])


def gen_long_disclaimer():
    return dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.H1("Disclaimer"),
                    html.Div(LONG_DISCLAIMER)
                ])
            ])
        ])
    ])
