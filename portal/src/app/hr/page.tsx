export default function HRPage() {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">HR Portal</h1>
        <p className="text-gray-600">Manual employee support and policy questions</p>
        
        <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-6">
          <h3 className="text-lg font-semibold text-yellow-900 mb-2">⏱️ Current Manual Process</h3>
          <ul className="space-y-2 text-yellow-800 text-sm">
            <li>• <strong>50+ questions per day</strong> - Same questions repeatedly</li>
            <li>• HR team manually looking up policy documents</li>
            <li>• Employees waiting hours for simple answers</li>
            <li>• HR can't focus on strategic initiatives</li>
            <li>• Inconsistent answers from different HR reps</li>
            <li>• 10 hours per week answering repetitive questions</li>
          </ul>
        </div>

        <div className="mt-6 text-center p-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-lg">Coming in Lesson 9</p>
          <p className="text-sm text-gray-400 mt-2">This module will demonstrate manual HR support workflow</p>
        </div>
      </div>
    </div>
  );
}
