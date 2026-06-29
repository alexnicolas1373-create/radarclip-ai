from app.database import Base, engine


def test_database_metadata():
    assert 'trends' in [table.name for table in Base.metadata.sorted_tables]
    assert engine is not None
