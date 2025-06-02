# Use uma imagem base Python oficial. Escolha a versão do Python que você usa.
FROM python:3.13.3

# Define variáveis de ambiente para o contêiner
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala dependências do sistema operacional (se necessário, para libs como psycopg2-binary)
# Adapte conforme as necessidades do seu projeto
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    gettext \
    # Adicione outras libs do sistema se suas dependências Python as exigirem
    # Ex: libjpeg-dev zlib1g-dev para Pillow
    # Ex: gcc python3-dev para outras compilações
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos e instala as dependências Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o contêiner
COPY . /app/

# Coleta arquivos estáticos (opcional, mas recomendado para produção)
# RUN python manage.py collectstatic --noinput

# Comando padrão para iniciar o serviço (será sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]