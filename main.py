from domain.Input_args import Input_args

try:
    f = open('config.json')
except:
    print('Crie um arquivo \"config.json\" na raiz do projeto!')
    exit()


try:
    args = Input_args(f)
    args.exec()
except Exception as error:
    print(error)
