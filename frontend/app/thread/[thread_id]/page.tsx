function generateStaticParams() {}

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
 
export default async function Page(
    { params }: { 
        params: Promise<{ thread_id: string }>
    }
) {
    const { thread_id } = await params;
    const thread = await fetch(`http://backend:8000/api/v1/threads/${thread_id}`).then((res) => res.json());
    const posts = await getPosts(thread_id);

    return (
        <div>
            <h1 className="text-center text-3xl md:text-4xl font-bold tracking-tight">
                {thread.title}
            </h1>

            <div className="mx-auto max-w-3xl px-4 py-12">
                <ul className="divide-y">
                    {posts.map((post) => (
                        <li key={post.id} className="py-3">
                            <article className="grid grid-cols-1 md:grid-cols-[1fr_220px] gap-2 md:gap-6 items-start">
                                <div>
                                    <p className="leading-tight">{post.content}</p>
                                </div>
                                <div className="md:text-right text-xs text-slate-600">
                                    <p>作成日：{post.created_at}</p>
                                    <p>投稿者：{post.author}</p>
                                </div>
                            </article>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}