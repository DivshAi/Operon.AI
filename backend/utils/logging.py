# AI Agentic Platform - Logging Utility
"""
Structured logging setup for monitoring and debugging.
"""

import logging
import sys
from datetime import datetime
from typing import Dict, Any

# Configure logging
logger = logging.getLogger("ai_agentic_platform")
logger.setLevel(logging.INFO)

# Create console handler with structured formatting
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)

def log_request_info(request_data: Dict[str, Any]) -> None:
    """Log incoming request information."""
    logger.info(f"Incoming request: {request_data}")

def log_response_info(response_data: Dict[str, Any]) -> None:
    """Log outgoing response information."""
    logger.info(f"Outgoing response: {response_data}")

def log_error(error_message: str, error_details: Dict[str, Any] = None) -> None:
    """Log error information."""
    if error_details:
        logger.error(f"Error: {error_message} - Details: {error_details}")
    else:
        logger.error(f"Error: {error_message}")

def log_performance(metric_name: str, value: float, unit: str = "") -> None:
    """Log performance metrics."""
    logger.info(f"Performance metric - {metric_name}: {value} {unit}")

def log_user_action(user_id: str, action: str, details: Dict[str, Any] = None) -> None:
    """Log user actions for audit trails."""
    if details:
        logger.info(f"User {user_id} performed action '{action}' with details: {details}")
    else:
        logger.info(f"User {user_id} performed action '{action}'")

def log_system_event(event_type: str, message: str, details: Dict[str, Any] = None) -> None:
    """Log system events."""
    if details:
        logger.info(f"System event [{event_type}]: {message} - Details: {details}")
    else:
        logger.info(f"System event [{event_type}]: {message}")

# Example usage in the application
if __name__ == "__main__":
    # Test logging
    log_system_event("startup", "AI Agentic Platform started")
    log_user_action("user_123", "login", {"ip": "192.168.1.1"})
    log_performance("response_time", 0.5, "seconds")