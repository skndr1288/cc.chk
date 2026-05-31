"""
🔧 Logging Configuration
نظام السجلات المتقدم
"""

import logging
import sys
from pathlib import Path
from loguru import logger as loguru_logger


def setup_logging():
    """إعداد نظام السجلات"""
    
    # إنشاء مجلد السجلات
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # حذف معالجات الافتراضية
    logging.getLogger().handlers.clear()
    
    # إضافة معالج Console
    loguru_logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level="INFO"
    )
    
    # إضافة معالج File
    loguru_logger.add(
        log_dir / "bot.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        level="DEBUG",
        rotation="10 MB",
        retention="7 days"
    )
    
    # إضافة معالج للأخطاء
    loguru_logger.add(
        log_dir / "errors.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        level="ERROR",
        rotation="10 MB",
        retention="30 days"
    )
    
    return loguru_logger
