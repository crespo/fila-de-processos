class Processo:
    def __init__(self, protocolo, nomeInteressado, assunto):
        if protocolo and nomeInteressado and assunto:
            self.protocolo = protocolo
            self.nomeInteressado = nomeInteressado
            self.assunto = assunto
            return True
        
        return False