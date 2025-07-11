<template>
  <aside
    :class="[
      darkMode
        ? 'bg-gray-800/90 border-gray-700 text-white'
        : 'bg-gray-100/80 border-gray-200 text-gray-900',
      'fixed transition-all duration-300 z-40',
      'md:top-16 md:h-[calc(100vh-4rem)] md:border-r',
      isMobile ? 'bottom-0 w-full h-16 border-t' : (collapsed ? 'md:w-20' : 'md:w-64'),
      'backdrop-blur-md'
    ]"
    style="border-right-width: 1px; border-top-width: 1px"
  >
    <!-- Bouton de collapse/expand -->
    <button
      @click="toggleCollapse"
      v-if="!isMobile"
      class="flex items-center justify-center w-8 h-8 rounded-full absolute -right-4 top-4 z-50 transition-all duration-300 shadow-md"
      :class="{
        'bg-gray-700 hover:bg-gray-600 text-gray-300': darkMode,
        'bg-white hover:bg-gray-100 text-gray-600': !darkMode,
      }"
    >
      <svg
        class="h-5 w-5 transition-transform duration-300"
        :class="{ 'rotate-180': collapsed }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>

    <div class="flex flex-col h-full overflow-hidden">
      <!-- Menu principal -->
      <nav :class="isMobile ? 'h-full grid grid-cols-5' : 'flex-1 px-3 py-4'">
        <div :class="isMobile ? 'flex' : 'space-y-1'">
          <div
            v-for="item in items"
            :key="item.key"
            class="sidebar-btn-wrapper"
          >
            <button
              @click="navigateTo(item.key)"
              class="sidebar-btn group w-full"
              :class="{
                'bg-indigo-50 dark:bg-indigo-900/30': activeItem === item.key,
                'hover:bg-gray-100 dark:hover:bg-gray-700': activeItem !== item.key,
                'text-gray-900 dark:text-white': true,
                'justify-center': collapsed || isMobile,
                'justify-start': !collapsed && !isMobile,
              }"
            >
              <span
                class="icon-container rounded-full flex-shrink-0 flex items-center justify-center"
                :class="{
                  'bg-indigo-500 text-white': activeItem === item.key,
                  'bg-gray-200 dark:bg-gray-600 group-hover:bg-gray-300 dark:group-hover:bg-gray-500': activeItem !== item.key,
                  'w-10 h-10': collapsed && !isMobile,
                  'w-9 h-9': !collapsed || isMobile,
                }"
              >
                <span v-if="item.icon" v-html="item.icon" class="flex items-center justify-center"></span>
              </span>
              <span
                class="sidebar-label"
                :class="{
                  'hidden': collapsed && !isMobile,
                  'block': !collapsed || isMobile,
                }"
              >
                {{ item.label }}
              </span>
            </button>
          </div>
        </div>
      </nav>

      <!-- Réseaux sociaux (masqué en mobile) -->
      <div 
        v-if="!isMobile"
        class="mt-auto px-3 py-4 border-t"
        :class="{
          'border-gray-700': darkMode,
          'border-gray-200': !darkMode,
        }"
      >
        <div 
          class="flex"
          :class="{
            'justify-center space-x-4': !collapsed,
            'flex-col items-center space-y-3': collapsed,
          }"
        >
          <a 
            v-for="(social, index) in socials"
            :key="index"
            :href="social.url" 
            target="_blank" 
            rel="noopener noreferrer"
            class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            :class="darkMode ? social.color.dark : social.color.light"
          >
            <span v-html="social.icon" class="flex items-center justify-center w-5 h-5"></span>
          </a>
        </div>
      </div>
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
  data() {
    return {
      activeItem: "dashboard",
      isMobile: false,
      collapsed: false,
      items: [
        {
          key: "dashboard",
          name: "dashboard",
          label: "Tableau de bord",
          icon: `<svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>`,
        },
        {
          key: "courses",
          name: "courses",
          label: "Cours",
          icon: `<svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>`,
        },
        {
          key: "services",
          name: "services",
          label: "Services",
          icon: `<svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>`,
        },
        {
          key: "forum",
          name: "forum",
          label: "Forum",
          icon: `<div class='relative h-5 w-5'><svg class="h-4 w-4 absolute top-0 left-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg><svg class="h-4 w-4 absolute top-0.5 left-0.5 opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg></div>`,
        },
        {
          key: "exercises",
          name: "exercises",
          label: "Exercices",
          icon: `<svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>`,
        },
      ],
      socials: [
        {
          name: 'facebook',
          url: 'https://facebook.com',
          icon: `<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>`,
          color: {
            light: 'text-blue-600',
            dark: 'text-blue-400'
          }
        },
        {
          name: 'instagram',
          url: 'https://instagram.com',
          icon: `<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>`,
          color: {
            light: 'text-pink-600',
            dark: 'text-pink-400'
          }
        },
        {
          name: 'twitter',
          url: 'https://twitter.com',
          icon: `<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg>`,
          color: {
            light: 'text-blue-400',
            dark: 'text-blue-300'
          }
        },
        {
          name: 'pinterest',
          url: 'https://pinterest.com',
          icon: `<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738a.36.36 0 01.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/></svg>`,
          color: {
            light: 'text-red-600',
            dark: 'text-red-400'
          }
        }
      ],
    };
  },
  watch: {
    isMobile(newVal) {
      if (newVal) {
        this.collapsed = false;
      }
    },
  },
  mounted() {
    this.checkMobile();
    window.addEventListener("resize", this.checkMobile);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkMobile);
  },
  methods: {
    toggleCollapse() {
      this.collapsed = !this.collapsed;
      this.$emit('toggle-collapse', this.collapsed);
    },
    navigateTo(item) {
      this.activeItem = item;
      const routes = {
        dashboard: "/dashboard",
        courses: "/cours",
        services: "/services",
        forum: "/forum",
        exercises: "/exercices",
      };
      this.$router.push(routes[item] || "/");
    },
    checkMobile() {
      this.isMobile = window.innerWidth < 768;
    },
  },
};
</script>

<style scoped>
.sidebar-btn {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  border-radius: 0.75rem;
  width: 100%;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  gap: 0.75rem;
}

.icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar-label {
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sidebar-btn-wrapper {
  width: 100%;
  margin: 0.125rem 0;
}

/* Styles desktop */
@media (min-width: 768px) {
  .sidebar-btn {
    padding: 0.5rem;
  }
  
  .sidebar-label {
    opacity: 1;
    width: auto;
    margin-left: 0.75rem;
  }
  
  .collapsed .sidebar-label {
    opacity: 0;
    width: 0;
    margin-left: 0;
    display: none;
  }
}

/* Styles mobile */
@media (max-width: 767px) {
  aside {
    width: 100vw;
    height: 4.5rem;
    border-top-width: 1px;
  }

  nav {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    height: 100%;
    padding: 0 0.5rem;
    gap: 0.25rem;
  }

  .sidebar-btn {
    flex-direction: column;
    padding: 0.25rem;
    gap: 0.25rem;
    border-radius: 0.5rem;
    justify-content: center;
    height: 100%;
  }

  .icon-container {
    width: 2rem;
    height: 2rem;
    margin: 0 auto;
  }
  
  .sidebar-label {
    font-size: 0.65rem;
    text-align: center;
    line-height: 1.2;
    opacity: 1 !important;
    width: auto !important;
    margin-left: 0 !important;
    display: block !important;
  }
  
  .sidebar-btn-wrapper {
    display: flex;
    justify-content: center;
    height: 100%;
  }
}

/* Fond transparent */
aside {
  background-color: rgba(243, 244, 246, 0.8);
  backdrop-filter: blur(12px);
}

.dark aside {
  background-color: rgba(31, 41, 55, 0.9);
}
</style>