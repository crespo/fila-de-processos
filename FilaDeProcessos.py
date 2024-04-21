class FilaDeProcessos:
    def __init__(self):
        self.filaDeProcessos = []
        
    
    def queue(self, processo):
        self.filaDeProcessos.append(processo)
        
    
    def dequeue(self):
        if self.filaDeProcessos:
            return self.filaDeProcessos.pop(0)
        
        return "Fila está vazia.\n"
    
    
    def next(self):
        if self.filaDeProcessos:
            processo = self.filaDeProcessos[0]
            return f"Protocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
        
        return "Fila está vazia.\n"
    
    
    def findByProtocolo(self, protocolo):
        stringRetorno = ""
        
        if not self.filaDeProcessos:
            stringRetorno = "Fila está vazia.\n"
        else:
            posicao = 0
            for processo in self.filaDeProcessos:
                posicao += 1
                if processo.protocolo == protocolo:
                    stringRetorno = f"Posição na fila: {posicao}°\nProtocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
            
            if not stringRetorno:
                stringRetorno = "Processo não encontrado.\n"

        return stringRetorno
    
    
    def protocoloIsValid(self, protocolo):
        if self.filaDeProcessos:
            for processo in self.filaDeProcessos:
                if processo.protocolo == protocolo:
                    return False
        
        return True
    
    
    def toString(self):
        stringRetorno = "Processo(s) na fila:\n"
        
        if self.filaDeProcessos:
            posicao = 0
            for processo in self.filaDeProcessos:
                posicao += 1
                stringRetorno += f"{posicao}° - Protocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
        else:
            stringRetorno = "Fila está vazia.\n"
        
        return stringRetorno