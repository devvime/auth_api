# Auth API

Duplicate the **.env.example** file and rename the copy to **.env**.

### Create a virtual environment and install the dependencies.

```bash
./install.sh
```
---

### Create migration

```bash
./migrate.sh create "add table table_name"
```

### Run migrations

```bash
./migrate.sh apply
```

### Revert the last migration.

```bash
./migrate.sh rollback
```

---

### Application flow

```bash
REQUEST → Controller → Schema(Pydantic) → UseCase → Repository → DB
                         ↑ DTO interno ↑
```