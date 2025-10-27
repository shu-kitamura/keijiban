"use client";

import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function handleSubmit(event: React.FormEvent<HTMLFormElement>, router: ReturnType<typeof useRouter>) {
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
            res.json().then(data => router.push(`/thread/${data.id}`));
        }
    });
}

export default function Page() {
    const router = useRouter();
    return (
        <div className="w-full max-w-sm">
            <Card>
                <CardHeader>
                    <CardTitle>Create Thread</CardTitle>
                    <CardDescription>
                        Enter your title below to create a new thread
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    
                    <form onSubmit={(event) => handleSubmit(event, router)} method="post">
                        <div className="mb-2">
                            <Label htmlFor="title" className="mb-2">Title</Label>
                            <Input name="title" placeholder="Title" />
                        </div>
                        <div className="mb-2">
                            <Label htmlFor="description" className="mb-2">Description</Label>
                            <Input name="description" placeholder="Description" />
                        </div>
                        <Button type="submit" className="mt-4 w-full">Create</Button>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}