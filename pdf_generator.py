from fpdf import FPDF 
import pandas as pd
import matplotlib.pyplot as plt


def simple_table(spacing=3):
    data = [['MODEL', 'RMSE', 'PARAMETERS'],
            ['GradientBoostRegressor', '679.00129', 'n_estimators=100'],
            ['GradientBoostRegressor500', '592.70065', 'n_estimators=500'],
            ['RandomForestRegressor', '547.71650', 'n_estimators=100'],
            ['RandomForestRegressor500', '540.62785', 'n_estimators=500']
            ]
    
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 12)

    pdf.text(60,10,"Kaggle Diamond Competition")
    pdf.text(10,20,"Pablo Estévez")
    pdf.text(80,20,'Model & RMSE')

    """
    pdf.set_xy(10, 20)
    col_width = pdf.w / 2
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=2)
        pdf.ln(row_height*spacing)
    """
    col_width = pdf.w / 4
    th = pdf.font_size
    epw = pdf.w - 3*pdf.l_margin
        
    pdf.ln(4*th)
    
    pdf.set_font('Times','B',14.0) 
    pdf.set_font('Times','',10.0) 
    pdf.ln(2)
    
    # Here we add more padding by passing 2*th as height
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 4*th, str(datum), border=1)
    
        pdf.ln(4*th)
    

    pdf.output('pablo_estevez.pdf')

simple_table()
