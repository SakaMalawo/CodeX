<template>
  <div class="flex h-screen" :class="{ 'bg-gray-900': darkMode, 'bg-gray-100': !darkMode }">
    <!-- Sidebar des conversations -->
    <div class="w-1/4 border-r" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
      <div class="p-4 border-b flex justify-between items-center" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
        <h2 class="text-xl font-bold flex items-center" :class="{ 'text-white': darkMode, 'text-gray-800': !darkMode }">
          Messages
          <div class="flex ml-2 space-x-2">
            <!-- Nouveau message -->
            <button 
              @click="showNewMessageModal = true"
              class="p-1 rounded-full hover:bg-opacity-10 hover:bg-indigo-400 relative group"
            >
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
              </svg>
              <span class="tooltip">Nouveau message</span>
            </button>
            
            <!-- Archives -->
            <button 
              class="p-1 rounded-full hover:bg-opacity-10 hover:bg-indigo-400 relative group"
            >
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
              </svg>
              <span class="tooltip">Archives</span>
            </button>
          </div>
        </h2>
      </div>
      
      <div class="h-[calc(100vh-60px)]">
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
        <div class="p-4 border-b flex items-center justify-between" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
          <div class="flex items-center">
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
          <div class="flex space-x-2">
            <!-- Boutons d'actions -->
            <button class="p-2 rounded-full hover:bg-opacity-10 hover:bg-indigo-400 relative group">
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <span class="tooltip">Appeler</span>
            </button>
            <button class="p-2 rounded-full hover:bg-opacity-10 hover:bg-indigo-400 relative group">
              <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
              </svg>
              <span class="tooltip">Vidéo</span>
            </button>
          </div>
        </div>
        
        <!-- Messages -->
        <div class="flex-1 p-4 space-y-4">
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
        
        <!-- Input d'envoi - Position fixe en bas -->
        <div class="sticky bottom-0 p-4 border-t bg-opacity-90 backdrop-blur-sm" 
             :class="{ 
               'border-gray-700 bg-gray-900': darkMode, 
               'border-gray-200 bg-white': !darkMode 
             }">
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
          <button
            @click="showNewMessageModal = true"
            class="mt-4 px-4 py-2 bg-indigo-500 text-white rounded-full hover:bg-indigo-600 transition-colors"
          >
            Nouveau message
          </button>
        </div>
      </div>
    </div>

    <!-- Modal Nouveau Message -->
    <div v-if="showNewMessageModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg w-full max-w-md" :class="{ 'bg-gray-800': darkMode }">
        <div class="p-4 border-b flex justify-between items-center" :class="{ 'border-gray-700': darkMode, 'border-gray-200': !darkMode }">
          <h3 class="text-lg font-medium" :class="{ 'text-white': darkMode }">Nouveau message</h3>
          <button @click="showNewMessageModal = false" class="text-gray-500 hover:text-gray-700">
            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="p-4">
          <input
            type="text"
            placeholder="Rechercher des contacts..."
            class="w-full py-2 px-4 rounded-full mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            :class="{
              'bg-gray-700 text-white placeholder-gray-400': darkMode,
              'bg-gray-100 text-gray-900 placeholder-gray-500': !darkMode
            }"
          >
          <div>
            <div 
              v-for="contact in contacts"
              :key="contact.id"
              class="p-3 hover:bg-gray-100 cursor-pointer flex items-center"
              :class="{ 'hover:bg-gray-700': darkMode }"
              @click="startNewConversation(contact)"
            >
              <img :src="contact.avatar" class="h-10 w-10 rounded-full mr-3">
              <div>
                <p :class="{ 'text-white': darkMode }">{{ contact.name }}</p>
                <p class="text-sm" :class="{ 'text-gray-400': darkMode, 'text-gray-500': !darkMode }">@{{ contact.username }}</p>
              </div>
            </div>
          </div>
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
      showNewMessageModal: false,
      contacts: [
        {
          id: 3,
          name: "Sophie Lambert",
          username: "sophiel",
          avatar: "https://randomuser.me/api/portraits/women/2.jpg"
        },
        {
          id: 4,
          name: "Thomas Leroy",
          username: "thomasl",
          avatar: "https://randomuser.me/api/portraits/men/3.jpg"
        },
        {
          id: 5,
          name: "Emma Dubois",
          username: "emmad",
          avatar: "https://randomuser.me/api/portraits/women/3.jpg"
        }
      ],
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
      }
    },
    startNewConversation(contact) {
      const newConversation = {
        id: Math.max(...this.conversations.map(c => c.id)) + 1,
        user: {
          name: contact.name,
          avatar: contact.avatar
        },
        lastMessage: {
          text: "",
          time: new Date()
        },
        messages: []
      };
      
      this.conversations.unshift(newConversation);
      this.selectedConversation = newConversation.id;
      this.showNewMessageModal = false;
    },
    formatTime(date) {
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

<style scoped>
.tooltip {
  @apply absolute left-full ml-2 px-2 py-1 text-xs rounded shadow-lg whitespace-nowrap;
  @apply bg-gray-800 text-white opacity-0 pointer-events-none;
  @apply transition-opacity duration-200;
  transform: translateY(-50%);
}

.group:hover .tooltip {
  @apply opacity-100;
}
</style>