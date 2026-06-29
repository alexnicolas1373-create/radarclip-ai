# API do RadarClip AI

## Visão geral
A API do RadarClip AI fornece endpoints para autenticação, gestão de tendências, vídeos e clipes.

## Principais módulos
- Auth;
- Trends;
- Videos;
- Clips;
- Process.

## Endpoints previstos
### Autenticação
- POST /auth/register;
- POST /auth/login.

### Tendências
- GET /trends;
- POST /trends;
- GET /trends/{trend_id};
- PUT /trends/{trend_id};
- DELETE /trends/{trend_id}.

### Vídeos
- GET /videos;
- POST /videos;
- GET /videos/{video_id};
- PUT /videos/{video_id};
- DELETE /videos/{video_id}.

### Clipes
- GET /clips;
- POST /clips;
- GET /clips/{clip_id};
- PUT /clips/{clip_id};
- DELETE /clips/{clip_id}.

### Processamento
- POST /process.

## Segurança
- Autenticação com JWT;
- Endpoints sensíveis protegidos por token Bearer.

## Formatos de resposta
- JSON;
- Status HTTP padrão para sucesso, validação e erros de negócio.

## Documentação
- O projeto deve manter documentação automática via Swagger/OpenAPI, fornecida pelo FastAPI.
