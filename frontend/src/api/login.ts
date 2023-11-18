import api from "./axios";

export const UserLogin = (username: any, password: string) =>
  api({
    url: "/api/account/login/",
    method: "post",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    data: {
      username,
      password,
    },
  });
