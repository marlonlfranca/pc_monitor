from prometheus_client import start_http_server, Gauge
import psutil
import time

# Crie métricas
CPU_USAGE = Gauge('cpu_usage_percent', 'Uso atual da CPU (%)')
RAM_USAGE = Gauge('ram_usage_percent', 'Uso atual da RAM (%)')
DISK_USAGE = Gauge('disk_usage_percent', 'Uso atual do disco (%)')

if __name__ == '__main__':
    # Inicia servidor HTTP na porta 8000 (para o Prometheus coletar)
    start_http_server(8000)
    
    while True:
        # Atualiza métricas
        CPU_USAGE.set(psutil.cpu_percent())
        RAM_USAGE.set(psutil.virtual_memory().percent)
        DISK_USAGE.set(psutil.disk_usage('/').percent)
        time.sleep(5)  # Atualiza a cada 5s
