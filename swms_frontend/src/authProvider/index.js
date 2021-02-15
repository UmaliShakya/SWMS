export default (apiUrl, options = {}) => {
  return {
    login: ({ username, password }) => {
      const request = new Request(`${apiUrl}/${options.authUrl}/token/login/`, {
        method: "POST",
        body: JSON.stringify({ username, password }),
        headers: new Headers({ "Content-Type": "application/json" }),
      });
      return fetch(request)
        .then((response) => {
          let json = response.json();
          if (response.status >= 200 && response.status < 300) {
            return json;
          } else {
            return json.then((err) => {
              throw err;
            });
          }
        })
        .then(({ auth_token }) => {
          localStorage.setItem("token", auth_token);
        });
    },
    logout: () => {
      localStorage.removeItem("token");
      return Promise.resolve();
    },
    checkError: (error) => {
      const status = error.status;
      if (status < 200 && status >= 300) {
        localStorage.removeItem("token");
        return Promise.reject();
      }
      return Promise.resolve();
    },
    checkAuth: () =>
      localStorage.getItem("token")
        ? Promise.resolve()
        : Promise.reject({ redirectTo: "/no-access" }),
    getPermissions: () => {
      return Promise.resolve();
    },
  };
};
