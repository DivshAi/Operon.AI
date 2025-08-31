// AI Agentic Platform - Agent Detail Page
// Detailed configuration page for a specific AI agent

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { agents, mcp } from '../../lib/api';

const AgentDetailPage = () => {
  const [agent, setAgent] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    status: 'inactive',
    config: {}
  });
  
  const router = useRouter();
  const { id } = router.query;

  useEffect(() => {
    if (!id) return;

    const fetchAgent = async () => {
      try {
        setLoading(true);
        const data = await agents.getAgent(id as string);
        setAgent(data);
        setFormData({
          name: data.name,
          description: data.description || '',
          status: data.status,
          config: data.config || {}
        });
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to fetch agent');
      } finally {
        setLoading(false);
      }
    };

    fetchAgent();
  }, [id]);

  const handleSave = async () => {
    try {
      setLoading(true);
      await agents.updateAgent(id as string, formData);
      setIsEditing(false);
      
      // Refresh the agent data
      const updatedAgent = await agents.getAgent(id as string);
      setAgent(updatedAgent);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to update agent');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="container mx-auto p-4">Loading agent details...</div>;
  if (error) return <div className="container mx-auto p-4 text-red-500">{error}</div>;
  if (!agent) return <div className="container mx-auto p-4">Agent not found</div>;

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold text-gray-900">Agent Configuration</h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-gray-900">{agent.name}</h2>
            <div className="flex gap-2">
              {isEditing ? (
                <>
                  <button
                    onClick={handleSave}
                    disabled={loading}
                    className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-sm"
                  >
                    {loading ? 'Saving...' : 'Save Changes'}
                  </button>
                  <button
                    onClick={() => setIsEditing(false)}
                    className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md text-sm"
                  >
                    Cancel
                  </button>
                </>
              ) : (
                <button
                  onClick={() => setIsEditing(true)}
                  className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm"
                >
                  Edit Agent
                </button>
              )}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Basic Information */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3 pb-2 border-b border-gray-100">
                Basic Information
              </h3>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Agent Name
                  </label>
                  {isEditing ? (
                    <input
                      type="text"
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  ) : (
                    <p className="bg-gray-50 px-3 py-2 rounded-md">{agent.name}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Description
                  </label>
                  {isEditing ? (
                    <textarea
                      value={formData.description}
                      onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      rows={3}
                    />
                  ) : (
                    <p className="bg-gray-50 px-3 py-2 rounded-md">{agent.description || 'No description'}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Status
                  </label>
                  {isEditing ? (
                    <select
                      value={formData.status}
                      onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                      <option value="active">Active</option>
                      <option value="inactive">Inactive</option>
                      <option value="error">Error</option>
                    </select>
                  ) : (
                    <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-sm">
                      {agent.status}
                    </span>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Last Executed
                  </label>
                  <p className="bg-gray-50 px-3 py-2 rounded-md">
                    {agent.last_executed ? new Date(agent.last_executed).toLocaleString() : 'Never'}
                  </p>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Performance Metrics
                  </label>
                  <div className="bg-gray-50 px-3 py-2 rounded-md">
                    <ul className="space-y-1 text-sm">
                      <li><strong>Success Rate:</strong> {agent.performance_metrics?.success_rate || 'N/A'}%</li>
                      <li><strong>Avg Response Time:</strong> {agent.performance_metrics?.avg_response_time || 'N/A'}ms</li>
                      <li><strong>Requests:</strong> {agent.performance_metrics?.total_requests || 'N/A'}</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            {/* Configuration */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3 pb-2 border-b border-gray-100">
                Configuration
              </h3>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    JSON Configuration
                  </label>
                  {isEditing ? (
                    <textarea
                      value={JSON.stringify(formData.config, null, 2)}
                      onChange={(e) => {
                        try {
                          const parsed = JSON.parse(e.target.value);
                          setFormData({ ...formData, config: parsed });
                        } catch (err) {
                          // Invalid JSON, keep the last valid value
                        }
                      }}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      rows={8}
                    />
                  ) : (
                    <pre className="bg-gray-50 p-3 rounded-md text-sm overflow-x-auto">
                      {JSON.stringify(agent.config, null, 2) || '{}'}
                    </pre>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    MCP Tools Connected
                  </label>
                  <div className="bg-gray-50 px-3 py-2 rounded-md">
                    {agent.mcp_tools && agent.mcp_tools.length > 0 ? (
                      <ul className="space-y-1 text-sm">
                        {agent.mcp_tools.map((tool: string) => (
                          <li key={tool} className="flex items-center">
                            <span className="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                            {tool}
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <p className="text-sm text-gray-500">No MCP tools connected</p>
                    )}
                  </div>
                </div>

                <button
                  onClick={() => router.push('/dashboard')}
                  className="mt-4 bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md text-sm"
                >
                  Back to Dashboard
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default AgentDetailPage;