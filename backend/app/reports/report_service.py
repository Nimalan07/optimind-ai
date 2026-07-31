import os
from app.reports.report_builder import ReportBuilder
from app.reports.pdf_generator import PDFGenerator
from app.reports.html_generator import HTMLGenerator


class ReportService:

    @staticmethod
    def generate_report(report_data):
        report_content = ReportBuilder.build_report(report_data)
        pdf_path = PDFGenerator.generate(report_content)
        html_content = HTMLGenerator.generate(report_content)
        
        # Save HTML report as well
        html_dir = "reports"
        os.makedirs(html_dir, exist_ok=True)
        html_path = os.path.join(html_dir, "optimization_report.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        return {
            "pdf_path": pdf_path,
            "html_path": html_path,
            "report_content": report_content
        }
