# Python 接口自动化测试练习

本项目为个人学习 Python 自动化测试的实战练习仓库，使用 Pytest 框架与 Requests 库对公开 API 进行接口测试。

## 🛠 技术栈
- Python
- Pytest
- Requests

## 📁 包含模块
- `test_api.py`：基础 GET/POST 请求及状态码断言。
- `test_fixture_demo.py`：使用 Fixture 提取公共前置条件（基础 URL）。
- `test_parametrize.py`：使用 `@pytest.mark.parametrize` 实现数据驱动测试。
- `test_login.py`：模拟登录接口，校验返回的 JSON 数据一致性。

*(状态：持续学习中，将不断完善测试用例与自动化框架...)*
