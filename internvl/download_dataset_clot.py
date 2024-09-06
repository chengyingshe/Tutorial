from modelscope.hub.api import HubApi
api = HubApi()
api.login('8295c677-b6c1-4d53-8b5b-b4eac302704e')

#数据集下载
from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('shan233/CLoT-Oogiri-GO', subset_name='default', split='train')
#您可按需配置 subset_name、split，参照“快速使用”示例代码