import axios from "axios";

export default {
  addAuthorizationHeader(config) {
    return {
      ...config,
      headers: { Authorization: `JWT ${config.token}` }
    };
  },
  all(config) {
    return axios.get("/api/boards/", this.addAuthorizationHeader(config));
  },
  create(resource, config) {
    return axios.post(
      "/api/boards/",
      resource,
      this.addAuthorizationHeader(config)
    );
  },
  read(resource, config) {
    return axios.get(
      "/api/boards/" + resource.id + "/",
      this.addAuthorizationHeader(config)
    );
  },
  update(resource, config) {
    return axios.put(
      "/api/boards/" + resource.id + "/",
      resource,
      this.addAuthorizationHeader(config)
    );
  },
  delete(resource, config) {
    return axios.delete(
      "/api/boards/" + resource.id + "/",
      this.addAuthorizationHeader(config)
    );
  }
};
