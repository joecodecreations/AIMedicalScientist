from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Flowable
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet,  ParagraphStyle
from datetime import date
import json
import os
from dotenv import load_dotenv
load_dotenv()

class AbsolutePositionedText(Flowable):
    def __init__(self, text, x=0, y=0, right_offset=None, left_offset=None, top_offset=None, bottom_offset=None):
        Flowable.__init__(self)
        self.text = text

        # Assuming letter page size for the calculations.
        page_width, page_height = letter

        # If offsets are provided, calculate the absolute position
        if right_offset is not None:
            text_width = 100
            # text_width = self.stringWidth(text, "Helvetica", 12) # Assuming 12pt Helvetica for the text
            x = page_width - right_offset - text_width

        if left_offset is not None:
            x = left_offset

        if top_offset is not None:
            text_height = 12  # Assuming a height of 12pt for the Helvetica text
            y = page_height - top_offset - text_height

        if bottom_offset is not None:
            y = bottom_offset

        self.x, self.y = x, y

    def draw(self):
        self.canv.drawString(self.x, self.y, self.text)
# story.append(AbsolutePositionedText("A.I. Medical Scientist", right_offset=45, y=5))
def create_pdf(title, content, output_filename):

    research_topic = os.environ.get("RESEARCH_TOPIC")
    # cures
    curative_surgery_treatments = os.environ.get("curative_surgery_treatments")
    curative_vitamin_treatments = os.environ.get("curative_vitamin_treatments")
    curative_rx_treatments = os.environ.get("curative_rx_treatments")
    # symptoms
    symptomatic_rx_treatments = os.environ.get("symptomatic_rx_treatments")
    symptomatic_vitamin_treatments = os.environ.get("symptomatic_vitamin_treatments")
    symptomatic_surgery_treatments = os.environ.get("symptomatic_surgery_treatments")



    left_margin = .25 * inch
    right_margin = .25 * inch
    top_margin = .25 * inch
    bottom_margin = .25 * inch


    # Create New Document
    doc = SimpleDocTemplate(output_filename, pagesize=letter, 
                            leftMargin=left_margin, rightMargin=right_margin,
                            topMargin=top_margin, bottomMargin=bottom_margin)

    story = []  # This list will store the content of the PDF
    
    # Define some styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    body_style = styles["BodyText"]

    # Create a bold body style
    bold_style = ParagraphStyle("Bold", parent=styles["BodyText"], fontName="Helvetica-Bold")

    bold_style_title = ParagraphStyle("Centered", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=14)

# create a small centered body style
    small_centered_style = ParagraphStyle(
        "Centered", parent=styles["BodyText"], alignment=TA_CENTER, fontSize=8
    )
    # Create a centered body style
    centered_style = ParagraphStyle(
        "Centered", parent=styles["BodyText"], alignment=TA_CENTER
    )

    # Add Header Image
    img = Image("./images/header.jpg")
    img.drawHeight = 2.25*inch  # You can set the height and width
    img.drawWidth = 5.0*inch   # of the image as you require
    story.append(img)


    
# Page 1
    # Add Report Generated With Date
    today = date.today()
    today = today.strftime("%B %d, %Y")
    story.append(Paragraph("A.I Medical Scientist Report Summary", title_style))
    story.append(Paragraph(F"Report on {research_topic} Generated on"+ today, centered_style))
    story.append(Paragraph("MIT License - Report Generated from https://github.com/joecodecreations/AIMedicalScientist", small_centered_style))
    story.append(PageBreak()) 

    # Cures
    story.append(Spacer(1, 3 * inch))
    story.append(Paragraph(F"{research_topic} Cures", title_style))
    story.append(PageBreak()) 

        # Page 1 cures
    story.append(Spacer(1, 3 * inch))
    story.append(Paragraph(F"{research_topic} Treatments", title_style))
    story.append(PageBreak()) 
        # Page 2 cures
    story.append(AbsolutePositionedText("A.I. Medical Scientist", right_offset=45, y=5))
    story.append(AbsolutePositionedText("Page 2 of 2", bottom_offset=10))

    smallLogo = Image("./images/header.jpg")
    smallLogo.drawHeight = 0.75*inch  # You can set the height and width
    smallLogo.drawWidth = 2.0*inch   # of the image as you require

    story.append(smallLogo)
    story.append(Paragraph("Surgical - Cures", title_style))
    story.append(Paragraph(f"Treatments for symptoms related to {research_topic} using Perscriptions", centered_style))
    if(curative_surgery_treatments is not None):
        for item in json.loads(curative_surgery_treatments):
            print(item)
            story.append(Paragraph(item['title'], bold_style_title))
            story.append(Paragraph('Summary', bold_style))
            story.append(Paragraph(item['summary'], body_style))
            story.append(Paragraph('Treatments', bold_style))
            for sentence in item['sentences']:
                story.append(Paragraph(sentence, body_style))
            story.append(Spacer(1, 0.2 * inch))


    # # Page 2 
    # story.append(Spacer(1, 3 * inch))
    # story.append(Paragraph(F"{research_topic} Treatments", title_style))
    # story.append(PageBreak()) 
    # # Page 3 
    # story.append(AbsolutePositionedText("A.I. Medical Scientist", right_offset=45, y=5))
    # story.append(AbsolutePositionedText("Page 2 of 2", bottom_offset=10))

    # smallLogo = Image("./images/header.jpg")
    # smallLogo.drawHeight = 0.75*inch  # You can set the height and width
    # smallLogo.drawWidth = 2.0*inch   # of the image as you require

    # story.append(smallLogo)
    # story.append(Paragraph("Perscription (RX) - Symptomatic Treatments", title_style))
    # story.append(Paragraph(f"Treatments for symptoms related to {research_topic} using Perscriptions", centered_style))
    # if(symptomatic_rx_treatments is not None):
    #     for item in json.loads(symptomatic_rx_treatments):
    #         print(item)
    #         story.append(Paragraph(item['title'], bold_style_title))
    #         story.append(Paragraph('Summary', bold_style))
    #         story.append(Paragraph(item['summary'], body_style))
    #         story.append(Paragraph('Treatments', bold_style))
    #         for sentence in item['sentences']:
    #             story.append(Paragraph(sentence, body_style))
    #         story.append(Spacer(1, 0.2 * inch))


    story.append(PageBreak()) 
    story.append(smallLogo)
    story.append(AbsolutePositionedText("A.I. Medical Scientist", right_offset=45, y=5))
    story.append(Paragraph("Surgical - Symptomatic Treatments", title_style))
    story.append(Paragraph(f"Surgical Treatments for symptoms related to {research_topic}", centered_style))
    if(symptomatic_surgery_treatments is not None):
        for item in json.loads(symptomatic_surgery_treatments):
            print(item)
            story.append(Paragraph(item['title'], bold_style_title))
            story.append(Paragraph('Summary', bold_style))
            story.append(Paragraph(item['summary'], body_style))
            story.append(Paragraph('Treatments', bold_style))
            for sentence in item['sentences']:
                story.append(Paragraph(sentence, body_style))
            story.append(Spacer(1, 0.2 * inch))
    story.append(PageBreak()) 

    # story.append(Paragraph("Vitamin", bold_style))
    # if(symptomatic_vitamin_treatments is not None):
    #     for item in json.loads(symptomatic_vitamin_treatments):
    #         print(item)
    #         story.append(Paragraph(item['title'], body_style))
    #         story.append(Paragraph(item['summary'], body_style))
    #         for sentence in item['sentences']:
    #             story.append(Paragraph(sentence, body_style))
    #         story.append(Spacer(1, 0.5 * inch))
    #     story.append(Spacer(1, 0.5 * inch))


    # story.append(Paragraph(title, title_style))
    # story.append(Paragraph("Report Generated "+ today, centered_style))
    # story.append(Spacer(1, 0.2 * inch))
    # story.append(Paragraph(content, body_style))
    # story.append(Spacer(1, 0.5 * inch))
    # story.append(Paragraph("Hardcoded Footer", body_style))
    
    # Build the PDF
    doc.build(story)
