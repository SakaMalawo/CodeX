<template>
  <div class="h-full bg-white flex items-center justify-center p-4">
    <div class="w-[45rem] bg-white border border-gray-200 shadow-xl rounded-md flex flex-col h-[95vh]">

      <!-- Header -->
      <header class="p-4 border-b border-gray-200 flex-shrink-0">
        <h1 class="text-2xl font-semibold text-gray-800">Créer une vidéo</h1>
      </header>

      <!-- Info utilisateur -->
      <div class="flex items-center gap-3 border-b border-gray-100 px-4 py-3 flex-shrink-0">
        <img src="#" alt="" class="w-10 h-10 border-2 border-[#1976d2] rounded-full bg-gray-200" />
        <div>
          <h2 class="text-[#1976d2] font-medium">Nom d'utilisateur</h2>
          <p class="text-gray-500 text-sm">Description de l'utilisateur</p>
        </div>
      </div>

      <!-- Formulaire + QR Code + Bouton -->
      <div class="flex flex-col flex-1 overflow-hidden bg-gray-50 px-6 py-4">

        <form @submit.prevent="submitForm" class="flex flex-col flex-1 overflow-auto space-y-6">

          <!-- Titre -->
          <div>
            <label for="title" class="block text-sm font-medium text-gray-800 mb-1">Titre de la vidéo</label>
            <input
              type="text"
              id="title"
              v-model="title"
              required
              class="w-full border border-gray-400 rounded-md p-3 placeholder-gray-500 text-gray-800 focus:outline-none focus:ring-2 focus:ring-[#1976d2]"
              placeholder="Entrez le titre de la vidéo"
            />
          </div>

          <!-- Description fixe hauteur -->
          <div>
            <label for="description" class="block text-sm font-medium text-gray-800 mb-1">Description</label>
            <textarea
              id="description"
              v-model="description"
              required
              class="w-full border border-gray-400 rounded-md p-3 placeholder-gray-500 text-gray-800 focus:outline-none focus:ring-2 focus:ring-[#1976d2] resize-none"
              placeholder="Entrez la description de la vidéo"
              style="height: 150px;"
            ></textarea>
          </div>

          <!-- Visibilité -->
          <div>
            <label class="block text-sm font-medium text-gray-800 mb-1">Confidentialité</label>
            <div class="flex gap-6 mt-2">
              <label class="flex items-center gap-2 text-gray-700">
                <input type="radio" value="public" v-model="visibility" />
                <span>Publique</span>
              </label>
              <label class="flex items-center gap-2 text-gray-700">
                <input type="radio" value="private" v-model="visibility" />
                <span>Privée</span>
              </label>
            </div>
          </div>

          <!-- Champ "Inviter" -->
          <Transition name="fade">
            <div v-if="visibility === 'private'">
              <label for="invitees" class="block text-sm font-medium text-gray-800 mb-1">Inviter (emails ou identifiants)</label>
              <input
                type="text"
                id="invitees"
                v-model="invitees"
                class="w-full border border-gray-400 rounded-md p-3 placeholder-gray-500 text-gray-800 focus:outline-none focus:ring-2 focus:ring-[#1976d2]"
                placeholder="ex : ami@example.com, utilisateurX"
              />
            </div>
          </Transition>
        </form>

        <!-- Card QR Code -->
        <transition name="fade">
          <div
            v-if="showQRCode"
            class="mt-4 bg-white border border-gray-300 shadow rounded-md p-4 flex flex-col items-center space-y-4"
            style="flex-shrink: 0;"
          >
            <h3 class="text-lg font-semibold text-gray-800">QR Code généré</h3>
            <canvas ref="qrCanvas" class="w-40 h-40"></canvas>

            <div class="w-full flex gap-3 items-center">
              <input
                type="text"
                readonly
                :value="generatedLink"
                class="flex-grow border border-gray-400 rounded-md p-2 text-gray-700 text-center cursor-pointer"
                @click="copyLink"
                title="Cliquez pour copier le lien"
              />
              <button
                @click="copyLink"
                class="bg-[#1976d2] hover:bg-[#155a9c] text-white px-4 py-2 rounded-md transition font-semibold flex-shrink-0"
              >
                Copier
              </button>
              <button class="bg-gray-400 w-10 h-10 rounded-md flex items-center justify-center hover:bg-gray-500 transition">
                <svg xmlns="http://www.w3.org/2000/svg" f viewBox="0 0 24 24" width="20" height="20" class="color-[#1976d2]">
                  <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7a3.27 3.27 0 000-1.4l7.05-4.11a3 3 0 10-.91-1.41L8 9.9a3 3 0 100 4.2l7.05 4.11a3 3 0 101.91-2.13z"/>
                </svg>
              </button>
            </div>
          </div>
        </transition>

        <!-- Bouton Créer -->
        <div class="mt-auto pt-6 border-t border-gray-200">
          <button
            type="button"
            @click="submitForm"
            class="w-full bg-[#1976d2] hover:bg-[#155a9c] text-white py-3 rounded-md transition font-semibold"
          >
            Créer la vidéo
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import QRCode from 'qrcode'

const title = ref('')
const description = ref('')
const visibility = ref('public')
const invitees = ref('')

const showQRCode = ref(false)
const generatedLink = ref('')
const qrCanvas = ref(null)

async function submitForm() {
  if (!title.value) {
    alert('Le titre est requis.')
    return
  }

  generatedLink.value = `https://mon-site.com/videos/${encodeURIComponent(title.value.trim().replace(/\s+/g, '-').toLowerCase())}`

  showQRCode.value = true

  await nextTick()

  if (qrCanvas.value) {
    QRCode.toCanvas(qrCanvas.value, generatedLink.value, { width: 160 }, (error) => {
      if (error) console.error(error)
    })
  }

  console.log({
    title: title.value,
    description: description.value,
    visibility: visibility.value,
    invitees: visibility.value === 'private' ? invitees.value : null,
    generatedLink: generatedLink.value,
  })
}

function copyLink() {
  if (!generatedLink.value) return
  navigator.clipboard.writeText(generatedLink.value)
    .then(() => alert('Lien copié dans le presse-papier !'))
    .catch(() => alert('Impossible de copier le lien.'))
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}
</style>
