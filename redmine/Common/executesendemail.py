from redmine.Common.sendEmail import SendSmptEmail
from redmine.Common.lastest_report import latest_report

report_url = r'E:\\pythonfile\redmine\\Reports'
SendSmptEmail.send_email(latest_report(report_url))
