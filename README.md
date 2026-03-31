# TF04 - E-commerce com Load Balancer Avançado

## Aluno
- **Nome:** Diogo Vieira Amorim
- **RA:** 6324639
- **Curso:** Análise e Desenvolvimento de Sistemas

## Arquitetura

O sistema foi desenvolvido utilizando uma arquitetura baseada em containers Docker com os seguintes componentes:

- **Nginx:** Atua como Load Balancer e Proxy Reverso
- **Backend:** 3 instâncias da API (Flask) para alta disponibilidade
- **Frontend:** Aplicação estática (HTML + CSS)
- **Admin:** Painel administrativo separado
- **SSL:** Certificado self-signed para HTTPS

## Funcionalidades Implementadas

- ✅ Load balancing com algoritmo **least_conn**
- ✅ Health checks automáticos com failover
- ✅ 3 instâncias de backend
- ✅ Proxy reverso configurado
- ✅ SSL/TLS com certificado self-signed
- ✅ Rate limiting (5 requisições por segundo)
- ✅ Logs detalhados com upstream
- ✅ Compressão gzip habilitada
- ✅ Monitoramento com endpoint `/nginx-status`
- ✅ Endpoint `/health` para verificação de serviços

## Como Executar

### Pré-requisitos

- Docker
- Docker Compose

### Passos

```bash
git clone [URL_DO_REPOSITORIO]
```
```bash
cd TF04
```

# Gerar certificado SSL
openssl req -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout nginx/ssl/key.pem \
-out nginx/ssl/cert.pem

# Subir containers
docker-compose up -d --build

# Verificar containers
docker ps

Endpoints
Frontend: http://localhost
API: http://localhost/api/info
Admin: http://localhost/admin/
Status: http://localhost/nginx-status
Health: http://localhost/health
HTTPS: https://localhost
Testes de Load Balancing
for i in {1..10}; do
  curl -s http://localhost/api/info
done

Resultado esperado:

Respostas alternadas entre as instâncias (1, 2, 3)
Teste de Failover
docker stop backend1
curl http://localhost/api/info

Resultado esperado:

Sistema continua funcionando mesmo com uma instância parada
Monitoramento
Logs:
docker-compose logs nginx
Status:
http://localhost/nginx-status
Conclusão

O sistema implementa alta disponibilidade com balanceamento de carga eficiente, garantindo distribuição equilibrada de requisições e tolerância a falhas.