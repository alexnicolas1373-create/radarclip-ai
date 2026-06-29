# Arquitetura do RadarClip AI

## Objetivo do sistema
O RadarClip AI é uma plataforma que identifica tendências, seleciona trechos relevantes de vídeos e gera clipes curtos com apoio de IA.

## Visão geral
O sistema é composto por:
- Frontend web para usuários finais;
- Backend API para gestão de recursos e autenticação;
- Banco de dados relacional para persistência;
- Serviços de IA e FFmpeg para processamento de vídeo.

## Componentes principais
### 1. Frontend
- Interface para autenticação, dashboard e upload de vídeos;
- Consumo da API REST.

### 2. Backend
- API REST em FastAPI;
- Autenticação JWT;
- Gestão de usuários, tendências, vídeos e clipes;
- Orquestração do processamento de vídeo.

### 3. Banco de dados
- PostgreSQL;
- Armazenamento das entidades principais e seus relacionamentos.

### 4. Processamento de mídia
- Integração com IA para análise de tendências e sugestão de cortes;
- Integração com FFmpeg para geração de clipes.

## Arquitetura sugerida para o MVP
- Camada de API: FastAPI;
- Camada de negócio: serviços organizados por domínio;
- Camada de dados: SQLAlchemy + PostgreSQL + Alembic;
- Camada de processamento: worker assíncrono para tarefas de IA e FFmpeg.

## Fluxo principal
1. O usuário autentica-se.
2. O sistema carrega tendências relevantes.
3. O usuário envia ou seleciona um vídeo.
4. A plataforma identifica trechos potenciais.
5. O sistema gera um clipe curto.
6. O clipe é salvo e disponibilizado para visualização.

## Critérios de qualidade esperados
- API documentada e versionada;
- Segurança com autenticação e autorização;
- Observabilidade básica;
- Testes automatizados para regras críticas.
