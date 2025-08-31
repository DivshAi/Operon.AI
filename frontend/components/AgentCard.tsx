// AI Agentic Platform - Agent Card Component
// Reusable component for displaying agent information

import React from 'react';
import { useRouter } from 'next/router';

interface AgentCardProps {
  agent: {
    id: string;
    name: string;
    description?: string;
    status: string;
    performance_metrics?: any;
  };
}

const AgentCard = ({ agent }: AgentCardProps) => {
  const router = useRouter();

  // Status color mapping
  const statusColors = {
    active: 'bg-green-100 text-green-800',
    inactive: 'bg-gray-100 text-gray-800',
    error: 'bg-red-100 text-red-800',
    running: 'bg-blue-100 text-blue-800'
  };

  const handleViewDetails = () => {
    router.push(`/agents/${agent.id}`);
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="p-5">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-xl font-bold text-gray-900">{agent.name}</h3>
          <span className={`px-2 py-1 text-xs font-semibold rounded-full ${statusColors[agent.status || 'inactive']}`}>
            {agent.status}
          </span>
        </div>
        
        {agent.description && (
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">
            {agent.description}
          </p>
        )}
        
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <p className="text-xs text-gray-500">Success Rate</p>
            <p className="font-semibold text-gray-900">
              {agent.performance_metrics?.success_rate || 'N/A'}%
            </p>
          </div>
          <div>
            <p className="text-xs text-gray-500">Avg Response Time</p>
            <p className="font-semibold text-gray-900">
              {agent.performance_metrics?.avg_response_time || 'N/A'}ms
            </p>
          </div>
        </div>
        
        <button
          onClick={handleViewDetails}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md transition-colors duration-200"
        >
          View Details
        </button>
      </div>
    </div>
  );
};

export default AgentCard;