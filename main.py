from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Marcos', '11111111111', 'mcastrosouza@live.com')
	banco.inserir_cliente('Thomas', '22222222222', 'thomas@gmail.com')
	banco.inserir_cliente('João', '3333333', 'joaosouza@live.com')
	banco.inserir_cliente('José', '44444444', 'jose@gmail.com')
	banco.inserir_cliente('Manoel','55555555', 'manoelima@live.com')
	banco.inserir_cliente('Ines', '66666666', 'inespereira@gmail.com')
	banco.inserir_cliente('Henrique', '88888888', 'Henrique@gmail.com')
	banco.buscar_cliente('11111111111')
	banco.remover_cliente('7777777777')
	banco.buscar_email('joseg@gmail.com')
	banco.desconecta()
