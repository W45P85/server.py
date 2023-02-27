# https://docs.python.org/3/howto/sockets.html
# https://realpython.com/python-sockets/
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries
# !! Dieser Server sendet auf jede GET-Request ausschließlich "Hello World" zurück.


from socket import *

def createServer():
'''Startet den Server und wartet auf Verbindungen.'''
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        # Öffnet einen Socket als Endpunkt im 'localhost'. Port 9000.
        serversocket.bind(('localhost',9000))
        # hält den Port offen für Anfragen und stellt sicher, dass kein zweiter Webserver getartet werden kann.
        # 5  Anfragen kann der Webserver nach einander verarbeiten.
        serversocket.listen(5)
        while(1):
        '''Nachdem serversocket.accept() das Client-Socket-Objekt (clientsocket) übergeben hat, 
           werden mit der while-Schleife die blockierenden Calls von clientsocket.recv() durchlaufen. 
           Diese liest alle Daten, die der Client sendet, und sendet sie mit clientsocket.sendall() 
           als Echo in UTF-8 codiert zurück.'''
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
