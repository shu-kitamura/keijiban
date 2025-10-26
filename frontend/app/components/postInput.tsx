"use client"

import { ArrowUpIcon } from "lucide-react"
import { useState } from "react";

import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
import { Switch } from "@/components/ui/switch"
import { Separator } from "@/components/ui/separator"


type PostFormProps = {
    thread_id: string;
}

function sendPost(content: string, author: string, thread_id: string) {
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
          window.location.reload();
        }
    });
}

export default function PostInput({ thread_id }: PostFormProps) {
  const [content, setContent] = useState("");
  const [isAnonymous, setIsAnonymous] = useState(true);

  return (
    <div className="grid w-full max-w-sm gap-6 mb-4">
      <InputGroup>
        <InputGroupTextarea
          placeholder="ポストを入力"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <InputGroupAddon align="block-end">
          <div className="flex items-center gap-2 px-2 ml-auto">
            <InputGroupText className="ml-auto">匿名投稿</InputGroupText>
            <Switch
              defaultChecked={isAnonymous}
              onCheckedChange={setIsAnonymous}
            />
          </div>
          <Separator orientation="vertical" className="!h-4" />
          <InputGroupButton
            variant="default"
            className="rounded-full"
            size="icon-xs"
            onClick={() => { sendPost(content, isAnonymous ? "Anonymous" : "User", thread_id); }}
          >
            <ArrowUpIcon />
            <span className="sr-only">Send</span>
          </InputGroupButton>
        </InputGroupAddon>
      </InputGroup>
    </div>
  );
}
