class Encryption:

    def substitution_simple_encode(self, chave, texto):
        
        alfaupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfalower = "abcdefghijklmnopqrstuvwxyz"

        cifra = ""

        tam_text = len(texto)
        
        for i in range(tam_text):

            if texto[i].isdigit():
                # Se for número é simplesmente deixado no texto
                cifra += texto[i]
                continue
            
            for h in range(len(chave)):
                if texto[i] == alfaupper[h] or texto[i] == alfalower[h]:
                    # Percorrendo a chave, encontra a letra equivalente no texto e devolve o 
                    # index da letra na chave 
                    index = h
                    break
            
            if texto[i].isalpha():
                if texto[i].isupper():
                    # Se letra for Maiuscula é adicionada como Maiuscula
                    cifra += chave[index].upper()
                    
                else:
                    cifra += chave[index].lower()
                
            else:
                # Quando é algum carácter especial (pontuação, etc) é adicionado normalmente 
                cifra += texto[i]   

        return cifra

    def substitution_simple_decode(self, chave, texto):
        alfaupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfalower = "abcdefghijklmnopqrstuvwxyz"

        texto_decode = ""

        tam_text = len(texto)
        
        for i in range(tam_text):

            if texto[i].isdigit():
                # Se for número é simplesmente deixado no texto
                texto_decode += texto[i]
                continue
            
            for h in range(len(chave)):
                if texto[i].upper() == chave[h]:
                    # Percorrendo o texto, encontra a letra equivalente na cahve e devolve o 
                    # index da letra na chave 
                    index = h
                    break
            
            if texto[i].isalpha():
                if texto[i].isupper():
                    # Se letra for Maiuscula é adicionada como Maiuscula
                    texto_decode += alfaupper[index]
                    
                else:
                    texto_decode += alfalower[index]
                
            else:
                # Quando é algum carácter especial (pontuação, etc) é adicionado normalmente 
                texto_decode += texto[i]   

        return texto_decode
