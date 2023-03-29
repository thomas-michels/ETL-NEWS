from app.core.repositories.raw_news import RawNewsRepository
from app.core.repositories.post import PostRepository
from app.core.repositories.news import NewsRepository
from app.core.entities import News
from bs4 import BeautifulSoup


class NewsServices:
    def __init__(
        self,
        raw_news_repository: RawNewsRepository,
        post_repository: PostRepository,
        news_repository: NewsRepository,
    ) -> None:
        self.__raw_news_repository = raw_news_repository
        self.__post_repository = post_repository
        self.__news_repository = news_repository

    def extract_raw_news(self, post_id: int) -> bool:
        post = self.__post_repository.get_post_by_id(post_id=post_id)

        if post:
            raw_news = self.__raw_news_repository.get_news(post.link)

            soup = BeautifulSoup(raw_news.data["html"], "html.parser")

            title = soup.find("meta", attrs={"property": "og:title"})["content"]
            description = soup.find("meta", attrs={"property": "og:description"})[
                "content"
            ]
            author = soup.find("meta", attrs={"name": "author"})
            author = author["content"] if author else ""
            date_published = soup.find(
                "meta", attrs={"property": "article:published_time"}
            )
            date_published = date_published["content"] if date_published else None

            news = News(
                title=title,
                description=description,
                link=raw_news.link,
                author=author,
                inserted_at=date_published,
            )

            news_id = self.__news_repository.insert(news=news)
            self.__news_repository.connection.commit()
            return news_id
