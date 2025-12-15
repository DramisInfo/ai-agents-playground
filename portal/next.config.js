/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  env: {
    // Feature flags loaded from .env
    ENABLE_SUPPORT_BOT: process.env.ENABLE_SUPPORT_BOT || 'false',
    ENABLE_FAQ_EXPERT: process.env.ENABLE_FAQ_EXPERT || 'false',
    ENABLE_SMART_ROUTER: process.env.ENABLE_SMART_ROUTER || 'false',
    ENABLE_SALES_ASSISTANT: process.env.ENABLE_SALES_ASSISTANT || 'false',
    ENABLE_CODE_REVIEWER: process.env.ENABLE_CODE_REVIEWER || 'false',
    ENABLE_ONBOARDING_COACH: process.env.ENABLE_ONBOARDING_COACH || 'false',
    ENABLE_INVOICE_PROCESSOR: process.env.ENABLE_INVOICE_PROCESSOR || 'false',
    ENABLE_RESEARCH_TEAM: process.env.ENABLE_RESEARCH_TEAM || 'false',
    ENABLE_HR_ASSISTANT: process.env.ENABLE_HR_ASSISTANT || 'false',
  },
};

module.exports = nextConfig;
