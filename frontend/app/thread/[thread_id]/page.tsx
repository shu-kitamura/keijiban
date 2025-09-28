function generateStaticParams() {}
 
export default async function Page(
    { params }: { 
        params: Promise<{ thread_id: string }>
    }
) {
    const { thread_id } = await params;
    return <h1>{thread_id}</h1>
}