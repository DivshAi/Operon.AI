// AI Agentic Platform - Prompts Library Page
// Displays all prompts with search and filter capabilities

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { prompts } from '../../lib/api';
import PromptCard from '../../components/PromptCard';

const PromptsPage = () => {
  const [promptsList, setPromptsList] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [filterTags, setFilterTags] = useState<string[]>([]);
  
  const router = useRouter();

  useEffect(() => {
    const fetchPrompts = async () => {
      try {
        setLoading(true);
        const data = await prompts.getPrompts();
        setPromptsList(data);
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to fetch prompts');
      } finally {
        setLoading(false);
      }
    };

    fetchPrompts();
  }, []);

  // Get all unique tags from prompts for filtering
  const allTags = Array.from(new Set(
    promptsList.flatMap(prompt => prompt.tags || [])
  )).sort();

  // Filter prompts based on search and tags
  const filteredPrompts = promptsList.filter(prompt => {
    const matchesSearch = prompt.body.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         prompt.version.includes(searchTerm);
    
    const matchesTags = filterTags.length === 0 || 
                      filterTags.every(tag => prompt.tags?.includes(tag));
    
    return matchesSearch && matchesTags;
  });

  const handleAddTag = (tag: string) => {
    if (!filterTags.includes(tag)) {
      setFilterTags([...filterTags, tag]);
    }
  };

  const handleRemoveTag = (tag: string) => {
    setFilterTags(filterTags.filter(t => t !== tag));
  };

  if (loading) return <div className="container mx-auto p-4">Loading prompts...</div>;
  if (error) return <div className="container mx-auto p-4 text-red-500">{error}</div>;

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold text-gray-900">Prompt Library</h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        {/* Search and Filters */}
        <div className="bg-white rounded-lg shadow-md p-4 mb-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Search</label>
              <input
                type="text"
                placeholder="Search prompts by content or version..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Filter by Tags</label>
              <div className="flex flex-wrap gap-2">
                {allTags.slice(0, 10).map((tag) => (
                  <button
                    key={tag}
                    onClick={() => handleAddTag(tag)}
                    className="px-2 py-1 text-xs font-medium rounded-full bg-gray-100 text-gray-800 hover:bg-blue-100 hover:text-blue-800 transition-colors"
                  >
                    {tag}
                  </button>
                ))}
                
                {allTags.length > 10 && (
                  <span className="text-xs text-gray-500">+{allTags.length - 10} more tags</span>
                )}
              </div>
            </div>

            <div className="flex items-end">
              <button
                onClick={() => router.push('/prompts/new')}
                className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm"
              >
                Create New Prompt
              </button>
            </div>
          </div>

          {/* Active Filters */}
          {filterTags.length > 0 && (
            <div className="mt-3 flex flex-wrap gap-2">
              {filterTags.map((tag) => (
                <span key={tag} className="flex items-center px-2 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-800">
                  {tag}
                  <button
                    onClick={() => handleRemoveTag(tag)}
                    className="ml-1 text-blue-600 hover:text-blue-900"
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Prompts Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredPrompts.length > 0 ? (
            filteredPrompts.map((prompt) => (
              <PromptCard key={prompt.id} prompt={prompt} />
            ))
          ) : (
            <div className="col-span-full bg-white rounded-lg shadow-md p-8 text-center">
              <p className="text-gray-500 mb-4">No prompts found matching your criteria.</p>
              <button
                onClick={() => router.push('/prompts/new')}
                className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md"
              >
                Create Your First Prompt
              </button>
            </div>
          )}
        </div>

        {/* Pagination (placeholder) */}
        {filteredPrompts.length > 0 && (
          <div className="mt-8 flex justify-center">
            <nav className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
              <a href="#" className="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                Previous
              </a>
              <a href="#" className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-blue-50 text-sm font-medium text-blue-600">
                1
              </a>
              <a href="#" className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
                2
              </a>
              <span className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                ...
              </span>
              <a href="#" className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
                8
              </a>
              <a href="#" className="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                Next
              </a>
            </nav>
          </div>
        )}
      </main>
    </div>
  );
};

export default PromptsPage;