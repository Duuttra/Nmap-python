import nmap
import json
from datetime import datetime

# Pede o alvo pro usuário
target = input("Digite o IP ou domínio: ")

print(f"\nEscaneando {target}... aguarde!\n")

# Cria o scanner e roda o scan
scanner = nmap.PortScanner()

try:
    scanner.scan(target, arguments="-sV")
except Exception as erro:
    print(f"Deu erro no scan: {erro}")
    exit()

# Monta o resultado
resultados = {}

for host in scanner.all_hosts():
    print(f"Host: {host} — estado: {scanner[host].state()}")
    resultados[host] = {"estado": scanner[host].state(), "portas": []}

    for proto in scanner[host].all_protocols():
        for porta in scanner[host][proto].keys():
            info = scanner[host][proto][porta]

            print(f"  Porta {porta}/{proto} — {info['state']} — serviço: {info['name']}")

            resultados[host]["portas"].append({
                "porta":   porta,
                "estado":  info["state"],
                "servico": info["name"],
                "versao":  info.get("version", ""),
            })

# Salva em JSON
arquivo = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(arquivo, "w") as f:
    json.dump(resultados, f, indent=4)

print(f"\nRelatório salvo em: {arquivo}")
