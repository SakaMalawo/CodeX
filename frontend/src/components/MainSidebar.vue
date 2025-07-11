<template>
  <aside
    :class="[
      darkMode
        ? 'bg-gray-800/90 border-gray-700'
        : 'bg-gray-100/80 backdrop-blur-md border-gray-200 shadow-md',
      'fixed md:w-64 w-full md:left-0 md:top-[4rem] md:h-[calc(100vh-4rem-1px)] md:border-r z-40 bottom-0 md:bottom-auto transition-colors duration-300',
    ]"
    style="left: 0; border-right-width: 1px"
  >
    <!-- Chevron collapse/expand supprimé, sidebar toujours visible sans bouton -->
    <!-- contenu de la sidebar -->
    <div class="flex flex-col h-full md:h-auto md:flex-col">
      <nav
        :class="
          isMobile
            ? 'sidebar-mobile-grid'
            : 'flex-1 px-2 py-4 space-y-2 flex md:flex-col'
        "
      >
        <div
          v-for="item in items"
          :key="item.key"
          :class="[
            'sidebar-btn-wrapper',
            activeItem === item.key ? 'bg-indigo-gradient text-white' : '',
          ]"
        >
          <button
            @click="navigateTo(item.key)"
            class="sidebar-btn"
            :class="{
              'text-white': activeItem === item.key,
              'text-gray-600 hover:bg-gray-100 hover:border-l-4 hover:border-indigo-400':
                activeItem !== item.key && !darkMode,
              'text-gray-300 hover:bg-gray-700 hover:border-l-4 hover:border-indigo-400':
                activeItem !== item.key && darkMode,
            }"
          >
            <span v-if="item.icon" v-html="item.icon"></span>
            <span class="sidebar-label">{{ item.label }}</span>
          </button>
        </div>
      </nav>
    </div>
  </aside>
</template>

<script>
export default {
  props: {
    darkMode: {
      type: Boolean,
      required: true,
    },
  },
  // emits: ['update:collapsed'],
  data() {
    return {
      activeItem: "dashboard",
      isMobile: false,
      // isCollapsed supprimé, sidebar toujours visible
      items: [
        {
          key: "dashboard",
          name: "dasboard",
          label: "Tableau de bord",
          icon: `<svg class="h-7 w-7 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>`,
        },
        {
          key: "courses",
          name: "courses",
          label: "Cours",
          icon: `<svg class="h-7 w-7 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>`,
        },
        {
          key: "services",
          name: "services",
          label: "Services",
          icon: `<svg class="h-7 w-7 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>`,
        },
        {
          key: "forum",
          name: "forum",
          label: "Forum",
          icon: `<div class='relative h-7 w-7 flex-shrink-0'><svg class="h-5 w-5 absolute top-0 left-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg><svg class="h-5 w-5 absolute top-1 left-1 opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg></div>`,
        },
        {
          key: "exercises",
          name: "exercisess",
          label: "Exercices",
          icon: `<svg class="h-7 w-7 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>`,
        },
      ],
    };
  },
  // watch supprimé, sidebar toujours visible
  mounted() {
    this.checkMobile();
    window.addEventListener("resize", this.checkMobile);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkMobile);
  },
  methods: {
    navigateTo(item) {
      this.activeItem = item;
      // Correspondance clé -> route
      let route = "/";
      switch (item) {
        case "dashboard":
          route = "/dashboard";
          break;
        case "courses":
          route = "/cours";
          break;
        case "services":
          route = "/generate";
          break;
        case "forum":
          route = "/forum";
          break;
        case "exercises":
          route = "/exercices";
          break;
        default:
          route = "/";
      }
      this.$router.push(route);
      this.$emit("item-changed", item);
    },
    checkMobile() {
      this.isMobile = window.innerWidth <= 768;
    },
  },
};
</script>

<style scoped>
.transition-opacity {
  transition-property: opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
.bg-indigo-gradient {
  background-image: linear-gradient(
    to right,
    rgba(79, 70, 229, 0.9),
    rgba(124, 58, 237, 0.9)
  );
}
.sidebar-label {
  margin-top: 0.25rem;
  @apply md:mt-0 md:ml-3 text-lg transition-opacity duration-200 hidden md:block;
}
.sidebar-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 0 0.25rem 0;
  border-radius: 0;
  min-width: 0;
  margin: 0;
  transition: background 0.2s;
  width: 100%;
  height: 100%;
}
.sidebar-btn-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
}
@media (min-width: 769px) {
  .sidebar-btn {
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 0.75rem;
    border-radius: 0.375rem;
    height: auto;
  }
  .sidebar-label {
    display: block !important;
  }
  .sidebar-btn-wrapper {
    height: auto;
  }
}
@media (max-width: 768px) {
  aside {
    width: 100vw !important;
    left: 0 !important;
    right: 0 !important;
    top: auto !important;
    bottom: 0 !important;
    height: 4rem !important;
    border-right-width: 0 !important;
    border-top-width: 1px !important;
    border-color: #e5e7eb !important;
    display: flex !important;
    flex-direction: row !important;
    z-index: 50;
  }
  .sidebar-mobile-grid {
    display: grid !important;
    grid-template-columns: repeat(5, 1fr) !important;
    width: 100vw !important;
    gap: 0 !important;
    justify-content: space-between !important;
    align-items: stretch !important;
    padding: 0 !important;
    height: 100%;
  }
  .sidebar-btn-wrapper {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: stretch;
  }
  .sidebar-btn {
    width: 100%;
    height: 100%;
    min-width: 0;
    border-radius: 0 !important;
    margin: 0 !important;
    padding: 0.5rem 0 0.25rem 0 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.25rem !important;
  }
  .sidebar-label {
    display: none !important;
  }
}
</style>
