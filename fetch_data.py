from supabase import create_client
import os
import json

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase = create_client(url, key)

# 🔁 Ändra detta till din tabell
data = supabase.table("utstallningar").select("*").execute().data

# 💾 Spara till JSON-fil
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
