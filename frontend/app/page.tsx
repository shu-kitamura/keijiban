"use client";
import { useState, useTransition } from "react";

import type { Thread } from "@/app/types";
import ThreadSearchResult from "@/app/components/threadSearchResult";
import ThreadSearchInput from "./components/threadSearchInput";

async function searchThreads(query: string): Promise<Thread[]> {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  const response = await fetch(`http://localhost:8000/api/v1/threads/search?q=${encodeURIComponent(q)}`);
  const threads = await response.json();
  console.log(threads);
  return threads
}

export default function Home() {
  console.log("home");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<Thread[] | null>(null);
  const [isPending, startTransition] = useTransition();

  return (
  <main className="min-h-screen text-slate-900">
    <div className="mx-auto max-w-3xl px-4 py-12">
      <h1 className="text-center text-3xl md:text-4xl font-bold tracking-tight">
        ブリン・板・板・ボン
      </h1>

      <ThreadSearchInput
        query={query}
        setQuery={setQuery}
        startTransition={startTransition}
        setResults={setResults}
      />

      <section className="mt-10">
      <div className="rounded-2xl   p-4">
        {!isPending && results && results.length > 0 && (
            <ul className="divide-y">
              {results.map((t) => (
                <li key={t.id} className="py-3">
                  <ThreadSearchResult thread={t} />
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>
    </div>

    {/* スレッド作成 */}
    <div>

    </div>
  </main>
  );
}
