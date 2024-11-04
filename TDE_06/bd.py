import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    #database='TDE6'
)

m = conexao.cursor()

m.execute('create database tde6')


m.execute('create table cliente(nome varchar(50) not null,
          endereco varchar(50),
	      telefone varchar(12), idCliente int(10) primary key AUTO_INCREMENT,lista_livro
	      varchar(100), tipo ENUM('fisica','juridica'))')

m.execute('create table compra(idCompra int(10) AUTO_INCREMENT primary key,
	   dataCompra DATE NOT NULL,
	   idcliente int(10),
	   isbn varchar(50),
	   FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),

	   FOREIGN KEY (isbn) REFERENCES livro(isbn))')


m.execute('create table livro(isbn varchar(50) PRIMARY KEY,
	   nomeAutor VARCHAR(50) NOT NULL,
	   assunto VARCHAR(100),
	   idEditora INT(10),
	   QuantidadeEstoque INT(50),
	   FOREIGN KEY (idEditora) REFERENCES editora(idEditora))')


m.execute('create table editora(idEditora INT(10) AUTO_INCREMENT PRIMARY KEY,
	   nomeEditora VARCHAR(50) NOT NULL,
	   endereco VARCHAR(50),
	   telefone VARCHAR(12),
	   nomeGerente VARCHAR(50))')





'''m.execute('show tables')
for i in m:
    print(i)'''
