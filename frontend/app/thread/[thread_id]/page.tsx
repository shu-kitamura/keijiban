
import PostCard from "@/app/components/postCard";
import PostInput from "@/app/components/postInput";
import type { Post, Thread } from "@/app/types";

import Header from "@/app/components/header";

const backendOrigin = process.env.BACKEND_ORIGIN;

async function getPosts(thread_id: string): Promise<Post[]> {
    const response = await fetch(`${backendOrigin}/api/v1/threads/${thread_id}/posts`);
    return response.json();
}

 
export default async function Page(
    { params }: { 
        params: Promise<{ thread_id: string }>
    }
) {
    console.log("pages")
    const { thread_id } = await params;
    const thread: Thread = await fetch(`${backendOrigin}/api/v1/threads/${thread_id}`).then((res) => res.json());
    const posts = await getPosts(thread_id);

    return (
        <div>
            <Header title={thread.title} />

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

            <div className="flex justify-center">
                <PostInput
                    thread_id={thread_id}
                />
            </div>
        </div>
    );
}