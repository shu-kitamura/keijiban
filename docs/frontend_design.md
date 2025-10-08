# Frontend design document

## Abstract

This document describes the design of the API used by the frontend.

## Technology Stack

- **Language**: TypeScript
- **Framework**: Next.js

## Endpoints

| HTTP Method | Endpoint | Description | Authorization |
|-------------|----------|-------------|---------------|
| GET | `/` | Top page | - |
| GET | `/thread` | Thread creation page | - |
| GET | `/thread/{thread_id}` | Thread and Posts Page | - |
| - | `/api/...` | Route to the backend | - |
