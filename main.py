# main.py
from utils import get_timestamp
from report_generator import generate_pdf_report
import os

# Example input data
data = {
    "timestamp": get_timestamp(),
    "app_count": 120,
    "platform_count": 2,
    "ai_generated_executive_summary": "The app market is growing rapidly with a focus on user engagement...",
    "success_factors": [
        {"name": "User Experience", "impact": 9, "analysis": "Apps with seamless UX show higher retention."},
        {"name": "Feature Set", "impact": 8, "analysis": "Unique features drive downloads and reviews."},
        {"name": "Marketing Reach", "impact": 7, "analysis": "High visibility in app stores correlates with success."},
    ],
    "categories": [
        {"name": "Games", "rating": 4.5, "success_rate": 80, "revenue": "$50K", "recommendation": "Focus on casual games"},
        {"name": "Productivity", "rating": 4.2, "success_rate": 70, "revenue": "$30K", "recommendation": "Enhance collaboration features"},
    ],
    "pricing": {
        "Games": "$0.99 - $4.99",
        "Productivity": "$4.99 - $9.99",
        "Health & Fitness": "$1.99 - $5.99",
        "Education": "$2.99 - $7.99"
    },
    "opportunities": [
        {"name": "Health & Fitness", "score": 9, "analysis": "High demand due to wellness trends."},
        {"name": "Education", "score": 8, "analysis": "Growing online learning market."}
    ],
    "actions": {
        "immediate": ["Launch marketing campaign", "Optimize app store pages"],
        "short_term": ["Add social sharing features", "Run A/B tests on pricing"],
        "long_term": ["Expand to new platforms", "Integrate AI-powered recommendations"]
    }
}

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# Generate PDF report
pdf_path = generate_pdf_report(data, filename="App_Market_Report.pdf")
print(f"Report generated: {pdf_path}")