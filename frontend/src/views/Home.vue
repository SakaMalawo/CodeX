<template>
  <div class="min-h-screen md:h-screen w-full flex flex-col md:flex-row bg-gradient-to-r from-green-200 via-white to-white font-sans overflow-hidden">
    <!-- Branding -->
    <div class="flex flex-col justify-center items-center flex-1 h-1/2 md:h-full bg-gradient-to-b from-blue-700 via-black to-blue-900 text-white px-4 py-6 md:px-10 md:py-12 shadow-2xl shadow-black text-center">
      <img src="/logoHay.png" alt="Logo" class="w-40 h-40 md:w-96 md:h-96 mb-4 drop-shadow-lg" />
      <h1 class="text-3xl md:text-6xl font-bold mb-2">BIENVENUE SUR HAY</h1>
      <p class="text-base md:text-xl opacity-90 max-w-xs md:max-w-md">
        Découvrez nos études en ligne et accédez à la connaissance depuis chez vous !
      </p>
    </div>

    <!-- Formulaires -->
    <div class="flex flex-col justify-center items-center flex-1 h-1/2 md:h-full px-4 py-6 md:px-8 md:py-12 overflow-y-auto">
      <div class="w-full max-w-full md:max-w-3xl bg-white rounded-2xl shadow-2xl p-4 md:p-12">
        <!-- Onglets -->
        <div class="flex flex-col sm:flex-row mb-6" v-if="activeTab !== 'reset'">
          <button
            @click="activeTab = 'login'"
            :class="['flex-1 py-2 rounded-t-lg sm:rounded-l-lg sm:rounded-tr-none font-semibold transition', activeTab === 'login' ? 'bg-blue-600 text-white shadow' : 'bg-gray-100 text-gray-600 hover:bg-blue-50']"
          >
            Connexion
          </button>
          <button
            @click="activeTab = 'register'"
            :class="['flex-1 py-2 rounded-b-lg sm:rounded-r-lg sm:rounded-bl-none font-semibold transition', activeTab === 'register' ? 'bg-blue-600 text-white shadow' : 'bg-gray-100 text-gray-600 hover:bg-blue-50']"
          >
            Inscription
          </button>
        </div>

        <!-- Connexion -->
        <form
  v-if="activeTab === 'login'"
  @submit.prevent="handleLogin"
  autocomplete="off"
  class="flex flex-col gap-4"
>
  <h2 class="text-2xl font-bold text-gray-800 mb-2">Se connecter</h2>
  <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>

  <div>
    <label class="block text-gray-600 mb-1">EMAIL</label>
    <input
      v-model="email"
      type="email"
      required
      placeholder="Type your Email"
      class="input-style"
      autocomplete="off"
    />
  </div>

  <div>
    <label class="block text-gray-600 mb-1">PASSWORD</label>
    <input
      v-model="password"
      type="password"
      required
      placeholder="Type your password"
      class="input-style"
      autocomplete="new-password"
    />
  </div>

  <button type="submit" class="btn-primary">Login</button>

  <p v-if="errorMessage" class="text-red-500 text-center text-sm mt-2">{{ errorMessage }}</p>

  <div class="flex justify-end items-center mt-4 text-sm text-gray-400">
    <a href="#" @click.prevent="activeTab = 'reset'" class="hover:underline text-gray-500">
      Mot de passe oublié ?
    </a>
  </div>
</form>


        <!-- Inscription -->
        <form v-else-if="activeTab === 'register'" @submit.prevent="handleRegister" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Créer un compte</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>

          <label class="block text-gray-600 mb-2">Veuillez sélectionner votre rôle</label>
          <div class="flex flex-col sm:flex-row justify-between mb-6 gap-2 sm:gap-0">
            <button
              v-for="role in roles"
              :key="role.value"
              @click="selectedRole = role.value"
              type="button"
              :class="[
                'flex-1 py-3 rounded-lg border text-center transition',
                selectedRole === role.value ? 'border-blue-600 bg-blue-50 text-blue-700 font-semibold shadow' : 'border-gray-200 bg-gray-50 text-gray-500 hover:border-blue-300'
              ]"
            >
              <span class="block text-2xl mb-1">{{ role.icon }}</span>
              <span class="block text-xs uppercase tracking-widest">{{ role.label }}</span>
              <span v-if="selectedRole === role.value" class="block text-blue-600 text-lg mt-1">✔</span>
            </button>
          </div>
          <label class="block text-gray-600 mb-1">Nom du compte</label>
<input
  v-model="registerName"
  required
  placeholder="Votre nom complet"
  class="input-style"
  autocomplete="off"
/>

<label class="block text-gray-600 mb-1">EMAIL</label>
<input
  v-model="registerEmail"
  type="email"
  required
  placeholder="Votre email"
  class="input-style"
  autocomplete="off"
/>

<label class="block text-gray-600 mb-1">Mot de passe</label>
<input
  v-model="registerPassword"
  type="password"
  required
  placeholder="Votre mot de passe"
  class="input-style"
  autocomplete="new-password"
/>

<label class="block text-gray-600 mb-1">Confirmer</label>
<input
  v-model="registerConfirmPassword"
  type="password"
  required
  placeholder="Confirmez votre mot de passe"
  class="input-style"
  autocomplete="new-password"
/>

<button type="submit" class="btn-primary">S'inscrire</button>

          <p v-if="registerErrorMessage" class="text-red-500 text-center text-sm mt-2">{{ registerErrorMessage }}</p>
        </form>

        <!-- Réinitialisation mot de passe -->
        <form v-else @submit.prevent="handleReset" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Réinitialiser le mot de passe</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>

          <label class="block text-gray-600 mb-1">Code de vérification</label>
<input
  v-model="verificationCode"
  required
  placeholder="Code de vérification"
  class="input-style"
  autocomplete="off"
/>

<label class="block text-gray-600 mb-1">Nouveau mot de passe</label>
<input
  v-model="newPassword"
  type="password"
  required
  placeholder="Nouveau mot de passe"
  class="input-style"
  autocomplete="new-password"
/>

<label class="block text-gray-600 mb-1">Confirmer</label>
<input
  v-model="confirmPassword"
  type="password"
  required
  placeholder="Confirmer le mot de passe"
  class="input-style"
  autocomplete="new-password"
/>


          <button type="submit" class="btn-primary">Réinitialiser</button>
          <p v-if="resetErrorMessage" class="text-red-500 text-center text-sm mt-2">{{ resetErrorMessage }}</p>
          <p v-if="resetSuccessMessage" class="text-green-600 text-center text-sm mt-2">{{ resetSuccessMessage }}</p>
          <button @click="activeTab = 'login'" class="mt-4 text-sm text-blue-600 hover:underline">Retour à la connexion</button>
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
      activeTab: "login",
      email: "",
      password: "",
      errorMessage: "",
      registerName: "",
      registerEmail: "",
      registerPassword: "",
      registerConfirmPassword: "",
      registerErrorMessage: "",
      selectedRole: "tutor",
      roles: [
        { value: "student", label: "Étudiant", icon: "🎓" },
        { value: "tutor", label: "Professeur", icon: "👨‍🏫" },
        { value: "parent", label: "Nouvel Étudiant", icon: "🆕" },
      ],
      // Réinitialisation
      verificationCode: "",
      newPassword: "",
      confirmPassword: "",
      resetErrorMessage: "",
      resetSuccessMessage: "",
    };
  },
  methods: {
    handleLogin() {
      const superUser = { username: "saka@hay.com", password: "1234" };
      if (this.email === superUser.username && this.password === superUser.password) {
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
      this.registerErrorMessage = "";
      this.activeTab = "login";
      this.registerName = "";
      this.registerEmail = "";
      this.registerPassword = "";
      this.registerConfirmPassword = "";
      this.selectedRole = "tutor";
    
    },
    handleReset() {
      if (!this.verificationCode || !this.newPassword || !this.confirmPassword) {
        this.resetErrorMessage = "Tous les champs sont obligatoires.";
        this.resetSuccessMessage = "";
        return;
      }
      if (this.newPassword !== this.confirmPassword) {
        this.resetErrorMessage = "Les mots de passe ne correspondent pas.";
        this.resetSuccessMessage = "";
        return;
      }
      this.resetErrorMessage = "";
      this.resetSuccessMessage = "Mot de passe réinitialisé avec succès.";
      this.verificationCode = "";
      this.newPassword = "";
      this.confirmPassword = "";
    },
  },
};
</script>

<style scoped>
.input-style {
  width: 100%;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border: 1px solid #e5e7eb;
  background-color: #f9fafb;
  color: #1f2937;
  outline: none;
  transition: border-color 0.2s;
}
.input-style:focus {
  border-color: #22c55e;
}
.btn-primary {
  width: 100%;
  padding: 0.75rem;
  background-color: #2563eb;
  color: white;
  font-weight: 600;
  border-radius: 0.5rem;
  margin-top: 0.5rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: background-color 0.2s;
}
.btn-primary:hover {
  background-color: #1e40af;
}
</style>
