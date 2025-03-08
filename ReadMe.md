# InsuraChain

InsuraChain is a blockchain-powered insurance management system designed to enhance transparency, efficiency, and security in the insurance sector. It enables users to register policies, submit claims, and track claim statuses while maintaining an immutable audit trail for all transactions.

## Features
- **Policy Management**: Users can create, update, and view insurance policies.
- **Claims Processing**: Users can submit and track their insurance claims.
- **Audit Logs**: Maintains a record of actions for transparency.
- **User Authentication**: Secure authentication using Django's built-in authentication.
- **Admin Dashboard**: Admins can manage policies, claims, and users.

## Tech Stack
- **Backend**: Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: Django Authentication
- **Blockchain Integration**: Future integration planned

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Virtualenv

### Steps to Run Locally
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/insurachain.git
   cd insurachain
   ```
2. **Create and activate a virtual environment**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser** (for admin access)
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login

### Policies
- `GET /api/policies/` - List all policies
- `POST /api/policies/` - Create a new policy
- `GET /api/policies/{id}/` - Retrieve policy details
- `PUT /api/policies/{id}/` - Update a policy
- `DELETE /api/policies/{id}/` - Delete a policy

### Claims
- `GET /api/claims/` - List all claims
- `POST /api/claims/` - Submit a new claim
- `GET /api/claims/{id}/` - Retrieve claim details
- `PUT /api/claims/{id}/` - Update claim status

### Audit Logs
- `GET /api/audits/` - Retrieve audit logs

## Contributing
We welcome contributions! To contribute:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to GitHub: `git push origin feature-name`
5. Open a Pull Request

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, reach out via [ondeyostephen0@gmail.com](mailto:email@example.com) or open an issue in the repository.

