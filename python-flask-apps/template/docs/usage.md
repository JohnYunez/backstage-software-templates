# Usage

## Running Locally

1. Install dependencies:
    ```bash
    pip install flask
    ```
2. Run the app:
    ```bash
    python app.py
    ```
3. Access endpoints:
    - /api/v1/${{values.api_path}}
    - /api/v1/healthz

## Environment Variables

- `INFRA_DATA`: Optional. Used to inject infrastructure-related data into the `/api/v1/${{values.api_path}}` response.
- `APP_ENV`: Optional. Used to inject application data into the `/api/v1/${{values.api_path}}` response.
