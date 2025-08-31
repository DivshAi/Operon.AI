// AI Agentic Platform - Dashboard Page
// Main dashboard showing overview of agents, teams, and prompts

import React from 'react';

const DashboardPage = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-gray-900">AI Agentic Platform</h1>
          <div className="flex items-center space-x-4">
            <span className="text-gray-700">Welcome, User</span>
            <button className="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded">
              Logout
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        {/* Stats Overview */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Total Agents</h3>
            <p className="text-3xl font-bold mt-2">12</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Active Teams</h3>
            <p className="text-3xl font-bold mt-2">5</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-lg font-medium text-gray-900">Prompts</h3>
            <p className="text-3xl font-bold mt-2">42</p>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="bg-white p-6 rounded-lg shadow mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Quick Actions</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
            <button className="bg-blue-500 hover:bg-blue-700 text-white py-3 px-4 rounded">
              Create Agent
            </button>
            <button className="bg-green-500 hover:bg-green-700 text-white py-3 px-4 rounded">
              Create Team
            </button>
            <button className="bg-purple-500 hover:bg-purple-700 text-white py-3 px-4 rounded">
              Add Prompt
            </button>
            <button className="bg-yellow-500 hover:bg-yellow-700 text-white py-3 px-4 rounded">
              View Analytics
            </button>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Recent Agents</h2>
            <ul className="space-y-2">
              <li className="flex justify-between border-b pb-2">
                <span>Research Assistant</span>
                <span className="text-sm text-gray-500">Active</span>
              </li>
              <li className="flex justify-between border-b pb-2">
                <span>Code Reviewer</span>
                <span className="text-sm text-gray-500">Active</span>
              </li>
              <li className="flex justify-between border-b pb-2">
                <span>Data Analyzer</span>
                <span className="text-sm text-gray-500">Inactive</span>
              </li>
            </ul>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Recent Teams</h2>
            <ul className="space-y-2">
              <li className="flex justify-between border-b pb-2">
                <span>Research Team</span>
                <span className="text-sm text-gray-500">3 members</span>
              </li>
              <li className="flex justify-between border-b pb-2">
                <span>Development Team</span>
                <span className="text-sm text-gray-500">5 members</span>
              </li>
              <li className="flex justify-between border-b pb-2">
                <span>Analysis Team</span>
                <span className="text-sm text-gray-500">2 members</span>
              </li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;