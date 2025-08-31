// AI Agentic Platform - Prompt Card Component
// Reusable component for displaying prompt information

import React from 'react';
import { useRouter } from 'next/router';

interface PromptCardProps {
  prompt: {
    id: string;
    body: string;
    version: string;
    tags?: string[];
  };
}

const PromptCard = ({ prompt }: PromptCardProps) => {
  const router = useRouter();

  const handleViewDetails = () => {
    router.push(`/prompts/${prompt.id}`);
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="p-5">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-xl font-bold text-gray-900">Prompt {prompt.version}</h3>
          <span className="px-2 py-1 text-xs font-semibold rounded-full bg-purple-100 text-purple-800">
            {prompt.version}
          </span>
        </div>
        
        <p className="text-gray-600 text-sm mb-4 line-clamp-3">
          {prompt.body}
        </p>
        
        {prompt.tags && prompt.tags.length > 0 && (
          <div className="flex flex-wrap gap-2 mb-4">
            {prompt.tags.slice(0, 3).map((tag) => (
              <span key={tag} className="px-2 py-1 text-xs font-semibold rounded-full bg-blue-100 text-blue-800">
                {tag}
              </span>
            ))}
            
            {prompt.tags.length > 3 && (
              <span className="text-xs text-gray-500">+{prompt.tags.length - 3} more</span>
            )}
          </div>
        )}
        
        <button
          onClick={handleViewDetails}
          className="w-full bg-purple-500 hover:bg-purple-600 text-white py-2 px-4 rounded-md transition-colors duration-200"
        >
          View Prompt
        </button>
      </div>
    </div>
  );
};

export default PromptCard;