# O módulo models contém a classe da aplicação que fará
# a interface com as demais camadas da arquiterura da
# api. A classe pode ser editada conforme a necessidade
# da aplicação.

class Application(object):
    def __init__(self):
        pass

    def check(self, param):
        print("The App return ", param)
        return param

    def clear(self, param):
        return "App delete register " + str(param) 


    def __del__(self):
        print("Close App.")
