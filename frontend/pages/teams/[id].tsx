// AI Agentic Platform - Team Detail Page
// Detailed configuration page for a specific agent team

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { teams, agents } from '../../lib/api';

const TeamDetailPage = () => {
  const [team, setTeam] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    orchestration_rules: {}
  });
  
  const router = useRouter();
  const { id } = router.query;

  useEffect(() => {
    if (!id) return;

    const fetchTeam = async () => {
      try {
        setLoading(true);
        const data = await teams.getTeam(id as string);
        setTeam(data);
        setFormData({
          name: data.name,
          description: data.description || '',
          orchestration_rules: data.orchestration_rules || {}
        });
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to fetch team');
      } finally {
        setLoading(false);
      }
    };

    fetchTeam();
  }, [id]);

  const handleSave = async () => {
    try {
      setLoading(true);
      await teams.updateTeam(id as string, formData);
      setIsEditing(false);
      
      // Refresh the team data
      const updatedTeam = await teams.getTeam(id as string);
      setTeam(updatedTeam);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to update team');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="container mx-auto p-4">Loading team details...</div>;
  if (error) return <div className="container mx-auto p-4 text-red-500">{error}</div>;
  if (!team) return <div className="container mx-auto p-4">Team not found</div>;

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold text-gray-900">Team Configuration</h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-gray-900">{team.name}</h2>
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
                  Edit Team
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
                    Team Name
                  </label>
                  {isEditing ? (
                    <input
                      type="text"
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  ) : (
                    <p className="bg-gray-50 px-3 py-2 rounded-md">{team.name}</p>
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
                    <p className="bg-gray-50 px-3 py-2 rounded-md">{team.description || 'No description'}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Team Members (Agents)
                  </label>
                  <div className="bg-gray-50 px-3 py-2 rounded-md">
                    {team.members && team.members.length > 0 ? (
                      <ul className="space-y-1 text-sm">
                        {team.members.map((member: string) => (
                          <li key={member} className="flex items-center">
                            <span className="w-2 h-2 bg-blue-500 rounded-full mr-2"></span>
                            {member}
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <p className="text-sm text-gray-500">No agents in this team</p>
                    )}
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Workflow Status
                  </label>
                  <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-sm">
                    {team.workflow_status || 'Idle'}
                  </span>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Last Workflow Execution
                  </label>
                  <p className="bg-gray-50 px-3 py-2 rounded-md">
                    {team.last_workflow_execution ? new Date(team.last_workflow_execution).toLocaleString() : 'Never'}
                  </p>
                </div>
              </div>
            </div>

            {/* Configuration */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-3 pb-2 border-b border-gray-100">
                Orchestration Configuration
              </h3>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Orchestration Rules (JSON)
                  </label>
                  {isEditing ? (
                    <textarea
                      value={JSON.stringify(formData.orchestration_rules, null, 2)}
                      onChange={(e) => {
                        try {
                          const parsed = JSON.parse(e.target.value);
                          setFormData({ ...formData, orchestration_rules: parsed });
                        } catch (err) {
                          // Invalid JSON, keep the last valid value
                        }
                      }}
                      className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                      rows={8}
                    />
                  ) : (
                    <pre className="bg-gray-50 p-3 rounded-md text-sm overflow-x-auto">
                      {JSON.stringify(team.orchestration_rules, null, 2) || '{}'}
                    </pre>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Team Performance
                  </label>
                  <div className="bg-gray-50 px-3 py-2 rounded-md">
                    <ul className="space-y-1 text-sm">
                      <li><strong>Total Workflows:</strong> {team.performance_metrics?.total_workflows || 'N/A'}</li>
                      <li><strong>Avg Workflow Time:</strong> {team.performance_metrics?.avg_workflow_time || 'N/A'}s</li>
                      <li><strong>Success Rate:</strong> {team.performance_metrics?.success_rate || 'N/A'}%</li>
                    </ul>
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

export default TeamDetailPage;