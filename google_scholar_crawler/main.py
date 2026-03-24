from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

# 配置代理池，防止被谷歌学术封锁 IP
pg = ProxyGenerator()
# print("正在寻找可用的免费代理，这可能需要几分钟...")
# pg.FreeProxies()
# scholarly.use_proxy(pg)
# print("代理配置完成，开始抓取数据...")
success = pg.ScraperAPI(os.environ.get('SCRAPER_API_KEY'))
scholarly.use_proxy(pg)

# 直接定义GOOGLE_SCHOLAR_ID
GOOGLE_SCHOLAR_ID = "ZKXXk4IAAAAJ"
author: dict = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
scholarly.fill(author, sections=['basics', 'indices', 'counts'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author.get('publications', [])}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
