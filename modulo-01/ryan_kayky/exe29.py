import json

resposta_api = """
{
    "cidade": "Manaus",
    "pais": "BR",
    "temperatura": {
        "atual": 32.4,
        "minima": 26.1,
        "maxima": 35.8,
        "sensacao": 38.2
    },
    "umidade": 87,
    "condicao": "Parcialmente nublado",
    "vento": { "velocidade_kmh": 12, "direcao": "NE" },
    "atualizado_em": "2025-01-15T14:30:00"
}
"""

clima = json.loads(resposta_api)

print(f"🌤 Boletim de {clima['cidade']} - {clima['pais']}")
print(f"Condição: {clima['condicao']}")
print(f"Temperatura Atual: {clima['temperatura']['atual']}°C (Sensação: {clima['temperatura']['sensacao']}°C)")
print(f"Umidade: {clima['umidade']}%")
print(f"Vento: {clima['vento']['velocidade_kmh']} km/h ({clima['vento']['direcao']})")
