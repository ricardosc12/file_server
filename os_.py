import os
import base64

def getFiles(dir = ''):
    try:
        files = os.listdir(dir)
        return {
            'status':True,
            'dados':list(map(lambda x: x, files)),
            'mensagem':'Listado com sucesso !'
        }
    except NotADirectoryError:
        return {'status':False,'mensagem':'Não é um diretório !'}
    except FileNotFoundError:
        return {'status':False,'mensagem':'Não é um arquivo !'}
    except PermissionError:
        return {'status':False,'mensagem':'Sem permissão de acesso !'}

def getFile_(file):
    try:
        file = open(file,'rb')
        binary = file.read()
        base64_ = base64.b64encode(binary).decode('utf-8')
        return {'status':True,'dados':{
            'content':base64_,
        }}
    except FileNotFoundError:
        return {'status':False,'mensagem':'Não é um arquivo !'}
    except PermissionError:
        return {'status':False,'mensagem':'Sem permissão de acesso !'}
    except:
        return {'status':False,'mensagem':'Erro inesperado !'}



def getConfig(IP,PORT):
    try:
        page = open('./config.txt','r')
        file = page.readlines()
        str_ = ''
        public = False
        port = PORT
        for line in file:
            try:
                line = line.replace('\n','')
                if(line[0]=="#" or line[0] == ''): continue
                values = line.split('=')
                config = values[0]
                value = "=".join(values[1:])
                if(config=='HOST' and 'local' in value): 
                    value = value.replace('local',IP)
                if(config=="PUBLIC"):
                    public=True if value=='true' else False
                    continue
                if(config=="PORT"):
                    port = value
                    continue
                str_ = str_+"let {} = '{}'\n".format(config,value)
            except:
                continue
        return public,str_,port
    except:
        return public,"let HOST='127.0.0.1:789'\nlet PATH='./temp'",port
