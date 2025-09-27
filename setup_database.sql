-- UUID-OSSP extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Minimal schema (PostgreSQL)
CREATE TABLE thread (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE post (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  thread_id uuid NOT NULL REFERENCES thread(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  author_name VARCHAR(80),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
);

-- Test data insert

-- Threads
INSERT INTO thread (name, description) VALUES
  ('General', '雑談用スレッド'),
  ('Tech', '技術トピック用'),
  ('Random', 'その他 / テスト')
ON CONFLICT (name) DO NOTHING;

-- Posts
WITH general AS (SELECT id FROM thread WHERE name = 'General'),
     tech    AS (SELECT id FROM thread WHERE name = 'Tech'),
     random  AS (SELECT id FROM thread WHERE name = 'Random')
INSERT INTO post (thread_id, content, author_name)
SELECT g.id, 'はじめまして。General スレへようこそ。', 'alice' FROM general g
WHERE NOT EXISTS (SELECT 1 FROM post WHERE content = 'はじめまして。General スレへようこそ。')
UNION ALL
SELECT g.id, '雑談どうぞ！', 'bob' FROM general g
WHERE NOT EXISTS (SELECT 1 FROM post WHERE content = '雑談どうぞ！')
UNION ALL
SELECT t.id, 'Python 3.13 の新機能使ってみた？', 'dev_user' FROM tech t
WHERE NOT EXISTS (SELECT 1 FROM post WHERE content = 'Python 3.13 の新機能使ってみた？')
UNION ALL
SELECT t.id, 'FastAPI + PostgreSQL の構成動作確認中。', 'dev_user' FROM tech t
WHERE NOT EXISTS (SELECT 1 FROM post WHERE content = 'FastAPI + PostgreSQL の構成動作確認中。')
UNION ALL
SELECT r.id, 'ランダムな話題を書いてテスト。', 'tester' FROM random r
WHERE NOT EXISTS (SELECT 1 FROM post WHERE content = 'ランダムな話題を書いてテスト。');
