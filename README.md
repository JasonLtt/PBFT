# PBFT
The Network Manager communicates with the Server using a string-based command protocol.
The list of commands and their corresponding syntaxes are provided below:
  1. 'create:[# of non-Byzantine nodes]:[# of Byzantine nodes]' : Adds the specified number of new nodes to the network.
  2. 'make_b:[# of non-Byzantine nodes to turn Byzantine]' : Turns the specified number of non-Byzantine nodes into Byzantine nodes.  If the number specified is greater than the number of available non-Byzantine nodes, the server simply turns all available non-Byzantine nodes into Byzantine nodes.
  3. 'make_nb:[# of Byzantine nodes to turn non-Byzantine]' : Turns the specified number of Byzantine nodes into non-Byzantine nodes.  If the number specified is greater than the number of available Byzantine nodes, the server simply turns all available Byzantine nodes into non-Byzantine nodes.
  4. 'delete:[# of non-Byzantine nodes]:[# of Byzantine nodes]' : Deletes the specified number of nodes from the network.  If the number specified for either non-Byzantine or Byzantine nodes is greater than the number of nodes of that type that actually exist, the server deletes all of the nodes of that type.
  5. 'compute:[add|subtract]:[number to use in calculation (in conjunction with existing distributed-state value)]' : Sends a value to be used to update the distributed-state value of the distributed ledger.  The provided number will either be added to or subtracted from the distributed state value, depending on which operation is specified.
  6. 'info' : Returns all relevant information pertaining to the network.
  7. 'help' : Display the list of commands and their corresponding syntaxes.
  8. 'exit' : Closes the Network Manager console; the server and the corresponding client nodes remain active.

As a simplification unique to this design, the Server will always serve as the view primary.  While this isn't necessary, the case of having Byzantine leaders would simply result in a timeout after the network fails to arrive at a consensus.  
The Client nodes also communicate with the Server using a string-based command protocol.
The list of commands and their corresponding syntaxes are provided below:
  1.
