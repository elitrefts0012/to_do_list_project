<template>
    <v-card>
        <v-card-title>
            Registered Firearms
            <v-spacer></v-spacer>
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
            />
        </v-card-title>
        <v-data-table
            :headers="columns"
            :items="guns"
            :search="search"
        >
            <template v-slot:item.actions="{item}">
                <v-icon @click="deleteGun(item)">
                    mdi-delete
                </v-icon>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
export default {
    name: "Guns",
    props: ["guns"],
    data () {
        return {
            search: '',
            columns: [
                {
                    text: 'Manufacturer',
                    value: 'manufacturer'
                },
                {
                    text: 'Model',
                    value: 'model'
                },
                {
                    text: 'Caliber',
                    value: 'caliber'
                },
                {
                    text: 'Current Owner',
                    value: 'current_owner'
                },
                {
                    text: 'Actions',
                    value: 'actions',
                    sortable: false
                },
            ],
        }
    },
    methods: {
        async deleteGun(item) {
            try {
                if (confirm(`Confirm: Delete ${item.manufacturer} ${item.model} Owned By ${item.current_owner}`)) {
                    await this.$axios.delete(`/api/guns/${item.id}`)
                    this.$emit('gun-deleted')
                }
            } catch {
                console.log('delete request failed')
            }
        }
    }
}
</script>
