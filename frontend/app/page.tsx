"use client";
import { useState, useTransition } from "react";

import type { Thread } from "@/app/types";
import ThreadSearchResult from "@/app/components/threadSearchResult";
import ThreadSearchInput from "@/app/components/threadSearchInput";
import ThreadCreateInput from "@/app/components/threadCreateInput";
import Header from "@/app/components/header";

import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"

export default function Home() {
  console.log("home");
  const [query, _setQuery] = useState("");
  const [results, setResults] = useState<Thread[] | null>(null);
  const [isPending, startTransition] = useTransition();

  return (
  <main className="min-h-screen text-slate-900">
    <div>
      <Header title="ブリン・板・板・ボン" />

      <div className="flex justify-center mt-4">
        <Tabs defaultValue="search" className="w-full">
          <div className="flex justify-center">
            <TabsList className="">
              <TabsTrigger value="search">Search</TabsTrigger>
              <TabsTrigger value="create">Create</TabsTrigger>
            </TabsList>
          </div>
          <TabsContent value="search">
            <div className="flex justify-center mt-4">
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

          </TabsContent>

          <TabsContent value="create">
            <div className="flex justify-center mt-4">
              <ThreadCreateInput />
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>



    {/*
      TODO: スレッド作成
      ボタンを押したら、投稿作成ページに飛ぶ
    */} 
  </main>
  );
}
