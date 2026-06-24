# Fixture 的依赖注入和生命周期管理
import pytest

# 1. 🛠️ 组装一只后勤队：专门负责在测试前“登录系统”
@pytest.fixture
def login_token():
    print("\n🚀 [后勤队出发]：正在启动浏览器，疯狂输入暗号，成功登录！")
    # 登录成功后，后勤队拿到了一个通关令牌（Token）
    return "secret_token_12345"  # 把物资打包好，准备送货

@pytest.fixture
def database_cleaner():
    print("\n🚀 [前置] 连上数据库，疯狂插入测试数据...")
    yield  # ⏸️ 暂停！物资送出，把舞台留给测试用例先跑
    
    # 🎬 当测试用例全部跑完的一瞬间，Pytest 会自动杀个回马枪，执行 yield 后面的代码：
    print("\n🧹 [后勤清洁工上线]：测试结束，正在全量清空测试脏数据，关闭连接！")

# 2. 🎯 测试用例：饭来张口
# 注意：函数参数里直接写了后勤队的名字 `login_token`
def test_view_cart(login_token, database_cleaner):
    print(f"📦 [用例收到快递]：顺利拿到通关令牌 -> {login_token}")
    print("🎬 [正式执行]：成功进入购物车页面进行点检！")

def test_something():
    assert 1 + 1 == 2