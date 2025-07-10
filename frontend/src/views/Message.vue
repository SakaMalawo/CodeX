<template>
  <div class="flex h-screen" :class="{ 'bg-gray-900': darkMode, 'bg-gray-100': !darkMode }">
    <!-- Sidebar des conversations -->
    <div class="w-1/4 border-r" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
      <div class="p-4 border-b" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
        <h2 class="text-xl font-bold" :class="{ 'text-white': darkMode, 'text-gray-800': !darkMode }">
          Messages
        </h2>
      </div>
      
      <div class="overflow-y-auto h-full">
        <div 
          v-for="conversation in conversations"
          :key="conversation.id"
          @click="selectConversation(conversation.id)"
          class="p-3 border-b flex items-center cursor-pointer hover:bg-opacity-10 hover:bg-indigo-400"
          :class="{
            'border-gray-700': darkMode,
            'border-gray-200': !darkMode,
            'bg-indigo-500 bg-opacity-20': selectedConversation === conversation.id
          }"
        >
          <img :src="conversation.user.avatar" class="h-10 w-10 rounded-full mr-3">
          <div class="flex-1">
            <div class="flex justify-between items-center">
              <p :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }" class="font-medium">
                {{ conversation.user.name }}
              </p>
              <span class="text-xs" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">
                {{ formatTime(conversation.lastMessage.time) }}
              </span>
            </div>
            <p class="text-sm truncate" :class="{ 'text-gray-400': darkMode, 'text-gray-600': !darkMode }">
              {{ conversation.lastMessage.text }}
            </p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Zone de conversation -->
    <div class="flex-1 flex flex-col">
      <div v-if="selectedConversation" class="flex-1 flex flex-col">
        <!-- En-tête -->
        <div class="p-4 border-b flex items-center" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
          <img :src="currentConversation.user.avatar" class="h-10 w-10 rounded-full mr-3">
          <div>
            <p class="font-medium" :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }">
              {{ currentConversation.user.name }}
            </p>
            <p class="text-xs" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">
              En ligne
            </p>
          </div>
        </div>
        
        <!-- Messages -->
        <div class="flex-1 overflow-y-auto p-4 space-y-4">
          <div 
            v-for="message in currentConversation.messages"
            :key="message.id"
            class="flex"
            :class="{ 'justify-end': message.sender === 'me' }"
          >
            <div 
              class="max-w-xs lg:max-w-md px-4 py-2 rounded-lg"
              :class="{
                'bg-indigo-500 text-white': message.sender === 'me',
                'bg-gray-200': !darkMode && message.sender !== 'me',
                'bg-gray-700': darkMode && message.sender !== 'me',
                'text-gray-800': !darkMode && message.sender !== 'me',
                'text-gray-100': darkMode && message.sender !== 'me'
              }"
            >
              <p>{{ message.text }}</p>
              <p class="text-xs text-right mt-1 opacity-70">
                {{ formatTime(message.time) }}
              </p>
            </div>
          </div>
        </div>
        
        <!-- Input d'envoi -->
        <div class="p-4 border-t" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
          <div class="flex items-center">
            <input
              v-model="newMessage"
              type="text"
              placeholder="Écrire un message..."
              class="flex-1 py-2 px-4 rounded-full focus:outline-none focus:ring-2 focus:ring-indigo-500"
              :class="{
                'bg-gray-700 text-white placeholder-gray-400': darkMode,
                'bg-white text-gray-900 placeholder-gray-500': !darkMode
              }"
              @keyup.enter="sendMessage"
            >
            <button
              @click="sendMessage"
              class="ml-2 p-2 rounded-full text-indigo-500 hover:bg-indigo-500 hover:bg-opacity-10"
            >
              <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </button>
          </div>
        </div>
      </div>
      
      <!-- Aucune conversation sélectionnée -->
      <div v-else class="flex-1 flex items-center justify-center">
        <div class="text-center p-6">
          <svg class="h-16 w-16 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
          </svg>
          <h3 class="mt-2 text-lg font-medium" :class="{ 'text-white': darkMode, 'text-gray-900': !darkMode }">
            Sélectionnez une conversation
          </h3>
          <p class="mt-1 text-sm" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">
            Ou commencez une nouvelle discussion
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    darkMode: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      selectedConversation: null,
      newMessage: '',
      conversations: [
        {
          id: 1,
          user: {
            name: "Jean Dupont",
            avatar: "https://randomuser.me/api/portraits/men/1.jpg"
          },
          lastMessage: {
            text: "Salut, comment ça va ? J'ai une question...",
            time: new Date(Date.now() - 1000 * 60 * 5)
          },
          messages: [
            {
              id: 1,
              text: "Salut Jean, ça fait longtemps !",
              time: new Date(Date.now() - 1000 * 60 * 60 * 2),
              sender: "me"
            },
            {
              id: 2,
              text: "Salut, comment ça va ? J'ai une question...",
              time: new Date(Date.now() - 1000 * 60 * 5),
              sender: "them"
            }
          ]
        },
        {
          id: 2,
          user: {
            name: "Marie Martin",
            avatar: "https://randomuser.me/api/portraits/women/1.jpg"
          },
          lastMessage: {
            text: "Réunion demain à 10h, n'oublie pas !",
            time: new Date(Date.now() - 1000 * 60 * 60 * 3)
          },
          messages: [
            {
              id: 1,
              text: "Tu as préparé la présentation pour demain ?",
              time: new Date(Date.now() - 1000 * 60 * 60 * 24),
              sender: "them"
            },
            {
              id: 2,
              text: "Oui, tout est prêt. J'ai ajouté les nouveaux chiffres.",
              time: new Date(Date.now() - 1000 * 60 * 60 * 20),
              sender: "me"
            },
            {
              id: 3,
              text: "Réunion demain à 10h, n'oublie pas !",
              time: new Date(Date.now() - 1000 * 60 * 60 * 3),
              sender: "them"
            }
          ]
        }
      ]
    };
  },
  computed: {
    currentConversation() {
      return this.conversations.find(c => c.id === this.selectedConversation);
    }
  },
  methods: {
    selectConversation(id) {
      this.selectedConversation = id;
      // Marquer comme lu
      const conversation = this.conversations.find(c => c.id === id);
      if (conversation) {
        // Mettre à jour le dernier message comme lu
        // (vous pourriez avoir besoin d'une logique plus complexe selon vos besoins)
      }
    },
    sendMessage() {
      if (!this.newMessage.trim() || !this.selectedConversation) return;
      
      const conversation = this.conversations.find(c => c.id === this.selectedConversation);
      if (conversation) {
        const newMsg = {
          id: conversation.messages.length + 1,
          text: this.newMessage,
          time: new Date(),
          sender: "me"
        };
        
        conversation.messages.push(newMsg);
        conversation.lastMessage = {
          text: this.newMessage,
          time: new Date()
        };
        
        this.newMessage = '';
        
        // Faire défiler vers le bas
        this.$nextTick(() => {
          const container = this.$el.querySelector('.overflow-y-auto');
          if (container) {
            container.scrollTop = container.scrollHeight;
          }
        });
      }
    },
    formatTime(date) {
      // La même fonction que dans le composant Navbar
      const now = new Date();
      const diff = now - date;
      
      if (diff < 60000) return 'à l\'instant';
      if (diff < 3600000) return `${Math.floor(diff / 60000)} min`;
      
      if (date.toDateString() === now.toDateString()) {
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      }
      
      const yesterday = new Date(now);
      yesterday.setDate(yesterday.getDate() - 1);
      if (date.toDateString() === yesterday.toDateString()) {
        return 'Hier';
      }
      
      if (date.getFullYear() === now.getFullYear()) {
        return date.toLocaleDateString([], { month: 'short', day: 'numeric' });
      }
      
      return date.toLocaleDateString([], { year: 'numeric', month: 'short', day: 'numeric' });
    }
  }
};
</script>