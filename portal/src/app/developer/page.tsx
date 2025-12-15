export default function DeveloperPage() {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Developer Portal</h1>
        <p className="text-gray-600">Manual code reviews and developer onboarding</p>
        
        <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-6">
          <h3 className="text-lg font-semibold text-yellow-900 mb-2">⏱️ Current Manual Process</h3>
          <ul className="space-y-2 text-yellow-800 text-sm">
            <li>• <strong>2-3 days per code review</strong> - Blocking development velocity</li>
            <li>• Senior developers spending 40% of time reviewing code</li>
            <li>• Inconsistent feedback across different reviewers</li>
            <li>• Common issues not caught until human review</li>
            <li>• New developers wait days for feedback on learning</li>
            <li>• Onboarding takes 3 months before productivity</li>
          </ul>
        </div>

        <div className="mt-6 text-center p-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-lg">Coming in Lessons 5-6</p>
          <p className="text-sm text-gray-400 mt-2">This module will demonstrate manual code review and onboarding</p>
        </div>
      </div>
    </div>
  );
}
