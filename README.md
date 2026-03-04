# Auth API

Duplicate the **.env.example** file and rename the copy to **.env**.

### Create a virtual environment and install the dependencies.

```bash
./pipu.sh install
```
---

### Create migration

```bash
./pipu.sh migrate create "add table table_name"
```

### Run migrations

```bash
./pipu.sh migrate apply
```

### Revert the last migration.

```bash
./pipu.sh migrate rollback
```

---

### Start dev server

```bash
./pipu.sh start
```

---

### Run with Docker

```bash
docker compose up -d
```

---

### Application flow

```bash
REQUEST → Controller → Schema(Pydantic) → UseCase → Repository → DB
                         ↑ DTO interno ↑
```