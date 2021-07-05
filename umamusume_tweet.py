import tweepy

# 上で取得した各種キーを入れる
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth)

api.update_status('【サポートカード】
駿河たづな　Lv50（完凸）

【代表ウマ娘】
メジロマックイーン
パワー3、固有2、芝2
直線加速2

【親1】
スペシャルウィーク
スピード3、固有1、中距離1
末脚2

【親2】
ダイワスカーレット
パワー3、マイル2
コーナー巧者2、直線巧者1
集中力1、尻尾上がり2、URA1

青因子9URA1')
