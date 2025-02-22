<template>
  <div>
    <Navbar />
    
    <section class="hero bg-blue-800 text-black text-center py-20">
      <h1 class="text-4xl font-bold mb-4 text-blue">Welcome to Our Website</h1>
      <p class="text-xl mb-6">We provide amazing services to help you succeed.</p>
      <router-link to="/contact" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Get in Touch
      </router-link>
    </section>

    <!-- Services Section -->
    <section class="services py-20 bg-gray-100">
      <div class="container mx-auto text-center">
        <h2 class="text-3xl font-bold mb-8">Our Services</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="service bg-white p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Service 1</h3>
            <p>Details about service 1...</p>
          </div>
          <div class="service bg-white p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Service 2</h3>
            <p>Details about service 2...</p>
          </div>
          <div class="service bg-white p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Service 3</h3>
            <p>Details about service 3...</p>
          </div>
        </div>
      </div>
    </section>

    <section class="testimonials py-20 bg-gray-800 text-white">
      <div class="container mx-auto text-center">
        <h2 class="text-3xl font-bold mb-8">What Our Clients Say</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div class="testimonial p-6 bg-gray-700 rounded shadow">
            <p class="mb-4">"Amazing service, really helped my business grow!"</p>
            <p class="font-semibold">- Client A</p>
          </div>
          <div class="testimonial p-6 bg-gray-700 rounded shadow">
            <p class="mb-4">"Great experience, highly recommend!"</p>
            <p class="font-semibold">- Client B</p>
          </div>
          <div class="testimonial p-6 bg-gray-700 rounded shadow">
            <p class="mb-4">"Professional and reliable service!"</p>
            <p class="font-semibold">- Client C</p>
          </div>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'Home',
  components: { Navbar, Footer },
};
</script>

<style scoped>
.hero {
  background-image: url('@/assets/logo.jpeg'); 
  background-size: cover;
  background-position: center;
}

.services {
  background-color: #f7fafc;; 
}

.testimonials {
  background-color: #1f2937; 
}

.testimonial {
  transition: transform 0.2s;
}

.testimonial:hover {
  transform: scale(1.05);
}
</style>