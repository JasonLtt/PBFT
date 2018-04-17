import asyncio

nb_clients=[]
b_clients=[]

port_counter=8160

def run_server(reader, writer):
    while True:
        global port_counter
        global loop
        data=yield from reader.read(100)
        message=data.decode()
        print('Received: ',message)
        params=message.split(':')
        command=params[0]
        if command =='create':
            nb_count=int(params[1])
            for x in range(0,nb_count):
                new_coro=asyncio.start_server(run_client,'localhost',port_counter,loop=loop)
                new_server=yield from asyncio.ensure_future(new_coro,loop=loop)
                print('New non-Byzantine Client running at {}'.format(new_server.sockets[0].getsockname()))
                port_counter+=80
                nb_clients.append(new_server)
            b_count=int(params[2])
            for x in range(0,b_count):
                new_coro=asyncio.start_server(run_client,'localhost',port_counter,loop=loop)
                new_server=yield from asyncio.ensure_future(new_coro,loop=loop)
                print('New Byzantine Client running at {}'.format(new_server.sockets[0].getsockname()))
                port_counter+=80
                b_clients.append(new_server)
            response_string='Created '+params[1]+' new non-Byzantine nodes and '+params[2]+' new Byzantine nodes.'
            writer.write(response_string.encode())
            yield from writer.drain()
        elif command =='make_b':
            b_count=int(params[1])
            if b_count>len(nb_clients):
                b_count=len(nb_clients)
            for x in range(0,b_count):
                b_clients.append(nb_clients.pop(0))
            response_string='Made '+str(b_count)+' non-Byzantine clients into Byzantine clients'
            writer.write(response_string.encode())
            yield from writer.drain()
        elif command =='make_nb':
            nb_count=int(params[1])
            if nb_count>len(b_clients):
                nb_count=len(b_clients)
            for x in range(0,nb_count):
                nb_clients.append(b_clients.pop(0))
            response_string='Made '+str(nb_count)+' Byzantine clients into non-Byzantine clients'
            writer.write(response_string.encode())
            yield from writer.drain()
        elif command =='delete':
            nb_count=int(params[1])
            if nb_count>len(nb_clients):
                nb_count=len(nb_clients)
            for x in range(0,nb_count):
                del nb_clients[0]
            b_count=int(params[2])
            if b_count>len(b_clients):
                b_count=len(b_clients)
            print('Adjusted b_count: '+str(b_count))
            for x in range(0,b_count):
                del b_clients[0]
            response_string='Deleted '+str(nb_count)+'  non-Byzantine nodes and '+str(b_count)+'  Byzantine nodes.'
            writer.write(response_string.encode())
            yield from writer.drain()
        elif command =='compute':
            writer.write(command.encode())
            yield from writer.drain()
        elif command =='info':
            response_string='There are currently '+str(len(nb_clients))+' non-Byzantine clients and '+str(len(b_clients))+' Byzantine clients'
            writer.write(response_string.encode())
            yield from writer.drain()


def run_client(reader, writer):
    print('RUNNING CLIENT')
    while True:
        yield from asyncio.sleep(5)
        #print('Client at {} awoke'.format(self.sockets[0].getsockname()))
        print('Client awoke')

loop = asyncio.get_event_loop()
server_coroutine=asyncio.start_server(run_server,'localhost',8080, loop=loop)
server=loop.run_until_complete(server_coroutine)
print('serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    print('Exiting server')
finally:
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
