class FilaDeProcessos:
    def __init__(self):
        self.fila = []
        
    
    def queue(self, processo):
        self.fila.append(processo)
        
    
    def dequeue(self):
        return self.fila.pop(0)
    
    
    def next(self):
        return self.fila[0]
    
    
    def findByProtocolo(self, protocolo):
        stringRetorno = ""
        
        if not self.fila:
            stringRetorno = "Fila está vazia."
        else:
            posicao = 0
            for processo in self.fila:
                posicao += 1
                if processo.protocolo == protocolo:
                    stringRetorno = f"{posicao}° - Protocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
            
            if not stringRetorno:
                stringRetorno = "Processo não encontrado."

        return stringRetorno
    
    
    def toString(self):
        stringRetorno = "Processo(s) na fila:\n"
        
        if self.fila:
            posicao = 0
            for processo in self.fila:
                posicao += 1
                stringRetorno += f"{posicao}° - Protocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
        else:
            stringRetorno = "Fila está vazia."
        
        return stringRetorno