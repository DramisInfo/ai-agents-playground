export default function SalesPage() {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Sales Hub</h1>
        <p className="text-gray-600">Manual prospect research and proposal generation</p>
        
        <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-6">
          <h3 className="text-lg font-semibold text-yellow-900 mb-2">⏱️ Current Manual Process</h3>
          <ul className="space-y-2 text-yellow-800 text-sm">
            <li>• <strong>6 hours per prospect</strong> - Manual research across multiple sources</li>
            <li>• Open 20+ browser tabs to gather company information</li>
            <li>• Manually copy data into proposal template</li>
            <li>• Research competitors manually</li>
            <li>• Look up financial information on multiple sites</li>
            <li>• Draft personalized proposal from scratch</li>
          </ul>
        </div>

        <div className="mt-6 text-center p-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-lg">Coming in Lesson 4</p>
          <p className="text-sm text-gray-400 mt-2">This module will demonstrate manual sales research workflow</p>
        </div>
      </div>
    </div>
  );
}
