import base64
import json
import requests

header = {"Host": "cloud.eais.go.kr",
          "Content-Type": "application/json;charset=UTF-8",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
          "Referer": "https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01"}

data = {"param": "UP0YaT6dECzlUetdlnt%2FHF8CFL%2BS2naXIGMEtIOrSCK2x5DBWZPwF7mh4hxFbpLY7Kb9Bj7qgLOomE8XfI02nLVStfX9nS4d%2B3cR%2BBPQoxI76vG36GhMSofhXJ%2F5EnX9TT8c%2FCgqHidQftABdMjG7NHVdqequygLqzDPjIPg3xt9BNb71VE1Yaxvw%2FMH4a7HEweSoXyE8WfcpNnHyLcbi5D7v0N5EWlvipSvr9FZd9f2wtis2sCPP6bLmly%2B27vJBVodXHmTw%2FZ9B4Vi1TiOaNfrqmWfeLL2GsRtEofLAGSD6yQgXOOu7yxAK3ncwJk4jNXxR6rxZTJi9wQqcV1vJcJPjSNEnTosIqpOyH0MMjBk5IE9nQbObrFbhpVRrf9hHKGpQqACWYmXxqXmPO8bnZkvoXmE%2BrmmguYFICBdNkWBpKJHOuR%2BC5ZHxlXlSDMbvAjz4zP0L9yhufgD2YWWPh6HzrZfkA4aTHLnWaDoJByKSAd4ErQlF%2FRzada93G2%2B4sKNm184nUJo5yLzerygwsuhDddoUImYcLbLLW%2Fvy0VXxgM8cUwjnMDysSPkKa8NUbe9VHgUK5ckzreh8sSsz5BixfK95LeNR%2BsBQ%2Fry2Xwczfh4i0f7wG2zZhYYIb8jFM4OQyGel5ARvB5lZb5ZrKFlI6HbWrvvwc6b%2Fk%2BrbnTgUVVN7xOGa5osG%2BkNMzexzbs8ItA%3D%3D"}

url = 'https://cloud.eais.go.kr/report/BCIAAA04V01?param=asd&actionId=BCIAAA04L01'
result = requests.get(url, headers=header)
print(result.text)
