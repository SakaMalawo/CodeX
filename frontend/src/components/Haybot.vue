<template>
  <div class="flex h-screen justify-end bg-gray-100">
    <div class="flex-1"></div>
    <!-- filepath: /opt/lampp/htdocs/Projet/hayBot../frontend/src/components/Haybot.vue -->
<div
  v-if="minimized"
  class="fixed z-50 bg-indigo-600 text-white rounded-full shadow-lg flex items-center justify-center cursor-pointer w-16 h-16 select-none"
  :style="{ left: bubbleX + 'px', top: bubbleY + 'px' }"
  @mousedown="onBubbleMouseDown"
  @mouseup="onBubbleMouseUpOpen"
  title="Ouvrir le chatbot"
>
  <span class="text-2xl">💬</span>
</div>
    <!-- Chatbot principal -->
    <div
      v-else
      ref="chatbot" class="relative min-h-[600px] sm:p-8 max-w-full border-2 border-indigo-200 bg-white shadow-lg overflow-hidden flex flex-col"
      :style="{ width: width + 'px', minWidth: '400px' }"
    >
      <!-- filepath: /opt/lampp/htdocs/Projet/hayBot../frontend/src/components/Haybot.vue -->
<div class="flex items-center justify-between px-4 h-16  bg-gray-100 rounded-t-lg">
  <div class="flex items-center gap-2">
    <!-- Icône du bot -->
    <span class="font-bold text-indigo-700 text-lg">Haybot</span>
  </div>
  <button
    class="bg-indigo-600 text-white px-3 py-1 rounded-full shadow hover:bg-indigo-700 transition z-50"
    @click="minimized = true"
    title="Réduire"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
    </svg>
  </button>
</div>
      <!-- Handle de redimensionnement à GAUCHE -->
      <div
        class="absolute top-0 left-0 h-full w-3 cursor-ew-resize z-40"
        @mousedown="startResize"
        style="pointer-events: auto;"
      ></div>
      <div
        ref="chatContainer"
        class="rounded-md p-2 flex-1 overflow-y-auto space-y-4 "
      >
        <div
          v-for="(msg, i) in messages"
          :key="i"
          :class="[
            'flex items-start',
            msg.from === 'user' ? 'justify-end' : 'justify-start'
          ]"
        >
          <div class="flex items-end space-x-2 gap-2 pt-3" :class="msg.from === 'user' ? 'flex-row-reverse' : ''">
            <div
              class="w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center text-sm font-bold"
            >
              {{ msg.from === 'user' ? 'U' : 'H' }}
            </div>
            <div
              :class="[
                'px-4 py-2 max-w-full sm:max-w-[90%] rounded-2xl text-sm break-words',
                msg.from === 'user'
                  ? 'bg-indigo-100 text-indigo-800'
                  : 'bg-gray-200 text-gray-900'
              ]"
            >
              {{ msg.text }}
            </div>
          </div>
        </div>
        <div v-if="loading" class="text-sm italic text-gray-500 mr-3 mt-2">Haybot est en train d’écrire...</div>
      </div>
      <!-- filepath: /opt/lampp/htdocs/Projet/hayBot../frontend/src/components/Haybot.vue -->
<form @submit.prevent="sendMessage" class="flex items-center gap-2 bg-white border-t border-indigo-100 px-3 py-2 rounded-b-lg">
  <!-- Upload document -->
  <label class="cursor-pointer flex items-center">
    <input
      type="file"
      class="hidden"
      multiple
      @change="handleFileUpload"
    />
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-indigo-600 hover:text-indigo-800 transition" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16.24 7.76l-7.07 7.07a3 3 0 104.24 4.24l7.07-7.07a5 5 0 10-7.07-7.07l-7.07 7.07"/>
    </svg>
  </label>

  <!-- Zone de texte -->
  <input
    v-model="input"
    class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400 text-sm text-black"
    placeholder="Pose ta question..."
    :disabled="loading"
    autocomplete="off"
  />

  <!-- Envoyer -->
  <button
    type="submit"
    :disabled="!input || loading"
    class="p-2 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 disabled:opacity-50 flex items-center justify-center"
    aria-label="Envoyer"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12l14-7-7 14-2-5-5-2z"/>
    </svg>
  </button>
</form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount  } from 'vue'
import axios from 'axios'

const input = ref('')
const messages = ref([])
const loading = ref(false)

const width = ref(600)
const resizing = ref(false)
const startX = ref(0)
const startWidth = ref(600)
const chatbot = ref(null)

const minimized = ref(false) // <-- Ajout de l'état minimisé


// Position de la bulle
const bubbleX = ref(window.innerWidth - 100)
const bubbleY = ref(window.innerHeight - 100)
const dragging = ref(false)
const dragMoved = ref(false) // <-- AJOUT
const dragOffsetX = ref(0)
const dragOffsetY = ref(0)

const onBubbleMouseDown = (e) => {
  dragging.value = true
  dragMoved.value = false // <-- AJOUT
  dragOffsetX.value = e.clientX - bubbleX.value
  dragOffsetY.value = e.clientY - bubbleY.value
  document.addEventListener('mousemove', onBubbleMouseMove)
  document.addEventListener('mouseup', onBubbleMouseUp)
}

const onBubbleMouseMove = (e) => {
  if (!dragging.value) return
  dragMoved.value = true // <-- AJOUT
  bubbleX.value = e.clientX - dragOffsetX.value
  bubbleY.value = e.clientY - dragOffsetY.value
}

const onBubbleMouseUp = () => {
  dragging.value = false
  document.removeEventListener('mousemove', onBubbleMouseMove)
  document.removeEventListener('mouseup', onBubbleMouseUp)
}

onBeforeUnmount(() => {
  document.removeEventListener('mousemove', onBubbleMouseMove)
  document.removeEventListener('mouseup', onBubbleMouseUp)
})

// Nouvelle fonction pour ouvrir le chatbot uniquement si pas de drag
const onBubbleMouseUpOpen = () => {
  if (!dragMoved.value) {
    minimized.value = false
  }
}

const sendMessage = async () => {
  if (!input.value.trim()) return

  const userText = input.value
  input.value = ''
  loading.value = true
  messages.value.push({ from: 'user', text: userText })

  try {
    const res = await axios.post('http://localhost:8000/api/chat', {
      message: userText
    })
    messages.value.push({ from: 'bot', text: res.data.reply })
  } catch (err) {
    messages.value.push({ from: 'bot', text: '❌ Erreur serveur.' })
  } finally {
    loading.value = false
  }
}

// Redimensionnement manuel
const startResize = (e) => {
  resizing.value = true
  startX.value = e.clientX
  startWidth.value = width.value
  document.addEventListener('mousemove', resize)
  document.addEventListener('mouseup', stopResize)
}

const resize = (e) => {
  if (!resizing.value) return
  const delta = e.clientX - startX.value
  width.value = Math.max(300, startWidth.value - delta)
}

const stopResize = () => {
  resizing.value = false
  document.removeEventListener('mousemove', resize)
  document.removeEventListener('mouseup', stopResize)
}

onBeforeUnmount(() => {
  document.removeEventListener('mousemove', resize)
  document.removeEventListener('mouseup', stopResize)
})




const uploadedFiles = ref([])
const analyzing = ref(false)

const handleFileUpload = async (event) => {
  const files = event.target.files
  for (let i = 0; i < files.length; i++) {
    const formData = new FormData()
    formData.append('file', files[i])
    analyzing.value = true
    try {
      const res = await axios.post('http://localhost:8000/api/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      uploadedFiles.value.push(files[i])
      messages.value.push({ from: 'user', text: `📎 Document importé : ${files[i].name}` })
      if (res.data.evaluation) {
        messages.value.push({ from: 'bot', text: `🤖 Analyse du document : ${res.data.evaluation}` })
      }
    } catch (err) {
      messages.value.push({ from: 'user', text: `❌ Erreur lors de l'import du document : ${files[i].name}` })
    } finally {
      analyzing.value = false
    }
  }
  event.target.value = ''
}

</script>
