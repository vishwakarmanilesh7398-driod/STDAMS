import os
import random
from datetime import datetime, timedelta

# User Configuration
email = "vishwakarmanilesh7398@gmail.com"
username = "vishwakarmanilesh7398-driod"
days_to_backdate = 365 

os.system(f'git config user.email "{email}"')
os.system(f'git config user.name "{username}"')

def start_committing():
    # Ek dummy file banate hain
    open('data.txt', 'a').close()
    
    for i in range(days_to_backdate, -1, -1):
        date = datetime.now() - timedelta(days=i)
        
        # 30% chance skip (Real look ke liye)
        if random.random() < 0.30:
            continue
            
        # Random commits (kabhi 1, kabhi 15)
        commit_count = random.randint(1, 15) if random.random() < 0.15 else random.randint(1, 4)

        for _ in range(commit_count):
            h, m, s = random.randint(9, 21), random.randint(0, 59), random.randint(0, 59)
            commit_date = date.replace(hour=h, minute=m, second=s).strftime('%Y-%m-%d %H:%M:%S')
            
            with open('data.txt', 'a') as f:
                f.write(f'Update: {commit_date}\n')
            
            # Windows command
            cmd = f'set GIT_AUTHOR_DATE="{commit_date}" && set GIT_COMMITTER_DATE="{commit_date}" && git add data.txt && git commit -m "refactor: optimize data structures"'
            os.system(cmd)

    print("\n[DONE] Ab 'git push origin master' (ya main) type karein.")

if __name__ == "__main__":
    start_committing()