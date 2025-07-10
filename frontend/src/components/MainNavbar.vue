<template>
  <nav
    :class="[
      darkMode
        ? 'bg-gray-800 border-b border-gray-700'
        : 'bg-gray-100 border-b border-gray-300 shadow',
      'fixed top-0 left-0 right-0 h-16 z-50 transition-colors duration-300 px-4 flex items-center justify-between backdrop-blur-md',
    ]"
  >
    <!-- MOBILE NAVBAR -->
    <div class="flex w-full items-center justify-between md:hidden">
      <button
        @click="toggleMobileMenu"
        class="p-2 rounded-md focus:outline-none"
        :class="{
          'text-gray-400 hover:text-white': darkMode,
          'text-gray-600 hover:text-gray-900': !darkMode,
          'hover:border hover:border-indigo-400': true,
        }"
      >
        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      <div class="flex items-center gap-2">
        <div class="relative w-10 h-10 flex items-center justify-center">
          <img src="/logoHay.png" alt="Logo HAY" class="w-full h-full object-contain" style="filter: drop-shadow(0 0 24px #38bdf8) drop-shadow(0 0 12px #38bdf8);" />
        </div>
        <h1 class="hay-title text-2xl font-bold" :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }">
          HAY
        </h1>
      </div>

      <div class="flex items-center gap-2">
        <button
          @click="$emit('toggle-dark-mode')"
          class="p-2 rounded-full focus:outline-none hover:border hover:border-indigo-400"
          :class="{
            'hover:bg-gray-700': darkMode,
            'hover:bg-gray-200': !darkMode,
          }"
        >
          <svg v-if="darkMode" class="h-7 w-7 text-yellow-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else class="h-7 w-7 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>

        <div class="relative">
          <button
            @click.stop="navigateToMessages"
            class="p-1 rounded-full focus:outline-none relative hover:border hover:border-indigo-400"
            :class="{
              'text-gray-400 hover:text-white': darkMode,
              'text-gray-600 hover:text-indigo-600': !darkMode,
            }"
          >
            <svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span v-if="unreadMessages.length > 0" class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
              {{ unreadMessages.length }}
            </span>
          </button>
        </div>
      </div>
    </div>

    <!-- DESKTOP NAVBAR -->
    <div class="hidden md:flex w-full items-center">
      <div class="flex items-center gap-3 mr-4">
        <div class="relative w-12 h-12 flex items-center justify-center">
          <img src="/logoHay.png" alt="Logo HAY" class="w-full h-full object-contain" style="filter: drop-shadow(0 0 32px #38bdf8) drop-shadow(0 0 16px #38bdf8);" />
        </div>
        <h1 class="hay-title text-3xl font-bold" :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }">
          HAY
        </h1>
      </div>

      <div class="flex-1 flex justify-center">
        <div class="relative w-full max-w-md">
          <input
            type="text"
            placeholder="Rechercher..."
            :class="{
              'bg-gray-700 text-white placeholder-gray-300': darkMode,
              'border-gray-300': !darkMode,
            }"
            class="w-full pl-5 pr-10 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-300"
          />
          <div class="absolute right-3 top-2.5">
            <svg
              :class="{
                'text-gray-400': !darkMode,
                'text-gray-500': darkMode,
              }"
              class="h-5 w-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="flex items-center space-x-6 ml-4">
        <button
          @click="$emit('toggle-dark-mode')"
          class="p-2 rounded-full focus:outline-none hover:border hover:border-indigo-400"
          :class="{
            'hover:bg-gray-700': darkMode,
            'hover:bg-gray-200': !darkMode,
          }"
        >
          <svg v-if="darkMode" class="h-7 w-7 text-yellow-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else class="h-7 w-7 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>

        <div class="relative">
          <button
            @click.stop="toggleDropdown('messages')"
            class="p-1 rounded-full focus:outline-none relative hover:border hover:border-indigo-400"
            :class="{
              'text-gray-400 hover:text-white': darkMode,
              'text-gray-600 hover:text-indigo-600': !darkMode,
            }"
          >
            <svg class="h-7 w-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span v-if="unreadMessages.length > 0" class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
              {{ unreadMessages.length }}
            </span>
          </button>

          <div
            v-show="activeDropdown === 'messages'"
            class="origin-top-right absolute right-0 mt-2 w-80 rounded-md shadow-lg z-50"
            :class="{ 'bg-gray-700': darkMode, 'bg-white': !darkMode }"
          >
            <div class="py-1">
              <div class="px-4 py-2 border-b" :class="{ 'border-gray-600': darkMode, 'border-gray-100': !darkMode }">
                <p :class="{ 'text-gray-300': darkMode, 'text-gray-700': !darkMode }" class="text-sm font-medium">
                  Messages
                </p>
              </div>

              <div v-if="unreadMessages.length > 0" class="max-h-60 overflow-y-auto">
                <div
                  v-for="message in unreadMessages"
                  :key="message.id"
                  @click="markAsRead(message.id)"
                  class="px-4 py-3 cursor-pointer hover:bg-opacity-10 hover:bg-indigo-400"
                  :class="{
                    'text-gray-300': darkMode,
                    'text-gray-700': !darkMode,
                  }"
                >
                  <div class="flex items-center">
                    <img :src="message.sender.avatar" class="h-8 w-8 rounded-full mr-3">
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-medium truncate">
                        {{ message.sender.name }}
                      </p>
                      <p class="text-xs truncate">
                        {{ message.preview }}
                      </p>
                    </div>
                    <span class="text-xs" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">
                      {{ formatTime(message.time) }}
                    </span>
                  </div>
                </div>
              </div>

              <div v-else class="px-4 py-4 text-center text-sm" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">
                Aucun nouveau message
              </div>

              <div class="px-4 py-2 border-t text-center" :class="{ 'border-gray-600': darkMode, 'border-gray-100': !darkMode }">
                <button
                  @click="navigateToMessages"
                  :class="{
                    'text-indigo-400 hover:text-indigo-300': darkMode,
                    'text-indigo-600 hover:text-indigo-500': !darkMode,
                  }"
                  class="text-sm font-medium"
                >
                  Voir tous les messages
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="relative">
          <button
            @click.stop="toggleDropdown('profile')"
            class="flex items-center text-sm rounded-full focus:outline-none hover:border hover:border-indigo-400"
            :class="{
              'ring-2 ring-indigo-500': activeDropdown === 'profile',
            }"
          >
            <img class="h-9 w-9 rounded-full" :src="user.photo" />
          </button>
        </div>
      </div>
    </div>

    <!-- MENU MOBILE -->
    <div
      v-if="mobileMenuOpen"
      class="md:hidden fixed top-16 left-0 right-0 shadow-lg py-2 px-4 z-40"
      :class="{ 'bg-gray-800': darkMode, 'bg-white': !darkMode }"
    >
      <div class="mb-4">
        <input
          type="text"
          placeholder="Rechercher..."
          :class="[
            'w-full pl-5 pr-10 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-300',
            darkMode
              ? 'bg-gray-800 text-white placeholder-gray-400 border-gray-700'
              : 'bg-white text-gray-900 placeholder-gray-400 border-gray-300',
          ]"
        />
      </div>
      <button
        @click="navigateToMessages"
        class="block py-2 w-full text-left"
        :class="darkMode ? 'text-white' : 'text-gray-900'"
      >
        Messages
        <span v-if="unreadMessages.length > 0" class="ml-2 bg-red-500 text-white text-xs rounded-full px-2 py-0.5">
          {{ unreadMessages.length }}
        </span>
      </button>
    </div>
  </nav>
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
      activeDropdown: null,
      mobileMenuOpen: false,
      user: {
        photo: "https://randomuser.me/api/portraits/men/1.jpg",
      },
      unreadMessages: [
        {
          id: 1,
          sender: {
            name: "Jean Dupont",
            avatar: "https://randomuser.me/api/portraits/men/1.jpg"
          },
          preview: "Salut, comment ça va ? J'ai une question...",
          time: new Date(Date.now() - 1000 * 60 * 5), // 5 minutes ago
          read: false
        },
        {
          id: 2,
          sender: {
            name: "Marie Martin",
            avatar: "https://randomuser.me/api/portraits/women/1.jpg"
          },
          preview: "Réunion demain à 10h, n'oublie pas !",
          time: new Date(Date.now() - 1000 * 60 * 60 * 2), // 2 hours ago
          read: false
        }
      ]
    };
  },
  methods: {
    toggleDropdown(dropdown) {
      if (this.activeDropdown === dropdown) {
        this.activeDropdown = null;
      } else {
        this.activeDropdown = dropdown;
      }
    },
    closeDropdowns() {
      this.activeDropdown = null;
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.closeDropdowns();
      }
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
    markAsRead(messageId) {
      const message = this.unreadMessages.find(m => m.id === messageId);
      if (message && !message.read) {
        message.read = true;
        this.navigateToMessages();
      }
    },
    navigateToMessages() {
      this.$router.push('/Message');
      this.closeDropdowns();
      this.mobileMenuOpen = false;
    },
    formatTime(date) {
      const now = new Date();
      const diff = now - date;
      
      if (diff < 60000) return 'à l\'instant';
      if (diff < 3600000) return `${Math.floor(diff / 60000)} min`;
      
      if (date.toDateString() === now.toDateString()) {
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      }
      
      const yesterday = new Date(now);
      yesterday.setDate(yesterday.getDate() - 1);
      if (date.toDateString() === yesterday.toDateString()) {
        return 'Hier';
      }
      
      if (date.getFullYear() === now.getFullYear()) {
        return date.toLocaleDateString([], { month: 'short', day: 'numeric' });
      }
      
      return date.toLocaleDateString([], { year: 'numeric', month: 'short', day: 'numeric' });
    }
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeDestroy() {
    document.removeEventListener("click", this.handleClickOutside);
  },
};
</script>

<style scoped>
.hay-title {
  font-family: 'Arial', sans-serif;
  letter-spacing: 1px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.backdrop-blur-md {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}
</style>