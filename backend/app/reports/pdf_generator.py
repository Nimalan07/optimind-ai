import os


class PDFGenerator:

    @staticmethod
    def generate(report_content):

        pdf_dir = "reports"
        os.makedirs(pdf_dir, exist_ok=True)
        pdf_path = os.path.join(pdf_dir, "optimization_report.pdf")

        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib import colors
            
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                'TitleStyle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor("#1A365D"),
                spaceAfter=20
            )
            h2_style = ParagraphStyle(
                'H2Style',
                parent=styles['Heading2'],
                fontSize=16,
                textColor=colors.HexColor("#2B6CB0"),
                spaceBefore=15,
                spaceAfter=10
            )
            body_style = ParagraphStyle(
                'BodyStyle',
                parent=styles['BodyText'],
                fontSize=10,
                leading=14
            )
            
            story.append(Paragraph("AI Optimization Report", title_style))
            story.append(Spacer(1, 10))
            story.append(Paragraph(f"Model Architecture: {report_content['model'].upper()}", body_style))
            story.append(Paragraph(f"Optimization Score: {report_content['optimization_score']}/100", body_style))
            story.append(Paragraph(f"Status: {report_content['status']}", body_style))
            story.append(Spacer(1, 15))
            
            story.append(Paragraph("Executive Summary", h2_style))
            story.append(Paragraph(report_content['executive_summary']['summary'].replace('\n', '<br/>'), body_style))
            story.append(Spacer(1, 15))
            
            story.append(Paragraph("Model Recommendation Heuristic", h2_style))
            recs = report_content['recommendations']
            data = [
                ["Property", "Details"],
                ["Recommended Backend", recs['backend']],
                ["Backend Rationale", recs['backend_reason'] or "N/A"],
                ["Cloud Provider Target", recs['cloud_provider']],
                ["Cloud Instance Model", recs['cloud_instance']],
                ["Processor Architecture", recs['cloud_processor']],
                ["Cloud Selector Rationale", recs['cloud_reason'] or "N/A"],
            ]
            t = Table(data, colWidths=[150, 300])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0,0), (-1,0), 6),
                ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F7FAFC")),
                ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#E2E8F0")),
            ]))
            story.append(t)
            story.append(Spacer(1, 15))
            
            story.append(Paragraph("Deployment Readiness Check", h2_style))
            dep = report_content['deployment']
            dep_data = [
                ["Runtime/Environment", "Status"],
                ["Docker Containerization", f"✔ {dep['docker']}"],
                ["Kubernetes Manifests", f"✔ {dep['kubernetes']}"],
                ["FastAPI API Server", f"✔ {dep['fastapi']}"],
                ["ONNX Runtime Engine", f"✔ {dep['onnx_runtime']}"],
            ]
            t_dep = Table(dep_data, colWidths=[200, 250])
            t_dep.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#319795")),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#E2E8F0")),
            ]))
            story.append(t_dep)
            story.append(Spacer(1, 15))
            
            story.append(Paragraph("Visual Comparisons & Benchmarks", h2_style))
            for k, v in report_content['charts'].items():
                story.append(Paragraph(f"<b>{k.capitalize()} Scaling:</b><br/><font face='Courier'>{v.replace('\n', '<br/>')}</font>", body_style))
                story.append(Spacer(1, 10))
                
            doc.build(story)
            
        except Exception:
            # Fallback text file representation
            txt_path = pdf_path.replace(".pdf", ".txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"AI Optimization Report\n\nModel: {report_content['model']}\nScore: {report_content['optimization_score']}\nStatus: {report_content['status']}\n\nSummary:\n{report_content['executive_summary']['summary']}")
            return txt_path
            
        return pdf_path
