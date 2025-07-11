<template>
  <div
    class="min-h-screen flex flex-col dark:bg-gray-900 dark:text-white bg-white text-gray-900 transition-colors duration-300"
  >
    <template v-if="$route.name !== 'Home' && $route.name !== 'AppPage'">
      <MainNavbar :darkMode="darkMode" @toggle-dark-mode="toggleDarkMode" />
      <div class="flex flex-1">
        <MainSidebar :darkMode="darkMode" />
        <main class="mt-16 md:ml-64 w-full transition-all duration-300">
          <router-view v-slot="{ Component }">
            <component :is="Component" :darkMode="darkMode" />
          </router-view>
        </main>
        <Haybot />
      </div>
    </template>
    <template v-else>
      <router-view />
    </template>
  </div>
</template>

<script>
import MainNavbar from "./components/MainNavbar.vue";
import MainSidebar from "./components/MainSidebar.vue";
import Haybot from "./components/Haybot.vue";
export default {
  components: { MainNavbar, MainSidebar, Haybot },
  data() {
    return {
      darkMode: false,
    };
  },
  methods: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      if (this.darkMode) {
        document.documentElement.classList.add("dark");
        document.body.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
        document.body.classList.remove("dark");
      }
      this.persistDarkMode();
    },
    persistDarkMode() {
      this.$emit("dark-mode-changed", this.darkMode);
    },
    initializeDarkMode() {
      if (
        window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches
      ) {
        this.darkMode = true;
        document.documentElement.classList.add("dark");
      }
    },
  },
  created() {
    this.initializeDarkMode();
  },
  mounted() {
    if (window.matchMedia) {
      const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
      mediaQuery.addEventListener("change", (e) => {
        this.darkMode = e.matches;
        if (e.matches) {
          document.documentElement.classList.add("dark");
        } else {
          document.documentElement.classList.remove("dark");
        }
      });
    }
  },
};
</script>
