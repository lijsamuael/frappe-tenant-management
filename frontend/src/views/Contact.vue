<template>
  <div class="">
    <Navbar />
    <h1 class="text-2xl font-bold mt-6 mb-4 text-center">Our comapany is located near megenagna,Addis Ababa</h1>
    <h1 class="text-2xl font-bold mt-6 mb-4 p-5 text-center">Contact Us</h1>

    <div class="flex flex-col md:flex-row gap-6 p-5">
      <!-- Map Section -->
      <div class="flex-1">
        <h2 class="text-xl font-semibold mb-2 p-4">Our Location</h2>
        <div class="h-64 mb-4">
          <iframe
            class="w-full h-full"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.8354345094774!2d144.9537363153197!3d-37.81720997975159!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f0f3f7f%3A0xcb559dc3496e251!2sYour%20Business%20Location!5e0!3m2!1sen!2sus!4v1636023500759!5m2!1sen!2sus"
            allowfullscreen=""
            loading="lazy"
          ></iframe>
        </div>
      </div>

      <!-- Contact Information and Form Section -->
      <div class="flex-1">
        <h2 class="text-xl font-semibold mb-2">Contact Information</h2>
        <p class="mb-2"><strong>Phone:</strong> (+251) 9456-7890</p>
        <p class="mb-2"><strong>Email:</strong> contact@example.com</p>
        
        <h2 class="text-xl font-semibold mb-2 mt-4">Send Us a Message</h2>
        <form @submit.prevent="submitForm" class="space-y-4">
          <div>
            <label for="name" class="block text-gray-700">Name</label>
            <input type="text" id="name" v-model="formData.name" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" required />
          </div>

          <div>
            <label for="email" class="block text-gray-700">Email</label>
            <input type="email" id="email" v-model="formData.email" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" required />
          </div>

          <div>
            <label for="message" class="block text-gray-700">Message</label>
            <textarea id="message" v-model="formData.message" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2" rows="4" required></textarea>
          </div>

          <button type="submit" class="w-full bg-blue-500 text-white rounded-md px-4 py-2 hover:bg-blue-600">
            Send Message
          </button>
        </form>
      </div>
    </div>
      <Footer/>
  </div>

</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
export default {
  name: 'Contact',
  components: { Navbar,Footer },
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: ''
      }
    };
  },
  methods: {
    submitForm() {
      // Handle form submission logic here (e.g., sending to an API)
      console.log('Form submitted:', this.formData);
      
      // Clear the form after submission
      this.formData.name = '';
      this.formData.email = '';
      this.formData.message = '';
    }
  }
}
</script>

<style>
/* Any additional styles */
</style>