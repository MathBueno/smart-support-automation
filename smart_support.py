import json

# Lê os tickets do arquivo tickets.json
with open("tickets.json", encoding="utf-8") as f:
    tickets = json.load(f)

# Função que analisa cada ticket
def analyze_ticket(ticket_text):
    ticket_lower = ticket_text.lower()
    if "login" in ticket_lower or "logar" in ticket_lower:
        return {
            "category": "erro do usuário",
            "cause": "usuário digitou senha errada",
            "solution": "orientar usuário a resetar senha",
            "priority": "médio"
        }
    elif "api" in ticket_lower or "timeout" in ticket_lower:
        return {
            "category": "bug",
            "cause": "problema no servidor",
            "solution": "verificar logs e reiniciar serviço",
            "priority": "alto"
        }
    else:
        return {
            "category": "outro",
            "cause": "não identificado",
            "solution": "investigar",
            "priority": "baixo"
        }

# Processa os tickets e cria respostas automáticas
outputs = []

for t in tickets:
    analysis = analyze_ticket(t["ticket"])
    response = f"Olá! Problema: {analysis['category']}. Causa: {analysis['cause']}. Solução: {analysis['solution']}. Prioridade: {analysis['priority']}."
    outputs.append({"ticket": t["ticket"], "response": response})

# Cria o arquivo outputs.json com codificação UTF-8 para acentos
with open("outputs.json", "w", encoding="utf-8") as f:
    json.dump(outputs, f, indent=4, ensure_ascii=False)

print("Pronto! Veja outputs.json")