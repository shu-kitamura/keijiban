"use client";
import { useState, useTransition } from "react";
import { SearchIcon } from "lucide-react"

import type { Thread } from "@/app/types";
import ThreadSearchResult from "@/app/components/threadSearchResult";
import ThreadSearchInput from "@/app/components/threadSearchInput";
import Header from "@/app/components/header";

export default function Home() {
  console.log("home");
  const [query, _setQuery] = useState("");
  const [results, setResults] = useState<Thread[] | null>(null);
  const [isPending, startTransition] = useTransition();

  return (
  <main className="min-h-screen text-slate-900">
    <div>
      <Header title="ブリン・板・板・ボン" />

      <ThreadSearchInput
        query={query}
        startTransition={startTransition}
        setResults={setResults}
      />


    </div>
      <div className="mx-auto max-w-3xl px-4 py-12">      
        <section>
        <div className="rounded-2xl p-4">
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

    {/*
      TODO: スレッド作成
      ボタンを押したら、投稿作成ページに飛ぶ
    */} 
  </main>
  );
}
