from tabulate import tabulate
from API import *
import argparse
from docopt import docopt

usage = """
Usage: 
Spend_App.py --init
Spend_App.py --add <amount> <category> [<message>]
Spend_App.py --show [<category>]
Spend_App.py --delete [<category>]

"""

args = docopt(usage)

if args['--init'] : 
    init()
    print("The table was created successfully")

elif args['--show'] : 
    result , total = show(args['<category>'])
    print(f"Total amounts : {total}")
    print(tabulate(result))


elif args['--add'] : 
    amount = args['<amount>']
    category = args['<category>']
    message = args['<message>']

    add(amount , category , message)

elif args['--delete'] :
    category = args['<category>']

    Delete(category=category)

elif args['--Exit'] :
    Exit()
