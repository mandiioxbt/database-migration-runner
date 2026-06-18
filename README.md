# Database Migration Runner

Zero-downtime database migration runner with rollback.

## Features
- Forward and rollback migrations
- Online schema changes (no locks)
- Migration history and audit log
- Supports PostgreSQL, MySQL, SQLite

## CLI
```bash
migrate create add_users_table
migrate up
migrate down --steps 1
```

## License
MIT
