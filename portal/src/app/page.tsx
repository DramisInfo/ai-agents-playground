import Link from 'next/link';
import { Users, MessageSquare, Briefcase, Code, FileText, DollarSign } from 'lucide-react';

export default function Home() {
  const modules = [
    {
      title: 'Support Dashboard',
      description: 'Handle customer support tickets and queries',
      icon: MessageSquare,
      href: '/support',
      phase: 'Phase 1',
      lessons: ['Lesson 1-3'],
      color: 'bg-blue-500',
    },
    {
      title: 'Sales Hub',
      description: 'Research prospects and generate proposals',
      icon: Briefcase,
      href: '/sales',
      phase: 'Phase 2',
      lessons: ['Lesson 4'],
      color: 'bg-green-500',
    },
    {
      title: 'Developer Portal',
      description: 'Code review and onboarding assistance',
      icon: Code,
      href: '/developer',
      phase: 'Phase 2',
      lessons: ['Lesson 5-6'],
      color: 'bg-purple-500',
    },
    {
      title: 'Finance Dashboard',
      description: 'Process and manage invoices',
      icon: DollarSign,
      href: '/finance',
      phase: 'Phase 3',
      lessons: ['Lesson 7'],
      color: 'bg-yellow-500',
    },
    {
      title: 'HR Portal',
      description: 'Employee self-service and policy assistance',
      icon: Users,
      href: '/hr',
      phase: 'Phase 3',
      lessons: ['Lesson 9'],
      color: 'bg-pink-500',
    },
    {
      title: 'Research Center',
      description: 'Generate market research and competitive intelligence',
      icon: FileText,
      href: '/research',
      phase: 'Phase 3',
      lessons: ['Lesson 8'],
      color: 'bg-indigo-500',
    },
  ];



  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">
          Welcome to TechFlow Solutions
        </h1>
        <p className="text-xl text-gray-600">
          Operations Portal - Managing Daily Workflows
        </p>
        <p className="text-sm text-gray-500 mt-4">
          150 employees | Mid-sized software consulting company
        </p>
      </div>

      {/* Current Challenges */}
      <div className="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-lg">
        <h2 className="text-lg font-semibold text-yellow-900 mb-2">
          ⚠️ Current Operational Challenges
        </h2>
        <ul className="space-y-2 text-yellow-800">
          <li>• <strong>Customer Support</strong> - Overwhelmed with 200+ daily tickets, 60% repetitive</li>
          <li>• <strong>Sales Team</strong> - Spending 6+ hours per prospect on manual research</li>
          <li>• <strong>Engineering</strong> - Code reviews taking 2-3 days, blocking velocity</li>
          <li>• <strong>HR Department</strong> - Manually answering the same policy questions repeatedly</li>
          <li>• <strong>Operations</strong> - 80 hours/month processing invoices manually</li>
        </ul>
      </div>

      {/* Module Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {modules.map((module) => {
          const Icon = module.icon;
          return (
            <Link
              key={module.href}
              href={module.href}
              className="group bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-200 overflow-hidden"
            >
              <div className={`${module.color} p-4`}>
                <Icon className="h-8 w-8 text-white" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-bold text-gray-900 mb-2 group-hover:text-techflow-primary transition-colors">
                  {module.title}
                </h3>
                <p className="text-gray-600 mb-4">
                  {module.description}
                </p>
                <div className="flex items-center justify-between text-sm">
                  <span className="text-gray-500">{module.phase}</span>
                  <span className="text-techflow-secondary font-medium">{module.lessons.join(', ')}</span>
                </div>
              </div>
            </Link>
          );
        })}
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-sm text-gray-600 mb-1">Daily Tickets</p>
          <p className="text-3xl font-bold text-gray-900">200+</p>
          <p className="text-xs text-gray-500 mt-1">60% are repetitive</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-sm text-gray-600 mb-1">Proposal Research</p>
          <p className="text-3xl font-bold text-gray-900">6 hrs</p>
          <p className="text-xs text-gray-500 mt-1">Per prospect</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-sm text-gray-600 mb-1">Code Reviews</p>
          <p className="text-3xl font-bold text-gray-900">2-3 days</p>
          <p className="text-xs text-gray-500 mt-1">Blocking velocity</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-sm text-gray-600 mb-1">Invoice Processing</p>
          <p className="text-3xl font-bold text-gray-900">80 hrs</p>
          <p className="text-xs text-gray-500 mt-1">500 invoices/month</p>
        </div>
      </div>
    </div>
  );
}
