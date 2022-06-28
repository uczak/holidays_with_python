import argparse
import os
import threading
from sys import argv

from services import app

helpmessage = '\nPor padrao, o aplicativo iniciara em modo de Debug\
 no endereco http://localhost:10000.\n\
Para alterar o modo debug ou a porta,\
 sao utilizados os seguintes parametros:\n\n\
[--port | -p] <inteiro> para definir a porta utilizada.\n\
[--nodebug | -nd] para desativar o modo debug\n\n\
Exemplo, para rodar a aplicacao na porta 12000 sem debug:\npython ' +\
    argv[0] + ' -p 12000 -nd'


if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host='0.0.0.0', port=port)
    '''
    if len(argv) == 1:
        print(helpmessage)

    elif "-h" in argv or "--help" in argv:
        print(helpmessage)
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--port", "-p",
            help="Seleciona a porta tcp para rodar a aplicação")
        parser.add_argument(
            "--nodebug", "-nd",
            help="desativa o modo debug", action="store_true")

        args = parser.parse_args()
        port = int(args.port) if args.port is not None else 10000
        debug = not args.nodebug

        app.run(debug=debug, host='0.0.0.0', port=port)
        '''
