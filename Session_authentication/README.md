What is Session Authentication?

Session authentication is a method used to verify a user's identity across multiple requests after they've logged in, without requiring the user to re-enter their credentials on each request.

🧩 How It Works — Step-by-Step
User logs in by submitting their credentials (email + password) to an authentication endpoint.

Server verifies the credentials and creates a session, which is:

A unique identifier (like a session_id).

Typically stored server-side in memory, a database, or a file.

The server sends a cookie back to the client:

http
Copy
Edit
Set-Cookie: session_id=abc123; Path=/; HttpOnly
On every future request, the client automatically includes the cookie:

http
Copy
Edit
Cookie: session_id=abc123
The server reads the session ID, looks it up, and retrieves the associated user.

🛠️ In Practical Terms
Session ID is stored in the browser and sent with every request.

Session data (like who the user is) is stored on the server.

Once the session expires or is deleted (e.g. logout), the session is no longer valid.

🔐 Comparison with Basic Authentication
Feature Basic Authentication Session Authentication
Credentials sent? On every request Only on login
Secure over HTTPS? Yes Yes
Stores state? No (stateless) Yes (session-based)
Use case APIs, CLI tools Websites, interactive UIs
