

import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import AppPage from "../views/AppPage.vue";
import Dashboard from "../views/Dashboard.vue";
import Message from "../views/Message.vue";
import Cours from "../views/cours/cours.vue";
import Exercices from "../views/exercises/exercices.vue";

const routes = [
  { path: "/Home", name: "Home", component: Home },
  { path: "/AppPage", name: "AppPage", component: AppPage },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/message", name: "Message", component: Message },
  { path: "/cours", name: "Cours", component: Cours },
  { path: "/exercices", name: "Exercices", component: Exercices },
  { path: "/exercices/probabilites", name: "ExercicesProbabilites", component: () => import("../views/exercises/probabilites.vue") },
  { path: "/exercices/statistiques", name: "ExercicesStatistiques", component: () => import("../views/exercises/statistiques.vue") },
  { path: "/exercices/matrices", name: "ExercicesMatrices", component: () => import("../views/exercises/matrices.vue") },
  { path: "/exercices/vecteurs", name: "ExercicesVecteurs", component: () => import("../views/exercises/vecteurs.vue") },
  { path: "/exercices/sciences", name: "ExercicesSciences", component: () => import("../views/exercises/sciences.vue") },
  { path: "/exercices/algebre", name: "ExercicesAlgebre", component: () => import("../views/exercises/algebre.vue") },
  { path: "/exercices/physique", name: "ExercicesPhysique", component: () => import("../views/exercises/physique.vue") },
  { path: "/exercices/chimie", name: "ExercicesChimie", component: () => import("../views/exercises/chimie.vue") },
  { path: "/exercices/informatique", name: "ExercicesInformatique", component: () => import("../views/exercises/informatique.vue") },
  { path: "/exercices/langues", name: "ExercicesLangues", component: () => import("../views/exercises/langues.vue") },
  // Ajoute d'autres routes ici si tu ajoutes d'autres vues
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
