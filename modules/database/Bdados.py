import sqlite3
import datetime


def criar():
    #conecta banco de dados
    conexão = sqlite3.connect("brasil.db")
    #Cursores são objetos para enviar e receber comandos do banco de dados.
    cursor = conexão.cursor()
    # comando cursor.execute, envia o comando ao banco de dados
    #cria tabela estado com chave primaria automatica, nome e população
    cursor.execute("""create table estados(
                    id integer primary key autoincrement,
                    nome text,
                    população integer
                    )""")
    #Operação necessaria para modificar o banco de dados
    conexão.commit()
    cursor.close()
    conexão.close()


def inserir():
    #conecta banco de dados
    conexão = sqlite3.connect("brasil.db")
    # Anexar campos por posição,pode ser acessado como um dicionario
    conexão.row_factory = sqlite3.Row
    # comando cursor.execute, envia o comando ao banco de dados
    #Cursores são objetos para enviar e receber comandos do banco de dados.
    cursor = conexão.cursor()
    dados = [["São Paulo",43663672],["Minas Gerais",20593366],["Rio de Janeiro",16369178],["Bahia",15044127],["Rio Grande do Sul",11164050],["Paraná",10997462],["Pernambuco",9208511],["Ceará",8778575],["Pará",7969655],["Maranhão",6794298],["Santa Catarina",6634250],["Goiás",6434052],["Paraíba",3914418],["Espírito Santo",3838363],["Amazonas",3807923],["Rio Grande do Norte",3373960],["Alagoas",3300938],["Piauí",3184165],["Mato Grosso",3182114],["Distrito Federal",2789761],["Mato Grosso do Sul",2587267],["Sergipe",2195662],["Rondônia",1728214],["Tocantins",1478163],["Acre",776463],["Amapá",734995],["Roraima",488072]]
    # cursor.executemany, trabalha com varios valores(dicionario)
    #inseri na tabela estados valores nos campos nome e população.
    cursor.executemany("insert into estados(nome, população) values(?,?)", dados)
    conexão.commit()
    cursor.close()
    conexão.close()

def consulta():
    #conecta banco de dados
    conexão = sqlite3.connect("brasil.db")
    # Acessar como um dicionario
    conexão.row_factory = sqlite3.Row
    #Imprimir cabeçalho
    print("%3s %-20s %12s" % ("Id","Estado","População"))
    print("="*37)
    # Imprimir dados
    # Secionar dados da tabela estado ordenados por id, em ordem crescente
    # caso fosse decrescente seria("select * from estados order by id desc")
    for estado in conexão.execute("select * from estados order by id"):
        print("%3d %-20s %12d" %
            (estado["id"],
            estado["nome"],
            estado["população"]))
    conexão.close()

def alterar():
    #garante que seja aberto e fechado
    with sqlite3.connect("brasil.db") as conexão:
        conexão.execute("""alter table estados
                        add sigla text""")
        conexão.execute("""alter table estados
                        add região text""")

def inserirAlterados():
    dados = [["SP", "SE", "São Paulo"], ["MG", "SE", "Minas Gerais"], ["RJ", "SE", "Rio de Janeiro"], ["BA", "NE", "Bahia"], ["RS", "S", "Rio Grande do Sul"], ["PR", "S", "Paraná"], ["PE", "NE", "Pernambuco"], ["CE", "NE", "Ceará"], ["PA", "N", "Pará"], ["MA", "NE", "Maranhão"], ["SC", "S", "Santa Catarina"], ["GO", "CO", "Goiás"], ["PB", "NE", "Paraíba"], ["ES", "SE", "Espírito Santo"], ["AM", "N", "Amazonas"], ["RN", "NE", "Rio Grande do Norte"], ["AL", "NE", "Alagoas"], ["PI", "NE", "Piauí"], ["MT", "CO", "Mato Grosso"], ["DF", "CO", "Distrito Federal"], ["MS", "CO", "Mato Grosso do Sul"], ["SE", "NE", "Sergipe"], ["RO", "N", "Rondônia"], ["TO", "N", "Tocantins"], ["AC", "N", "Acre"], ["AP", "N", "Amapá"], ["RR", "N", "Roraima"] ]
    #garante que seja aberto e fechado
    with sqlite3.connect("brasil.db") as conexão:
        conexão.executemany("""update estados
                            set sigla = ?,
                            região = ?
                            where nome = ?""", dados)



def agrupamento():
    print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
    print("====== =======          ========= ========== ==========  ============")
    with sqlite3.connect("brasil.db") as conexão:
        #Quantos registros agrupados por região  que fazem parte do grupo
        for região in conexão.execute("""
            select região, count(*), min(população), max(população), avg(população), sum(população)
            from estados
            group by região
            order by sum(população)
            """):
            print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))

def agregacao():
    print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
    print("====== =======          ========= ========== ==========  ============")
    with sqlite3.connect("brasil.db") as conexão:
        print ("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
            *conexão.execute("select count(*), min(população), max(população), avg(população), sum(população) from estados").fetchone()))
    # fetchone()retorna um registro como uma tupla se existir




def having():                               
    print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
    print("====== =======          ========= ========== ==========  ============")
    with sqlite3.connect("brasil.db") as conexão:
    # select, seleciona todas, população minima, maxima, media e total(soma)
    # as, evita a repetição da função, facilitando a consulta
    # having, filtra os resultados apos o agrupamento(que tem mais de 5 estados).
    # having é diferente do where que é executado antes do agrupamento.
    # group by, Agrupamento
        for região in conexão.execute("""
            select região, count(*), min(população),
                max(população), avg(população), sum(população) as tpop
            from estados
            group by região
            having count(*)>5
            order by tpop desc"""):
            print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))

def criaTabelaData():
    feriados = [["2014-01-01", "Confraternização Universal"], ["2014-04-21", "Tiradentes"], ["2014-05-01", "Dia do trabalhador"], ["2014-09-07", "Independência"], ["2014-10-12", "Padroeira do Brasil"], ["2014-11-02", "Finados"], ["2014-11-15", "Proclamação da República"], ["2014-12-25", "Natal"] ]
    with sqlite3.connect("brasil.db") as conexão:
        # O formato de data é ANO-MÊS-DIA, ISO 8601
        conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
        conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)

def consultaTabelaDataString():
    with sqlite3.connect("brasil.db") as conexão:
        for feriado in conexão.execute("select * from feriados"):
            #retorna em string
            print(feriado)

def consultaTabelaData():
    with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
        conexão.row_factory = sqlite3.Row
        for feriado in conexão.execute("select * from feriados"):
            print("{0} {1}".format(feriado["data"].strftime("%d/%m/%Y"), feriado["descrição"]))



