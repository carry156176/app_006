import allure


class TestStep:
    @allure.step("测试步骤1")
    def test_step(self):
        allure.attach("步骤描述，比如第一步登录","附件")
