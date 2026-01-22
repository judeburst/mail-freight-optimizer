from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate that DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable is not set. "
        "Please create a .env file with DATABASE_URL=postgresql://user:password@localhost:5432/dbname"
    )

# Validate DATABASE_URL format (basic check)
if not DATABASE_URL.startswith(('postgresql://', 'sqlite://', 'mysql://')):
    raise ValueError(
        f"Invalid DATABASE_URL format: {DATABASE_URL}. "
        "Must start with postgresql://, sqlite://, or mysql://"
    )

# Create engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,         # Number of connections to maintain
    max_overflow=10      # Max connections beyond pool_size
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency function for FastAPI endpoints.
    Usage:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
