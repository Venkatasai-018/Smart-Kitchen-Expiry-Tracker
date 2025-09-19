import os
from supabase import create_client, Client
url: str = "https://pwcwnhapcvgljrvfuztm.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB3Y3duaGFwY3ZnbGpydmZ1enRtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc5NTc1MDEsImV4cCI6MjA3MzUzMzUwMX0.kXFUV4NZwlJbu1SmObRacuPJRk77CGYBUcSkzCZR16g"
supabase: Client = create_client(url, key)


