[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20017187)
# Estude





### Criar a base de dados sqlite3 padrão do django, mas podemos utilizar qualquer SGBD
```bash
python manage.py migrate
```
### Rodar o servidor web do Django
```bash
python manage.py runserver
```


### Efetivar alterações no banco de dados
```bash
python manage.py makemigrations
# E
python manage.py migrate
```

### Criando a venv e ativando
```bash
python -m venv venv
# Git Bash/Linux/Mac
source ./venv/Scripts/activate
# Windows CMD/PowerShell
.\venv\Scripts\activate
# Opcional instalar os requirimentos
pip install -r requirements/r.txt
# Opcional salvar os requirimentos
pip freeze > requirements/r.txt
```