"use client";

import { useState } from "react";
import type { Thread } from "@/app/types";
import { SearchIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { ButtonGroup } from "@/components/ui/button-group"
import { Input } from "@/components/ui/input"

import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

type ThreadSearchInputProps = {
    query: string;
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
        <div className="w-full max-w-sm">
            <Card>
                <CardHeader>
                    <CardTitle>Search Threads</CardTitle>
                    <CardDescription>
                        Enter your title below to search for threads
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <form onSubmit={onSubmit}>
                        <ButtonGroup>
                            <Input
                                placeholder="Search..."
                                value={query}
                                onChange={(e) => setQuery(e.target.value)}
                            />
                            <Button variant="outline" aria-label="Search">
                                <SearchIcon />
                            </Button>
                        </ButtonGroup>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}