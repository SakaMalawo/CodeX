import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import AppPage from "../views/AppPage.vue";
import Dashboard from "../views/Dashboard.vue";

const routes = [
  { path: "/Home", name: "Home", component: Home },
  { path: "/AppPage", name: "AppPage", component: AppPage },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
