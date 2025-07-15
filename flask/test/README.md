# Simple Flask Application

This is a basic Flask web application with two routes:
- Home page (`/`)
- About page (`/about`)

## Setup

1. Make sure you have Flask installed. The application is using the virtual environment in the `env` directory.

2. Activate the virtual environment:
   ```
   # Windows
   env\Scripts\activate
   ```

3. Run the application:
   ```
   python app.py
   ```
   
   Or using the Flask command:
   ```
   flask --app app run
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Project Structure

- `app.py`: The main Flask application file
- `templates/`: Directory containing HTML templates
  - `index.html`: Home page template
  - `about.html`: About page template
