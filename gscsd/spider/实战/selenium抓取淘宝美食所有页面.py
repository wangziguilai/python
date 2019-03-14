
#通过修改页数来操作======失败了，改变页数也改变不了页面，也没有看到设定不可修改
from selenium import webdriver
import time
from pyquery import PyQuery as pq

driver = webdriver.Firefox()
def getPagNum():
    driver.get('https://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&keyword=%E5%A5%B3%E8%A3%85&clk1=1be055f1586f0d2d0ca0d5d9fb43d2a3&upsid=1be055f1586f0d2d0ca0d5d9fb43d2a3')
    input_key = driver.find_element_by_xpath('//*[@id="q"]')
    input_key.clear()
    time.sleep(2)
    input_key.send_keys('美食')
    time.sleep(2)
    start_handle = driver.current_window_handle  # 跳转之前得到当前页面
    print('第一次页面的句柄值：', start_handle)
    driver.find_element_by_xpath('//*[@id="J_searchForm"]/input[4]').click()
    time.sleep(3)  # 一定要延时，不然没加载完新页面，要么是旧页面的数据，要么获取错误
    all_handles = driver.window_handles  # 跳转之后得到页面的全部handle
    for handle in all_handles:  # 遍历全部页面句柄
        if handle != start_handle:  # 判断条件
            driver.switch_to.window(handle)  # 移动句柄
    pagNum = driver.find_element_by_xpath('//*[@id="J_waterfallPagination"]/div/div/a[3]').text
    return int(pagNum)

def paging(maxNum):
    for i in range(1, maxNum+1):
        page_key = driver.find_element_by_xpath('//*[@id="Jumper"]')
        print('i = ', i)
        page_key.send_keys(i)
        start_handle = driver.current_window_handle  # 跳转之前得到当前页面
        print('第二次页面的句柄值：', start_handle)
        driver.find_element_by_xpath('//*[@id="J_waterfallPagination"]/div/div/a[6]').click()
        print('当前的句柄值： ', driver.current_window_handle)
        print('所有的句柄值：', driver.window_handles)
        print('当前页面URL： ', driver.current_url)
        current_handle = driver.current_window_handle
        time.sleep(3)  # 一定要延时，不然没加载完新页面，要么是旧页面的数据，要么获取错误
        all_handles = driver.window_handles  # 跳转之后得到页面的全部handle
        # for handle in all_handles:  # 遍历全部页面句柄
        #     if handle != start_handle:  # 判断条件
        #         driver.switch_to.window(handle)  # 移动句柄
        driver.switch_to.window(current_handle)
        content = driver.find_element_by_xpath('//*[@id="ItemWrapper"]').get_attribute('outerHTML')
        html = pq(content)
        data = html('div.item div.info').items()
        for i in data:
            name = i('span.title').text()
            parce = i('span.pricedetail strong').text().strip('')
            shopName = i('span.shopNick').text()
            payNum = i('span.payNum').text()
            pingfeng = i('span.dsr-info-num').text()
        #     print(name, parce, shopName, payNum, pingfeng)
        # print('---------------------')


def main():
    maxPageNum = getPagNum()
    paging(maxPageNum)
if __name__ == '__main__':
    main()
