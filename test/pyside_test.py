import requests
import json
import pandas as pd


s = requests.Session()
headers = {
    "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}


def get_title(pk):
    datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 100}
    res = s.post('https://cloud.eais.go.kr/bldrgsttitle/_search', headers=headers, json=datas)
    json_result = json.loads(res.text)['hits']

    result = pd.DataFrame(columns=['동명칭', 'PK'])

    for n, i in enumerate(json_result['hits']):
        result.loc[n] = {'동명칭': i['_source']['dongNm'], 'PK': i['_id']}

    result = result.sort_values(by=['동명칭'], axis=0)
    result.reset_index(drop=True, inplace=True)

    return result


def get_expos(pk):
    datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 200}
    res = s.post('https://cloud.eais.go.kr/bldrgstexpos/_search', headers=headers, json=datas)
    json_result = json.loads(res.text)['hits']

    result = pd.DataFrame(columns=['동명칭', '호명칭', 'PK'])

    for n, i in enumerate(json_result['hits']):
        info = i['_source']
        result.loc[n] = {'동명칭': info['dongNm'], '호명칭': info['hoNm'], 'PK': i['_id']}

    result['호명칭'] = pd.to_numeric(result['호명칭'])
    result = result.sort_values(by=['호명칭'], axis=0)
    result.reset_index(drop=True, inplace=True)

    return result


print(get_title('11260-100260630'))
print(get_expos(get_title('11260-100260630').loc[4]['PK']))
