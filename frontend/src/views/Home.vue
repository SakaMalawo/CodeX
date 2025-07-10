<template>
  <div class="min-h-screen w-full flex bg-gradient-to-r from-green-200 via-white to-white font-sans">
    <!-- Branding à gauche -->
    <div class="flex flex-col justify-center items-center flex-1 bg-gradient-to-b from-blue-700 via-black to-blue-900 text-white px-10 py-12 shadow-2xl shadow-black">
      <img src="/logoHay.png" alt="Logo" class="w-48 h-48 mb-6 drop-shadow-lg" />
      <h1 class="text-4xl font-bold mb-4">BIENVENUE SUR HAY<br /></h1>
      <p class="text-lg opacity-90 max-w-xs">
        Découvrez nos formations et accédez à la connaissance depuis chez vous !
      </p>
      <ul class="mt-8 text-left text-base opacity-90 max-w-xs list-disc pl-5 space-y-2">
        <li>Mathématiques, Sciences, Langues</li>
        <li>Cours en ligne interactifs</li>
        <li>Suivi personnalisé</li>
        <li>Pour tous les niveaux</li>
      </ul>
    </div>
    <!-- Formulaire à droite -->
    <div class="flex flex-col justify-center items-center flex-1 px-8 py-12">
      <div class="w-full max-w-3xl bg-white rounded-2xl shadow-2xl p-12">
        <!-- Onglets -->
        <div class="flex mb-6">
          <button
            @click="activeTab = 'login'"
            :class=" [
              'flex-1 py-2 rounded-l-lg font-semibold transition',
              activeTab === 'login'
                ? 'bg-blue-600 text-white shadow'
                : 'bg-gray-100 text-gray-600 hover:bg-blue-50'
            ]"
          >
            Connexion
          </button>
          <button
            @click="activeTab = 'register'"
            :class=" [
              'flex-1 py-2 rounded-r-lg font-semibold transition',
              activeTab === 'register'
                ? 'bg-blue-600 text-white shadow'
                : 'bg-gray-100 text-gray-600 hover:bg-blue-50'
            ]"
          >
            Inscription
          </button>
        </div>
        <!-- Formulaire de connexion -->
        <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Sign In</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>
          <label class="block text-gray-600 mb-2">Veuillez sélectionner votre rôle</label>
          <div class="flex justify-between mb-6">
            <button
              v-for="role in roles"
              :key="role.value"
              @click="selectedRole = role.value"
              type="button"
              :class=" [
                'flex-1 mx-1 py-3 rounded-lg border text-center transition',
                selectedRole === role.value
                  ? 'border-blue-600 bg-blue-50 text-blue-700 font-semibold shadow'
                  : 'border-gray-200 bg-gray-50 text-gray-500 hover:border-blue-300'
              ]"
            >
              <span class="block text-2xl mb-1">{{ role.icon }}</span>
              <span class="block text-xs uppercase tracking-widest">{{ role.label }}</span>
              <span v-if="selectedRole === role.value" class="block text-blue-600 text-lg mt-1">✔</span>
            </button>
          </div>
          <div>
            <label for="email" class="block text-gray-600 mb-1">EMAIL</label>
            <input
              type="email"
              id="email"
              v-model="email"
              required
              autocomplete="username"
              placeholder="Type your Email"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <div>
            <label for="password" class="block text-gray-600 mb-1">PASSWORD</label>
            <input
              type="password"
              id="password"
              v-model="password"
              required
              autocomplete="current-password"
              placeholder="Type your password"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <button
            type="submit"
            class="w-full py-3 bg-blue-600 text-white text-lg font-semibold rounded-lg mt-2 shadow hover:bg-blue-700 transition"
          >
            Login
          </button>
          <p v-if="errorMessage" class="text-red-500 text-center text-sm mt-2">
            {{ errorMessage }}
          </p>
          <div class="flex justify-between items-center mt-4 text-sm text-gray-400">
            <span></span>
            <a href="#" class="hover:underline text-gray-500">Mot de passe oublié ?</a>
          </div>
        </form>
        <!-- Formulaire d'inscription -->
        <form v-else @submit.prevent="handleRegister" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Créer un compte</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>
          <div>
            <label for="registerName" class="block text-gray-600 mb-1">NOM COMPLET</label>
            <input
              type="text"
              id="registerName"
              v-model="registerName"
              required
              placeholder="Votre nom complet"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <div>
            <label for="registerEmail" class="block text-gray-600 mb-1">EMAIL</label>
            <input
              type="email"
              id="registerEmail"
              v-model="registerEmail"
              required
              autocomplete="username"
              placeholder="Votre email"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <div>
            <label for="registerPassword" class="block text-gray-600 mb-1">MOT DE PASSE</label>
            <input
              type="password"
              id="registerPassword"
              v-model="registerPassword"
              required
              autocomplete="new-password"
              placeholder="Votre mot de passe"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <div>
            <label for="registerConfirmPassword" class="block text-gray-600 mb-1">CONFIRMER LE MOT DE PASSE</label>
            <input
              type="password"
              id="registerConfirmPassword"
              v-model="registerConfirmPassword"
              required
              autocomplete="new-password"
              placeholder="Confirmez votre mot de passe"
              class="w-full px-4 py-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-800 outline-none focus:border-green-500 transition"
            />
          </div>
          <button
            type="submit"
            class="w-full py-3 bg-blue-600 text-white text-lg font-semibold rounded-lg mt-2 shadow hover:bg-blue-700 transition"
          >
            S'inscrire
          </button>
          <p v-if="registerErrorMessage" class="text-red-500 text-center text-sm mt-2">
            {{ registerErrorMessage }}
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      // Onglet actif
      activeTab: "login",
      // Login
      email: "",
      password: "",
      selectedRole: "tutor",
      errorMessage: "",
      // Register
      registerName: "",
      registerEmail: "",
      registerPassword: "",
      registerConfirmPassword: "",
      registerErrorMessage: "",
      // Roles
      roles: [
        { value: "student", label: "Étudiant", icon: "🎓" },
        { value: "tutor", label: "Professeur", icon: "👨‍🏫" },
        { value: "parent", label: "Nouvel Étudiant", icon: "🆕" },
      ],
    };
  },
  methods: {
    handleLogin() {
      // Contrôle 100% frontend, sans appel Axios
      const superUser = {
        username: "saka@hay.com",
        password: "1234",
      };
      if (
        this.email === superUser.username &&
        this.password === superUser.password
      ) {
        this.$router.push("/AppPage");
      } else {
        this.errorMessage = "Identifiants incorrects !";
      }
    },
    handleRegister() {
      if (this.registerPassword !== this.registerConfirmPassword) {
        this.registerErrorMessage = "Les mots de passe ne correspondent pas.";
        return;
      }
      if (!this.registerName || !this.registerEmail || !this.registerPassword) {
        this.registerErrorMessage = "Veuillez remplir tous les champs.";
        return;
      }
      // Ici, tu peux ajouter la logique d'inscription (API, etc.)
      this.registerErrorMessage = "";
      // Redirection après inscription réussie (exemple)
      this.$router.push("/AppPage");
    },
  },
};
</script>

<style scoped>
body {
  background: #f0f4f8;
}
</style>
