# Database Migration Runner

Zero-downtime database migration runner with rollback support.

## Features
- Forward and rollback migrations
- Online schema changes (no table locks)
- Migration history and audit log
- Supports PostgreSQL, MySQL, SQLite

## CLI
```bash
migrate create add_users_table
migrate up --steps 1
migrate down --steps 1
```

## License: MIT
