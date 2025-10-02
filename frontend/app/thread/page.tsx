"use client";

function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    const title = formData.get("title") as string;
    const description = formData.get("description") as string;
    const owner = "匿名"; // 後にユーザ機能を実装したら変える
    console.log({ title, description });

    if (!title) {
        alert("タイトルを入力してください。");
        return;
    }

    fetch(`/api/threads/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title,
            description,
            owner,
        }),
    }).then((res) => {
        if (res.ok) {
            alert("スレッドを作成しました");
            window.location.reload();
        }
    });
}

export default function Page() {
    console.log("thread create page");
    return (
        <div>
            <div className="mx-auto max-w-3xl px-4 py-12">
                <h1 className="text-center text-3xl md:text-4xl font-bold tracking-tight">スレッド作成</h1>
            </div>

            <div className="relative max-w-2xl mx-auto">
                <form onSubmit={(event) => handleSubmit(event)} method="post">
                    <div className="mb-4">
                        <p>スレッド名</p>
                        <input name="title" type="text" className="w-full rounded-xl border border-slate-400 bg-white px-4 py-3 pr-12 shadow-sm outline-none focus:ring-2 focus:ring-sky-400"/>
                    </div>
                    <div className="mb-4">
                        <p>説明（任意）</p>
                        <input name="description" type="text" className="w-full rounded-xl border border-slate-400 bg-white px-4 py-3 pr-12 shadow-sm outline-none focus:ring-2 focus:ring-sky-400"/>
                    </div>
                    <div className="mb-4 flex justify-center">
                    <button type="submit" className="px-3 bg-blue-500 text-white rounded-md hover:bg-blue-600">作成</button>
                    </div>
                </form>
            </div>
        </div>
    );
}