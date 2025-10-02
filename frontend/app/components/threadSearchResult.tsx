import type { Thread } from "@/app/types";

type ThreadSearchResultProps = {
    thread: Thread;
}

export default function ThreadSearchResult({ thread }: ThreadSearchResultProps) {
    return (
        <article className="grid grid-cols-1 md:grid-cols-[1fr_220px] gap-2 md:gap-6 items-start">
            <div>
                <h3 className="font-semibold leading-tight text-sky-600 hover:underline">
                    <a href={`/thread/${thread.id}`}>{thread.title}</a>
                </h3>
                <p className="mt-1 text-sm text-slate-600">{thread.description}</p>
            </div>
            <div className="md:text-right text-xs text-slate-600">
                <div>作成日：{thread.created_at}</div>
                <div>更新日：{thread.updated_at}</div>
            </div>
        </article>
    );
}