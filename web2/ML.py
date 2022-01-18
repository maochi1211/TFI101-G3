import mplfinance as mpf
import yfinance as yf
import pandas as pd
import cv2
import time
import datetime


def etl_img(company, search_start_date, search_end_date):
    candlestickdata = yf.download('%s' % company, start=search_start_date, end=search_end_date, interval='1d')
    df = pd.DataFrame(candlestickdata)
    df = df.reindex(columns=['Open', 'Close', 'High', 'Low', 'Volume'])
    mc = mpf.make_marketcolors(up='r', down='g', edge='inherit', wick='black')
    style = mpf.make_mpf_style(marketcolors=mc)
    mpf.plot(df, type='candle', style=style,savefig=r'static\img\search\%s.jpg' % company,figsize=(9.6, 5.4))


def ml_forecast_v(company):
    config_path = 'YOLO/yolov4-tiny-custom-v.cfg'
    weight_path = 'YOLO/yolov4-tiny-1227_V62.weights'

    net = cv2.dnn_DetectionModel(config_path, weight_path)
    net.setInputSize(608, 608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)

    x_axis = list()
    frame = cv2.imread('static/img/search/%s.jpg' % company)
    with open(r'YOLO/V.names', 'rt') as f:
        names = f.read().rstrip('\n').split('\n')

    try:
        classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.2)

        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            label = '%s' % (names[classId])
            left, top, width, height = box
            tmp_x_axis = left + width
            cv2.rectangle(frame, box, color=(0, 0, 235), thickness=1)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
            x_axis.append(tmp_x_axis)

    except AttributeError:
        print('No value')

    except IndexError:
        pass
    cv2.imwrite('static/img/forecast/%s.jpg' % company, frame)
    return x_axis

def ml_forecast_w(company):
    config_path = 'YOLO/W50_yolov4-tiny-custom.cfg'
    weight_path = 'YOLO/W50_yolov4-tiny-custom_final.weights'

    net = cv2.dnn_DetectionModel(config_path, weight_path)
    net.setInputSize(608, 608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    x_axis = list()
    frame = cv2.imread('static/img/search/%s.jpg' % company)
    with open(r'YOLO/W.names', 'rt') as f:
        names = f.read().rstrip('\n').split('\n')

    try:
        classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.2)
        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            label = '%s' % (names[classId])
            left, top, width, height = box
            tmp_x_axis = left + width
            cv2.rectangle(frame, box, color=(0, 0, 235), thickness=1)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
            x_axis.append(tmp_x_axis)

    except AttributeError:
        print('No value')

    except IndexError:
        pass
    cv2.imwrite('static/img/forecast/%s.jpg' % company, frame)
    return x_axis


def ml_forecast_m(company):
    config_path = 'YOLO/yolov4-tiny-custom-m.cfg'
    weight_path = 'YOLO/M_yolov4-tiny-custom_final.weights'

    net = cv2.dnn_DetectionModel(config_path, weight_path)
    net.setInputSize(608, 608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    x_axis = list()
    frame = cv2.imread('static/img/search/%s.jpg' % company)
    with open(r'YOLO/M.names', 'rt') as f:
        names = f.read().rstrip('\n').split('\n')
    try:
        classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.2)
        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            label = '%s' % (names[classId])
            left, top, width, height = box
            tmp_x_axis = left + width
            cv2.rectangle(frame, box, color=(0, 0, 235), thickness=1)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
            x_axis.append(tmp_x_axis)

    except AttributeError:
        print('No value')

    except IndexError:
        pass
    cv2.imwrite('static/img/forecast/%s.jpg' % company, frame)
    return x_axis


def x_axis_to_date(x_axis, search_start_date, search_end_date):
    date_list = list()
    interval = (datetime.datetime.strptime(search_end_date, '%Y-%m-%d') - datetime.datetime.strptime(search_start_date, '%Y-%m-%d')).days
    for x in x_axis:
        n = (int(x) - 207) / 625 * interval
        date = datetime.datetime.strptime(search_start_date, '%Y-%m-%d') + datetime.timedelta(days=n)
        time_format = date.strftime('%Y-%m-%d')
        date_list.append(time_format)
    return date_list
