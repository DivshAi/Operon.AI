// AI Agentic Platform - New Team Creation Page
// Allows users to create new agent teams with orchestration rules

import React, { useState } from 'react';
import { useRouter } from 'next/router';
import { teams } from '../../lib/api';

const NewTeamPage = () => {
  const router = useRouter();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    agent_ids: [],
    orchestration_rules: '',
    workflow_status: 'active'
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleAgentSelection = (agentId: string) => {
    // In a real implementation, this would show a modal with available agents
    // For now, we'll just log it as a placeholder
    console.log(`Agent selected: ${agentId}`);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.name.trim()) {
      setError('Team name is required');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      
      // In a real implementation, we would call the API to create the team
      // const response = await teams.createTeam(formData);
      
      // For demo purposes, we'll just simulate success
      setSuccess(true);
      setTimeout(() => {
        router.push('/teams');
      }, 1500);

    } catch (err) {
      setError('Failed to create team. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-gray-900">Create New Team</h1>
          <button
            onClick={() => router.push('/teams')}
            className="text-gray-600 hover:text-gray-900 font-medium"
          >
            Cancel
          </button>
        </div>
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        {success && (
          <div className="mb-6 bg-green-100 border-l-4 border-green-500 p-4">
            <p className="text-green-700">Team created successfully! Redirecting to teams dashboard...</p>
          </div>
        )}

        {error && (
          <div className="mb-6 bg-red-100 border-l-4 border-red-500 p-4">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-md p-6 space-y-6">
          <div>
            <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
              Team Name <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleInputChange}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter a name for your team"
              required
            />
          </div>

          <div>
            <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              rows={3}
              placeholder="Describe what this team does..."
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Team Members (Agents) <span className="text-red-500">*</span>
            </label>
            <div className="bg-gray-50 p-4 rounded-md border border-gray-200">
              <p className="text-sm text-gray-600 mb-3">Select agents to include in this team</p>
              <button
                type="button"
                onClick={() => handleAgentSelection('demo-agent-1')}
                className="w-full bg-blue-50 hover:text-blue-600 text-gray-700 py-2 px-4 rounded-md text-left flex justify-between items-center"
              >
                <span>Add Agent</span>
                <svg className="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </button>
              
              <div className="mt-4 space-y-2">
                {/* In a real implementation, these would be dynamically added based on selection */}
                <div className="flex items-center justify-between bg-gray-100 p-2 rounded">
                  <span className="text-sm text-gray-700">Research Assistant</span>
                  <button className="text-gray-400 hover:text-red-500">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div>
            <label htmlFor="orchestration_rules" className="block text-sm font-medium text-gray-700 mb-1">
              Orchestration Rules
            </label>
            <textarea
              id="orchestration_rules"
              name="orchestration_rules"
              value={formData.orchestration_rules}
              onChange={handleInputChange}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              rows={4}
              placeholder="Define how agents should collaborate (e.g., 'Agent A processes first, then Agent B reviews')"
            />
          </div>

          <div>
            <label htmlFor="workflow_status" className="block text-sm font-medium text-gray-700 mb-1">
              Initial Workflow Status
            </label>
            <select
              id="workflow_status"
              name="workflow_status"
              value={formData.workflow_status}
              onChange={handleInputChange}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="active">Active</option>
              <option value="paused">Paused</option>
              <option value="idle">Idle</option>
            </select>
          </div>

          <div className="pt-4 flex justify-end space-x-3">
            <button
              type="button"
              onClick={() => router.push('/teams')}
              className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md transition-colors disabled:opacity-50"
            >
              {loading ? 'Creating...' : 'Create Team'}
            </button>
          </div>
        </form>
      </main>
    </div>
  );
};

export default NewTeamPage;