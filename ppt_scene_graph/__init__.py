"""ppt_pipeline — Unified PPT Production Pipeline"""
from .design import DesignSystem, load_theme, list_themes, FONT_SIZES
from .pipeline import beautify, create_from_outline, evaluate, cli_main
