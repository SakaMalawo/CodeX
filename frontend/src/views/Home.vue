<template>
<<<<<<< HEAD
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
        <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" autocomplete="off" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Se connecter</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>

          <div>
            <label class="block text-gray-600 mb-1">EMAIL</label>
            <input v-model="email" type="email" required placeholder="Type your Email" class="input-style" autocomplete="off" />
          </div>

          <div>
            <label class="block text-gray-600 mb-1">PASSWORD</label>
            <input v-model="password" type="password" required placeholder="Type your password" class="input-style" autocomplete="new-password" />
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

          <label class="block text-gray-600 mb-1">Nom du compte</label>
          <input v-model="registerName" required placeholder="Votre nom complet" class="input-style" autocomplete="off" />

          <label class="block text-gray-600 mb-1">EMAIL</label>
          <input v-model="registerEmail" type="email" required placeholder="Votre email" class="input-style" autocomplete="off" />

          <label class="block text-gray-600 mb-1">Mot de passe</label>
          <input v-model="registerPassword" type="password" required placeholder="Votre mot de passe" class="input-style" autocomplete="new-password" />

          <label class="block text-gray-600 mb-1">Confirmer</label>
          <input v-model="registerConfirmPassword" type="password" required placeholder="Confirmez votre mot de passe" class="input-style" autocomplete="new-password" />

          <button type="submit" class="btn-primary">S'inscrire</button>
          <p v-if="registerErrorMessage" class="text-red-500 text-center text-sm mt-2">{{ registerErrorMessage }}</p>
        </form>

        <!-- Réinitialisation mot de passe -->
        <form v-else @submit.prevent="handleReset" class="flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-gray-800 mb-2">Réinitialiser le mot de passe</h2>
          <div class="h-1 w-12 bg-blue-600 rounded mb-6"></div>

          <label class="block text-gray-600 mb-1">Tapez votre email</label>
          <div class="flex gap-2">
            <input v-model="resetEmail" type="email" required placeholder="Votre email" class="input-style flex-1" autocomplete="off" />
            <button @click="sendVerificationCode" type="button" class="btn-primary w-auto whitespace-nowrap">Envoyer</button>
          </div>

          <label class="block text-gray-600 mb-1">Code de vérification</label>
          <input v-model="verificationCode" required placeholder="Code de vérification" class="input-style" autocomplete="off" />

          <label class="block text-gray-600 mb-1">Nouveau mot de passe</label>
          <input v-model="newPassword" type="password" required placeholder="Nouveau mot de passe" class="input-style" autocomplete="new-password" />

          <label class="block text-gray-600 mb-1">Confirmer</label>
          <input v-model="confirmPassword" type="password" required placeholder="Confirmer le mot de passe" class="input-style" autocomplete="new-password" />

          <button type="submit" class="btn-primary">Réinitialiser</button>
          <p v-if="resetErrorMessage" class="text-red-500 text-center text-sm mt-2">{{ resetErrorMessage }}</p>
          <p v-if="resetSuccessMessage" class="text-green-600 text-center text-sm mt-2">{{ resetSuccessMessage }}</p>
          <button @click="activeTab = 'login'" class="mt-4 text-sm text-blue-600 hover:underline">Retour à la connexion</button>
        </form>
      </div>
    </div>
=======
  <div
    class="min-h-screen w-full flex flex-col md:flex-row bg-black font-sans relative"
  >
    <!-- Branding (3/4) -->
    <div
      class="flex flex-col items-center justify-center md:justify-center flex-[3_1_0%] md:h-screen h-auto md:min-h-0 min-h-[320px] w-full md:py-0 py-8"
      id="logoS"
    >
      <div
        class="flex flex-col items-center justify-center gap-10 mb-6 mt-6 w-full md:gap-10 md:mb-6 md:mt-6 sm:gap-3 sm:mb-2 sm:mt-0"
      >
        <div class="flex flex-col items-center gap-2 sm:gap-1">
          <img src="/logoHay.png" alt="Logo HAY" class="w-[200px] h-[200px] md:w-[220px] md:h-[220px] sm:w-[32px] sm:h-[32px] object-contain drop-shadow-[0_0_24px_#2196f3aa] z-10 sm:mt-2" />
        </div>
        <span
          id="titleL"
          class="text-white font-bold tracking-widest text-[58px] md:text-[38px] sm:text-base mt-2 md:mt-6 sm:mt-2 whitespace-nowrap z-20 drop-shadow-[0_2px_16px_#39ff14,0_2px_16px_#2196f3]"
        >
          HAY
        </span>
      </div>
    </div>

    <!-- Login (1/4) -->
    <section class="hay_log">
      <div
        class="flex flex-col justify-center items-center flex-1 w-full md:max-w-[420px] bg-[#181c24] md:rounded-none rounded-t-2xl md:h-screen h-auto md:min-h-0 min-h-[320px] p-8 md:p-10 sm:p-4 text-center shadow-2xl sm:rounded-none sm:shadow-none sm:border-t sm:border-[#232a36] sm:pt-6 sm:pb-8 sm:px-2"
      >
        <h2 class="text-white text-2xl font-semibold mb-8 sm:text-base sm:mb-4">
          Connexion à Hay
        </h2>
        <form
          @submit.prevent="handleLogin"
          class="w-full flex flex-col gap-5 sm:gap-3 max-w-md mx-auto"
        >
          <div class="flex flex-col items-start w-full">
            <label
              for="email"
              class="text-gray-400 text-base mb-2 sm:text-xs sm:mb-1"
              >Adresse e-mail</label
            >
            <input
              type="email"
              id="email"
              v-model="email"
              required
              autocomplete="username"
              placeholder="ex: example@example.com"
              class="w-full px-4 py-3 sm:px-3 sm:py-2 rounded-lg border border-[#232a36] bg-[#232a36] text-white text-base sm:text-sm outline-none transition duration-200 focus:bg-[#283040] focus:border-[#39ff14]"
            />
          </div>
          <div class="flex flex-col items-start w-full">
            <label
              for="password"
              class="text-gray-400 text-base mb-2 sm:text-xs sm:mb-1"
              >Mot de passe</label
            >
            <input
              type="password"
              id="password"
              v-model="password"
              required
              autocomplete="current-password"
              placeholder="Votre mot de passe"
              class="w-full px-4 py-3 sm:px-3 sm:py-2 rounded-lg border border-[#232a36] bg-[#232a36] text-white text-base sm:text-sm outline-none transition duration-200 focus:bg-[#283040] focus:border-[#39ff14]"
            />
          </div>
          <div
            class="flex justify-between items-center w-full text-sm sm:text-xs text-gray-400"
          >
            <label class="flex items-center gap-2">
              <input
                type="checkbox"
                v-model="remember"
                class="accent-[#39ff14]"
              />
              Se souvenir de moi
            </label>
            <a
              href="#"
              class="text-[#39ff14] hover:text-[#00ffa3] transition-colors"
              >Mot de passe oublié ?</a
            >
          </div>
          <button
            type="submit"
            class="w-full py-3 sm:py-2 bg-[#24292f] text-white text-lg sm:text-base font-semibold rounded-xl mb-5 sm:mb-3 cursor-pointer transition-colors duration-200 shadow-lg hover:bg-[#333940]"
          >
            Se connecter
          </button>
          <p
            v-if="errorMessage"
            class="text-red-500 text-base sm:text-sm text-center mb-2"
          >
            {{ errorMessage }}
          </p>
        </form>
        <div
          class="text-gray-400 text-base sm:text-xs text-center mt-6 sm:mt-2 w-full"
        >
          Pas encore de compte ?
          <a
            href="#"
            class="text-[#39ff14] hover:text-[#00ffa3] ml-1 transition-colors"
            >Inscription</a
          >
        </div>
      </div>
    </section>

    <!-- Description en bas sur mobile -->
    <span
      class="hidden sm:block absolute bottom-3 left-0 w-full text-white text-xs text-center max-w-[90vw] opacity-85 drop-shadow-[0_2px_8px_#0a0a0a] px-2"
    >
      La plateforme d'apprentissage moderne et interactive.
    </span>
    <span
      class="block sm:hidden fixed bottom-3 left-0 w-full text-white text-xs text-center max-w-[90vw] opacity-85 drop-shadow-[0_2px_8px_#0a0a0a] px-2 z-50"
    >
      La plateforme d'apprentissage moderne et interactive.
    </span>
>>>>>>> fa65a2ebc7d00b9e898d68f9e2381db78bb6e9e5
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
<<<<<<< HEAD
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
      resetEmail: "",
      verificationCode: "",
      newPassword: "",
      confirmPassword: "",
      resetErrorMessage: "",
      resetSuccessMessage: "",
=======
      email: "",
      password: "",
      remember: false,
      errorMessage: "",
>>>>>>> fa65a2ebc7d00b9e898d68f9e2381db78bb6e9e5
    };
  },
  methods: {
    handleLogin() {
<<<<<<< HEAD
      const superUser = { username: "saka@hay.com", password: "1234" };
      if (this.email === superUser.username && this.password === superUser.password) {
=======
      // Contrôle 100% frontend, sans appel Axios
      const superUser = {
        username: "saka@hay.com",
        password: "1234",
      };
      if (
        this.email === superUser.username &&
        this.password === superUser.password
      ) {
>>>>>>> fa65a2ebc7d00b9e898d68f9e2381db78bb6e9e5
        this.$router.push("/AppPage");
      } else {
        this.errorMessage = "Identifiants incorrects !";
      }
    },
<<<<<<< HEAD
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
    sendVerificationCode() {
      if (!this.resetEmail) {
        this.resetErrorMessage = "Veuillez entrer votre email.";
        this.resetSuccessMessage = "";
        return;
      }
      this.resetErrorMessage = "";
      this.resetSuccessMessage = `Un code de vérification a été envoyé à ${this.resetEmail}.`;
    },
=======
>>>>>>> fa65a2ebc7d00b9e898d68f9e2381db78bb6e9e5
  },
};
</script>

<style scoped>
<<<<<<< HEAD
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
  padding: 0.75rem 1rem;
  background-color: #2563eb;
  color: white;
  font-weight: 600;
  border-radius: 0.5rem;
  margin-top: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s;
}
.btn-primary:hover {
  background-color: #1e40af;
=======
@media (min-width: 500px) {
  * {
    size: inherit;
  }
  .hay_log {
    width: 400px;
    height: initial;
    margin: 20px;
  }
}
@media (max-width: 470px) {
  #titleL {
    margin-top: -135px;
  }
}
.hay_log {
  position: relative;
  top: -100px;
  padding: 5px;
  margin: 5px;
>>>>>>> fa65a2ebc7d00b9e898d68f9e2381db78bb6e9e5
}
</style>
