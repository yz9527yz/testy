import jsonpath
import requests
from pip._internal.network import session


url = "https://meiya-yf.meiya.com/external/tmcapi/loggerold/tmc/intra/Finance/FinanceCenter/QueryShouldReceiveList"
json ='{"Sid":"20230060","JavaSid":"20230060","pageIndex":1,"pageSize":200,"desc":"false","orderNoList":"","billNoList":"","tabOrderNoList":"","ticketNoList":"","groupCode":"NG001267","clientCode":"NC00001369","clientDepartmentID":"","processBeginDate":"2025-05-16","processEndDate":"2025-06-16 23:59:59","subProductType":"-1","pnrNo":"","amountBegin":"","amountEnd":"","offlineOrderType":"-1","nodeStr":"'meiyasl','konggu','tonghangsyb','20200001','chailushiye','gqdj','jtcwzxin','shkf_ty','cwmygzz15'","limitNode":"","isUnSorceOrder":0,"clientRefundStatus":"-1","clientRefundBeginDate":"","clientRefundEndDate":"","repaymentType":"-1","sellCurrency":""}'
requests.post(url=url,json=json)