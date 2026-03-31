```md id="pfysxt"
# Load Balancing

## Estratégia

Foi utilizado o algoritmo:

- **least_conn**

Este método distribui as requisições para o servidor com menos conexões ativas, garantindo melhor desempenho.

## Arquitetura

- 3 instâncias de backend
- Nginx como balanceador

## Testes Realizados

### Teste de distribuição

```bash
for i in {1..10}; do
  curl -s http://localhost/api/info
done
```
Resultado:

Requisições distribuídas entre as instâncias
Teste de Failover
docker stop backend1

Resultado:

Outras instâncias assumem automaticamente
Benefícios
Alta disponibilidade
Escalabilidade
Melhor uso de recursos
Conclusão

O uso de múltiplas instâncias com Nginx garante um sistema resiliente e eficiente.