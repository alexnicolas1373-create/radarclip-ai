# Banco de Dados do RadarClip AI

## Objetivo
Documentar a estrutura inicial de dados necessária para o MVP do RadarClip AI.

## Entidades principais
### users
- id;
- email;
- name;
- hashed_password;
- is_active;
- created_at;
- updated_at.

### trends
- id;
- title;
- platform;
- topic;
- score;
- created_at.

### videos
- id;
- title;
- url;
- platform;
- user_id;
- trend_id;
- created_at.

### clips
- id;
- title;
- start_time;
- end_time;
- video_id;
- user_id;
- created_at.

## Relacionamentos
- users -> videos (1:N);
- users -> clips (1:N);
- trends -> videos (1:N);
- videos -> clips (1:N).

## Considerações de persistência
- O banco deve suportar autenticação e rastreio de autoria dos conteúdos;
- O relacionamento com tendências permite organizar vídeos por tema ou demanda;
- O armazenamento de clipes deve manter vínculo com o vídeo original e com o usuário responsável.

## Estratégia de migração
- Utilização de Alembic para versionamento do esquema;
- Migrações incrementais para criação e evolução das tabelas.
