email_sujo = "   joao.silva@EMPRESA.com.br   "

email_limpo = email_sujo.strip().lower()
usuario, dominio = email_limpo.split("@")

print(f"Email normalizado: {email_limpo}")
print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")