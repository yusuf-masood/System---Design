import asyncpg
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection details
SOURCE_DB = {
    "user": "source_user",
    "password": "source_pass",
    "database": "source_db",
    "host": "localhost",
    "port": "5433",
}

DEST_DB = {
    "user": "dest_user",
    "password": "dest_pass",
    "database": "destination_db",
    "host": "localhost",
    "port": "5434",
}


async def fetch_data():
    """Fetch recommendation data from source DB."""
    conn = await asyncpg.connect(**SOURCE_DB)
    rows = await conn.fetch("SELECT * FROM recommendation;")
    await conn.close()
    return rows

async def insert_data(rows):
    """Insert recommendation data into destination DB."""
    conn = await asyncpg.connect(**DEST_DB)
    async with conn.transaction():
        for row in rows:
            await conn.execute(
                "INSERT INTO recommendation (customer_id, product_id, score) VALUES ($1, $2, $3) ON CONFLICT DO NOTHING;",
                row["customer_id"], row["product_id"], row["score"]
            )
    await conn.close()

async def validate_transfer():
    """Validate data transfer by comparing row counts."""
    source_conn = await asyncpg.connect(**SOURCE_DB)
    dest_conn = await asyncpg.connect(**DEST_DB)
    
    source_count = await source_conn.fetchval("SELECT COUNT(*) FROM recommendation;")
    dest_count = await dest_conn.fetchval("SELECT COUNT(*) FROM recommendation;")
    
    await source_conn.close()
    await dest_conn.close()
    
    print(f"Source count: {source_count}, Destination count: {dest_count}")
    assert source_count == dest_count, "Data transfer incomplete!"
    print("Data transfer validated successfully.")

async def main():
    data = await fetch_data()
    await insert_data(data)
    await validate_transfer()

if __name__ == "__main__":
    asyncio.run(main())
