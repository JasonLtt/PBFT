from asyncio import *
from aioconsole import ainput

help_string=  """\n1. 'create:[# of non-Byzantine nodes]:[# of Byzantine nodes]' : Adds the specified number of new nodes to the network.
2. 'make_b:[# of non-Byzantine nodes to turn Byzantine]' : Turns the specified number of non-Byzantine nodes into Byzantine nodes.  If the number specified is greater than the number of available non-Byzantine nodes, the server simply turns all available non-Byzantine nodes into Byzantine nodes.
3. 'make_nb:[# of Byzantine nodes to turn non-Byzantine]' : Turns the specified number of Byzantine nodes into non-Byzantine nodes.  If the number specified is greater than the number of available Byzantine nodes, the server simply turns all available Byzantine nodes into non-Byzantine nodes.
4. 'delete:[# of non-Byzantine nodes]:[# of Byzantine nodes]' : Deletes the specified number of nodes from the network.  If the number specified for either non-Byzantine or Byzantine nodes is greater than the number of nodes of that type that actually exist, the server deletes all of the nodes of that type.
5. 'compute:[add|subtract]:[number to use in calculation (in conjunction with existing distributed-state value)]' : Sends a value to be used to update the distributed-state value of the distributed ledger.  The provided number will either be added to or subtracted from the distributed state value, depending on which operation is specified.
6. 'info' : Returns all relevant information pertaining to the network.
7. 'help' : Display the list of commands and their corresponding syntaxes.
8. 'exit' : Closes the Network Manager console; the server and the corresponding client nodes remain active."""

async def console_input(host,port,loop):
    reader,writer=await open_connection(host,port,loop=loop)
    while True:
        input = await ainput('Insert Command >')
        params=input.split(':')
        if input=='exit':
            #netman.disconnect()
            break
        elif params[0]=='create' or params[0]=='make_b' or params[0]=='make_nb' or params[0]=='delete' or params[0]=='compute' or params[0]=='info':#ideally this would check parameters
            writer.write(input.encode())
            response=await reader.read(1024)
            print('Response from Server: ',response.decode())
        else:
            print('The list of commands and their corresponding syntaxes are provided below:',help_string)


#host = input('On what host is the server running? ')
host='localhost'
#port_string = input('On what port is the server running? ')
#port=int(port_string)
port=8080


loop = get_event_loop()

try:
    loop.run_until_complete(console_input(host,port,loop))
except:
    pass
finally:
    print('Exiting Network Manager console.')
    loop.close()
