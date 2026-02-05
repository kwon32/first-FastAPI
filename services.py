from typing import List

from repositories import PostRepository
from schemas import Post, PostCreate


class PostService:
    def __init__(self, repo: PostRepository):
        self._repo = repo

    def list_posts(self) -> List[Post]:
        return self._repo.list()

    def get_post(self, post_id: int) -> Post | None:
        return self._repo.get(post_id)

    def create_post(self, payload: PostCreate) -> Post:
        return self._repo.create(payload)

    def update_post(self, post_id: int, payload: PostCreate) -> Post | None:
        return self._repo.update(post_id, payload)

    def delete_post(self, post_id: int) -> bool:
        return self._repo.delete(post_id)
