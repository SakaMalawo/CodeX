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
      <!-- Burger menu à gauche -->
      <button
        @click="toggleMobileMenu"
        class="p-2 rounded-md focus:outline-none"
        :class="{
          'text-gray-400 hover:text-white': darkMode,
          'text-gray-600 hover:text-gray-900': !darkMode,
          'hover:border hover:border-indigo-400': true,
        }"
      >
        <svg
          class="h-6 w-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
      </button>
      <!-- Logo/flamme + titre au centre -->
      <div class="flex items-center gap-2">
        <div class="relative w-10 h-10 flex items-center justify-center">
          <img src="/logoHay.png" alt="Logo HAY" class="w-full h-full object-contain" style="filter: drop-shadow(0 0 24px #38bdf8) drop-shadow(0 0 12px #38bdf8);" />
        </div>
        <h1
          class="hay-title text-2xl font-bold"
          :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }"
        >
          HAY
        </h1>
      </div>
      <!-- Darkmode et Profil à droite -->
      <div class="flex items-center gap-2">
        <button
          @click="$emit('toggle-dark-mode')"
          class="p-2 rounded-full focus:outline-none hover:border hover:border-indigo-400"
          :class="{
            'hover:bg-gray-700': darkMode,
            'hover:bg-gray-200': !darkMode,
          }"
        >
          <svg
            v-if="darkMode"
            class="h-7 w-7 text-yellow-300"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
            />
          </svg>
          <svg
            v-else
            class="h-7 w-7 text-gray-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
            />
          </svg>
        </button>
        <!-- Profil (mobile) -->
        <div class="relative">
          <button
            @click.stop="toggleDropdown('profile')"
            class="flex items-center justify-center p-2 rounded-full focus:outline-none hover:border hover:border-indigo-400"
            :class="{
              'ring-2 ring-indigo-500': activeDropdown === 'profile',
              'text-gray-400 hover:text-white': darkMode,
              'text-gray-600 hover:text-indigo-600': !darkMode,
            }"
          >
            <!-- Petit bonhomme (User Icon) -->
            <img
              :src="Super_User_photo"
              alt="Admin"
              class="w-8 h-8 ring-2 ring-gray-500 rounded-full"
              :class="{ 'ring-2 ring-green-500': darkmode }"
            />
          </button>
          <!-- Dropdown Profil (mobile) -->
          <div
            v-show="activeDropdown === 'profile'"
            class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg z-50"
            :class="{ 'bg-gray-700': darkMode, 'bg-white': !darkMode }"
          >
            <div class="py-1">
              <div
                class="px-4 py-2 border-b"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <p :class="{ 'text-gray-300': darkMode }" class="text-sm">
                  Connecté en tant que
                </p>
                <p
                  :class="{
                    'text-white': darkMode,
                    'text-gray-900': !darkMode,
                  }"
                  class="text-sm font-medium truncate"
                >
                  utilisateur@example.com
                </p>
              </div>
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Profil</a
              >
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Paramètres</a
              >
              <div
                class="border-t"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              ></div>
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Déconnexion</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- DESKTOP NAVBAR -->
    <div class="hidden md:flex w-full items-center">
      <!-- Logo et titre à gauche -->
      <div class="flex items-center gap-3 mr-4">
        <div class="relative w-12 h-12 flex items-center justify-center">
          <img src="/logoHay.png" alt="Logo HAY" class="w-full h-full object-contain" style="filter: drop-shadow(0 0 32px #38bdf8) drop-shadow(0 0 16px #38bdf8);" />
        </div>
        <h1
          class="hay-title text-3xl font-bold"
          :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }"
        >
          HAY
        </h1>
      </div>
      <!-- Barre de recherche centrée -->
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
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </div>
        </div>
      </div>
      <!-- Actions à droite -->
      <div class="flex items-center space-x-6 ml-4">
        <!-- Darkmode -->
        <button
          @click="$emit('toggle-dark-mode')"
          class="p-2 rounded-full focus:outline-none hover:border hover:border-indigo-400"
          :class="{
            'hover:bg-gray-700': darkMode,
            'hover:bg-gray-200': !darkMode,
          }"
        >
          <svg
            v-if="darkMode"
            class="h-7 w-7 text-yellow-300"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
            />
          </svg>
          <svg
            v-else
            class="h-7 w-7 text-gray-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
            />
          </svg>
        </button>
        <!-- Messages -->
        <div class="relative">
          <button
            @click.stop="toggleDropdown('messages')"
            class="p-1 rounded-full focus:outline-none relative hover:border hover:border-indigo-400"
            :class="{
              'text-gray-400 hover:text-white': darkMode,
              'text-gray-600 hover:text-indigo-600': !darkMode,
            }"
          >
            <svg
              class="h-7 w-7"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              />
            </svg>
            <span
              v-if="unreadMessages > 0"
              class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
            >
              {{ unreadMessages }}
            </span>
          </button>
          <!-- Dropdown Messages -->
          <div
            v-show="activeDropdown === 'messages'"
            class="origin-top-right absolute right-0 mt-2 w-80 rounded-md shadow-lg z-50"
            :class="{ 'bg-gray-700': darkMode, 'bg-white': !darkMode }"
          >
            <div class="py-1">
              <div
                class="px-4 py-2 border-b"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <p
                  :class="{
                    'text-gray-300': darkMode,
                    'text-gray-700': !darkMode,
                  }"
                  class="text-sm font-medium"
                >
                  Messages
                </p>
              </div>
              <div
                class="px-4 py-4 text-center text-sm"
                :class="{
                  'text-gray-400': darkMode,
                  'text-gray-500': !darkMode,
                }"
              >
                <template v-if="unreadMessages === 0">
                  Aucun nouveau message
                </template>
                <template v-else>
                  Vous avez {{ unreadMessages }} nouveau(x) message(s)
                </template>
              </div>
              <div
                class="px-4 py-2 border-t text-center"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <a
                  href="#"
                  :class="{
                    'text-indigo-400 hover:text-indigo-300': darkMode,
                    'text-indigo-600 hover:text-indigo-500': !darkMode,
                  }"
                  class="text-sm font-medium"
                  >Voir tous</a
                >
              </div>
            </div>
          </div>
        </div>
        <!-- Notifications -->
        <div class="relative">
          <button
            @click.stop="toggleDropdown('notifications')"
            class="p-1 rounded-full focus:outline-none relative hover:border hover:border-indigo-400"
            :class="{
              'text-gray-400 hover:text-white': darkMode,
              'text-gray-600 hover:text-indigo-600': !darkMode,
            }"
          >
            <svg
              class="h-7 w-7"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
              />
            </svg>
            <span
              v-if="unreadNotifications > 0"
              class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
            >
              {{ unreadNotifications }}
            </span>
          </button>
          <!-- Dropdown Notifications -->
          <div
            v-show="activeDropdown === 'notifications'"
            class="origin-top-right absolute right-0 mt-2 w-80 rounded-md shadow-lg z-50"
            :class="{ 'bg-gray-700': darkMode, 'bg-white': !darkMode }"
          >
            <div class="py-1">
              <div
                class="px-4 py-2 border-b"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <p
                  :class="{
                    'text-gray-300': darkMode,
                    'text-gray-700': !darkMode,
                  }"
                  class="text-sm font-medium"
                >
                  Notifications
                </p>
              </div>
              <div
                class="px-4 py-4 text-center text-sm"
                :class="{
                  'text-gray-400': darkMode,
                  'text-gray-500': !darkMode,
                }"
              >
                <template v-if="unreadNotifications === 0">
                  Aucune nouvelle notification
                </template>
                <template v-else>
                  Vous avez {{ unreadNotifications }} nouvelle(s)
                  notification(s)
                </template>
              </div>
              <div
                class="px-4 py-2 border-t text-center"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <a
                  href="#"
                  :class="{
                    'text-indigo-400 hover:text-indigo-300': darkMode,
                    'text-indigo-600 hover:text-indigo-500': !darkMode,
                  }"
                  class="text-sm font-medium"
                  >Voir toutes</a
                >
              </div>
            </div>
          </div>
        </div>
        <!-- Profil -->
        <div class="relative">
          <button
            @click.stop="toggleDropdown('profile')"
            class="flex items-center text-sm rounded-full focus:outline-none hover:border hover:border-indigo-400"
            :class="{
              'ring-2 ring-indigo-500': activeDropdown === 'profile',
            }"
          >
            <img class="h-9 w-9 rounded-full" :src="Super_User_photo" />
          </button>
          <!-- Dropdown Profil -->
          <div
            v-show="activeDropdown === 'profile'"
            class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg z-50"
            :class="{ 'bg-gray-700': darkMode, 'bg-white': !darkMode }"
          >
            <div class="py-1">
              <div
                class="px-4 py-2 border-b"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              >
                <p :class="{ 'text-gray-300': darkMode }" class="text-sm">
                  Connecté en tant que
                </p>
                <p
                  :class="{
                    'text-white': darkMode,
                    'text-gray-900': !darkMode,
                  }"
                  class="text-sm font-medium truncate"
                >
                  {{ Super_User_login }}
                </p>
              </div>
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Profil</a
              >
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Paramètres</a
              >
              <div
                class="border-t"
                :class="{
                  'border-gray-600': darkMode,
                  'border-gray-100': !darkMode,
                }"
              ></div>
              <a
                href="#"
                :class="{
                  'text-gray-300 hover:bg-gray-600': darkMode,
                  'text-gray-700 hover:bg-gray-100': !darkMode,
                  'hover:border-l-4 hover:border-indigo-400': true,
                }"
                class="block px-4 py-2 text-sm"
                >Déconnexion</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- DESKTOP NAVBAR ... (inchangé) ... -->

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
      <a
        href="#"
        class="block py-2"
        :class="darkMode ? 'text-white' : 'text-gray-900'"
        >Accueil</a
      >
      <a
        href="#"
        class="block py-2"
        :class="darkMode ? 'text-white' : 'text-gray-900'"
        >Messages
        <span
          v-if="unreadMessages > 0"
          class="ml-2 bg-red-500 text-white text-xs rounded-full px-2 py-0.5"
        >
          {{ unreadMessages }}
        </span>
      </a>
      <a
        href="#"
        class="block py-2"
        :class="darkMode ? 'text-white' : 'text-gray-900'"
        >Notifications
        <span
          v-if="unreadNotifications > 0"
          class="ml-2 bg-red-500 text-white text-xs rounded-full px-2 py-0.5"
        >
          {{ unreadNotifications }}
        </span>
      </a>
      <!-- Profil supprimé du menu mobile -->
    </div>

    <!-- Logo SVG supprimé, remplacé par logoHay.png -->
  </nav>
</template>

<script>
import photo from "../assets/mimihy.png";
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
      unreadMessages: 2,
      unreadNotifications: 6,
      mobileMenuOpen: false,
      Super_User_login: "admin@hay.com",
      Super_User_photo: photo,
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
.flame-animation {
  animation: flameBlink 3s infinite;
}
@keyframes flameBlink {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
.flame-animation path {
  fill: url(#flame-gradient);
}
</style>
