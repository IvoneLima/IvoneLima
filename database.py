import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados (database) da aplicação"""

	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None

	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		"""Desconecta do banco"""
		try:
			self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		"""Cria as tabelas do banco"""
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					nome TEXT NOT NULL,
					cpf VARCHAR(11) UNIQUE NOT NULL,
					email TEXT NOT NULL
			);
			""")

		except AttributeError:
			print('Faça a conexão do banco antes de criar as tabelas.')

	def __repr__(self):	
    		nome = '<Nome: %s>' % self.nome

	def inserir_cliente(self, nome, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
				""", (nome, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpf %s já existe!' % cpf)

			self.conexao.commit()

		except AttributeError:
			print('Faça a conexão do banco antes de inserir clientes.')

	def buscar_cliente(self, cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()

			# obtém todos os dados
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[2] == cpf:
					print('Cliente %s encontrado.' % linha[1])
					break
		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')

	def remover_cliente(self, cpf):
		"""Remover cliente no banco"""
		try:
			cursor = self.conexao.cursor()
           
			try:
				cursor.execute(""" select count(*) FROM clientes 
				where cpf =?;""",(cpf,)) 
				count_row=cursor.fetchone()
				count = count_row[0]
				
				print(f'qtd=  {count}')
				if count != 0:
					cursor.execute(""" DELETE FROM clientes 
					where cpf =?;""",(cpf,))  
					print('O cpf %s foi removido!' % cpf)
				else:
					print('O cpf %s não encontrado!' % cpf)
    					
			except sqlite3.IntegrityError:
				print('Faça a conexão do banco antes de deletar cliente.')

			finally:
				self.conexao.commit()

		except AttributeError:
			print('Faça a conexão do banco antes de deletar cliente.')

		finally:
			self.conexao.commit()

	def buscar_email(self, email):
		"""Buscar cliente no banco"""
		try:
			cursor = self.conexao.cursor()
           
			try:
				cursor.execute(""" Select count(*) FROM clientes 
				where email =?;""",(email,))  
				res=cursor.fetchone()
				if max(res) > 0:
					print(True)
				else:
    					print(False)
	    		
			except sqlite3.IntegrityError:
				print('Faça a conexão do banco antes de buscar cliente.')

		except AttributeError:
			print('Faça a conexão do banco antes de buscar cliente.')
