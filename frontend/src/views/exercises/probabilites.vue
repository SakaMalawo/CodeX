<template>
  <section class="max-w-4xl mx-auto p-6 space-y-6 bg-white dark:bg-gray-900 rounded-xl shadow-lg">
    <button @click="$router.back()" class="btn-secondary mb-4">⬅️ Retour</button>
    <!-- 📘 Leçon interactive -->
    <div class="text-gray-700">
      <h2 class="text-2xl font-bold mb-2">📘 Introduction à la loi binomiale</h2>
      <p>
        La loi binomiale permet de calculer la probabilité d'obtenir exactement k succès dans n essais indépendants,
        avec une probabilité constante p de succès à chaque essai.
      </p>
      <div class="mt-4 bg-indigo-50 p-4 rounded-lg">
        Exemple : Quelle est la probabilité d’obtenir <strong>7 piles</strong> lors de <strong>10 lancers</strong> d’une pièce équilibrée ?
      </div>
    </div>

    <!-- 🎲 Simulateur interactif -->
    <div class="bg-gray-50 p-5 rounded-lg">
      <h3 class="text-xl font-semibold mb-4">🎲 Simulateur de loi binomiale</h3>

      <div class="grid gap-4">
        <label class="block">
          <span class="font-medium">Nombre d’essais (n)</span>
          <input v-model.number="n" type="number" class="input-field" />
        </label>

        <label class="block">
          <span class="font-medium">Probabilité de succès (p)</span>
          <input v-model.number="p" type="number" step="0.01" class="input-field" />
        </label>

        <label class="block">
          <span class="font-medium">Succès observés (k)</span>
          <input v-model.number="k" type="number" class="input-field" />
        </label>

        <button @click="calculer" class="btn-primary">Calculer la probabilité</button>
      </div>

      <p v-if="resultat !== null" class="mt-4 font-semibold text-green-700 text-center">
        Résultat : {{ resultat.toFixed(5) }}
      </p>
    </div>

    <!-- ✅ Bouton vers le quiz -->
    <div class="text-center">
      <button @click="afficherQuiz = true" class="btn-secondary">
        📚 Passer au Quiz
      </button>
    </div>

    <!-- 🧠 Quiz affiché après clic -->
    <div v-if="afficherQuiz" class="mt-6 bg-blue-50 p-4 rounded-lg">
      <h3 class="text-xl font-semibold mb-4">✅ Quiz — vérifie ta compréhension</h3>
      <p>Quel est le bon calcul pour la probabilité de 7 succès sur 10 ?</p>
      <div class="grid gap-3 mt-3">
        <button
          v-for="(opt, i) in options"
          :key="i"
          :class="[
            'px-4 py-2 rounded',
            selected === i ? (i === answer ? 'bg-green-400' : 'bg-red-400') : 'bg-white hover:bg-blue-100',
          ]"
          @click="selected = i"
        >
          {{ opt }}
        </button>
      </div>
      <p v-if="selected !== null" class="mt-4">
        {{ selected === answer ? "🎉 Bonne réponse !" : "❌ Incorrect. Revois la formule binomiale." }}
      </p>
    </div>
  </section>
</template>

<script>
export default {
  name: "ExerciceProbaModule",
  props: { darkMode: Boolean },
  data() {
    return {
      n: 10,
      p: 0.5,
      k: 7,
      resultat: null,
      afficherQuiz: false,
      options: [
        "C(10,7) × (0.5)^7 × (0.5)^3",
        "10 × 0.5",
        "7 × 0.5^7",
        "C(7,10) × 0.5^7",
      ],
      answer: 0,
      selected: null,
    };
  },
  methods: {
    factorial(n) {
      return n <= 1 ? 1 : n * this.factorial(n - 1);
    },
    calculer() {
      const C = this.factorial(this.n) / (this.factorial(this.k) * this.factorial(this.n - this.k));
      const prob = C * Math.pow(this.p, this.k) * Math.pow(1 - this.p, this.n - this.k);
      this.resultat = prob;
    },
  },
};
</script>

<style scoped>
.input-field {
  @apply w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-400;
}
.btn-primary {
  @apply bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition;
}
.btn-secondary {
  @apply bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition;
}
</style>