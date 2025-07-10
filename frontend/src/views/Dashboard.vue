<template>
  <div :class="['h-full overflow-auto p-4 md:p-8 rounded-xl', darkMode ? 'dark bg-[#10192b]' : 'bg-gray-50']">
    <div class="max-w-[1800px] mx-auto w-full">
      <!-- Ligne 1 -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <!-- Bonjour -->
        <section
          class="col-span-1 md:col-span-2 relative rounded-2xl shadow-lg p-6 md:p-10 flex flex-col justify-between min-h-[180px] bg-white dark:bg-[#17213a]"
        >
          <h2 class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white z-10">
            Bonjour
            <span class="text-indigo-600 dark:text-indigo-300">{{ userName }}</span>
          </h2>
          <p class="mt-2 text-gray-600 dark:text-gray-100 z-10">
            Voici un rappel de vos derniers événements et activités importantes.
          </p>
          <div class="mt-4 flex flex-wrap gap-2 z-10 relative">
            <svg class="absolute left-0 top-0 w-full h-full opacity-10 pointer-events-none" viewBox="0 0 200 40" fill="none">
              <defs>
                <pattern id="dots" x="0" y="0" width="10" height="10" patternUnits="userSpaceOnUse">
                  <circle cx="1" cy="1" r="1" fill="#6366f1" />
                </pattern>
              </defs>
              <rect width="200" height="40" fill="url(#dots)" />
            </svg>
            <span
              v-for="event in recentEvents"
              :key="event"
              class="px-3 py-1 rounded-full bg-gradient-to-r from-indigo-400 via-sky-300 to-green-200 dark:from-indigo-700 dark:via-indigo-500 dark:to-sky-700 text-xs text-white font-semibold shadow flex items-center gap-2 relative"
              style="backdrop-filter: blur(2px); border: 1.5px solid #6366f1;"
            >
              <svg class="w-4 h-4 text-white opacity-80" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
              {{ event }}
            </span>
          </div>
        </section>
        <!-- Calendrier -->
        <section
          class="col-span-1 bg-white dark:bg-[#17213a] rounded-2xl shadow-lg p-6 flex flex-col gap-4 min-h-[180px]"
        >
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Calendrier</h3>
            <div class="flex gap-1">
              <span
                v-for="day in days"
                :key="day"
                :class="[
                  'px-2 py-1 rounded-lg text-xs font-medium',
                  day === today
                    ? 'bg-indigo-500 text-white'
                    : 'bg-gray-100 dark:bg-[#22345a] text-gray-700 dark:text-white',
                ]"
              >
                {{ day }}
              </span>
            </div>
          </div>
          <div class="text-sm text-gray-500 dark:text-gray-100">
            {{ events.length }} évènement(s) cette semaine
          </div>
          <div class="mt-4">
            <h4 class="font-bold text-gray-900 dark:text-white">{{ nextLesson.name }}</h4>
            <div class="text-xs text-gray-500 dark:text-white">{{ nextLesson.time }}</div>
          </div>
          <div class="mt-4">
            <h5 class="font-semibold text-gray-900 dark:text-white mb-2">Agenda</h5>
            <ul class="space-y-1">
              <li
                v-for="item in agenda"
                :key="item.name"
                class="flex justify-between items-center py-1 text-sm text-gray-700 dark:text-white relative pl-4"
              >
                <span class="absolute left-0 top-1/2 -translate-y-1/2 w-1 h-6 rounded bg-gradient-to-b from-indigo-400 via-sky-400 to-green-300 dark:from-indigo-600 dark:to-sky-700"></span>
                <span>{{ item.name }}</span>
                <span class="text-xs text-gray-500 dark:text-gray-100">{{ item.time }}</span>
                <span class="text-xs text-gray-500 dark:text-white">{{ item.time }}</span>
              </li>
            </ul>
          </div>
        </section>
      </div>

      <!-- Ligne 2 -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Performance -->
        <section
          class="col-span-1 bg-gray-100 dark:bg-[#17213a] rounded-2xl shadow-lg p-6 flex flex-col gap-4"
        >
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Performance</h3>
            <select
              v-model="selectedMonth"
              class="rounded-lg px-3 py-1 text-sm font-medium border-none bg-gray-200 dark:bg-[#22345a] text-gray-700 dark:text-gray-100"
            >
              <option v-for="month in months" :key="month" :value="month">{{ month }}</option>
            </select>
          </div>
          <div class="bg-white dark:bg-[#22345a] rounded-xl shadow p-4 flex items-center justify-between gap-4 mb-10">
            <div>
              <div class="text-xs uppercase font-bold text-gray-500 dark:text-gray-100 mb-1">Meilleure leçon</div>
              <div class="flex items-center gap-3">
                <span class="text-2xl font-bold text-gray-900 dark:text-white">{{ bestLesson.percent }}%</span>
                <span class="text-base font-semibold text-gray-700 dark:text-white">{{ bestLesson.module }}</span>
              </div>
            </div>
            <button
              class="px-4 py-2 rounded-lg shadow bg-gray-100 dark:bg-[#22345a] text-gray-900 dark:text-white font-semibold text-sm hover:bg-gray-200 dark:hover:bg-[#2b3a5a]"
            >
              Toutes les leçons
            </button>
          </div>
          <!-- Histogramme vertical -->
          <div class="flex items-end gap-6 h-48 w-full relative mt-16">
            <div class="flex flex-1 items-end h-full">
              <div
                v-for="item in performances"
                :key="item.label"
                class="flex flex-col items-center flex-1"
              >
                <div class="relative flex items-end w-7 h-full">
                  <!-- Barre 100% grise -->
                  <div
                    class="absolute bottom-0 left-0 w-full"
                    style="height:5cm; background:#e5e7eb; opacity:0.6; border-radius:0.375rem; z-index:0;"
                  ></div>
                  <!-- Barre colorée -->
                  <div
                    :style="{
                      height: (item.percent * 5) / 100 + 'cm',
                      background: `${item.color}`,
                      boxShadow: `0 8px 24px 0 ${item.color}33`,
                      borderRadius: '0.375rem',
                      zIndex: 1
                    }"
                    class="w-7 border-2 border-gray-300 dark:border-gray-600 shadow-lg transition-all duration-500"
                  ></div>
                </div>
                <span class="mt-1 text-xs font-medium text-gray-700 dark:text-white">{{ item.label }}</span>
                <span class="text-xs text-gray-500 dark:text-white">{{ item.percent }}%</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Mes visites -->
        <section
          class="col-span-1 bg-gray-100 dark:bg-[#17213a] rounded-2xl shadow-lg p-6 flex flex-col gap-4"
        >
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Mes visites</h3>
            <select
              v-model="selectedMonth"
              class="rounded-lg px-3 py-1 text-sm font-medium border-none bg-gray-200 dark:bg-[#22345a] text-gray-700 dark:text-gray-100"
            >
              <option v-for="month in months" :key="month" :value="month">{{ month }}</option>
            </select>
          </div>
          <div class="grid grid-cols-2 gap-4 mt-4">
            <div
              v-for="item in performances"
              :key="item.label"
              class="flex flex-col items-center"
            >
              <svg viewBox="0 0 36 36" class="w-20 h-20">
                <path
                  class="text-gray-200 dark:text-[#22345a]"
                  stroke="currentColor"
                  stroke-width="4"
                  fill="none"
                  d="M18 2.0845
                    a 15.9155 15.9155 0 0 1 0 31.831
                    a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  :stroke="item.color"
                  stroke-width="4"
                  fill="none"
                  :d="describeArc(18, 18, 15.9155, 0, item.percent * 3.6)"
                />
              </svg>
              <span class="mt-2 text-xs font-medium text-gray-700 dark:text-white">{{ item.label }}</span>
              <span class="text-xs text-gray-500 dark:text-white">{{ item.percent }}%</span>
            </div>
          </div>
        </section>

        <!-- Événements à venir -->
        <section
          class="col-span-1 bg-white dark:bg-[#17213a] rounded-2xl shadow-lg p-6 flex flex-col gap-4"
        >
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Événements à venir</h3>
            <button
              class="px-3 py-1 rounded-lg bg-gray-100 dark:bg-[#22345a] text-gray-900 dark:text-white text-sm font-medium shadow hover:bg-gray-200 dark:hover:bg-[#2b3a5a]"
            >
              Voir plus
            </button>
          </div>
          <ul>
            <li v-for="event in upcomingEvents" :key="event.name" class="mb-2">
              <div class="font-semibold text-gray-900 dark:text-white">{{ event.name }}</div>
              <div class="text-xs text-gray-500 dark:text-white">{{ event.date }}</div>
            </li>
          </ul>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      userName: "Toi",
      recentEvents: [
        "Rendu devoir HTML",
        "Nouveau message",
        "Cours Symfony à venir",
      ],
      months: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin"],
      selectedMonth: "Juin",
      bestLesson: { percent: 92, module: "Vue.js" },
      performances: [
        { label: "HTML", percent: 80, color: "#e44d26" }, // orange HTML5
        { label: "Tailwind", percent: 65, color: "#38bdf8" }, // bleu Tailwind
        { label: "Vue", percent: 92, color: "#42b883" }, // vert Vue
        { label: "Symfony", percent: 70, color: "#000000" }, // noir Symfony
        { label: "Django", percent: 55, color: "#092e20" }, // vert foncé Django
        { label: "Rasa", percent: 40, color: "#5e60ba" }, // violet Rasa
      ],
      days: ["Lun", "Mar", "Mer", "Jeu", "Ven"],
      today: "Mar",
      events: [],
      nextLesson: { name: "Cours Vue.js", time: "Aujourd'hui 14:00 - 16:00" },
      agenda: [
        { name: "Cours Vue.js", time: "14:00 - 16:00" },
        { name: "Devoir Symfony", time: "16:30 - 18:00" },
      ],
      upcomingEvents: [
        { name: "Hackathon", date: "20 Juin 2025, 09:00" },
        { name: "Présentation Projet", date: "22 Juin 2025, 15:00" },
      ],
    };
  },
  methods: {
    describeArc(cx, cy, r, startAngle, endAngle) {
      const start = this.polarToCartesian(cx, cy, r, endAngle);
      const end = this.polarToCartesian(cx, cy, r, startAngle);
      const arcSweep = endAngle - startAngle <= 180 ? "0" : "1";
      return ["M", start.x, start.y, "A", r, r, 0, arcSweep, 0, end.x, end.y].join(" ");
    },
    polarToCartesian(cx, cy, r, angleInDegrees) {
      const angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
      return {
        x: cx + r * Math.cos(angleInRadians),
        y: cy + r * Math.sin(angleInRadians),
      };
    },
  },
};
</script>
