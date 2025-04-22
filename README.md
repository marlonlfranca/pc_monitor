#Monitoramento de Recursos de PC com Prometheus + Grafana  

Neste projeto, fiz um script que coleta métricas de CPU, RAM e Disco de uma VM Windows e as plota em tempo real no Grafana.  

#Tecnologias  
- Python (psutil, prometheus-client)  
- Prometheus  
- Grafana  
- NSSM (para serviços Windows)

#Sumário
1. Instale as dependências no VSCode (requirements.txt)
2. Crie um arquivo de coleta dos dados (pc_monitor.py)
3. Baixe, instale e inicie e configure o Prometheus \n
4. Execute o Prometheus em segundo plano (start_monitor.bat)  - opcional.
5. Instale o Grafana e o configure para receber os dados do Prometheus
6. Crie um dashboard e monitore os dados em tempo real.


#Como Executar
Na máquina que será monitorada:
1. Baixe os arquivos deste repositório.
2. Baixe o Prometheus: https://prometheus.io/download/ e o instale.
3. Na pasta do Prometheus, localize o arquivo prometheus.yml, apague todos os dados e cole as informações do arquivo ymlconfig.txt.
   (ESCOLHA UMA DAS OPÇÕES)
OPÇÃO 1 - EXECUÇÃO EM SEGUNDO PLANO
4. Abra o Terminal de Comandos com administrador.
5. Rode o arquivo em background com o comando:
      start /B python pc_monitor.py
6. Obs: Assim que o terminal de comandos for fechado, a execução será interrompida.
OPÇÃO 2 - EXECUÇÃO COMO SERVIÇO (PARA MONITORAMENTO CONTÍNUO)
7. Baixe e instale o NSSM: https://nssm.cc/download
8. Abra o terminal de comandos (admin) e navegue até a pasta NSSM
      cd CAMINHO_DO_ARQUIVO_NSSM
10. O NSSM será executado pela primeira vez já na criação do serviço (pc_monitor.py), então, copie o caminho do arquivo pc_monitor.py e o insira no comando abaixo:
      nssm install pc_monitor
11. A seguinte janela será aberta:

![image](https://github.com/user-attachments/assets/7c6ed3e9-c77f-412a-90db-930f88116c9f)!
12. Em PATH, insira o caminho do arquivo python que roda na máquina
13. Em STARTUP DIRECTORY, insira o caminho do arquivo pc_monitor.py
14. Em ARGUMENTS, insira o nome do arquivo.
15. Pressione OK, será retornada a mensagem "Sucesso", para confirmar o sucesso da instalação, no terminal, utilize o comando:
      nssm status pc_monitor
16. A mensagem esperada é SERVICE_RUNNING. Caso seja retornada a mensagem SERVICE_STOPPED, remova a atual instalação com o comando _nssm remove pc_monitor confirm_ e reinstale. Caso ainda não funcione após a segunda tentativa, verifique o path (variáveis de ambiente) e as permissões de seu usuário _regedit_.

INSTALAÇÃO DO GRAFANA
17. Baixe e instale o Grafana: https://grafana.com/grafana/download
18. Acesse o grafana na página padrão: http://localhost:3000
19. Acesse a aba CONNECTIONS, depois, no campo SEARCH, digite Prometheus, selecione a opção que aparecer com o indicador "instalado"
![image](https://github.com/user-attachments/assets/943a5837-04b9-4ca6-b114-ae435b8b46f6)






