##Monitoramento de Recursos de PC com Prometheus + Grafana  

Neste projeto, fiz um script que coleta métricas de CPU, RAM e Disco de uma VM Windows e as plota em tempo real no Grafana.  

##Tecnologias  
- Python (psutil, prometheus-client)  
- Prometheus  
- Grafana  
- NSSM (para serviços Windows)

##Sumário
1. Instale as dependências no VSCode (requirements.txt)
2. Crie um arquivo de coleta dos dados (pc_monitor.py)
3. Baixe, instale e inicie e configure o Prometheus \n
4. Execute o Prometheus em segundo plano (start_monitor.bat)  - opcional.
5. Instale o Grafana e o configure para receber os dados do Prometheus
6. Crie um dashboard e monitore os dados em tempo real.


##Como Executar
**Na máquina que será monitorada:**

1. Baixe os arquivos deste repositório.
2. Baixe o Prometheus: https://prometheus.io/download/ e o instale.
3. Na pasta do Prometheus, localize o arquivo prometheus.yml, apague todos os dados e cole as informações do arquivo ymlconfig.txt.
   (ESCOLHA UMA DAS OPÇÕES)

**OPÇÃO 1 - EXECUÇÃO EM SEGUNDO PLANO**

4. Abra o Terminal de Comandos com administrador.
5. Rode o arquivo em background com o comando:
      start /B python pc_monitor.py
6. Obs: Assim que o terminal de comandos for fechado, a execução será interrompida.

**OPÇÃO 2 - EXECUÇÃO COMO SERVIÇO (PARA MONITORAMENTO CONTÍNUO)**

7. Baixe e instale o NSSM: https://nssm.cc/download
8. Abra o terminal de comandos (admin) e navegue até a pasta NSSM
      cd CAMINHO_DO_ARQUIVO_NSSM
10. O NSSM será executado pela primeira vez já na criação do serviço (pc_monitor.py), então, copie o caminho do arquivo pc_monitor.py e o insira no comando abaixo:
      nssm install pc_monitor
11. A seguinte janela será aberta:

![image](https://github.com/user-attachments/assets/7c6ed3e9-c77f-412a-90db-930f88116c9f)





12. Em PATH, insira o caminho do arquivo python que roda na máquina
13. Em STARTUP DIRECTORY, insira o caminho do arquivo pc_monitor.py
14. Em ARGUMENTS, insira o nome do arquivo.
15. Pressione OK, será retornada a mensagem "Sucesso", para confirmar o sucesso da instalação, no terminal, utilize o comando:
      nssm status pc_monitor
16. A mensagem esperada é SERVICE_RUNNING. Caso seja retornada a mensagem SERVICE_STOPPED, remova a atual instalação com o comando _nssm remove pc_monitor confirm_ e reinstale. Caso ainda não funcione após a segunda tentativa, verifique o path (variáveis de ambiente) e as permissões de seu usuário _regedit_.

**INSTALAÇÃO DO GRAFANA**

17. Baixe e instale o Grafana: https://grafana.com/grafana/download
18. Acesse o grafana na página padrão: http://localhost:3000
19. Acesse a aba CONNECTIONS, depois, no campo SEARCH, digite Prometheus, selecione a opção que aparecer com o indicador "instalado"


![image](https://github.com/user-attachments/assets/b8e1ff78-5825-42dd-8bbc-13f79aac8a74)

20. Na página seguinte, selecione ADD NEW DATA SOURCE
21. Na página de configuração, informe a URL: http://localhost:9000 e SCRAPE INTERVAL: 5s (5 segundos), nada mais precisa ser alterado.

**VISUALIZAÇÃO**
22. Crie um novo dashboard na opção "+" e NEW DASHBOARD:


![image](https://github.com/user-attachments/assets/735de1ab-ac9f-46d8-ad75-b81c85dfd624)

23. No novo dash, selecione ADD VISUALIZATION
24. Em DATA SOURCE, clique em Prometheus

![image](https://github.com/user-attachments/assets/552e897a-eaba-443c-93dc-7f3c1207c399)


25. Em METRIC, selecione a métrica _cpu_usage_percent_, em LABEL FILTERS, selecione JOB, em SELECT VALUE, selecione _pc_metrics_
26. Pressione RUN QUERIES para visualizar os dados obtidos

![image](https://github.com/user-attachments/assets/e3b18296-1e97-4605-be4f-29d5264e593a)

27. Pressione BACK TO DASHBOARD
28. Clique nos 3 pontos do canto superior direito do primeiro painel, depois, MORE, depois, DUPLICATE

![image](https://github.com/user-attachments/assets/5b2a4324-bfd5-40d3-a927-46543a652506)


29. Clique em qualquer parte do painel duplicado, pressione "E", agora, altere a informação da métrica (anteriormente _cpu_user_percent_), desta vez, selecione _ram_usage_percent_
30. Repita o mesmo processo para um terceiro painel, e neste, selecione a métrica _disk_usage_percent_
31. Faça quantas alterações mais achar necessário no visual do painel.

**RESULTADO FINAL**
Uso de CPU


![image](https://github.com/user-attachments/assets/ca03706e-b7b1-45c3-857f-12b7a1e41ff0)

Uso de Memória

![image](https://github.com/user-attachments/assets/b1d534fb-62d5-4d63-b2d2-4a10093f8cfb)



Uso de Disco

![image](https://github.com/user-attachments/assets/2942fa7f-9cb8-4b61-9af4-a31c7f2f146e)






**OBSERVAÇÕES**

Caso você tenha selecionado a opção 1, seu programa estará sendo executado enquanto o terminal estiver aberto, assim que for fechado, a execução será interrompida. Na opção 2, o programa é executado automaticamente, como parte do sistema.

Boas práticas.
