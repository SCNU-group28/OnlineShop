import api from "./axios";

export const UserRegister = (
  username: Object,
  password: string,
  first_name: string,
  last_name: string,
  email: string,
  gender: string,
  phone: string,
  user_type: string,
  company: string,
  position: string
) =>
  api({
    url: "/api/account/register/",
    method: "post",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    data: {
      username,
      password,
      first_name,
      last_name,
      email,
      gender,
      phone,
      user_type,
      company,
      position,
    },
  });
