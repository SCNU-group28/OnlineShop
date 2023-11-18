import { defineConfig, loadEnv } from "vite";
import { resolve } from "path";
import { UserConfigExport, ConfigEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

// https://vitejs.dev/config/

export default ({ command, mode }: ConfigEnv): UserConfigExport => {
  // 根据当前工作目录中的 `mode` 加载 .env 文件
  // 设置第三个参数为 '' 来加载所有环境变量，而不管是否有 `VITE_` 前缀。
  const env = loadEnv(mode, process.cwd(), "");
  return {
    // vite 配置
    plugins: [vue(), vueJsx()],
    resolve: {
      alias: [
        {
          find: "@",
          replacement: resolve(__dirname, "src"),
        },
      ],
    },
    base: "./", // 打包路径
    server: {
      https: false,
      port: 8484, // 服务端口号
      open: true, // 服务启动时是否自动打开浏览器
      cors: true, // 允许跨域
      host: "0.0.0.0",
      hmr: true,
      proxy: {
        "^/api/.*": {
          // target: env.VITE_TARGET_URL,
          target: env.VITE_TARGET_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  };
};
