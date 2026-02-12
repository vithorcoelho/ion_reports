"""Constants for VidaNova plugin configuration."""

from app.domain.report import (
    FindingsSection,
    MarkdownReport,
    SummaryContent,
    SupplementRecommendationSectionWrapper,
    TrainingRecommendation,
    VidaNovaDietSuggestions,
)

# Schema mappings for different sections
SECTION_SCHEMAS = {
    "summary": SummaryContent,
    "findings": FindingsSection,
    "diet_suggestions": VidaNovaDietSuggestions,
    "supplements": SupplementRecommendationSectionWrapper,
    "training": TrainingRecommendation,
    "markdown_report": MarkdownReport,
}
