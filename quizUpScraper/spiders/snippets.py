i=0
while i < (len(response.xpath('//tr[contains(@class, "row")]'))-1):
    print(response.xpath('//td[contains(@class, "column-1")]/text()').extract()[i])
    i=i+1

