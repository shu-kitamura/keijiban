"use client";

import { useState } from "react";
import type { Thread } from "@/app/types";

type ThreadSearchInputProps = {
    query: string;
    setQuery: (query: string) => void;
    startTransition: (callback: () => Promise<void>) => void;
    setResults: (results: any) => void;
}

async function searchThreads(query: string): Promise<Thread[]> {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  const response = await fetch(`/api/threads/search?q=${encodeURIComponent(q)}`);
  const threads = await response.json();
  console.log(threads);
  return threads
}

export default function ThreadSearchInput({startTransition, setResults }: ThreadSearchInputProps) {
    const [query, setQuery] = useState("");
    
    const onSubmit = (e: React.FormEvent) => {
            e.preventDefault();
            startTransition(async () => {
                const res = await searchThreads(query);
                setResults(res);
            });
    };
    return (
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
    );
}