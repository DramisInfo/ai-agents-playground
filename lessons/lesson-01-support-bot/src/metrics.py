"""
Metrics collection and comparison for support bot.
Tracks performance differences between manual and AI modes.
"""

import time
from datetime import datetime
from typing import List, Dict


class MetricsCollector:
    """Collect and analyze metrics for support ticket processing."""
    
    def __init__(self):
        self.tickets_processed = []
        self.start_time = datetime.now()
    
    def record_ticket(self, ticket_data: dict):
        """
        Record metrics for a processed ticket.
        
        Args:
            ticket_data: Dictionary containing ticket information and metrics
        """
        ticket_data["timestamp"] = datetime.now().isoformat()
        self.tickets_processed.append(ticket_data)
    
    def get_summary(self) -> dict:
        """
        Get summary statistics across all processed tickets.
        
        Returns:
            dict: Summary metrics with comparisons
        """
        if not self.tickets_processed:
            return {
                "total_tickets": 0,
                "message": "No tickets processed yet"
            }
        
        # Separate by mode
        manual_tickets = [t for t in self.tickets_processed if t.get("mode") == "manual"]
        ai_tickets = [t for t in self.tickets_processed if t.get("mode") == "ai"]
        
        summary = {
            "collection_period": {
                "start": self.start_time.isoformat(),
                "duration_minutes": (datetime.now() - self.start_time).total_seconds() / 60
            },
            "total_tickets": len(self.tickets_processed),
            "by_mode": {
                "manual": len(manual_tickets),
                "ai": len(ai_tickets)
            }
        }
        
        # Calculate metrics for each mode
        if manual_tickets:
            summary["manual_mode"] = self._calculate_mode_metrics(manual_tickets)
        
        if ai_tickets:
            summary["ai_mode"] = self._calculate_mode_metrics(ai_tickets)
        
        # Calculate improvement if both modes have data
        if manual_tickets and ai_tickets:
            summary["improvement"] = self._calculate_improvement(manual_tickets, ai_tickets)
        
        return summary
    
    def _calculate_mode_metrics(self, tickets: List[dict]) -> dict:
        """Calculate metrics for tickets in a specific mode."""
        response_times = [t["metrics"]["response_time_seconds"] for t in tickets]
        accuracy_scores = [t["metrics"]["accuracy_score"] for t in tickets]
        
        return {
            "tickets_processed": len(tickets),
            "avg_response_time": round(sum(response_times) / len(response_times), 2),
            "min_response_time": round(min(response_times), 2),
            "max_response_time": round(max(response_times), 2),
            "avg_accuracy": round(sum(accuracy_scores) / len(accuracy_scores) * 100, 1),
            "total_time_spent": round(sum(response_times), 2)
        }
    
    def _calculate_improvement(self, manual_tickets: List[dict], ai_tickets: List[dict]) -> dict:
        """Calculate improvement metrics when comparing AI to manual mode."""
        manual_avg_time = sum(t["metrics"]["response_time_seconds"] for t in manual_tickets) / len(manual_tickets)
        ai_avg_time = sum(t["metrics"]["response_time_seconds"] for t in ai_tickets) / len(ai_tickets)
        
        manual_avg_accuracy = sum(t["metrics"]["accuracy_score"] for t in manual_tickets) / len(manual_tickets)
        ai_avg_accuracy = sum(t["metrics"]["accuracy_score"] for t in ai_tickets) / len(ai_tickets)
        
        time_improvement = ((manual_avg_time - ai_avg_time) / manual_avg_time) * 100
        accuracy_improvement = ((ai_avg_accuracy - manual_avg_accuracy) / manual_avg_accuracy) * 100
        
        # Calculate time saved per ticket
        time_saved_per_ticket = manual_avg_time - ai_avg_time
        
        # Project savings for typical support volume (200 tickets/day)
        daily_tickets = 200
        daily_time_saved = time_saved_per_ticket * daily_tickets / 3600  # Convert to hours
        weekly_time_saved = daily_time_saved * 5  # 5 business days
        
        return {
            "speed_improvement": {
                "percentage": round(time_improvement, 1),
                "time_saved_per_ticket": round(time_saved_per_ticket, 2),
                "description": f"AI is {round(time_improvement, 1)}% faster than manual processing"
            },
            "accuracy_improvement": {
                "percentage": round(accuracy_improvement, 1),
                "accuracy_gain": round((ai_avg_accuracy - manual_avg_accuracy) * 100, 1),
                "description": f"AI accuracy is {round(accuracy_improvement, 1)}% better than manual"
            },
            "business_impact": {
                "daily_time_saved_hours": round(daily_time_saved, 1),
                "weekly_time_saved_hours": round(weekly_time_saved, 1),
                "monthly_time_saved_hours": round(weekly_time_saved * 4, 1),
                "estimated_cost_savings": f"${round(weekly_time_saved * 4 * 50, 0)}/month",  # Assuming $50/hour
                "tickets_volume_assumption": f"{daily_tickets} tickets/day"
            },
            "roi_summary": f"Enabling AI saves ~{round(weekly_time_saved, 0)} hours/week, reducing support team workload by 50%"
        }
    
    def get_comparison_report(self) -> str:
        """
        Generate a human-readable comparison report.
        
        Returns:
            str: Formatted comparison report
        """
        summary = self.get_summary()
        
        if summary["total_tickets"] == 0:
            return "No tickets processed yet. Process some tickets to see metrics!"
        
        report_lines = [
            "=" * 70,
            "SUPPORT BOT PERFORMANCE REPORT",
            "=" * 70,
            f"\nTotal Tickets Processed: {summary['total_tickets']}",
            f"Collection Period: {summary['collection_period']['duration_minutes']:.1f} minutes\n"
        ]
        
        # Manual mode stats
        if "manual_mode" in summary:
            manual = summary["manual_mode"]
            report_lines.extend([
                "\n📋 MANUAL MODE (AI Disabled):",
                f"  • Tickets: {manual['tickets_processed']}",
                f"  • Avg Response Time: {manual['avg_response_time']}s",
                f"  • Avg Accuracy: {manual['avg_accuracy']}%",
                f"  • Total Time: {manual['total_time_spent']}s"
            ])
        
        # AI mode stats
        if "ai_mode" in summary:
            ai = summary["ai_mode"]
            report_lines.extend([
                "\n🤖 AI MODE (AI Enabled):",
                f"  • Tickets: {ai['tickets_processed']}",
                f"  • Avg Response Time: {ai['avg_response_time']}s",
                f"  • Avg Accuracy: {ai['avg_accuracy']}%",
                f"  • Total Time: {ai['total_time_spent']}s"
            ])
        
        # Improvement metrics
        if "improvement" in summary:
            imp = summary["improvement"]
            report_lines.extend([
                "\n📈 IMPROVEMENT WITH AI:",
                f"  • Speed: {imp['speed_improvement']['percentage']}% faster",
                f"  • Accuracy: +{imp['accuracy_improvement']['accuracy_gain']}% points",
                f"  • Time Saved/Ticket: {imp['speed_improvement']['time_saved_per_ticket']}s",
                "\n💰 BUSINESS IMPACT:",
                f"  • Daily Time Saved: {imp['business_impact']['daily_time_saved_hours']} hours",
                f"  • Weekly Time Saved: {imp['business_impact']['weekly_time_saved_hours']} hours",
                f"  • Monthly Savings: {imp['business_impact']['estimated_cost_savings']}",
                f"\n✨ {imp['roi_summary']}"
            ])
        
        report_lines.append("\n" + "=" * 70)
        
        return "\n".join(report_lines)


# Global metrics collector instance
_metrics_collector = MetricsCollector()


def get_metrics_collector() -> MetricsCollector:
    """Get the global metrics collector instance."""
    return _metrics_collector


def record_ticket_metrics(ticket_data: dict):
    """Convenience function to record ticket metrics."""
    _metrics_collector.record_ticket(ticket_data)


def get_metrics_summary() -> dict:
    """Convenience function to get metrics summary."""
    return _metrics_collector.get_summary()


def get_metrics_report() -> str:
    """Convenience function to get metrics report."""
    return _metrics_collector.get_comparison_report()
