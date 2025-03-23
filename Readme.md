Here’s a simple and human-friendly **README.md**:  

```md
# 📦 PostgreSQL Data Transfer

This project moves a `recommendation` table from one PostgreSQL database to another using **Docker, asyncpg, and Python**.  

## 🚀 How to Run

1. **Clone the repo & go to the project folder**  
   ```sh
   git clone <your-repo-url> && cd <your-project-folder>
   ```

2. **Start the databases (make sure Docker is installed)**  
   ```sh
   docker-compose up -d
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the script**  
   ```sh
   python main.py
   ```

   If everything works, you’ll see:  
   ```
   Source count: X, Destination count: X
   Data transfer validated successfully.
   ```

## 📂 What's Inside?

- `docker-compose.yml` → Sets up two PostgreSQL databases.  
- `main.py` → Transfers the data.  
- `.env` (optional) → Stores database credentials.  

## 🛠 Need Help?  
If you run into issues, check your `.env` file or database settings.  
Happy coding! 🚀  