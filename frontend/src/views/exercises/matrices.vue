<template>
  <section :class="['mt-16 md:ml-64 px-4 py-6 max-w-3xl mx-auto rounded-xl shadow', darkMode ? 'bg-[#203054] text-white' : 'bg-gray-50 text-gray-900']">
    <h1 class="text-2xl font-bold text-center mb-8">Exercices : Matrices</h1>
    <p>Bienvenue sur la page des exercices de matrices.</p>
  </section>
</template>

<script>
export default {
  name: "ExercicesMatrices",
  props: {
    darkMode: {
      type: Boolean,
      required: true,
    },
  },
};
</script>
