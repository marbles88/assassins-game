import React from 'react';
import SignupForm from './components/SignupForm';
import './App.css'; // Assuming you have some styles defined here

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Assassins</h1>
      </header>
      <main className="App-main">
        <section className="signup-section">
          <SignupForm />
        </section>
      </main>
      <footer className="App-footer">
        <p>&copy; 2023 Assassins Game. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;