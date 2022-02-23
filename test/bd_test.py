import PublicDataReader as pdr

serviceKey = "sfSPRX%2BxNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy%2Fnxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA%3D%3D"

bd = pdr.Building(serviceKey, debug=True)
sigunguName = "분당구"                                  # 시군구코드: 41135
code = pdr.code_list()
var = code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) & (code['읍면동명'].isna())]

category = "표제부"                                   # 건축물대장 종류 (ex. 표제부, 총괄표제부, 전유부 등)
sigunguCd = "11260"                                     # 시군구코드(5)
bjdongCd = "10100"                                      # 읍면동코드(5)
bun = "0090"                                            # 본번(4)
ji = "0027"                                             # 부번(4)

df = bd.read_data(category=category, sigunguCd=sigunguCd, bjdongCd=bjdongCd, bun=bun, ji=ji)
df.head()
print(df)