import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape
import pandas as pd
from textwrap import dedent

from reusable_components import Section, Chapter
from tutorial import styles
from tutorial import tools

examples = {
    example: tools.load_example('tutorial/examples/cytoscape/{}'.format(example))
    for example in ['simple.py']
}

layout = html.Div([

    dcc.Markdown(dedent('''
    # Dash Cytoscape
    
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
    > components, as well as established computational biology and network 
    > science libraries such as Biopython and networkX.
    >
    > -- xhlulu
    ''')),

    Section('Quickstart', [
        dcc.SyntaxHighlighter(
            '''pip install dash-cytoscape=={}'''.format(dash_cytoscape.__version__),
            customStyle=styles.code_container
        ),

        dcc.SyntaxHighlighter(
            examples['simple.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(examples['simple.py'][1], className='example-container'),

    ]),

    Section('Dash Cytoscape User Guide', [
        Chapter(
            'Part 1. Elements',
            '/cytoscape/elements',
            '''
            Elements declaration in Cytoscape are designed to be clear, simple,
            and JSON-friendly. This chapter will get you started 
            with examples for:
            - Data and position dictionaries 
            - Mutability properties
            - Defining groups and classes
            - Compound nodes
            '''
        ),

        Chapter(
            'Part 2. Layout',
            '/cytoscape/layout',
            '''
            Make your graphs interpretable by using the built-in 
            collection of easy-to-modify layouts. We show you how to:
            - Display pre-determined and random layouts
            - Represent your graph as a circle, a grid or a tree
            - Finetune your representations by modifying the default options
            - Use physics-based simulations to generate your layout 
            '''
        ),

        Chapter(
            'Part 3. Styling',
            '/cytoscape/styling',
            '''
            Modify the color, shape and style of your elements with a syntax
            similar to CSS. Cytoscape incldues a wide variety of properties,
            equiping you with everything you need to display your graphs with
            aesthetics, creativity, and understandability in mind. This chapter
            covers:
            - Basic style properties for nodes and edges
            - Using selectors to modify specific groups of elements
            - Organize your edges with curve and line properties
            - Advanced node styling with pie charts and images
            '''
        ),

        Chapter(
            'Part 4. Dash Callbacks',
            '/cytoscape/callbacks',
            '''
            Update your layout, elements, or style with other Dash components
            using callbacks. This chapter covers:
            - Adding and removing elements
            - Modifying the layout and the stylesheet
            - Advanced usage of callbacks
            '''
        ),

        Chapter(
            'Part 5. Events Callbacks for User Interactions',
            '/cytoscape/events',
            '''
            Dash Cytoscape fires callbacks whenever the user interact with the
            graph you created, which can be used to update the graph itself,
            or to interact with other components. This chapter includes 
            examples for:
            - Simple integrations with HTML components
            - Different types of data returned
            - Node versus edges callbacks
            = Tap, hover or select callbacks
            '''
        ),

        Chapter(
            'Part 6. Applications',
            '/cytoscape/applications',
            '''
            We show how Dash Cytoscape can be applied for fields as diverse as
            bioinformatics and social networks analysis. Examples include:
            - Displaying Phylogeny Data with Biopython
            - Interactive exploration of large social networks
            '''
        ),


        Chapter(
            'Part 7. Object Reference',
            '/cytoscape/reference',
            '''
            You can find here all the properties of the `Cytoscape` object.
            '''
        )
    ]),

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
