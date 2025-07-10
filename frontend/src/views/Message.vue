
<template>
  <section :class="['mt-16 md:ml-64 px-4 py-6 max-w-3xl mx-auto rounded-xl shadow', darkMode ? 'bg-[#203054] text-white' : 'bg-gray-50 text-gray-900']">
    <h1 class="text-2xl font-bold mb-4">Vos messages</h1>
  </section>
</template>

<script>
export default {
  name: 'Message',
  props: {
    darkMode: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      message: '',
      photo: true,
    };
  },
  methods: {
    showMessage() {
      if (this.message && this.message.length > 0) {
        return this.message;
      } else {
        return false;
      }
    },
  },
};
</script>
