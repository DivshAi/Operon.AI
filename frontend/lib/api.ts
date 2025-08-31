// AI Agentic Platform - API Client
// Axios instance with JWT interceptor and error handling

import axios from 'axios';
import { useRouter } from 'next/router';

// Create Axios instance with base URL
const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// JWT interceptor - add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor - handle errors globally
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle unauthorized errors (401) - redirect to login
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      // In a real app, we would use Next.js router here
      console.log('Unauthorized - redirecting to login');
    }
    
    // Handle forbidden errors (403)
    if (error.response?.status === 403) {
      console.log('Forbidden - insufficient permissions');
    }
    
    return Promise.reject(error);
  }
);

// Auth endpoints
export const auth = {
  login: async (email: string, password: string) => {
    const response = await api.post('/auth/login', { email, password });
    return response.data;
  },
  
  register: async (email: string, password: string, full_name: string, user_persona: string) => {
    const response = await api.post('/auth/register', { 
      email, 
      password, 
      full_name,
      user_persona 
    });
    return response.data;
  },
  
  getCurrentUser: async () => {
    const token = localStorage.getItem('authToken');
    if (!token) return null;
    
    try {
      const response = await api.get('/auth/me'); // Note: This endpoint doesn't exist yet in backend
      return response.data;
    } catch (error) {
      localStorage.removeItem('authToken');
      return null;
    }
  },
  
  logout: () => {
    localStorage.removeItem('authToken');
  }
};

// Agents endpoints
export const agents = {
  getAgents: async () => {
    const response = await api.get('/agents');
    return response.data;
  },
  
  getAgent: async (agentId: string) => {
    const response = await api.get(`/agents/${agentId}`);
    return response.data;
  },
  
  createAgent: async (agentData: any) => {
    const response = await api.post('/agents', agentData);
    return response.data;
  },
  
  updateAgent: async (agentId: string, agentData: any) => {
    const response = await api.put(`/agents/${agentId}`, agentData);
    return response.data;
  },
  
  deleteAgent: async (agentId: string) => {
    const response = await api.delete(`/agents/${agentId}`);
    return response.data;
  }
};

// Teams endpoints
export const teams = {
  getTeams: async () => {
    const response = await api.get('/teams');
    return response.data;
  },
  
  getTeam: async (teamId: string) => {
    const response = await api.get(`/teams/${teamId}`);
    return response.data;
  },
  
  createTeam: async (teamData: any) => {
    const response = await api.post('/teams', teamData);
    return response.data;
  },
  
  updateTeam: async (teamId: string, teamData: any) => {
    const response = await api.put(`/teams/${teamId}`, teamData);
    return response.data;
  },
  
  deleteTeam: async (teamId: string) => {
    const response = await api.delete(`/teams/${teamId}`);
    return response.data;
  }
};

// Prompts endpoints
export const prompts = {
  getPrompts: async () => {
    const response = await api.get('/prompts');
    return response.data;
  },
  
  getPrompt: async (promptId: string) => {
    const response = await api.get(`/prompts/${promptId}`);
    return response.data;
  },
  
  createPrompt: async (promptData: any) => {
    const response = await api.post('/prompts', promptData);
    return response.data;
  },
  
  updatePrompt: async (promptId: string, promptData: any) => {
    const response = await api.put(`/prompts/${promptId}`, promptData);
    return response.data;
  },
  
  deletePrompt: async (promptId: string) => {
    const response = await api.delete(`/prompts/${promptId}`);
    return response.data;
  },
  
  getPromptVersions: async (promptId: string) => {
    const response = await api.get(`/prompts/${promptId}/versions`);
    return response.data;
  }
};

// MCP endpoints
export const mcp = {
  getConnections: async () => {
    const response = await api.get('/mcp/connections');
    return response.data;
  },
  
  createConnection: async (connectionData: any) => {
    const response = await api.post('/mcp/connections', connectionData);
    return response.data;
  },
  
  connectToServer: async (connectionName: string) => {
    const response = await api.post(`/mcp/connections/${connectionName}/connect`);
    return response.data;
  },
  
  getTools: async () => {
    const response = await api.get('/mcp/tools');
    return response.data;
  }
};

export default api;