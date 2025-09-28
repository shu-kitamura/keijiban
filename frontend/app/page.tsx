"use client";

import { useState, useTransition } from "react";

export type Thread = {
  id: string;
  title: string;
  description: string;
  createdAt: string; // ISO
  updatedAt: string; // ISO
};


// --- ダミーデータ ---
const SEED: Thread[] = [
  {
    id: "1",
    title: "Next.js × FastAPI 連携メモ",
    description: "API 設計、CORS、型の共有などのメモ",
    createdAt: "2025-09-20T10:05:00Z",
    updatedAt: "2025-09-27T13:40:00Z",
  },
  {
    id: "2",
    title: "eBPF/XDP 学習ログ",
    description: "チェックサム、XDP_TX、ツールのリンク",
    createdAt: "2025-08-30T03:00:00Z",
    updatedAt: "2025-09-15T22:10:00Z",
  },
  {
    id: "3",
    title: "正規表現エンジンの最適化",
    description: "NFA 化、Boyer-Moore、プロファイル結果",
    createdAt: "2025-07-12T09:12:00Z",
    updatedAt: "2025-09-10T12:00:00Z",
  },
];

// --- ここをバックエンド呼び出しに置き換える ---
async function searchThreads(query: string): Promise<Thread[]> {
  // ダミー: 前方・部分一致でフィルタ
  const q = query.trim().toLowerCase();
  if (!q) return [];
  await new Promise((r) => setTimeout(r, 400)); // 擬似ロード
  return SEED.filter(
    (t) =>
      t.title.toLowerCase().includes(q) ||
      t.description.toLowerCase().includes(q)
  );
}

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<Thread[] | null>(null);
  const [isPending, startTransition] = useTransition();

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    startTransition(async () => {
      const res = await searchThreads(query);
      setResults(res);
    });
  };

  return (
  <main className="min-h-screen text-slate-900">
    <div className="mx-auto max-w-3xl px-4 py-12">
      {/* タイトル */}
      <h1 className="text-center text-3xl md:text-4xl font-bold tracking-tight">
        ブリン・板・板・ボン
      </h1>

      {/* 入力欄 + 検索ボタン */}
      <form onSubmit={onSubmit} className="mt-10">
        <label htmlFor="search" className="sr-only">
          検索キーワード
        </label>
        <div className="relative max-w-2xl mx-auto">
          <input
            id="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="キーワードを入力"
            className="w-full rounded-xl border border-slate-400 bg-white px-4 py-3 pr-12 shadow-sm outline-none focus:ring-2 focus:ring-sky-400"
          />
          <button
            type="submit"
            aria-label="検索"
            className="absolute right-1.5 top-1.5 inline-flex h-10 w-10 items-center justify-center rounded-lg border border-slate-400 bg-white hover:bg-slate-50 active:scale-[.98]"
          >
          {/* 虫眼鏡アイコン（SVG） */}
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-slate-700">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          </button>
        </div>
      </form>

      {/* 検索結果 */}
      <section className="mt-10">
      <div className="rounded-2xl   p-4">
        {!isPending && results && results.length > 0 && (
            <ul className="divide-y">
              {results.map((t) => (
                <li key={t.id} className="py-3">
                  <article className="grid grid-cols-1 md:grid-cols-[1fr_220px] gap-2 md:gap-6 items-start">
                    <div>
                      <h3 className="font-semibold leading-tight">{t.title}</h3>
                      <p className="mt-1 text-sm text-slate-600">{t.description}</p>
                    </div>
                    <div className="md:text-right text-sm text-slate-600">
                      <div>作成日：{t.createdAt}</div>
                      <div>更新日：{t.updatedAt}</div>
                    </div>
                  </article>
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>

    </div>
  </main>
  );
}
