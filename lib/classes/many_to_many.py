class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title length must be between 5 and 50 characters")
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        raise AttributeError("Title is immutable and cannot be changed")


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name must be longer than 0 characters")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Author name cannot be changed")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return (
            list(set([article.magazine.category for article in self.articles()]))
            if self.articles()
            else None
        )

    @staticmethod
    def contributing_authors():
        return [author for author in Author.all if len(author.articles()) > 0]


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name length must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Magazine category must have a length greater than 0")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Magazine name must be a string")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name length must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Magazine category must be a string")
        if len(new_category) == 0:
            raise ValueError("Magazine category must have a length greater than 0")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return (
            [article.title for article in self.articles()] if self.articles() else None
        )

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None
