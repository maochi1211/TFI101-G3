from flask import Flask, render_template, request
from yahoo_fin.stock_info import tickers_sp500
import model
import ML


app = Flask(__name__, static_url_path='/static', static_folder='./static')


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/typev', methods=['GET', 'POST'])
def type_v():
    tickers_list = tickers_sp500()
    company = request.form.get("company")
    search_start_date = request.form.get("start_date")
    search_end_date = request.form.get("end_date")
    data = ()
    forecast_date = []
    if request.method == 'POST':
        ML.etl_img(company, search_start_date, search_end_date)
        x_axis = ML.ml_forecast_v(company)
        forecast_date = ML.x_axis_to_date(x_axis, search_start_date, search_end_date)
        data = model.search_ROI(company, forecast_date)
    return render_template('IndexV.html', tickers_list=tickers_list, data=data, company=company,
                           search_start_date=search_start_date, search_end_date=search_end_date,
                           forecast_date=forecast_date)


@app.route('/typew', methods=['GET', 'POST'])
def type_w():
    tickers_list = tickers_sp500()
    company = request.form.get("company_w")
    search_start_date = request.form.get("start_date_w")
    search_end_date = request.form.get("end_date_w")
    data = ()
    forecast_date = []
    if request.method == 'POST':
        ML.etl_img(company, search_start_date, search_end_date)
        x_axis = ML.ml_forecast_w(company)
        forecast_date = ML.x_axis_to_date(x_axis, search_start_date, search_end_date)
        data = model.search_ROI(company, forecast_date)
    return render_template('IndexW.html', tickers_list=tickers_list, data=data, company=company,
                           search_start_date=search_start_date, search_end_date=search_end_date,
                           forecast_date=forecast_date)


@app.route('/typem', methods=['GET', 'POST'])
def type_m():
    tickers_list = tickers_sp500()
    company = request.form.get("company_m")
    search_start_date = request.form.get("start_date_m")
    search_end_date = request.form.get("end_date_m")
    data = ()
    forecast_date = []
    if request.method == 'POST':
        ML.etl_img(company, search_start_date, search_end_date)
        x_axis = ML.ml_forecast_m(company)
        forecast_date = ML.x_axis_to_date(x_axis, search_start_date, search_end_date)
        data = model.search_ROI(company, forecast_date)
    return render_template('IndexM.html',tickers_list=tickers_list, data=data, company=company,
                           search_start_date=search_start_date, search_end_date=search_end_date,
                           forecast_date=forecast_date)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


