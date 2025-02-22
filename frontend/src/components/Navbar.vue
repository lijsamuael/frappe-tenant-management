<template>
  <nav class="w-full flex flex-col md:flex-row justify-between items-center p-4 bg-black rounded-sm">
    <div class="flex items-center justify-between w-full">
      <div class="flex items-center space-x-2">
        <img src="@/assets/logo.jpeg" alt="Logo" class="h-8 w-auto rounded-md" />
        <router-link to="/" class="font-bold text-white">Logo</router-link>
      </div>
      <button @click="toggleMenu" class="md:hidden text-white">
        <svg
          class="h-6 w-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
        </svg>
      </button>
    </div>
    <ul :class="['flex-col justify-center items-center space-y-4 md:flex md:flex-row md:space-y-0 md:space-x-4', { hidden: !menuOpen }]">
      <li><router-link to="/" class="text-white hover:underline">Home</router-link></li>
      <li><router-link to="/services" class="text-white hover:underline">Services</router-link></li>
      <li><router-link to="/contact" class="text-white hover:underline">Contact</router-link></li>
      <li><router-link 
  to="/account/login"
  class="text-white hover:text-black-500 rounded-md bg-blue-600 hover:bg-blue-300 px-3 py-3 inline-block"
>
  Login
</router-link></li>
</ul>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      menuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
  },
};
</script>

<style scoped>
nav {
  padding: 10px;
  background: #001F3F;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

li a {
  color: white;
  text-decoration: none;
}
</style>