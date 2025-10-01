// ./components/PostForm.tsx
"use client";
import React, { useState, FormEvent, KeyboardEvent } from "react";

type PostFormProps = {
  onSubmit: (payload: { content: string; name: string }) => Promise<void> | void;
  isSubmitting?: boolean;
};

export default function PostForm({ onSubmit, isSubmitting }: PostFormProps) {
  const [content, setContent] = useState("");
  const [name, setName] = useState("");

  const handleSubmit = async (e?: FormEvent) => {
    e?.preventDefault();
    if (!content.trim()) return;
    await onSubmit({ content: content.trim(), name: name.trim() });
    setContent("");
    // 名前は保持する派
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      handleSubmit();
    }
  };

  return (
    <form onSubmit={handleSubmit} className="">
      {/* 横並び：左=本文、右=投稿者名+送信 */}
      <div className="grid grid-flow-col grid-rows-3 gap-4">
        {/* 本文 */}
        <div className="bg-white border-2 border-black rounded-2xl p-4 row-span-3">
          <label htmlFor="content" className="sr-only">投稿内容</label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="投稿内容を入力…（Ctrl/⌘ + Enter で送信）"
            className="w-full h-48 md:h-64 resize-y outline-none text-base leading-relaxed placeholder-gray-400"
          />
        </div>

        {/* 右カラム */}
        <div className="flex flex-col gap-4">
          {/* 投稿者名 */}
          <div className="bg-white border-2 border-black rounded-2xl p-3">
            <label htmlFor="name" className="block text-xs text-gray-600 mb-1">投稿者名</label>
            <input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="名前（任意）"
              className="w-full outline-none"
            />
          </div>

          {/* 送信ボタン */}
          <button
            type="submit"
            disabled={isSubmitting || !content.trim()}
            className="aspect-square rounded-2xl border-4 border-black bg-blue-500 text-white grid place-items-center text-4xl disabled:opacity-60 disabled:cursor-not-allowed"
            aria-label="送信"
            title="送信"
          >
            {/* 上矢印アイコン（依存なしのSVG） */}
            <svg viewBox="0 0 24 24" className="w-9 h-9" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 5l0 14" strokeLinecap="round" />
              <path d="M5 12l7-7 7 7" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </button>
        </div>
      </div>
    </form>
  );
}
