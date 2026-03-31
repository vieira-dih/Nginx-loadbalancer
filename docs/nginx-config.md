# Configuração do Nginx

## Função

O Nginx foi configurado como:

- Proxy Reverso
- Load Balancer
- Servidor HTTPS

## Load Balancer

Foi utilizado o algoritmo:

- **least_conn**

Este algoritmo direciona as requisições para o servidor com menor número de conexões ativas.

## Upstream

```nginx
upstream backend_cluster {
    least_conn;
    server backend1:5000 max_fails=3 fail_timeout=10s;
    server backend2:5000 max_fails=3 fail_timeout=10s;
    server backend3:5000 max_fails=3 fail_timeout=10s;
}

Failover

O failover é implementado com:

max_fails=3
fail_timeout=10s

Quando uma instância falha, ela é temporariamente removida do pool.

Rate Limiting
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=5r/s;

Protege contra excesso de requisições.

Proxy Reverso

Encaminhamento de requisições:

/api → backend
/ → frontend
/admin → admin
SSL

Certificado self-signed configurado com:

Porta 443
HTTPS habilitado
Gzip

Compressão ativada para melhorar performance:

gzip on;
Logs

Logs personalizados com:

IP do cliente
upstream utilizado
tempo de resposta