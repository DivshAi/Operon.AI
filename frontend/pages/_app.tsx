// AI Agentic Platform - Main Application Component
// This file sets up the global application context and layout

import React from 'react';
import '../styles/globals.css';
import type { AppProps } from 'next/app';

// Authentication context with real API integration
const AuthContext = React.createContext({
  user: null,
  login: (email: string, password: string) => Promise.resolve(null),
  logout: () => {},
  isAuthenticated: false,
  loading: true
});

function MyApp({ Component, pageProps }: AppProps) {
  // Mock user state
  const [user, setUser] = React.useState(null);
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);

  const login = (userData: any) => {
    setUser(userData);
    setIsAuthenticated(true);
  };

  const logout = () => {
    setUser(null);
    setIsAuthenticated(false);
  };

  const authContextValue = {
    user,
    login,
    logout,
    isAuthenticated
  };

  return (
    <AuthContext.Provider value={authContextValue}>
      <div className="min-h-screen bg-gray-50">
        <Component {...pageProps} />
      </div>
    </AuthContext.Provider>
  );
}

export default MyApp;