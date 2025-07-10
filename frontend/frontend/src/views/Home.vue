<template>
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
          <svg
            id="green"
            class="w-[200px] h-[200px] md:w-[220px] md:h-[220px] sm:w-[32px] sm:h-[32px] filter drop-shadow-[0_0_24px_#39ff14aa] opacity-97 z-10 sm:mt-2"
            viewBox="0 0 64 64"
            fill="none"
          >
            <defs>
              <linearGradient
                id="flame-green"
                x1="0"
                y1="64"
                x2="0"
                y2="0"
                gradientUnits="userSpaceOnUse"
              >
                <stop offset="0%" stop-color="#39FF14" />
                <stop offset="100%" stop-color="#00FFA3" />
              </linearGradient>
            </defs>
            <path
              d="M32 2C20 14 8 28 32 62C56 28 44 14 32 2Z"
              fill="url(#flame-green)"
            />
          </svg>
          <svg
            id="blue"
            class="w-[200px] h-[500px] md:w-[220px] md:h-[220px] sm:w-[32px] sm:h-[32px] filter drop-shadow-[0_0_24px_#2196f3aa] opacity-97 -mt-[420px] md:-mt-[180px] sm:-mt-[22px] z-0"
            viewBox="0 0 64 64"
            fill="none"
          >
            <defs>
              <linearGradient
                id="flame-blue"
                x1="0"
                y1="0"
                x2="0"
                y2="64"
                gradientUnits="userSpaceOnUse"
              >
                <stop offset="0%" stop-color="#2196F3" />
                <stop offset="100%" stop-color="#00C6FB" />
              </linearGradient>
            </defs>
            <path
              d="M32 62C44 50 56 36 32 2C8 36 20 50 32 62Z"
              fill="url(#flame-blue)"
            />
          </svg>
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
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      email: "",
      password: "",
      remember: false,
      errorMessage: "",
    };
  },
  methods: {
    handleLogin() {
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
  },
};
</script>

<style scoped>
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
}
</style>
