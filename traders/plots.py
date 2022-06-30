from __future__ import annotations

import plotly.express as px


def plot_example() -> None:
    df = px.data.stocks()
    fig = px.line(df, x='date', y='GOOG')
    fig.show()
