<template>
  <div
    class="min-h-screen flex flex-col dark:bg-gray-900 dark:text-white bg-white text-gray-900 transition-colors duration-300"
  >
    <router-view />
  </div>
</template>

<script>
export default {
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
      } else {
        document.documentElement.classList.remove("dark");
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
