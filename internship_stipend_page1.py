from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

intershala_url = "https://internshala.com/internships/keywords-python/page-1"
uClient = uReq(intershala_url)
intershala_Page = uClient.read()
uClient.close()
intershala_html = bs(intershala_Page, "html.parser")
company1 = intershala_html.findAll("div", {
    "class":"container-fluid individual_internship"})
stipend = company1[0].find_all_next("span", {"class": "stipend"})
result_page1 = []
for idx in range(len(stipend)):
    result_page1.append(stipend[idx].text)
print(result_page1)
length_result_page1 = len(result_page1)
print("length of initial list", length_result_page1)

final_list = []
for ele in result_page1:
    salary = "".join(ele.lstrip().split(" /month"))
    if len(salary) < 6:
        final_list.append(int(salary))
    elif len(salary) > 5:
        if "-" in salary:
            salary = list(map(int, salary.split("-")))
            avg = (salary[0] + salary[1]) / 2
            final_list.append(avg)
        elif " lump sum +  Incentives" in salary:
            salary = "".join(salary.split(" lump sum +  Incentives"))
            final_list.append(int(salary))
        elif " +  Incentives" in salary:
            salary = "".join(salary.split(" +  Incentives"))
            final_list.append(int(salary))
        elif " lump sum" in salary:
            salary = "".join(salary.split(" lump sum"))
            final_list.append(int(salary))

total_stipend_page1 = sum(final_list)
print("final list:", final_list)
print("length of the final list", len(final_list))
print("total stipend is equal to:", total_stipend_page1)
print("Average stipend is equal to:", total_stipend_page1 / length_result_page1)