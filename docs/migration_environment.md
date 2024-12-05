- migrations are managed by `alembic`
- home of migration environment is in `alembic` folder
- `env.py` script is run every time alembic is invoked, it sets up db connection and invokes migration engine
- `script.py.mako` generates migration scripts
- `/versions` holds individual version scripts

