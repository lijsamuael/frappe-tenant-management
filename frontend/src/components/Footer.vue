<!-- src/components/Footer.vue -->
<template>
  <footer id="footer" class="footer mt-5 rounded-sm">
    <p>&copy; {{ currentYear }} Tenant Management System. All rights reserved.</p>
  </footer>
</template>

<script>
export default {
    name:"Footer",
  data() {
    return {
      currentYear: new Date().getFullYear(),
    };
  },
};
</script>

<style scoped>
.footer {
  background-color: #001F3F;
  color: white;
  text-align: center;
  padding: 10px 0;
}
</style>