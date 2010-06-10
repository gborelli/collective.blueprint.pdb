Overview
========

collective.blueprint.pdb provides a trivial method to debug a transmogrifier chain.

You can include this blueprint in your transmogrifier chain and put some conditional expression to set a simple pdb breakpoint.

USAGE
-----

[transmogrifier]
pipeline =
    source
    ...
    debug_item
    ...

[debug_item]
blueprint = collective.blueprint.pdb
condition = python:item/pippo == 'pippo'
