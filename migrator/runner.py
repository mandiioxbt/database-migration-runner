import os

class MigrationRunner:
    def __init__(self, db_url): self.db_url, self.applied = db_url, set()
    def migrate(self, path):
        for m in self.pending(path):
            self.apply(path, m); self.applied.add(m)
    def pending(self, path):
        if not os.path.exists(path): return []
        return sorted(f for f in os.listdir(path) if f.endswith(".sql") and f not in self.applied)
    def apply(self, path, m):
        with open(f"{path}/{m}") as f: sql = f.read()
    def rollback(self, steps=1): pass
