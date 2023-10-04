jv1 = 0
jv2 = 0
while jv1 or jv2 < 2:
    j1= str(input("jogador 1 qual sua jogada?(pedra, papel ou tesoura): " ))
    j2= str(input("jogador 2 qual sua jogada?(pedra, papel ou tesoura): "))
    if j1 == 'pedra':
        if j2 == 'papel':
            print("jogador 2 venceu")
            jv2 += 1
        if j2 == 'tesoura':
            print("jogador 1 venceu")
            jv1 += 1
        if j2 == 'pedra':
            print("empate joguem novamente")
    if j1 == 'papel':
        if j2 == 'papel':
            print("empate joguem novamente")
        if j2 == 'tesoura':
            print("jogador 2 venceu")
            jv2 += 1
            if j2 == 'pedra':
                print("jogador 1 venceu")
            jv1 += 1
    if j1 == 'tesoura':
        if j2 == 'papel':
            print("jogador 1 venceu")
            jv1 += 1
        if j2 == 'tesoura':
            print("empate joguem novamente")
        if j2 == 'pedra':
            print("jogador 2 venceu")
            jv2 += 1
