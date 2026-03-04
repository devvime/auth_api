import path from "path";

export default {
  entry: "./client/javascript/main.js",
  output: {
    path: path.resolve('static', "app"),
    filename: "main.js",
  },
};