# Tuesday, October 6, 2026: Week 1, Block 1

## What I did
- Created the backend-journey repo and practiced the Git cycle: status, add, commit, push
- Practiced HTTP by hand with curl: GET, POST, PUT, DELETE, and a 404
- get_post.py: GET requests with requests, status code check
- safe_get.py: fetch_post with try/except and timeout, returns (data, error)
- post_client.py: PostClient class with get_post and get_posts_count methods

## Main lessons
- A function returns the result, the calling code decides what to print
- Put in try only the code that can fail (the request itself)
- Always set timeout in requests.get
- Check the status code before calling .json()

## Mistakes I made
- Activate the venv with `source .venv/Scripts/activate`, not by running the file
- Forgot the f before the string: the error showed {self.base_url} as text
- Request was outside try, so except did not catch it
- len(response.status_code) instead of len(response.json())
- Copied a block and forgot to rename post to post2

## To repeat
- Thursday: write PostClient from scratch, without hints
- Thursday: 4 curl requests from memory (GET, 404, POST, DELETE)