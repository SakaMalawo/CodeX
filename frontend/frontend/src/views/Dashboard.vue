<template>
  <div>
    <!-- Sidebar affiché uniquement sur Dashboard -->
    <MainSidebar :darkMode="darkMode" />
    <div class="ml-0 md:ml-[240px]">
      <!-- Navbar affiché uniquement sur Dashboard -->
      <MainNavbar
        @toggle-dark-mode="toggleDarkMode"
        :darkMode="darkMode"
        class="fixed w-full left-0 top-0 z-30"
      />
      <!-- Contenu principal du Dashboard -->
      <main
        class="pt-[64px] mt-20 md:ml-6 h-[calc(100vh-64px-2rem)] overflow-auto bg-gray-50 dark:bg-[#0e1a2b] p-4 md:p-8 rounded-xl"
      >
        <div class="max-w-[1800px] mx-auto w-full">
          <!-- Ligne 1 : Bonjour + Calendrier -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <!-- Bloc Bonjour (2/3) -->
            <section
              class="col-span-1 md:col-span-2 relative rounded-2xl shadow-lg p-6 md:p-10 flex flex-col justify-between min-h-[180px] bg-white dark:bg-[#1a2942] transition-colors"
            >
              <h2
                class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white z-10"
              >
                Bonjour
                <span class="text-indigo-600 dark:text-indigo-300">{{
                  userName
                }}</span>
              </h2>
              <p class="mt-2 text-gray-600 dark:text-gray-300 z-10">
                Voici un rappel de vos derniers événements et activités
                importantes.
              </p>
              <div class="mt-4 flex flex-wrap gap-2 z-10">
                <span
                  v-for="event in recentEvents"
                  :key="event"
                  class="px-3 py-1 rounded-full bg-gray-200 dark:bg-[#22345a] text-xs text-gray-700 dark:text-gray-200"
                >
                  {{ event }}
                </span>
              </div>
            </section>
            <!-- Calendrier (1/3) -->
            <section
              class="col-span-1 bg-white dark:bg-[#1a2942] rounded-2xl shadow-lg p-6 flex flex-col gap-4 min-h-[180px]"
            >
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                  Calendrier
                </h3>
                <div class="flex gap-1">
                  <span
                    v-for="day in days"
                    :key="day"
                    :class="[
                      'px-2 py-1 rounded-lg text-xs font-medium',
                      day === today
                        ? 'bg-indigo-500 text-white'
                        : 'bg-gray-100 dark:bg-[#22345a] text-gray-700 dark:text-gray-200',
                    ]"
                  >
                    {{ day }}
                  </span>
                </div>
              </div>
              <div class="text-sm text-gray-500 dark:text-gray-300">
                {{ events.length }} évènement(s) cette semaine
              </div>
              <div class="mt-4">
                <h4 class="font-bold text-gray-900 dark:text-white">
                  {{ nextLesson.name }}
                </h4>
                <div class="text-xs text-gray-500 dark:text-gray-300">
                  {{ nextLesson.time }}
                </div>
              </div>
              <div class="mt-4">
                <h5 class="font-semibold text-gray-900 dark:text-white mb-2">
                  Agenda
                </h5>
                <ul>
                  <li
                    v-for="item in agenda"
                    :key="item.name"
                    class="flex justify-between items-center py-1 text-sm text-gray-700 dark:text-gray-200"
                  >
                    <span>{{ item.name }}</span>
                    <span class="text-xs text-gray-500 dark:text-gray-400">{{
                      item.time
                    }}</span>
                  </li>
                </ul>
              </div>
            </section>
          </div>
          <!-- Ligne 2 : Performance + Mes visites + Événements à venir -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Performance (1/3) -->
            <section
              class="col-span-1 bg-gray-100 dark:bg-[#18243a] rounded-2xl shadow-lg p-6 flex flex-col gap-4 min-w-[220px]"
            >
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                  Performance
                </h3>
                <select
                  v-model="selectedMonth"
                  class="rounded-lg px-3 py-1 text-sm font-medium border-none bg-gray-200 dark:bg-[#22345a] text-gray-700 dark:text-gray-200 focus:outline-none"
                >
                  <option v-for="month in months" :key="month" :value="month">
                    {{ month }}
                  </option>
                </select>
              </div>
              <!-- Best lesson -->
              <div
                class="bg-white dark:bg-transparent rounded-xl shadow p-4 flex items-center justify-between gap-4"
              >
                <div>
                  <div
                    class="text-xs uppercase font-bold text-gray-500 dark:text-gray-300 mb-1"
                  >
                    Best lesson
                  </div>
                  <div class="flex items-center gap-3">
                    <span
                      class="text-2xl font-bold text-gray-900 dark:text-white"
                      >{{ bestLesson.percent }}%</span
                    >
                    <span
                      class="text-base font-semibold text-gray-700 dark:text-gray-200"
                      >{{ bestLesson.module }}</span
                    >
                  </div>
                </div>
                <button
                  class="px-4 py-2 rounded-lg shadow bg-gray-100 dark:bg-[#22345a] text-gray-900 dark:text-white font-semibold text-sm hover:bg-gray-200 dark:hover:bg-[#2b3a5a] transition"
                >
                  Toutes les leçons
                </button>
              </div>
              <!-- Diagrammes verticaux -->
              <div class="flex items-end gap-4 mt-4 h-32">
                <div
                  v-for="item in performances"
                  :key="item.label"
                  class="flex flex-col items-center flex-1"
                >
                  <div class="relative w-7 h-full flex flex-col justify-end">
                    <div
                      class="absolute bottom-0 left-0 w-full rounded-t-lg"
                      :style="{
                        height: item.percent + '%',
                        background:
                          'linear-gradient(180deg,#39ff14 0%,#00ffa3 100%)',
                        boxShadow: '0 2px 8px #39ff1499',
                        transition: 'height 0.5s',
                      }"
                    ></div>
                    <div
                      class="absolute bottom-0 left-0 w-full rounded-t-lg"
                      :style="{
                        height: '100%',
                        background: darkMode ? '#22345a' : '#f5f5f5',
                        zIndex: 0,
                      }"
                    ></div>
                  </div>
                  <span
                    class="mt-2 text-xs font-medium text-gray-700 dark:text-gray-200"
                    >{{ item.label }}</span
                  >
                </div>
              </div>
            </section>
            <!-- Mes visites (1/3) -->
            <section
              class="col-span-1 bg-gray-100 dark:bg-[#18243a] rounded-2xl shadow-lg p-6 flex flex-col gap-4 min-w-[220px]"
            >
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                  Mes visites
                </h3>
                <select
                  v-model="selectedMonth"
                  class="rounded-lg px-3 py-1 text-sm font-medium border-none bg-gray-200 dark:bg-[#22345a] text-gray-700 dark:text-gray-200 focus:outline-none"
                >
                  <option v-for="month in months" :key="month" :value="month">
                    {{ month }}
                  </option>
                </select>
              </div>
              <!-- Diagrammes circulaires -->
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
                  <span
                    class="mt-2 text-xs font-medium text-gray-700 dark:text-gray-200"
                    >{{ item.label }}</span
                  >
                  <span class="text-xs text-gray-500 dark:text-gray-400"
                    >{{ item.percent }}%</span
                  >
                </div>
              </div>
            </section>
            <!-- Événements à venir (1/3) -->
            <section
              class="col-span-1 bg-white dark:bg-[#1a2942] rounded-2xl shadow-lg p-6 flex flex-col gap-4"
            >
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                  Événements à venir
                </h3>
                <button
                  class="px-3 py-1 rounded-lg bg-gray-100 dark:bg-[#22345a] text-gray-900 dark:text-white text-sm font-medium shadow hover:bg-gray-200 dark:hover:bg-[#2b3a5a] transition"
                >
                  Voir plus
                </button>
              </div>
              <ul>
                <li
                  v-for="event in upcomingEvents"
                  :key="event.name"
                  class="mb-2"
                >
                  <div class="font-semibold text-gray-900 dark:text-white">
                    {{ event.name }}
                  </div>
                  <div class="text-xs text-gray-500 dark:text-gray-300">
                    {{ event.date }}
                  </div>
                </li>
              </ul>
            </section>
          </div>
          <!-- Enseignants (en dessous) -->
          <div class="mt-6">
            <div class="flex items-center justify-between mb-2">
              <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                Les enseignants
              </h3>
              <button
                class="px-3 py-1 rounded-lg bg-gray-100 dark:bg-[#22345a] text-gray-900 dark:text-white text-sm font-medium shadow hover:bg-gray-200 dark:hover:bg-[#2b3a5a] transition"
              >
                Tout voir
              </button>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                v-for="teacher in teachers"
                :key="teacher.name"
                class="flex items-center bg-white dark:bg-[#1a2942] rounded-xl shadow p-4 gap-4"
              >
                <img
                  :src="teacher.avatar"
                  alt="avatar"
                  class="w-14 h-14 rounded-full object-cover"
                />
                <div class="flex-1">
                  <h4 class="font-bold text-gray-900 dark:text-white">
                    {{ teacher.name }}
                  </h4>
                  <div class="flex items-center gap-2 mt-1">
                    <a
                      :href="'mailto:' + teacher.email"
                      class="text-indigo-500 hover:text-indigo-700"
                    >
                      <svg
                        class="w-5 h-5"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M16 12H8m8 0a4 4 0 11-8 0 4 4 0 018 0zm0 0v1a4 4 0 01-8 0v-1m8 0V9a4 4 0 00-8 0v3"
                        />
                      </svg>
                    </a>
                    <a
                      :href="'https://wa.me/' + teacher.phone"
                      target="_blank"
                      class="text-green-500 hover:text-green-700"
                    >
                      <svg
                        class="w-5 h-5"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M16.72 11.06a6 6 0 10-8.48 0l-1.42 1.42a1 1 0 00.7 1.7h1.18a6 6 0 0011.18 0h1.18a1 1 0 00.7-1.7l-1.42-1.42z"
                        />
                      </svg>
                    </a>
                  </div>
                  <div class="text-xs text-gray-500 dark:text-gray-300 mt-1">
                    {{ teacher.specialty }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <!-- Bot persistant affiché uniquement sur Dashboard -->
      <Citra :dark="darkMode" />
    </div>
  </div>
</template>

<script>
import MainNavbar from "../components/MainNavbar.vue";
import MainSidebar from "../components/MainSidebar.vue";
import Citra from "../components/Citra.vue";

export default {
  name: "Dashboard",
  components: { MainNavbar, MainSidebar, Citra },
  data() {
    return {
      darkMode: document.documentElement.classList.contains("dark"),
      userName: "Saka",
      recentEvents: [
        "Rendu devoir HTML",
        "Nouveau message",
        "Cours Symfony à venir",
      ],
      months: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin"],
      selectedMonth: "Juin",
      bestLesson: { percent: 92, module: "Vue.js" },
      performances: [
        { label: "HTML", percent: 80, color: "#39ff14" },
        { label: "Tailwind", percent: 65, color: "#00ffa3" },
        { label: "Vue", percent: 92, color: "#2196F3" },
        { label: "Symfony", percent: 70, color: "#00C6FB" },
        { label: "Django", percent: 55, color: "#FFD600" },
        { label: "Rasa", percent: 40, color: "#FF9800" },
      ],
      teachers: [
        {
          name: "Jean Dupont",
          avatar: "https://randomuser.me/api/portraits/men/32.jpg",
          email: "jean.dupont@example.com",
          phone: "33612345678",
          specialty: "PHP, React",
        },
        {
          name: "Marie Curie",
          avatar: "https://randomuser.me/api/portraits/women/44.jpg",
          email: "marie.curie@example.com",
          phone: "33687654321",
          specialty: "Django, Vue",
        },
      ],
      days: ["Lun", "Mar", "Mer", "Jeu", "Ven"],
      today: "Mar",
      events: [
        { name: "Cours Vue.js", date: "2025-06-18" },
        { name: "Devoir Symfony", date: "2025-06-19" },
      ],
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
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      if (this.darkMode) {
        document.documentElement.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
      }
    },
    // Pour les diagrammes circulaires SVG
    describeArc(cx, cy, r, startAngle, endAngle) {
      const start = this.polarToCartesian(cx, cy, r, endAngle);
      const end = this.polarToCartesian(cx, cy, r, startAngle);
      const arcSweep = endAngle - startAngle <= 180 ? "0" : "1";
      return [
        "M",
        start.x,
        start.y,
        "A",
        r,
        r,
        0,
        arcSweep,
        0,
        end.x,
        end.y,
      ].join(" ");
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
