from app.core.services import NewsServices
from app.core.repositories.news import NewsRepository
from app.core.repositories.raw_news import RawNewsRepository
from app.core.repositories.post import PostRepository
from app.core.db import PGConnection


def news_composer() -> NewsServices:
    conn = PGConnection()
    news_repo = NewsRepository(conn=conn)
    raw_news_repo = RawNewsRepository()
    post_repo = PostRepository(conn=conn)

    services = NewsServices(
        news_repository=news_repo,
        post_repository=post_repo,
        raw_news_repository=raw_news_repo,
    )
    return services
