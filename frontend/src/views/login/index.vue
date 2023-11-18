<script setup lang="ts">
import { reactive, ref } from "vue";
// onMounted, onUnmounted,
// import { useRouter } from 'vue-router'
import { ElMessage, FormInstance, TabsPaneContext } from "element-plus";
import {
  User,
  Lock,
  Message,
  ChatRound,
  Iphone,
  Location,
  Suitcase,
} from "@element-plus/icons-vue";
import { UserLogin } from "@/api/login";
import { UserRegister } from "@/api/register";
import router from "@/router";

const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event);
};

// const router = useRouter()
const labelPosition = ref("left");

const loginForm = reactive({
  username: "",
  password: "",
});

const registerForm = reactive({
  username: "",
  password: "",
  first_name: "",
  last_name: "",
  email: "",
  gender: "",
  phone: "",
  user_type: "",
  company: "",
  position: "",
});

const loginFormRef = ref<FormInstance>();
const registerFormRef = ref<FormInstance>();

const submitForm = (formEl: FormInstance | undefined) => {
  console.log(111);

  if (!formEl) return;
  formEl.validate(async (valid) => {
    if (valid && activeName.value === "first") {
      await UserLogin(loginForm.username, loginForm.password).then((res) => {
        console.log(res.data);
        sessionStorage.setItem("token", res.data.access);
        ElMessage.success("登录成功");
        router.push("/point-view/content/black");
      });
    } else if (valid && activeName.value === "second") {
      await UserRegister(
        registerForm.username,
        registerForm.password,
        registerForm.first_name,
        registerForm.last_name,
        registerForm.email,
        registerForm.gender,
        registerForm.phone,
        registerForm.user_type,
        registerForm.company,
        registerForm.position
      )
        .then((res) => {
          console.log(res);
          ElMessage.success("注册成功");
          router.push("/home");
        })
        .catch((err) => {
          console.log(err);
          ElMessage.error("已存在一位使用该名字的用户");
        });
    } else {
      console.log("error submit!");
      return false;
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};

const loginRules = {
  username: [
    { required: true, message: "请输入账号", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  password: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 2, message: "长度在 5个字符以上", trigger: "blur" },
  ],
};

const registerRules = {
  username: [
    { required: true, message: "请输入账号", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  password: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 5, message: "长度在 5个字符以上", trigger: "blur" },
  ],
  email: [
    { required: true, message: "请输入邮箱", trigger: "blur" },
    { type: "email", message: "请输入正确的邮箱", trigger: ["blur", "change"] },
  ],
  first_name: [
    { required: true, message: "请输入姓", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  last_name: [
    { required: true, message: "请输入名", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  gender: [{ required: true, message: "请输入性别", trigger: "change" }],
  phone: [
    { required: true, message: "请输入电话", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  user_type: [{ required: true, message: "请输入用户类型", trigger: "change" }],
  company: [
    { required: true, message: "请输入公司", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
  position: [
    { required: true, message: "请输入职位", trigger: "blur" },
    { min: 2, message: "长度在 2个字符以上", trigger: "blur" },
  ],
};

</script>

<template>
  <div class="login-box">
    <div class="top-header">
      <div class="logo-left">Welcome to Online-shop</div>
      <div class="user-right">
        <p>
          账号
          <el-icon color="#fff">
            <UserFilled />
          </el-icon>
        </p>
      </div>
    </div>
    <el-tabs
      v-model="activeName"
      :stretch="true"
      class="login-tabs"
      @tab-click="handleClick"
    >
      <el-tab-pane label="登录" name="first" class="tab-item">
        <el-form
          ref="loginFormRef"
          :rules="loginRules"
          :label-position="labelPosition"
          :model="loginForm"
          style="max-width: 400px"
        >
          <el-form-item prop="username">
            <el-input
              :prefix-icon="User"
              placeholder="账号"
              v-model="loginForm.username"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              :prefix-icon="Lock"
              placeholder="密码"
              type="password"
              show-password
              v-model="loginForm.password"
              @keydown.enter="submitForm(loginFormRef)"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm(loginFormRef)"
              >登录</el-button
            >
            <el-button @click="resetForm(loginFormRef)">重置</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="注册" name="second" class="tab-item">
        <el-form
          ref="registerFormRef"
          :rules="registerRules"
          :label-position="labelPosition"
          :model="registerForm"
          style="max-width: 460px"
        >
          <el-form-item prop="username">
            <el-input
              :prefix-icon="User"
              placeholder="账号"
              v-model="registerForm.username"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              :prefix-icon="Lock"
              placeholder="密码"
              type="password"
              show-password
              v-model="registerForm.password"
            />
          </el-form-item>
          <el-form-item prop="email">
            <el-input
              :prefix-icon="Message"
              placeholder="邮箱"
              v-model="registerForm.email"
            />
          </el-form-item>
          <el-form-item prop="first_name">
            <el-input
              :prefix-icon="ChatRound"
              placeholder="姓"
              v-model="registerForm.first_name"
            />
          </el-form-item>
          <el-form-item prop="last_name">
            <el-input
              :prefix-icon="Message"
              placeholder="名"
              v-model="registerForm.last_name"
            />
          </el-form-item>

          <el-form-item prop="phone">
            <el-input
              :prefix-icon="Iphone"
              placeholder="电话"
              v-model="registerForm.phone"
            ></el-input>
          </el-form-item>
          <el-form-item prop="company">
            <el-input
              :prefix-icon="Location"
              placeholder="公司"
              v-model="registerForm.company"
            ></el-input>
          </el-form-item>
          <el-form-item prop="position">
            <el-input
              :prefix-icon="Suitcase"
              placeholder="职位"
              v-model="registerForm.position"
            ></el-input>
          </el-form-item>
          <el-form-item prop="gender">
            <el-radio-group v-model="registerForm.gender" class="gender-box">
              <el-radio label="female" border>女</el-radio>
              <el-radio label="male" border>男</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="user_type">
            <el-radio-group
              v-model="registerForm.user_type"
              class="user-type-box"
              @keydown.enter="submitForm(registerFormRef)"
            >
              <el-radio label="individual" border>个人</el-radio>
              <el-radio label="enterprise" border>企业</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm(registerFormRef)"
              >登录</el-button
            >
            <el-button @click="resetForm(registerFormRef)">重置</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<style scoped lang="less">
.login-box {
  background-image: url("@/assets/image/bg.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 100vh;
  padding-bottom: 50px;
}

.top-header {
  width: 100%;
  height: 40px;
  background-color:  #ed1c24;  
  display: flex;
  align-items: center;
  justify-content: space-between;

  .search-input {
    width: 300px;
  }

  .user-right {
    margin-right: 50px;
    color: #fff;

    p {
      display: inline-flex;
      align-items: center;
      .el-icon {
        margin-left: 5px;
      }
    }
  }
}

.login-tabs {
  margin: 50px auto;
  border-radius: 8px;
  width: 500px;
  // height: 400px;
  background-color: #fff;

  .tab-item {
    padding: 20px 50px;
  }

  .el-form {
    margin: 20px;
    text-align: center;
  }
}

.gender-box {
  width: 100%;
}

.user-type-box {
  width: 100%;
}

:deep(.el-radio.is-bordered) {
  width: 25%;
}

:deep(.el-tabs__header) {
  padding: 50px 50px 0px;
}

:deep(.el-form-item__content) {
  justify-content: center;
}
</style>
