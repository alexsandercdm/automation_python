import datetime
import shutil
import os
from pathlib import Path

if __name__ == '__main__':

    # Exclusão de arquivos anterioes
    try:
        pesquisa = [ ]
        _path = 'e:/BKP WARELINE'
        dir = os.listdir(_path)
        for file in dir:
            pesquisa.append(file)
        for file1, pesq in zip(dir, pesquisa):
            os.remove(f'{_path}/{file1}')
        print('Aqui foi 1')
    except FileNotFoundError:
        print(FileNotFoundError, 'Não existe registro para exclusão')

    try:
        diretorio = Path('//meu-ip-aqui/warewin/backsql/')
        # arquivo = diretorio / 'Seg_dbaih.sql.gz'

        dir = '//meu-ip-aqui/warewin/backsql/'
        arquivos = os.listdir(dir)
        arqui = [ ]

        for x in arquivos:
            arqui.append(x)

        dadosArquivo = [ ]

        for y in arqui:
            arquivo = diretorio / f'{y}'
            arquivoResultado = arquivo.stat().st_mtime
            time_str = datetime.datetime.fromtimestamp(arquivoResultado).strftime('%d/%m/%Y')
            dadosArquivo.append(time_str)

        datahj = datetime.date.today()
        _datahj = datahj - datahj.replace(day=1)
        dataFinal = f'0{_datahj.days}/{datahj.month}/{datahj.year}'

        print('Aqui foi 2', dataFinal)

    except:
        print('não deu certo')

    try:
        for nome, data in zip(arqui, dadosArquivo):
            if data in dataFinal:
                shutil.copyfile(
                    f'//meu-ip-aqui/warewin/backsql/{nome}',
                    os.path.join(f'{_path}', f'{nome}'))
                print('Finalizado')
        print('Aqui foi 3')

    except FileNotFoundError:
        print(FileNotFoundError)
    print('Final...')