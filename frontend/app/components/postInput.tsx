import {memo} from "react";


export default memo( function PostForm() {
    return (
        <form action="" method="post" className="p-4 w-full max-w-xl mx-auto">
            <input name="content" className="w-full h-24 border-2 border-black rounded-md p-2" placeholder="Write your post..."></input>
            <button type="submit" className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">
                ↑
            </button>
         </form>
    )
})