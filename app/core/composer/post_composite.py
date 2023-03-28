from app.core.services import PostServices
from app.core.repositories.raw_news import RawNewsRepository
from app.core.repositories.raw_response import PGRawResponseRepository
from app.core.repositories.post import PostRepository
from app.core.db import PGConnection


def post_composer() -> PostServices:
    conn = PGConnection()

    raw_response_repository = PGRawResponseRepository(conn=conn)
    raw_news_repository = RawNewsRepository()
    post_repository = PostRepository(conn=conn)

    services = PostServices(
        raw_response_repository=raw_response_repository,
        raw_news_repository=raw_news_repository,
        post_repository=post_repository,
    )
    return services
