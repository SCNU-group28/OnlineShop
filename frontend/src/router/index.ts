// import { createRouter, createWebHistory } from "vue-router";
import { createRouter, createWebHistory } from "vue-router";

//路由对应表

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      redirect: "/login",
      path: "/",
    },
    {
      path: "/login",
      name: "login",
      meta: { isAuth: false },
      //懒加载
      component: () => import("@/views/login/index.vue"),
    },
    {
      path: "/main",
      name: "colored",
      meta: { isAuth: true },
      component: () => import("@/views/main/index.vue"),
      // children: [
      //   {
      //   },
      // ],
    },
    {
      path: "/main",
      name: "main",
      meta: { isAuth: false },
      component: () => import("@/views/login/index.vue"),
      // children: [
      //   {
      //   },
      // ],
    },
  ],
},
)

export default router;
