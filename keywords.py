def get_number_of_searches(keywords):
    for text in keywords:
        encoded_string = urllib.parse.quote(text)
        geturl = searchbase + text+".tpo?order=date"
        response = requests.get(geturl)
        soup=BeautifulSoup(response.content,'html.parser')
        numbers = soup.find('h2',class_ = 'box-heading')
        pattern = r'\d+'  # This regex pattern matches one or more digits

        matches = re.findall(pattern, numbers.get_text())
        if matches:
            result = int(matches[0])
            print(str(text) +"\t "+ str(result))


keywords_s = [
    "chuyển đổi số","nền tảng số",
    "số hóa","xã hội số","chính phủ số","tài nguyên số",
    "dịch vụ số","số hóa dữ liệu","số hóa quy trình",
    "doanh nghiệp số", "nguồn nhân lực","nhân lực số","trải nghiệm số",
    "ngân hàng số","giải trí số","giáo dục số","công nghệ số","kinh doanh số",
    "thị trường số","AI","trí tuệ nhân tạo"
]
get_number_of_searches(keywords=keywords_s)
for i in range(0, len(links), 2):
            title = links[i].get('title')
            url = links[i].get('href')
            csv_writer.writerow([title, url])