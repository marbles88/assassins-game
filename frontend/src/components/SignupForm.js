import React, { useState } from 'react';

function SignupForm() {
    const [name, setName] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    // Async function that fetches from server
    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('');
        setError('');

        console.log('Submitting form...')
        try {
            console.log('Sending request to server...')
            const response = await fetch('http://localhost:5000', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, username, password }),
            });

            console.log('Response received:', response.status);
            const data = await response.json();
            console.log('Response data:', data);

            if (response.status === 201) {
                setMessage(data.message);
                // Clear form fields on success
                setName('');
                setUsername('');
                setPassword('');
            } else if (response.status === 400) {
                setError(data.error);
            } else if (response.status === 500) {
                setError('An unexpected error occurred. Please try again.');
            } else {
                setError('Failed to register user. Please try again.');
            }
        } catch (error) {
            setError('Network error. Please check your connection and try again.');
        }
    };

    return (
        <div>
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Name:</label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Sign Up</button>
            </form>
            {message && <p className="success-message">{message}</p>}
            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default SignupForm;