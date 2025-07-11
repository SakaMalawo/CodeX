<template>
  <main
    :class="[
      'min-h-screen flex flex-col items-center justify-center py-12',
      darkMode ? 'bg-gray-800 text-white' : 'bg-white text-gray-900',
    ]"
  >
    <img
      :src="user.avatar"
      alt="Photo de profil"
      class="w-24 h-24 rounded-full shadow-lg mb-6"
    />
    <h1 class="text-3xl font-bold mb-2">Bonjour {{ user.name }} !</h1>
    <p class="mb-8 text-center text-lg max-w-md">
      Nous sommes ravi de t'accueillir sur la Plateforme
      <span class="font-semibold text-green-500">Hay</span>
    </p>
    <button
      @click="goToDashboard"
      class="px-8 py-3 rounded-full bg-green-500 text-white font-semibold text-lg shadow hover:bg-green-600 transition"
    >
      Commencer
    </button>
  </main>
</template>

<script>
export default {
  name: "AppPage",
  data() {
    return {
      user: {
        name: "Saka",
        avatar: "https://randomuser.me/api/portraits/men/32.jpg",
      },
    };
  },
  computed: {
    darkMode() {
      return document.documentElement.classList.contains("dark");
    },
  },
  methods: {
    goToDashboard() {
      this.$router.push("/dashboard");
    },
  },
};
</script>
