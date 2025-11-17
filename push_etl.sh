#!/bin/zsh

# 2️⃣ Replace Twilio secret in the code with environment variables


# 3️⃣ Initialize Git repo if not already
git init

# 4️⃣ Stage all files
git add .

# 5️⃣ Commit files
git commit -m "Initial commit: ETL project without secrets"

# 6️⃣ Add GitHub remote (replace with your SSH URL)
git remote add origin git@github.com:Supraja1914/End-to-End-PySpark-ETL-Pipeline.git

# 7️⃣ Ensure branch is main
git branch -M main

# 8️⃣ Push to GitHub
git push -u origin main

