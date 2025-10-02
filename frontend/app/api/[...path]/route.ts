// app/api/[...path]/route.ts
import { NextRequest } from "next/server";

export async function GET(req: NextRequest, { params }: { params: { path: string[] } }) {
  const url = `http://backend:8000/api/v1/${params.path.join("/")}${req.nextUrl.search}`;
  const res = await fetch(url, { method: "GET" });
  return new Response(await res.text(), { status: res.status, headers: res.headers });
}

export async function POST(req: NextRequest, { params }: { params: { path: string[] } }) {
  const url = `http://backend:8000/api/v1/${params.path.join("/")}`;
  const body = await req.text();
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": req.headers.get("content-type") ?? "application/json" },
    body,
  });
  return new Response(await res.text(), { status: res.status, headers: res.headers });
}
