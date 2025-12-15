export default function FinancePage() {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Finance Dashboard</h1>
        <p className="text-gray-600">Manual invoice processing and validation</p>
        
        <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-6">
          <h3 className="text-lg font-semibold text-yellow-900 mb-2">⏱️ Current Manual Process</h3>
          <ul className="space-y-2 text-yellow-800 text-sm">
            <li>• <strong>80 hours per month</strong> - Processing 500 invoices manually</li>
            <li>• Manually extract data from PDF invoices</li>
            <li>• Type all information into accounting system</li>
            <li>• Manually validate amounts and vendor details</li>
            <li>• Cross-reference purchase orders by hand</li>
            <li>• 95% manual data entry prone to errors</li>
          </ul>
        </div>

        <div className="mt-6 text-center p-12 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-lg">Coming in Lesson 7</p>
          <p className="text-sm text-gray-400 mt-2">This module will demonstrate manual invoice processing</p>
        </div>
      </div>
    </div>
  );
}
