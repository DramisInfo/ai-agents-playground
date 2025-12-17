'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, MessageSquare, Briefcase, Code, Users, DollarSign, FileText } from 'lucide-react';

export default function Navigation() {
  const pathname = usePathname();

  const links = [
    { href: '/', label: 'Home', icon: Home },
    { href: '/support', label: 'Support', icon: MessageSquare },
    { href: '/faq', label: 'FAQ Expert', icon: FileText },
    { href: '/sales', label: 'Sales', icon: Briefcase },
    { href: '/developer', label: 'Developer', icon: Code },
    { href: '/hr', label: 'HR', icon: Users },
    { href: '/finance', label: 'Finance', icon: DollarSign },
    { href: '/research', label: 'Research', icon: FileText },
  ];

  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-2">
            <div className="w-10 h-10 bg-techflow-primary rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-xl">TF</span>
            </div>
            <span className="text-xl font-bold text-gray-900">TechFlow</span>
          </div>
          
          <div className="flex space-x-1">
            {links.map((link) => {
              const Icon = link.icon;
              const isActive = pathname === link.href;
              
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-colors ${
                    isActive
                      ? 'bg-techflow-primary text-white'
                      : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  <span className="font-medium">{link.label}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}
