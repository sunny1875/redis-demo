import requests
def test_set_and_get():
    # 测试set接口
    set_resp = requests.get('http://localhost:5000/set/name/test')
    assert 'success' in set_resp.text
    # 测试get接口
    get_resp = requests.get('http://localhost:5000/get/name')
    assert 'test' in get_resp.text
    print('✅ All tests passed!')
if __name__ == '__main__':
    test_set_and_get()
