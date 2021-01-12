class Encryption:

    def substitution_simple(self, chave, texto):
        
        alfaupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfalower = "abcdefghijklmnopqrstuvwxyz"

        cifra = ""
        
        for i in range(26):

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
                    cifra += chave[index].toupper()
                    
                else:
                    cifra += chave[index].tolower()
                
            else:
                # Quando é algum carácter especial (pontuação, etc) é adicionado normalmente 
                cifra += texto[i]   

        return cifra

