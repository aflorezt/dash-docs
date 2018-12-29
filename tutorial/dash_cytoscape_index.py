import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

from reusable_components import Section, Chapter
from tutorial import styles
from tutorial import tools

layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash DataTable
    
    ''')),

    html.Iframe(
        src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash-cytoscape&type=star&count=true&size=large",
        width="160px",
        height="30px",
        style={'border': 'none'}
    ),

    dcc.Markdown(dedent('''
    > **New! Released on TBD**
    >
    > Dash Cytoscape is a graph visualization component for creating easily
    > customizable, high-performance, interactive, and web-based networks. It
    > extends and renders [Cytoscape.js](http://js.cytoscape.org), and 
    > offers deep integration with Dash layouts and callbacks, enabling the 
    > creation of powerful networks jointly with the rich collection of Dash 
    > components, as well as powerful computational biology and network science
    > libraries such as Biopython and networkX.
    >
    > -- xhlulu
    ''')),

    Section('Roadmap, Sponsorships, and Contact', dcc.Markdown(dedent(
    '''
    Immediately, we're working on stability, virtualization, and
    a first-class data type system.
    Check out [our roadmap project board](https://github.com/orgs/plotly/projects/12)
    to see what's coming next.

    Many thanks to all of our customers who have sponsored the
    development of this table. Interested in steering the roadmap?
    [Get in touch](https://plot.ly/products/consulting-and-oem/)
    '''
    )))

])
