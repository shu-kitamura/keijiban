import React from "react";

type PostCardProps = {
  content: string;
  author: string;
  created_at: string;
};

export default function PostCard({ content, author, created_at }: PostCardProps) {
  return (
    <div className="bg-white border-2 border-black rounded-xl p-4 w-full max-w-xl mx-auto">
      <div className="mb-4 text-lg text-gray-800">
        {content}
      </div>
      <div className="flex justify-between items-center text-sm text-gray-600">
        <p>{author}</p>
        <p>{created_at}</p>
      </div>
    </div>
  );
}
