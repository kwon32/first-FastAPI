from typing import List, Optional

from schemas import Post, PostCreate


class PostRepository:
    def __init__(self):
        self._posts: List[Post] = []
        self._next_id = 1

    def list(self) -> List[Post]:
        return self._posts

    def get(self, post_id: int) -> Optional[Post]:
        for post in self._posts:
            if post.id == post_id:
                return post
        return None

    def create(self, payload: PostCreate) -> Post:
        post = Post(id=self._next_id, title=payload.title, content=payload.content)
        self._posts.append(post)
        self._next_id += 1
        return post

    def update(self, post_id: int, payload: PostCreate) -> Optional[Post]:
        for idx, post in enumerate(self._posts):
            if post.id == post_id:
                updated = Post(id=post_id, title=payload.title, content=payload.content)
                self._posts[idx] = updated
                return updated
        return None

    def delete(self, post_id: int) -> bool:
        for idx, post in enumerate(self._posts):
            if post.id == post_id:
                del self._posts[idx]
                return True
        return False
