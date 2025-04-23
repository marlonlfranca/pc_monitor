# Monitoramento de Recursos - Prometheus + Grafana  

Neste projeto, fiz um script que coleta métricas de CPU, RAM e Disco de uma VM Windows e as plota em tempo real no Grafana.  

## Tecnologias  
- Python (psutil, prometheus-client)  
- Prometheus  
- Grafana  
- NSSM (para serviços Windows)

## Sumário
1. Baixe e instale os arquivos deste repositório.
2. Siga os passos de instação dos recursos.
3. Baixe, instale, inicie e configure o Prometheus.
4. Baixe e instale o Grafana, configure para receber os dados do Prometheus.
5. Crie um dashboard e monitore sua máquina em tempo real.

## Como Executar
### **Na máquina que será monitorada:**

1. Baixe os arquivos deste repositório.
2. Baixe o [Prometheus](https://prometheus.io/download/) e o instale.
3. Na pasta do Prometheus, localize o arquivo _prometheus.yml_, apague todos os dados e cole as informações do arquivo [ymlconfig.txt](configs/ymlconfig.txt).

> [!IMPORTANT]
> ESCOLHA UMA DAS OPÇÕES

### **OPÇÃO 1 - EXECUÇÃO EM SEGUNDO PLANO[^1]**

4. Abra o Terminal de Comandos com permissões de administrador.
5. Rode o arquivo em background com o comando `start /B python pc_monitor.py`
6. Obs: Assim que o terminal de comandos for fechado, a execução será interrompida.

### **OPÇÃO 2 - EXECUÇÃO COMO SERVIÇO[^2]**

7. Baixe e instale o [NSSM](https://nssm.cc/download)
8. Abra o terminal de comandos (como administrador) e navegue até a pasta NSSM com o comando `cd CAMINHO_DO_ARQUIVO_NSSM`
10. O NSSM será executado pela primeira vez já na criação do serviço, esse serviço será chamado pc_monitor.py, então, localize o arquivo [pc_monitor.py](scripts/pc_monitor.py), copie o caminho e o insira no comando `nssm install pc_monitor`
11. A seguinte janela será aberta:

<p align="center">
      <img src="https://github.com/user-attachments/assets/7c6ed3e9-c77f-412a-90db-930f88116c9f" />
</p>


12. Em <ins>PATH</ins>, insira o caminho do arquivo python que roda na máquina.
> [!TIP]
> Caso não saiba o caminho do arquivo python na sua máquina, abra o Terminal de Comandos (com permissão admin) e digite o comando `where python`, será retornado o local do arquivo python. Copie o caminho para o passo seguinte.
14. Em <ins>STARTUP DIRECTORY</ins> , insira o caminho do arquivo pc_monitor.py[^2]
15. Em <ins>ARGUMENTS</ins>, insira o nome do arquivo.
16. Pressione OK, será retornada a mensagem "Sucesso", para confirmar o sucesso da instalação, no terminal, utilize o comando:
      nssm status pc_monitor
17. A mensagem esperada é <ins>SERVICE_RUNNING</ins>.
> Caso seja retornada a mensagem _SERVICE_STOPPED_, remova a atual instalação com o comando _nssm remove pc_monitor confirm_ e reinstale. Caso ainda não funcione após a segunda tentativa, verifique o path (variáveis de ambiente) e as permissões de seu usuário _regedit_.

### **INSTALAÇÃO DO GRAFANA**

17. Baixe e instale o [Grafana](https://grafana.com/grafana/download)
18. Acesse o grafana na [página padrão do Grafana](http://localhost:3000)
19. Acesse a aba <ins>CONNECTIONS</ins>, depois, no campo <ins>SEARCH</ins>, digite `Prometheus`, selecione a opção que aparecer com o indicador "instalado"

<p align="center">
      <img src="https://github.com/user-attachments/assets/b8e1ff78-5825-42dd-8bbc-13f79aac8a74">
</p>

20. Na página seguinte, selecione <ins>ADD NEW DATA SOURCE</ins>
21. Na página de configuração, informe a <ins>URL</ins>: http://localhost:9000 e <ins>SCRAPE INTERVAL</ins>: 5s (5 segundos), nada mais precisa ser alterado.

### **VISUALIZAÇÃO**
22. Crie um novo dashboard na opção "+" e <ins>NEW DASHBOARD</ins>:

<p align="center">
      <img src="https://github.com/user-attachments/assets/735de1ab-ac9f-46d8-ad75-b81c85dfd624">
</p>

23. No novo dash, selecione <ins>ADD VISUALIZATION</ins>
24. <ins>Em DATA SOURCE</ins>, clique em Prometheus
<p align="center">
      <img src="https://github.com/user-attachments/assets/552e897a-eaba-443c-93dc-7f3c1207c399">
</p>

25. Em <ins>METRIC</ins>, selecione a métrica _cpu_usage_percent_, em <ins>LABEL FILTERS</ins>, selecione <ins>JOB</ins>, em <ins>SELECT VALUE</ins>, selecione _pc_metrics_
26. Pressione <ins>RUN QUERIES</ins> para visualizar os dados obtidos

<p align="center">
      <img src="https://github.com/user-attachments/assets/e3b18296-1e97-4605-be4f-29d5264e593a">
</p>

27. Pressione <ins>BACK TO DASHBOARD</ins>
28. Clique nos 3 pontos do canto superior direito do primeiro painel, depois, MORE, depois, <ins>DUPLICATE</ins>

<p align="center">
      <img src="https://github.com/user-attachments/assets/5b2a4324-bfd5-40d3-a927-46543a652506">
</p>

29. Clique em qualquer parte do painel duplicado, pressione "E", agora, altere a informação da métrica (anteriormente _cpu_user_percent_), desta vez, selecione _ram_usage_percent_
30. Repita o mesmo processo para um terceiro painel, e neste, selecione a métrica _disk_usage_percent_
31. Faça quantas alterações mais achar necessário no visual do painel.

## **RESULTADO FINAL**
### Uso de CPU

<p align="center">
      <img src="https://github.com/user-attachments/assets/ca03706e-b7b1-45c3-857f-12b7a1e41ff0">
</p>

### Uso de Memória
<p align="center">
      <img src="https://github.com/user-attachments/assets/b1d534fb-62d5-4d63-b2d2-4a10093f8cfb">
</p>


### Uso de Disco
<p align="center">
      <img src="https://github.com/user-attachments/assets/2942fa7f-9cb8-4b61-9af4-a31c7f2f146e">
</p>

### Visão Geral
<p align="center">
      <img src="https://github.com/user-attachments/assets/025a933c-1d31-453b-9ddf-4cfca0810f08">
</p>

## **OBSERVAÇÕES**

[^1]: Opção 1 - seu programa estará sendo executado enquanto o terminal estiver aberto, assim que for fechado, a execução será interrompida.

[^2]: Opção 2 - o programa é executado automaticamente, como parte do sistema.

[^3]: aaaa 2 - 

Boas práticas.
