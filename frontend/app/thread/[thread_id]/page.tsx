
import PostCard from "@/app/components/postCard";
import PostForm from "@/app/components/postInput";
import type { Post, Thread } from "@/app/types";

async function getPosts(thread_id: string): Promise<Post[]> {
    const response = await fetch(`http://backend:8000/api/v1/threads/${thread_id}/posts`);
    return response.json();
}

 
export default async function Page(
    { params }: { 
        params: Promise<{ thread_id: string }>
    }
) {
    console.log("pages")
    const { thread_id } = await params;
    const thread: Thread = await fetch(`http://backend:8000/api/v1/threads/${thread_id}`).then((res) => res.json());
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
                <PostForm 
                    thread_id={thread_id}
                />
            </div>
        </div>
    );
}