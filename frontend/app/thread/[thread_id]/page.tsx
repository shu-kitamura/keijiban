"use client";

import PostCard from "@/app/components/postCard";
import PostForm from "@/app/components/postInput";
import type { Thread } from "../../types";

export type Post = {
  id: string;
  thread_id: string;
  content: string;
  author: string;
  created_at: string;
};

async function getPosts(thread_id: string): Promise<Post[]> {
    const response = await fetch(`http://backend:8000/api/v1/threads/${thread_id}/posts`);
    return response.json();
}

const thread: Thread = await fetch(`http://localhost:8000/api/v1/threads/1`).then((res) => res.json());
 
export default async function Page(
    { params }: { 
        params: Promise<{ thread_id: string }>
    }
) {
    console.log("pages")
    const { thread_id } = await params;
    const posts = await getPosts(thread_id);

    return (
        <div>
            <h1 className="text-center text-3xl md:text-4xl font-bold tracking-tight">
                {thread.title}
            </h1>

            <div className="mx-auto max-w-3xl px-4 py-12">
                <ul>
                    {posts.map((post) => (
                        <li key={post.id} className="py-3">
                            <PostCard
                                content={post.content}
                                author={post.author}
                                created_at={post.created_at}
                            />
                        </li>
                    ))}
                </ul>
            </div>

            <div className="mx-auto max-w-3xl px-4 py-12">
                <PostForm />
            </div>
        </div>
    );
}