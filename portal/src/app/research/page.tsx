export default function ResearchPage() {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Research Center</h1>
        <p className="text-gray-600">Manual market research and competitive analysis</p>
        
        <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-6">
          <h3 className="text-lg font-semibold text-yellow-900 mb-2">⏱️ Current Manual Process</h3>
          <ul className="space-y-2 text-yellow-800 text-sm">
            <li>• <strong>20+ hours per report</strong> - Creating market research manually</li>
            <li>• Research across dozens of sources</li>
            <li>• Manually compile and synthesize information</li>
            <li>• Write reports from scratch</li>
            <li>• Fact-checking is time-consuming and error-prone</li>
            <li>• Reports often outdated by publication</li>
          </ul>
        </div>

        <div className="mt-6 text-center p-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-lg">Coming in Lesson 8</p>
          <p className="text-sm text-gray-400 mt-2">This module will demonstrate manual research workflow</p>
        </div>
      </div>
    </div>
  );
}
