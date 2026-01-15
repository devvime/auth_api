# Auth API

Duplique o arquivo **.env.example** e renomeie a cópia para **.env**.

### Criar ambiente virtual e instalar as dependências

```bash
./install.sh
```
---

### Criar migration

```bash
./migrate.sh create "add table table_name"
```

### Executar migrations

```bash
./migrate.sh apply
```

### Executar rollback da última migration

```bash
./migrate.sh rollback
```

---

### Flow da aplicação

```bash
REQUEST → Controller → Schema(Pydantic) → Service → UseCase → Repository → DB
                         ↑ DTO interno ↑
```

### Estrutura do projeto

```bash
app/
│
├── api/
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── auth_controller.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── auth_service.py
├── core/
│   ├── security.py
│
├── domain/
│   ├── user/
│   │   ├── use_cases/
│   │   │   ├── create_user.py
│   │   │   ├── update_user.py
│   │   ├── schemas/
│   │   │   ├── user_schema.py
│   │   │   ├── create_user_schema.py
│
├── infrastructure/
│   ├── database/
│   │   ├── connection.py
│   │   ├── session.py
│   │   ├── models.py
│   ├── datarepositoriesbase/
│   │   ├── user_repository.py
│
├── main.py
```