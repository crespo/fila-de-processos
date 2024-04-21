class Atendimento:
    def __init__(self):
        self.atendimento = []
    
    
    def add(self, processo):
        self.atendimento.append(processo)
        
    
    def toString(self):
        stringRetorno = "Processos atendidos:\n"
        
        if self.atendimento:
            for processo in self.atendimento:
                stringRetorno += f"Protocolo: {processo.protocolo}\nNome Interessado(a): {processo.nomeInteressado}\nAssunto: {processo.assunto}\n"
        else:
            stringRetorno = "Nenhum processo foi atendido."
            
        return stringRetorno