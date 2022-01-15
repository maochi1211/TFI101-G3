from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import heapq


app = Flask(__name__, static_url_path='/static', static_folder='./static')

sexDic = {'男': 0, '女': 1}

jobDic = {'農牧業': 24, '漁業': 31, '木材森林業': 24, '礦業採石業': 28, '交通運輸業': 16, '餐旅業': 17, '建築工程業': 7, '製造業': 8, '新聞廣告業': 20,
           '衛生保健業': 5, '娛樂業': 21, '文教機關': 11, '宗教團體': 27, '公共事業': 4, '一般商業': 6, '服務業': 2, '家庭管理': 10,
           '治安人員': 22, '軍人': 15, '科技業': 0, '職業運動人員': 25, '金融業': 3, '學生': 14, '自由業': 1, '退休人士': 18, '一般職業':12,
           '業務': 9, '全職投資': 13, '會計': 19}

riskDic = {'台股': 2, 'ETF': 1, '台指期貨': 4, '權證': 5, '選擇權': 5, '美股': 2, '海外期貨': 4, '股票期貨': 3, '外匯': 5, '外股': 2, '基金': 1,
           '房地產': 1, '加密貨幣': 3, '原油': 2, '黃金': 2, '債券': 1, '保險': 1}

joinTimeDic = {'一~三年': 0, '十年以上': 4, '三~五年': 2, '五~十年': 3, '一年內': 1}

@app.route('/typeClassfication', methods=['GET', 'POST'])
def featureInput():

    if request.method == 'POST':

        '''
    
            featuresVec[0] = dataset.loc[i, 'SexIndex']
            featuresVec[1] = dataset.loc[i, 'jobIndex']
            featuresVec[2] = dataset.loc[i, 'age']
            featuresVec[3] = dataset.loc[i, 'riskIndex']
            featuresVec[4] = dataset.loc[i, 'joinTimeIndex']
    
        '''


        features = []
        sexIndex = request.form.get("sex")
        sexIndex = sexDic.get(sexIndex)
        features.append(float(sexIndex))

        jobIndex = request.form.get("job")
        jobIndex = jobDic.get(jobIndex)
        features.append(float(jobIndex))

        age = request.form.get("age")
        features.append(float(age))

        riskIndex = request.form.getlist('selectpicker')
        risk = 0
        for i in riskIndex:
            risk += riskDic.get(i)
        risk = risk / len(riskIndex)
        features.append(risk)

        joinTimeIndex = request.form.get("invest_time")
        joinTimeIndex = joinTimeDic.get(joinTimeIndex)
        features.append(float(joinTimeIndex))

        featuresInput = np.array(features)
        featuresInput = featuresInput.reshape(1, 5)
        # print(featuresInput.shape)
        # print(request.form)

        model = load_model('./modelTag_V3.h5', compile=False)
        predicted = model.predict(featuresInput)

        # print(predicted)
        # print("type:{}".format(np.where(predicted == np.max(predicted))[1]), "weight:{}".format(np.max(predicted)))
        # print(predicted[0])
        resh = predicted[0]
        top_k = 3
        top_k_idx = resh.argsort()[::-1][0:top_k]
        predictedType = top_k_idx+1
        print("困擾類型:", predictedType)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
