<template>
  <div class="max-w-3xl py-12 mx-auto">
    <!-- House List Grouped by Status -->
    <ListView
      :columns="[
        { label: 'House number', key: 'name' },
        { label: 'Status', key: 'status' },
        { label: 'Rent amount', key: 'rent_amount' }
      ]"
      :rows="groupedHouses"
      row-key="name"
    >
      <template #group-header="{ group }">
        <span class="text-base font-medium leading-6 text-gray-900">
          {{ group.group }} ({{ group.rows.length }}) 
        </span>
      </template>
    </ListView>

    <br>

    <!-- Contract List -->
    <ListView
      :columns="[
        { label: 'Contract Id', key: 'name' },
        { label: 'Broker', key: 'broker' },
        { label: 'House number', key: 'house_serial_number' }
      ]"

      :rows="contracts.list.data"

      :options="{
      selectable: true,
      showTooltip: true,
      resizeColumn: true,
    }"
      row-key="name"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { createListResource, ListView } from 'frappe-ui'

const doctypes = createListResource({
  doctype: 'House',
  fields: ['*'],
  auto: true,
  orderBy: 'name desc'
})

const contracts = createListResource({
  doctype: 'Contract',
  fields: ['*'],
  auto: true,
  orderBy: 'name desc'
})

// Grouping houses by status (Rented & Open for rent)
const groupedHouses = computed(() => {
  if (!doctypes.list.data) return []

  const rented = doctypes.list.data.filter(h => h.status === 'Rented')
  const openForRent = doctypes.list.data.filter(h => h.status === 'Open for rent')

  return [
    {
      group: 'Rented',
      collapsed: false,
      rows: rented
    },
    {
      group: 'Open for rent',
      collapsed: false,
      rows: openForRent
    }
  ]
})
</script>
