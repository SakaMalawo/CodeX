<template>
  <div class="app-container">
    <MainNavbar v-if="showNavbar" :darkMode="darkMode" @toggle-dark-mode="toggleDarkMode" />
    <div class="content-wrapper">
      <MainSidebar 
        v-if="showSidebar"
        :darkMode="darkMode" 
        @toggle-collapse="handleSidebarCollapse"
      />
      <main
        class="main-content"
        :class="{
          'md:pl-64': !sidebarCollapsed,
          'md:pl-20': sidebarCollapsed,
          'tablet-padding': isTablet
        }"
      >
        <div class="content-container">
          <router-view v-slot="{ Component }">
            <component :is="Component" :darkMode="darkMode" :sidebarCollapsed="sidebarCollapsed" />
          </router-view>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import MainNavbar from './components/MainNavbar.vue';
import MainSidebar from './components/MainSidebar.vue';

export default {
  components: { MainNavbar, MainSidebar },
  data() {
    return {
      darkMode: false,
      sidebarCollapsed: false,
      isTablet: false
    };
  },
  computed: {
    showNavbar() {
      return !['Home', 'AppPage'].includes(this.$route.name);
    },
    showSidebar() {
      return !['Home', 'AppPage'].includes(this.$route.name);
    }
  },
  methods: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      localStorage.setItem('darkMode', this.darkMode);
      document.documentElement.classList.toggle('dark', this.darkMode);
    },
    handleSidebarCollapse(collapsed) {
      this.sidebarCollapsed = collapsed;
    },
    checkViewport() {
      this.isTablet = window.innerWidth >= 768 && window.innerWidth < 1024;
    },
    initializeDarkMode() {
      const savedMode = localStorage.getItem('darkMode');
      if (savedMode !== null) {
        this.darkMode = savedMode === 'true';
      } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        this.darkMode = true;
      }
      document.documentElement.classList.toggle('dark', this.darkMode);
    }
  },
  mounted() {
    this.initializeDarkMode();
    this.checkViewport();
    window.addEventListener('resize', this.checkViewport);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkViewport);
  }
};
</script>

<style>
.app-container {
  @apply min-h-screen flex flex-col bg-white dark:bg-gray-900;
}

.content-wrapper {
  @apply flex flex-1;
}

.main-content {
  @apply flex-1 mt-16 transition-all duration-300 ease-in-out;
  min-height: calc(100vh - 4rem);
}

.content-container {
  @apply w-full max-w-full mx-auto px-4 py-6 sm:px-6 lg:px-8;
  transition: padding-left 0.3s ease-in-out;
}

.tablet-padding {
  padding-left: 1rem;
  padding-right: 1rem;
}

@media (min-width: 768px) and (max-width: 1023px) {
  .main-content {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  .content-container {
    max-width: 100%;
  }
}

@media (max-width: 767px) {
  .main-content {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
}
</style>