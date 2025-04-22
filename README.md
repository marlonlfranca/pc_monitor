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
8. Configure o NSSM com as seguintes informações:

9. Baixe o arquivo start_monitor.bat
10. 
11. 

7. No VsCode (ou IDE de sua escolha), instale as bibliotecas Python:
        pip install psutil prometheus-client
8. 
