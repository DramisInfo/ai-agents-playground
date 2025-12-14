"""
Shared Metrics Collection Module

This module provides standardized metrics collection for all lessons,
enabling before/after comparison when toggling AI feature flags.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Literal, Optional
import json
import os


@dataclass
class AgentMetrics:
    """Standard metrics structure for all lessons"""
    timestamp: str
    lesson: str
    mode: Literal["AI", "Manual"]
    request_count: int
    avg_response_time: float  # seconds
    accuracy: float  # 0.0 to 1.0
    error_rate: float  # 0.0 to 1.0
    cost_per_request: Optional[float] = None  # dollars
    custom_metrics: Optional[dict] = None
    
    def to_json(self) -> str:
        """Convert metrics to JSON string"""
        return json.dumps(asdict(self), indent=2)
    
    def to_dict(self) -> dict:
        """Convert metrics to dictionary"""
        return asdict(self)


class MetricsCollector:
    """
    Collects and displays metrics for AI vs Manual modes.
    
    Usage:
        collector = MetricsCollector(lesson_name="lesson-01-support-bot")
        collector.record_request(response_time=3.2, success=True, mode="AI")
        collector.display_summary()
    """
    
    def __init__(self, lesson_name: str):
        self.lesson_name = lesson_name
        self.ai_metrics = []
        self.manual_metrics = []
        
    def record_request(
        self,
        response_time: float,
        success: bool,
        mode: Literal["AI", "Manual"],
        cost: Optional[float] = None,
        custom: Optional[dict] = None
    ):
        """Record a single request's metrics"""
        metric = {
            "response_time": response_time,
            "success": success,
            "cost": cost,
            "custom": custom
        }
        
        if mode == "AI":
            self.ai_metrics.append(metric)
        else:
            self.manual_metrics.append(metric)
    
    def calculate_summary(self, mode: Literal["AI", "Manual"]) -> Optional[AgentMetrics]:
        """Calculate summary metrics for a mode"""
        metrics = self.ai_metrics if mode == "AI" else self.manual_metrics
        
        if not metrics:
            return None
        
        total_requests = len(metrics)
        successful = sum(1 for m in metrics if m["success"])
        avg_time = sum(m["response_time"] for m in metrics) / total_requests
        accuracy = successful / total_requests
        error_rate = 1 - accuracy
        
        costs = [m["cost"] for m in metrics if m["cost"] is not None]
        avg_cost = sum(costs) / len(costs) if costs else None
        
        return AgentMetrics(
            timestamp=datetime.utcnow().isoformat(),
            lesson=self.lesson_name,
            mode=mode,
            request_count=total_requests,
            avg_response_time=round(avg_time, 2),
            accuracy=round(accuracy, 2),
            error_rate=round(error_rate, 2),
            cost_per_request=round(avg_cost, 4) if avg_cost else None
        )
    
    def display_summary(self):
        """Display formatted metrics summary"""
        # Implementation will be added by each lesson
        pass
    
    def export_metrics(self, filepath: str):
        """Export metrics to file for analysis"""
        ai_summary = self.calculate_summary("AI")
        manual_summary = self.calculate_summary("Manual")
        
        data = {
            "lesson": self.lesson_name,
            "ai_metrics": ai_summary.to_dict() if ai_summary else None,
            "manual_metrics": manual_summary.to_dict() if manual_summary else None,
            "comparison": self._calculate_improvement(ai_summary, manual_summary) if ai_summary and manual_summary else None
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _calculate_improvement(self, ai: AgentMetrics, manual: AgentMetrics) -> dict:
        """Calculate percentage improvements"""
        return {
            "response_time_improvement": round((1 - ai.avg_response_time / manual.avg_response_time) * 100, 1),
            "accuracy_improvement": round((ai.accuracy - manual.accuracy) * 100, 1),
            "error_reduction": round((manual.error_rate - ai.error_rate) * 100, 1),
        }


def get_feature_flag(flag_name: str) -> bool:
    """
    Check if a feature flag is enabled.
    
    Args:
        flag_name: Name of the environment variable (e.g., 'ENABLE_AI_SUPPORT_BOT')
    
    Returns:
        True if flag is set to 'true', False otherwise
    """
    return os.getenv(flag_name, 'false').lower() == 'true'


def display_mode_banner(mode: Literal["AI", "Manual"], lesson_name: str):
    """Display a banner indicating current operating mode"""
    width = 50
    if mode == "AI":
        print("╔" + "═" * width + "╗")
        print(f"║  🤖 AI MODE ENABLED: {lesson_name:28} ║")
        print("╠" + "═" * width + "╣")
        print("║  Using Microsoft Agent Framework              ║")
        print("║  Intelligent, context-aware processing        ║")
        print("╚" + "═" * width + "╝")
    else:
        print("╔" + "═" * width + "╗")
        print(f"║  👤 MANUAL MODE: {lesson_name:33} ║")
        print("╠" + "═" * width + "╣")
        print("║  Using rule-based/manual processing           ║")
        print("║  Baseline performance (pre-AI state)          ║")
        print("╚" + "═" * width + "╝")
    print()
