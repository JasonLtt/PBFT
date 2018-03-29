class NetworkManager(object):
    """The NetworkManager creates new PBFT nodes based on user input.
    The nodes represent a Distributed State Machine which handles user requests
    to perform specified operations.  At this time, the nodes only support basic
     arithmetic operations; the entirety of the distributed state is a floating
    point value.
    """

    def __init__(self):
        self.nb_nodes=[]
        self.b_nodes=[]

    def run(self):
        running=True
        while running:
            command=input('What command would you like to perform?  ')
            if command=='add':
                try:
                    node_count=int(input('How many new nodes would you like to add?  '))
                    if node_count<=0:
                        print('The number of new nodes was not valid.  Please try '+
                        'again with a positive integer.')
                    try:
                        byz_count=int(input('How many of the '+str(node_count)+
                        ' new nodes would you like to be Byzantine?  '))
                        if byz_count<0 or byz_count>node_count:
                            print('The number of Byzantine nodes must be greater than or equal to zero'
                            +' and less than or equal to the number of new nodes.')
                            continue
                        else:
                            nb_name='nodes'
                            if node_count-byz_count==1:
                                nb_name='node'
                            b_name='nodes'
                            if byz_count==1:
                                b_name='node'
                            print(str(node_count-byz_count)+' new non-Byzantine '+nb_name+' and '+
                            str(byz_count)+' new Byzantine '+b_name+' will be created.')
                    except:
                        print('The value you input for the number of new Byzantine '+
                        'nodes was not valid.  Please try again with a non-negative integer.')
                except:
                    print('The value you input for the number of new nodes was '+
                    'not valid.  Please try again with a non-negative integer.')
            #add new command handling here (e.g. delete, corrupt, compute, etc.)
            elif command=='exit':
                running=False
                print('The program is now exiting...')
            else:
                print('Possible commands are:\n'+
                'add: add new nodes to the network\n'+
                'exit: exit the program\n'+
                'help: display this message\n')

netman=NetworkManager()
netman.run()
