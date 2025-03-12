primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))
if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento:
    print('Os segmentos digitados podem formar um triângulo: ', end='')
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print('Equilátero')
    elif primeiro_segmento != segundo_segmento != terceiro_segmento != primeiro_segmento:
        print('Escaléno')
    else:
        print('Isóceles')
else:
    print('Os segmentos digitados não podem formar um triângulo!')