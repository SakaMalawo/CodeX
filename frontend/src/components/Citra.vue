<template>
  <div>
    <!-- Bouton flottant pour ouvrir le bot -->
    <div
      v-if="!open"
      class="citra-bot-fab"
      @click="open = true"
      title="Ouvrir le bot"
    >
      <img
        src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png"
        alt="Bot"
        class="bot-avatar"
      />
    </div>

    <!-- Fenêtre du chatbot -->
    <transition name="fade">
      <div v-if="open" class="citra-bot-window" :class="{ dark: isDark }">
        <div class="citra-bot-header">
          <div class="bot-header-info">
            <img
              src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png"
              alt="Bot"
              class="bot-avatar"
            />
            <span class="bot-title">Citra Bot</span>
          </div>
          <button class="close-btn" @click="open = false" title="Fermer">
            ×
          </button>
        </div>
        <div class="citra-bot-messages" ref="messages">
          <div v-for="(msg, i) in messages" :key="i" :class="['msg', msg.from]">
            <span v-if="msg.from === 'bot'" class="msg-bot-avatar">
              <img
                src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png"
                alt="Bot"
              />
            </span>
            <span class="msg-content">{{ msg.text }}</span>
          </div>
        </div>
        <form class="citra-bot-input" @submit.prevent="sendMessage">
          <input
            v-model="input"
            type="text"
            placeholder="Écrivez votre message..."
            autocomplete="off"
            :disabled="loading"
          />
          <button type="submit" :disabled="!input || loading">Envoyer</button>
        </form>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "Citra",
  props: {
    dark: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      open: false,
      input: "",
      messages: [
        {
          from: "bot",
          text: "Bonjour ! Je suis Citra, comment puis-je vous aider ?",
        },
      ],
      loading: false,
    };
  },
  computed: {
    isDark() {
      return this.dark;
    },
  },
  methods: {
    sendMessage() {
      if (!this.input.trim()) return;
      const userMsg = this.input;
      this.messages.push({ from: "user", text: userMsg });
      this.input = "";
      this.loading = true;

      setTimeout(() => {
        this.messages.push({
          from: "bot",
          text: this.fakeBotReply(userMsg),
        });
        this.loading = false;
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }, 900);

      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },
    fakeBotReply(msg) {
      if (msg.toLowerCase().includes("bonjour")) return "Bonjour à vous !";
      if (msg.toLowerCase().includes("aide"))
        return "Je peux répondre à vos questions sur la plateforme Hay.";
      if (msg.toLowerCase().includes("merci")) return "Avec plaisir !";
      return "Je suis un bot de démonstration. Posez-moi une question sur Hay !";
    },
    scrollToBottom() {
      const el = this.$refs.messages;
      if (el) el.scrollTop = el.scrollHeight;
    },
  },
  mounted() {
    this.scrollToBottom();
  },
};
</script>

<style scoped>
.citra-bot-fab {
  position: fixed;
  right: 2.5vw;
  bottom: 2.5vw;
  z-index: 1002;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 4px 24px #0004;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: box-shadow 0.2s;
}
.citra-bot-fab:hover {
  box-shadow: 0 8px 32px #39ff1499;
}
.bot-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #fff;
  border: 2px solid #39ff14;
  object-fit: cover;
}
.citra-bot-window {
  position: fixed;
  right: 2vw;
  bottom: 2vw;
  width: 350px;
  max-width: 95vw;
  height: 540px;
  max-height: 90vh;
  background: #fff;
  color: #181c24;
  border-radius: 1.2rem;
  box-shadow: 0 8px 32px #000a;
  z-index: 1003;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  animation: popin 0.2s;
}
.citra-bot-window.dark {
  background: #181c24;
  color: #fff;
}
@keyframes popin {
  from {
    transform: scale(0.8);
    opacity: 0.2;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
.citra-bot-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f5f5f5;
  padding: 0.7rem 1rem;
  border-bottom: 1px solid #39ff1433;
}
.citra-bot-window.dark .citra-bot-header {
  background: #232a36;
}
.bot-header-info {
  display: flex;
  align-items: center;
  gap: 0.7rem;
}
.bot-title {
  color: #39ff14;
  font-weight: bold;
  font-size: 1.2rem;
  letter-spacing: 0.04em;
}
.close-btn {
  background: none;
  border: none;
  color: inherit;
  font-size: 1.7rem;
  cursor: pointer;
  transition: color 0.2s;
  padding: 0 0.5rem;
  line-height: 1;
}
.close-btn:hover {
  color: #ff4d4f;
}
.citra-bot-messages {
  flex: 1 1 0;
  overflow-y: auto;
  padding: 1rem;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  color: #181c24;
}
.citra-bot-window.dark .citra-bot-messages {
  background: #181c24;
  color: #fff;
}
.msg {
  display: flex;
  align-items: flex-end;
  gap: 0.5rem;
  max-width: 90%;
}
.msg.user {
  align-self: flex-end;
  flex-direction: row-reverse;
}
.msg.bot {
  align-self: flex-start;
}
.msg-content {
  background: #f0f0f0;
  color: #181c24;
  padding: 0.6rem 1rem;
  border-radius: 1.2rem;
  font-size: 1rem;
  max-width: 220px;
  word-break: break-word;
  box-shadow: 0 2px 8px #0002;
}
.citra-bot-window.dark .msg-content {
  background: #232a36;
  color: #fff;
}
.msg.user .msg-content {
  background: #39ff14;
  color: #181c24;
}
.citra-bot-window.dark .msg.user .msg-content {
  background: #39ff14;
  color: #181c24;
}
.msg-bot-avatar img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #39ff14;
  background: #fff;
}
.citra-bot-input {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: #f5f5f5;
  border-top: 1px solid #39ff1433;
  gap: 0.7rem;
}
.citra-bot-window.dark .citra-bot-input {
  background: #232a36;
}
.citra-bot-input input {
  flex: 1 1 0;
  padding: 0.7rem 1rem;
  border-radius: 1rem;
  border: none;
  background: #fff;
  color: #181c24;
  font-size: 1rem;
  outline: none;
  transition: background 0.2s;
}
.citra-bot-window.dark .citra-bot-input input {
  background: #181c24;
  color: #fff;
}
.citra-bot-input input:disabled {
  background: #e0e0e0;
  color: #888;
}
.citra-bot-window.dark .citra-bot-input input:disabled {
  background: #232a36;
  color: #888;
}
.citra-bot-input button {
  background: #39ff14;
  color: #181c24;
  border: none;
  border-radius: 1rem;
  padding: 0.7rem 1.2rem;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}
.citra-bot-input button:disabled {
  background: #b0ffb0;
  color: #232a36;
  cursor: not-allowed;
}

/* Remonte le bot sur mobile pour éviter la superposition avec le menu bas */
@media (max-width: 900px) {
  .citra-bot-fab,
  .citra-bot-window {
    bottom: 80px;
    right: 4vw;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
