<!-- src/views/Services.vue -->
<template>
  <div class="w-full">
    <Navbar />
    <h1 class="text-2xl font-bold mt-6 mb-4 text-center">Our Services</h1>
    <div class="grid md:grid-cols-2 gap-6 p-5" >
      <!-- Tenant Management Section -->
      <div class="bg-white rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-2 p-2">Tenant Management</h2>
        <p class="text-gray-700 mb-4 p-3">
          Our tenant management service includes screening potential tenants,
          managing lease agreements, and handling tenant relations to ensure a
          smooth and professional rental experience.
        </p>
      </div>

      <!-- Housing Contracts Section -->
      <div class="bg-white rounded-lg shadow-md p-4">
        <h2 class="text-xl font-semibold mb-2">Housing Contracts</h2>
        <p class="text-gray-700 mb-4">
          We provide comprehensive housing contracts that are legally binding
          and tailored to protect both landlords and tenants, ensuring clarity
          in responsibilities and expectations.
        </p>
      </div>

      <!-- Additional Services Section -->
      <div class="bg-white rounded-lg shadow-md p-4">
        <h2 class="text-xl font-semibold mb-2">Property Maintenance</h2>
        <p class="text-gray-700 mb-4">
          Our property maintenance services ensure that your property is well
          taken care of. From emergency repairs to routine inspections, we have
          you covered.
        </p>
      </div>

      <div class="bg-white rounded-lg shadow-md p-4">
        <h2 class="text-xl font-semibold mb-2">Financial Management</h2>
        <p class="text-gray-700 mb-4">
          We offer financial management services including rent collection,
          budgeting, and financial reporting, ensuring your investments are
          profitable and well-managed.
        </p>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'; 
import Footer from  '@/components/Footer.vue';
export default {
  name: 'Services',
  components: {
    Navbar ,
    Footer
  }
}
</script>

<style>
/* add styels here  */
</style>