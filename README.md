#Monitoramento de Recursos de PC com Prometheus + Grafana  

Neste projeto, fiz um script que coleta métricas de CPU, RAM e Disco de uma VM Windows e as plota em tempo real no Grafana.  

#Tecnologias  
- Python (psutil, prometheus-client)  
- Prometheus  
- Grafana  
- NSSM (para serviços Windows)

#Como Executar  
1. Instale as dependências no VSCode (requirements.txt)
2. Crie um arquivo .py e cole o código de coleta dos dados (pc_monitor.py)
3. Baixe, instale e inicie e configure o Prometheus
   3.1 Execute o Prometheus em segundo plano (start_monitor.bat)  - opcional.
4. Instale o Grafana e o configure para receber os dados do Prometheus
5. Crie um dashboard e monitore os dados em tempo real.
