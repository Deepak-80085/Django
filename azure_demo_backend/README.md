# Azure Demo Backend

A simple Django REST API with Azure Blob Storage integration.

## Quick Start

1. **Activate virtual environment**

   ```bash
   env\Scripts\activate
   ```

2. **Configure Azure credentials**
   Add your Azure storage details to the `.env` file:

   ```
   AZURE_ACCOUNT_NAME=your_storage_account_name
   AZURE_ACCOUNT_KEY=your_storage_account_key
   AZURE_CONTAINER=your_container_name
   ```

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start server**

   ```bash
   python manage.py runserver
   ```

5. **Access the app**
   - API: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## What's Inside

- Django REST Framework
- Azure Blob Storage for media files
- SQLite database
