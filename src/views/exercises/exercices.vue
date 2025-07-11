<template>
  <section :class="['min-h-screen w-full mt-16 md:ml-64 px-4 py-6 flex flex-col items-center', darkMode ? 'bg-[#10192b] text-white' : 'bg-gray-50 text-gray-900']" style="box-shadow:none; border-radius:0;">
    <h1 class="text-3xl font-bold text-center mb-8">Exercices interactifs</h1>
    <!-- 🧩 Grille des thèmes -->
    <div class="w-full max-w-6xl grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-6">
      <div
        v-for="item in themes"
        :key="item.nom"
        :class="['shadow-lg rounded-xl p-5 text-center hover:shadow-2xl hover:-translate-y-1 transition cursor-pointer', darkMode ? 'bg-[#17213a] text-white' : 'bg-white text-gray-900']"
        @click="naviguer(item.route)"
      >
        <div class="text-4xl mb-3">{{ item.emoji }}</div>
        <h2 class="font-semibold text-lg">{{ item.nom }}</h2>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Exercices",
  props: {
    darkMode: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      themes: [
        { nom: "Probabilités", emoji: "🎲", route: "/exercices/probabilites" },
        { nom: "Statistiques", emoji: "📊", route: "/exercices/statistiques" },
        { nom: "Matrices", emoji: "🧮", route: "/exercices/matrices" },
        { nom: "Vecteurs", emoji: "↔️", route: "/exercices/vecteurs" },
        { nom: "Sciences naturelles", emoji: "🌿", route: "/exercices/sciences" },
        { nom: "Algèbre", emoji: "➕", route: "/exercices/algebre" },
        { nom: "Physique", emoji: "⚡", route: "/exercices/physique" },
        { nom: "Chimie", emoji: "🧪", route: "/exercices/chimie" },
        { nom: "Informatique", emoji: "💻", route: "/exercices/informatique" },
        { nom: "Langues", emoji: "🗣️", route: "/exercices/langues" },
        // ... tu peux ajouter d'autres blocs ici
      ],
    };
  },
  methods: {
    naviguer(route) {
      this.$router.push(route);
    },
  },
};
</script>