from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

final_report = pd.read_csv('final_data_report.csv')
summary_final_report = pd.read_csv('Summary_final_report.csv')
selected_fiscal_year = None
selected_company = None

def financial_chatbot(user_input):
    global selected_fiscal_year, selected_company
    
    user_input = user_input.lower()
    if "hi" in user_input:
        return "Hello! Welcome to AI Driven Financial Chatbot!!!\n\nI can help you with your financial queries. Please select the company name from below:\n1. Microsoft\n2. Tesla\n3. Apple"
    elif any(company in user_input for company in ['microsoft', 'tesla', 'apple']):
        selected_company = [company for company in ['microsoft', 'tesla', 'apple'] if company in user_input][0].capitalize()
        return f"Would you like to review performance annually or on a year-by-year basis?"
    elif "performance annually" in user_input:
        return f".We have data available for the fiscal years 2021, 2022, and 2023 for {selected_company}. Please specify the year you'd like insights on:2021, 2022 or 2023"
    elif "year-by-year basis" in user_input:
        return f"What information are you looking to explore?"
    elif any(year in user_input for year in ['2023', '2022', '2021']):
        selected_fiscal_year = [year for year in ['2023', '2022', '2021'] if year in user_input][0]
        return f"Got it! You've selected the fiscal year {selected_fiscal_year}. Let's dive into the insights for that specific year. What information are you looking to explore?"
    elif "average revenue growth rate" in user_input:
        if selected_company is None:
            return "Please select a company first."
        year_avg_revenue_growth = summary_final_report[(summary_final_report['Company'] == selected_company)]['Revenue Growth (%)']
        if year_avg_revenue_growth.empty:
            return f"No data found for average revenue growth rate for {selected_company}."
        return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {selected_company} is {year_avg_revenue_growth.values[0].round(4)}(%)."

    elif "total revenue" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        revenue = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Total Revenue']
        if revenue.empty:
            return f"No Total Revenue data found for {selected_company} for fiscal year {selected_selected_fiscal_year}."
        return f"The Total Revenue for {selected_company} for fiscal year {selected_fiscal_year} is $ {revenue.values[0]}"
        
    elif "average net income growth rate" in user_input:
        if selected_company is None:
            return "Please select a company first."
        # Get the net income growth data for the selected company
        net_income_growth_data = summary_final_report[summary_final_report['Company'] == selected_company]['Net Income Growth (%)']
        
        if net_income_growth_data.empty:
            return f"No data available for net income growth rate for {selected_company}."
        return f"The Year By Year Net Income Revenue Growth Rate(%) from 2021 to 2023 for {selected_company} is {net_income_growth_data.values[0].round(4)}(%)"
       
    elif "net income" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        net_income = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Net Income']
        if net_income.empty:
            return f"No Net Income data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Net Income for {selected_company} for fiscal year {selected_fiscal_year} is $ {net_income.values[0]}"

    elif "sum of total assets" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        total_assets = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Total Assets']
        if total_assets.empty:
            return f"No Total Assets data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The sum of Total Assets for {selected_company} for fiscal year {selected_fiscal_year} is $ {total_assets.values[0]}"
        
    elif "sum of total liabilities" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        total_liabilities = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Total Liabilities']
        if total_liabilities.empty:
            return f"No Total Liabilities data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The sum of Total Liabilities for {selected_company} for fiscal year {selected_fiscal_year} is $ {total_liabilities.values[0]}"
        
    elif "cash flow from operating activities" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        cash_ops = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Cash Flow from Operating Activities']
        if cash_ops.empty:
            return f"No Cash Flow from Operating Activities data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Cash Flow from Operating Activities for {selected_company} for fiscal year {selected_fiscal_year} is $ {cash_ops.values[0]}"
        
    elif "revenue growth" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        revenue_growth = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Revenue Growth (%)']
        if revenue_growth.empty:
            return f"No Revenue Growth data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Revenue Growth(%) for {selected_company} for fiscal year {selected_fiscal_year} is {revenue_growth.values[0].round(4)}(%)."

    elif "net income growth" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        net_income_growth = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Net Income Growth (%)']
        if net_income_growth.empty:
            return f"No Net Income Growth data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Net Income Growth(%) for {selected_company} for fiscal year {selected_fiscal_year} is {net_income_growth.values[0].round(4)}(%)."

    elif "average assets growth rate" in user_input:
            if selected_company is None:
                return "Please select a company first."
            year_avg_assets_growth = summary_final_report[(summary_final_report['Company'] == selected_company)]['Assets Growth (%)']
            if year_avg_assets_growth.empty:
                return f"No data found for average assets growth rate for {selected_company}."
            return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {selected_company} is {year_avg_assets_growth.values[0].round(4)}(%)."

    elif "assets growth" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        assets_growth = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Assets Growth (%)']
        if assets_growth.empty:
            return f"No Assets Growth data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Assets Growth(%) for {selected_company} for fiscal year {selected_fiscal_year} is {assets_growth.values[0].round(4)}(%)."
 
    elif "average liabilities growth rate" in user_input:
            if selected_company is None:
                return "Please select a company first."
            year_avg_liabilities_growth = summary_final_report[(summary_final_report['Company'] == selected_company)]['Liabilities Growth (%)']
            if year_avg_liabilities_growth.empty:
                return f"No data found for average liabilities growth rate for {selected_company}."
            return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {selected_company} is {year_avg_liabilities_growth.values[0].round(4)}(%)."

    elif "liabilities growth" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        liabilities_growth = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Liabilities Growth (%)']
        if liabilities_growth.empty:
            return f"No Liabilities Growth data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Liabilities Growth(%) for {selected_company} for fiscal year {selected_fiscal_year} is {liabilities_growth.values[0].round(4)}(%)."
    elif "average cash flow from operations growth rate" in user_input:
        if selected_company is None:
            return "Please select a company first."
        year_avg_cash_ops_growth = summary_final_report[(summary_final_report['Company'] == selected_company)]['Cash Flow from Operations Growth(%)']
        if year_avg_cash_ops_growth.empty:
            return f"No data found for average cash flow from operations growth rate for {selected_company}."
        return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {selected_company} is {year_avg_cash_ops_growth.values[0].round(4)}(%)."

    elif "cash flow from operations growth" in user_input:
        if selected_fiscal_year is None or selected_company is None:
            return "Please select both a fiscal year and a company first."
        cash_ops_growth = final_report[(final_report['Year'] == int(selected_fiscal_year)) & (final_report['Company'] == selected_company)]['Cash Flow from Operations Growth(%)']
        if cash_ops_growth.empty:
            return f"No Cash Flow from Operations Growth data found for {selected_company} for fiscal year {selected_fiscal_year}."
        return f"The Cash Flow from Operations Growth(%) for {selected_company} for fiscal year {selected_fiscal_year} is {cash_ops_growth.values[0].round(4)}(%)."
    else:
        return "Sorry, I can only provide information on predefined queries."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    response = financial_chatbot(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
