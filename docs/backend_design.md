# API design document

## Abstract

This document describes the design of the API used by the backend service.  

## Technology Stack

- **Language**: Python 3.13.2
- **Framework**: Fastapi 0.117.1
- **Database**: SQL Server 2022
- **Infrastructure**:
  - Production: Azure (container apps, SQL Service, etc)
  - Development: Docker

## Endpoints

| HTTP Method | Endpoint | Description | Authorization |
|-------------|----------|-------------|---------------|
| GET | `/api/v1/threads/search` | Search threads | - |
| GET | `/api/v1/threads/{thread_id}` | Get the thread | - |
| POST | `/api/v1/threads` | Create thread | - |
| DELETE | `/api/v1/threads/{thread_id}` | Delete thread | - |
| GET | `/api/v1/threads/{thread_id}/posts` | Get posts in the thread | - |
| POST | `/api/v1/threads/{thread_id}/posts` | Create post | - |
| DELETE | `/api/v1/threads/{thread_id}/posts/{post_id}` | Delete post | - |

Adding authorization in the future.  
But authorization will not be implemented in this sprint.

### Versioning

- Base path: `/api/v1`
- Breaking changes → add `v2`

## Resource Model

### Thread

| Attribute | Type | Description |
|-------------|----------|-------------|
| id | `str` | UUID |
| title | `str` | 1 to 255 characters |
| description | `str` | Optional |
| owner | `str` | The username of the thread creator |
| create_at | `datetime` | The time the thread was created |
| update_at | `datetime` | The time the thread was updated |

### Post

| Attribute | Type | Description |
|-------------|----------|-------------|
| id | `str` | UUID |
| thread_id | `str` | UUID |
| content | `str` | Post body |
| author | `str` | The username of the post author |
| create_at | `datetime` | The time the post was created |
