<template>
	<div class="w-full bg-[#cce0f5] h-screen">
		<div class="px-16 py-8">
			<Breadcrumbs
				:items="[
					{ label: 'Tenant Management', icon: '🏡', route: { name: 'Home' } },
					{ label: 'House & Contracts', icon: '🏞️', route: '/components' },
					{ label: 'List', icon: '📃', route: '/components/breadcrumbs' },
				]"
			/>

			<div class="flex flex-col xl:flex-row gap-8 py-8">
				<div class="w-full flex flex-col items-start gap-2">
					<div class="p-1">
						<Button
							@click="dialogHouse = true"
							variant="subtle"
							theme="blue"
							size="md"
							label="Create House"
						/>
					</div>
					<ListView
						class="bg-[#99bfe6] hover:bg-[#80aee0] rounded-md p-4"
						:columns="[
							{ label: 'House number', key: 'name' },
							{ label: 'Status', key: 'status' },
							{ label: 'Rent amount', key: 'rent_amount' },
						]"
						:rows="groupedHouses"
						row-key="house"
					/>
				</div>

				<div class="w-full flex flex-col items-start gap-2">
					<div class="p-1">
						<Button
							@click="dialogContract = true"
							variant="subtle"
							theme="blue"
							size="md"
							label="Create Contract"
						/>
					</div>
					<ListView
						class="bg-[#80aee0] rounded-md p-4"
						:columns="[
							{ label: 'Contract Id', key: 'name' },
							{ label: 'Broker', key: 'broker' },
							{ label: 'House number', key: 'house_serial_number' },
						]"
						:rows="contracts.list.data"
						row-key="contract"
					/>
				</div>
			</div>
		</div>

		<!-- House Creation Modal -->
		<Dialog
    :options="{
    size: '3xl'
    }"
     v-model="dialogHouse">
			<template #body-title>
				<h3>Create House</h3>
			</template>
			<template #body-content>
				<div class="flex gap-8 w-full">
					<div class="flex flex-col gap-2 w-full">
						<FormControl
							v-model="houseData.serial_number"
							type="link"
							label="Serial Number"
						/>
						<FormControl
							v-model="houseData.house_type"
							type="select"
							label="House Type"
						/>
						<FormControl
							v-model="houseData.house_condition"
							type="select"
							label="House Condition"
						/>
						<FormControl
							v-model="houseData.door_number"
							type="number"
							label="Door Number"
						/>
						<FormControl
							v-model="houseData.window_type"
							type="select"
							label="Window Type"
						/>
						<FormControl
							v-model="houseData.water_service"
							type="select"
							label="Water Service"
						/>
						<FormControl
							v-model="houseData.electric_service"
							type="select"
							label="Electric Service"
						/>
						<FormControl
							v-model="houseData.telephone_service"
							type="select"
							label="Telephone Service"
						/>
						<FormControl
							v-model="houseData.number_of_floors"
							type="number"
							label="Number of Floors"
						/>
						<FormControl
							v-model="houseData.house_floor_area"
							type="number"
							label="House Floor Area"
						/>
					</div>
					<div class="flex flex-col gap-2 w-full">
						<FormControl
							v-model="houseData.roof_material"
							type="select"
							label="Roof Material"
						/>
						<FormControl
							v-model="houseData.wall_material"
							type="select"
							label="Wall Material"
						/>
						<FormControl
							v-model="houseData.floor_material"
							type="select"
							label="Floor Material"
						/>
						<FormControl v-model="houseData.address" type="link" label="Address" />
						<FormControl v-model="houseData.status" type="select" label="Status" />
						<FormControl
							v-model="houseData.rent_amount"
							type="number"
							label="Rent Amount"
						/>
						<FormControl
							v-model="houseData.organization"
							type="select"
							label="Organization"
						/>
						<FormControl
							v-model="houseData.accessibility_for_disables"
							type="checkbox"
							label="Accessibility for Disabled"
						/>
						<FormControl
							v-model="houseData.owns_boundary"
							type="checkbox"
							label="Owns Boundary"
						/>
						<FormControl
							v-model="houseData.shares_boundary"
							type="checkbox"
							label="Shares Boundary"
						/>
						<FormControl v-model="houseData.kitchen" type="checkbox" label="Kitchen" />
						<FormControl v-model="houseData.toilet" type="checkbox" label="Toilet" />
						<FormControl
							v-model="houseData.bathroom"
							type="checkbox"
							label="Bathroom"
						/>
					</div>
				</div>
			</template>
			<template #actions>
				<Button
					class="w-full bg-blue-300 text-black font-bold"
					@click="createHouse"
					variant="subtle"
					theme="blue"
					size="lg"
					label="Save"
				/>
			</template>
		</Dialog>

		<!-- Contract Creation Modal -->
		<Dialog class="w-2xl" v-model="dialogContract">
			<template #body-title>
				<h3>Create Contract</h3>
			</template>
			<template #body-content>
				<FormControl v-model="contractData.name" type="text" label="Contract ID" />
				<FormControl v-model="contractData.broker" type="text" label="Broker" />
				<FormControl
					v-model="contractData.house_serial_number"
					type="text"
					label="House Number"
				/>
			</template>
			<template #actions>
				<Button
					class="w-full bg-blue-300 text-black font-bold"
					@click="createContract"
					variant="subtle"
					theme="blue"
					size="lg"
					label="Save"
				/>
			</template>
		</Dialog>
	</div>
</template>

<script setup>
import { computed, reactive, ref } from 'vue'
import { createListResource, ListView, Breadcrumbs, Dialog, Button, FormControl } from 'frappe-ui'

const dialogHouse = ref(false)
const dialogContract = ref(false)

const contractData = ref({ name: '', broker: '', house_serial_number: '' })

const createHouse = () => {
	console.log('House Created:', houseData.value)
	dialogHouse.value = false
}

const createContract = () => {
	console.log('Contract Created:', contractData.value)
	dialogContract.value = false
}

const doctypes = createListResource({
	doctype: 'House',
	fields: ['*'],
	auto: true,
	orderBy: 'name desc',
})

const contracts = createListResource({
	doctype: 'Contract',
	fields: ['*'],
	auto: true,
	orderBy: 'name desc',
})

const newHouser = reactive({
	name: '',
	status: '',
	rent_amount: '',
})

const houseData = reactive({
	serial_number: '',
	house_type: '',
	house_condition: '',
	door_number: '',
	window_type: '',
	water_service: '',
	electric_service: '',
	telephone_service: '',
	number_of_floors: '',
	house_floor_area: '',
	roof_material: '',
	wall_material: '',
	floor_material: '',
	address: '',
	status: '',
	rent_amount: '',
	organization: '',
	accessibility_for_disables: '',
	owns_boundary: '',
	shares_boundary: '',
	kitchen: '',
	toilet: '',
	bathroom: '',
})

const groupedHouses = computed(() => {
	if (!doctypes.list.data) return []
	const rented = doctypes.list.data.filter((h) => h.status === 'Rented')
	const openForRent = doctypes.list.data.filter((h) => h.status === 'Open for rent')
	return [
		{ group: 'Rented', collapsed: false, rows: rented },
		{ group: 'Open for rent', collapsed: false, rows: openForRent },
	]
})
</script>
