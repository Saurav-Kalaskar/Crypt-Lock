import logging
import psutil

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_real_time_metrics():
    """Log real-time CPU and memory usage metrics."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Log the metrics
    logger.info(f"Real-time metrics: CPU Usage={cpu_usage}%, Memory Usage={memory_usage}%")

def get_real_time_metrics():
    """Fetch real-time CPU and memory usage metrics for the dashboard."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Return the metrics as a dictionary
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }
