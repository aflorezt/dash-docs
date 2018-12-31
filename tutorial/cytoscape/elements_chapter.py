import dash_html_components as html

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from textwrap import dedent

import dash_cytoscape
from .utils import html_table, CreateDisplay
from tutorial import tools
from tutorial import styles


# examples = {
#     example: tools.load_example('tutorial/examples/table/{}'.format(example))
#     for example in ['dropdown_per_column.py', 'dropdown_per_row.py']
# }

my_stylesheet = [
    # Group selectors
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)'
        }
    },

    # Class selectors
    {
        'selector': '.red',
        'style': {
            'background-color': 'red',
            'line-color': 'red'
        }
    },
    {
        'selector': '.triangle',
        'style': {
            'shape': 'triangle'
        }
    }
]

Display = CreateDisplay({
    'dash_cytoscape': dash_cytoscape,
    'my_stylesheet': my_stylesheet
})

# - Compound nodes

layout = html.Div([

    dcc.Markdown(dedent('''
    # Elements
    
    ## Element Declaration
    
    Each element is defined by a dictionary declaring its purpose and 
    describing its properties. Usually, you specify what group the 
    element belongs to (i.e. if it's a node or an edge), indicate what 
    position you want to give to your element (if it's a node), or what data 
    it contains. In fact, the `data` and `position` items are themselves 
    dictionaries, where each `item` specify an aspect of the `data` or 
    `position`.
    
    In the case of `data`, the typical keys fed to the dictionaries are:
    - `id`: The index of the element, useful when you want to uniquely interact 
    with it.
    - `label`: The name you give to the element when you display it
    
    If your element is an edge, the following items are required for your data
    dictionary:
    - `source`: The source node id, which is where the edge starts
    - `target`: The target node id, where the edge ends
    
    The position dictionary takes as items the `x` and `y` position of the node. If
    you use any other layout than `preset`, or if the element is an edge, the
    position item will be ignored.
    
    If we want a graph with two nodes, and an edge connecting those two nodes,
    we effectively need three of those element dictionaries, grouped as a list:
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            # The nodes elements
            {'data': {'id': 'one', 'label': 'Node 1'}, 
             'position': {'x': 50, 'y': 50}},
            {'data': {'id': 'two', 'label': 'Node 2'}, 
             'position': {'x': 200, 'y': 200}},
             
            # The edge elements
            {'data': {'source': 'one', 'target': 'two', 'label': 'Node 1 to 2'}}
        ]
    )
    '''),

    dcc.Markdown(dedent('''
    Notice that we also need to specify the `id`, the `layout`, and the `style` 
    of Cytoscape. The `id` parameter is needed for assigning callbacks,
    `style` lets you specify the CSS style of the component (similarly to core
    components), and layout tells you how to arrange your graph. It is 
    described in depth in part 2, so all you need to know is that `'preset'`
    will organize the nodes according to the positions you specified.
    
    The official Cytoscape.js documentation nicely outlines the [JSON format 
    for declaring elements](http://js.cytoscape.org/#notation/elements-json).
    
    ## Boolean Properties
    
    In addition to the properties presented above, the element dictionary can
    also accept boolean items that specify its state. We extend the previous
    example in the following way:
    
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {
                'data': {'id': 'one', 'label': 'Locked'},
                'position': {'x': 75, 'y': 75},
                'locked': True
            },
            {
                'data': {'id': 'two', 'label': 'Selected'},
                'position': {'x': 75, 'y': 200},
                'selected': True
            },
            {
                'data': {'id': 'three', 'label': 'Not Selectable'},
                'position': {'x': 200, 'y': 75},
                'selectable': False
            },
            {
                'data': {'id': 'four', 'label': 'Not grabbable'},
                'position': {'x': 200, 'y': 200},
                'grabbable': False
            },
            {'data': {'source': 'one', 'target': 'two'}},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}},
            {'data': {'source': 'two', 'target': 'four'}},
        ]
    )
    '''),

    dcc.Markdown(dedent('''
    > Note that those boolean properties can be overwritten by certain Cytoscape
    > parameters such as `autoungrabify` or `autounselectify`. Please refer to
    > the reference for more information.
    
    ## Classes
    
    Sometimes, you want to give your elements a specific class in order to 
    distinguish them from others. This is especially useful when you want to 
    perform specific actions using a selector, for example changing the style
    of an element based on its class. We modify the previous example by giving
    the elements a class or multiple classes (separated by a space), and 
    define a stylesheet that modifies the elements based on those classes. 
    ''')),

    Display('''
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        stylesheet=my_stylesheet,
        elements=[
            {
                'data': {'id': 'one', 'label': 'Modified Color'},
                'position': {'x': 75, 'y': 75},
                'classes': 'red' # Single class
            },
            {
                'data': {'id': 'two', 'label': 'Modified Shape'},
                'position': {'x': 75, 'y': 200},
                'classes': 'triangle' # Single class
            },
            {
                'data': {'id': 'three', 'label': 'Both Modified'},
                'position': {'x': 200, 'y': 75},
                'classes': 'red triangle' # Multiple classes
            },
            {
                'data': {'id': 'four', 'label': 'Regular'},
                'position': {'x': 200, 'y': 200}
            },
            {'data': {'source': 'one', 'target': 'two'}, 'classes': 'red'},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}, 'classes': 'red'},
            {'data': {'source': 'two', 'target': 'four'}},
        ]
    )
    '''),

    dcc.Markdown(dedent('''
    The stylesheet parameter will be described in depth in part 3 of this 
    guide. We will show extensive examples of using selectors to style 
    groups, classes, and data value comparisons. Expand below if you still
    want to take a look at the stylesheet used above.
    ''')),

    html.Details(open=False, children=[
        html.Summary('View the Stylesheet'),
        dcc.SyntaxHighlighter(dedent('''
        my_stylesheet = [
            # Group selectors
            {
                'selector': 'node',
                'style': {
                    'content': 'data(label)'
                }
            },
        
            # Class selectors
            {
                'selector': '.red',
                'style': {
                    'background-color': 'red',
                    'line-color': 'red'
                }
            },
            {
                'selector': '.triangle',
                'style': {
                    'shape': 'triangle'
                }
            }
        ]
        '''))
    ]),

    html.Hr(),

    dcc.Markdown(dedent('''
    ## Compound Nodes
    
    '''))

])
