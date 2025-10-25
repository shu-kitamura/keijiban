import React from "react";

type HeaderProps = {
    title: string;
};

export default function Header({ title }: HeaderProps) {
  return (
    <div className="flex justify-center bg-slate-200 p-4">
        <h1 className="text-3xl md:text-4xl font-bold tracking-tight">{title}</h1>
    </div>
  );
}