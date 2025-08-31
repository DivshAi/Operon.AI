// AI Agentic Platform - Team Panel Component
// Reusable component for displaying team information

import React from 'react';
import { useRouter } from 'next/router';

interface TeamPanelProps {
  team: {
    id: string;
    name: string;
    description?: string;
    members?: number;
    workflow_status?: string;
  };
}

const TeamPanel = ({ team }: TeamPanelProps) => {
  const router = useRouter();

  // Status color mapping
  const statusColors = {
    active: 'bg-green-100 text-green-800',
    idle: 'bg-gray-100 text-gray-800',
    error: 'bg-red-100 text-red-800',
    paused: 'bg-yellow-100 text-yellow-800'
  };

  const handleViewDetails = () => {
    router.push(`/teams/${team.id}`);
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="p-5">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-xl font-bold text-gray-900">{team.name}</h3>
          <span className={`px-2 py-1 text-xs font-semibold rounded-full ${statusColors[team.workflow_status || 'idle']}`}>
            {team.workflow_status || 'Idle'}
          </span>
        </div>
        
        {team.description && (
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">
            {team.description}
          </p>
        )}
        
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <p className="text-xs text-gray-500">Team Members</p>
            <p className="font-semibold text-gray-900">
              {team.members || 0} agents
            </p>
          </div>
          <div>
            <p className="text-xs text-gray-500">Last Execution</p>
            <p className="font-semibold text-gray-900">
              {team.last_executed || 'Never'}
            </p>
          </div>
        </div>
        
        <button
          onClick={handleViewDetails}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md transition-colors duration-200"
        >
          Manage Team
        </button>
      </div>
    </div>
  );
};

export default TeamPanel;