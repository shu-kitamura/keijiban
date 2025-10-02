"use client";

type PostFormProps = {
    thread_id?: string;
}

function handleSubmit(event: React.FormEvent, thread_id?: string) {
    event.preventDefault();
    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    const content = formData.get("content") as string;
    const author = formData.get("author") as string;
    console.log({ content, author });

    if (!content || !author) {
        alert("ポストかポストネームが空です");
        return;
    }

    fetch(`/api/threads/${thread_id}/posts`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            content,
            author,
        }),
    }).then((res) => {
        if (res.ok) {
            alert("ポストを送信しました");
            window.location.reload();
        }
    });
}

export default function PostForm({ thread_id }: PostFormProps) {
    return (
        <form onSubmit={(event) => handleSubmit(event, thread_id)} className="p-4 w-full max-w-xl mx-auto">
            <div>
                <input name="content" className="w-full border-2 border-sky-500 rounded-md p-2" placeholder="ポストを入力" />
            </div>
            <div className="flex justify-between items-center mt-1">
                <input name="author" className="border-2 border-sky-500 rounded-md" placeholder="ポストネーム" defaultValue="匿名" />
                <button type="submit" className="px-3 bg-blue-500 text-white rounded-md hover:bg-blue-600">
                    ↑
                </button>
            </div>
         </form>
    )
}