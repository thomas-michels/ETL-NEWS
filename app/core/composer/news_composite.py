from app.core.services import NewsServices
from app.core.repositories.news import NewsRepository
from app.core.repositories.raw_response import PGRawResponseRepository
from app.core.repositories.post import PostRepository
from app.core.db import PGConnection


def news_composer() -> NewsServices:
    conn = PGConnection()

    raw_response_repository = PGRawResponseRepository(conn=conn)
    news_repository = NewsRepository()
    post_repository = PostRepository(conn=conn)

    services = NewsServices(
        raw_response_repository=raw_response_repository,
        news_repository=news_repository,
        post_repository=post_repository,
    )
    return services
