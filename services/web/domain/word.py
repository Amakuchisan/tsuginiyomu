import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, TIMESTAMP, Text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import current_timestamp
from db.setting import Base
from db.setting import ENGINE


class Word(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'word'
    id = Column('id', BIGINT(unsigned=True), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column('name', Text, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False,
                        server_default=current_timestamp())
    updated_at = Column('updated_at', TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    deleted_at = Column('deleted_at', TIMESTAMP)

    article_word = relationship("Article_Word", back_populates="word")


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
