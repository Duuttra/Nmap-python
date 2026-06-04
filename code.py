import nmap
import json
from datetime import datetime

target = input("IP ou domínio: ")

scanner = nmap.PortScanner()

print(f"Escaneando {target}...")
scanner.scan(target, arguments="-sV")

resultados = {}

for host in scanner.all_hosts():
    resultados[host] = {
        "estado": scanner[host].state(),
        "protocolos": {}
    }

    for proto in scanner[host].all_protocols():
        resultados[host]["protocolos"][proto] = []

        for porta in scanner[host][proto].keys():
            resultados[host]["protocolos"][proto].append({
                "porta": porta,
                "servico": scanner[host][proto][porta]["name"]
            })

arquivo = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(arquivo, "w") as f:
    json.dump(resultados, f, indent=4)

print(f"Relatório salvo em {arquivo}")
