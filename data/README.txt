Desafio UniSoma 2021
Estrutura do Banco de Dados Eufraten_NFP

Este banco SQLite, criado pela UniSoma, contém os dados anonimizados fornecidos para modelagem. Contém também as tabelas para salvar os resultados. Um banco com a mesma estrutura, com dados atualizados, será criado para implementação na Fundação. 

Se necessário, os grupos podem criar tabelas para incorporar dados externos (não fornecidos pela Fundação). A criação dessas tabelas bem como de mecanismos para sua atualização são de responsabilidade do grupo.

Outras tabelas e novas colunas podem ser criadas, mas a estrutura pré-definida não pode ser alterada (retirar tabelas ou colunas, alterar tipo de coluna).

O banco tem a seguinte estrutura pré-definida:

notas_historico: 
	pré-populada, deve ser atualizada a cada mês
	colunas
		estabelecimento_id
		dt_emissao: data de emissão da nota fiscal
		dt_registro: data de registro da nota fiscal pelo estabelecimento no sistema
		valor_rs: valor total da nota em Reais
		credito_rs: crédito obtido em Reais

estabelecimentos_informacoes: 
	pré-populada, deve ser atualizada quando necessário
	colunas
		estabelecimento_id
		nome
		endereço
		celular
		email
		tipo: matriz ou filial
		natureza_jurídica: natureza jurídica da estabelecimento
		porte: tamanho do estabelecimento
		ano_abertura: ano de criação do estabelecimento
		uf
		municipio
		bairro
		tem_coleta: se o estabelecimento é visitado regularmente pela Fundação (1 caso seja visitado, 0 caso contrário)
		
estabelecimentos_atividades: 
	pré-populada, deve ser atualizada quando necessário
	colunas
		estabelecimento_id
		cnae: código CNAE com 7 dígitos da empresa
		descricao: descrição do CNAE
		principal: lógico - a CNAE dada é a principal? 

resultados_abt_modelagem: 
	deve ser populada pela aplicação com os dados usados como entrada da modelagem. 
	colunas extras devem ser criadas de acordo com o tratamento e a modelagem feitos
	colunas
		estabelecimento_id
		mes
		ano
		score: score real calculado
		
resultados_abt_previsoes: 
	deve ter a mesma estrutura de resultados_abt_modelagem
	populada com os dados usados para a previsão
	colunas
		estabelecimento_id
		mes
		ano
		score: score previsto
		
resultados_log: 
	logs do progresso da aplicação (passo em que está e tempo desde o último log)
	deve receber também a mensagem de erro gerada caso a aplicação pare

As tabelas com nome iniciado por "cnae_" contêm informações de estruturação da CNAE. Não precisam ser atualizadas.

Algumas tabelas contêm uma coluna timestamp. Essa coluna será automaticamente preenchida quando for feita a inserção da linha.
