export type Thread = {
  id: string;
  title: string;
  description: string;
  owner: string;
  created_at: string;
  updated_at: string;
};

export type Post = {
  id: string;
  thread_id: string;
  content: string;
  author: string;
  created_at: string;
};