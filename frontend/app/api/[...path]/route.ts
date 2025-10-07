// app/api/[...path]/route.ts
import { NextRequest } from "next/server";

const backendOrigin = process.env.BACKEND_ORIGIN;

export async function GET(req: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params;
  const url = `${backendOrigin}/api/v1/${path.join("/")}${req.nextUrl.search}`;
  const res = await fetch(url, { method: "GET" });
  return new Response(await res.text(), { status: res.status, headers: res.headers });
}

export async function POST(req: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params;
  const url = `${backendOrigin}/api/v1/${path.join("/")}`;
  const body = await req.text();
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": req.headers.get("content-type") ?? "application/json" },
    body,
  });
  return new Response(await res.text(), { status: res.status, headers: res.headers });
}
