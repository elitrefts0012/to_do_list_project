<template>
    <div>
        <div>
            <RegistrationForm @firearm-submitted="getGuns"/>
        </div>
        <div>
            <Guns v-bind:guns="guns" @gun-deleted="getGuns"/>
        </div>
    </div>
</template>

<script>
import RegistrationForm from '../components/gun_table/registration_form.vue'
import Guns from '../components/gun_table/guns.vue'

export default {
    name: 'app',
    components: {Guns, RegistrationForm},
    data () {
        return {
            guns: [],
        }
    },
    methods: {
        async getGuns() {
            try {
                let resp = await this.$axios.get('/api/guns/')
                console.log(resp.data)
                this.guns = resp.data
            } catch {
                console.log("get request failed")
            }
        },
    },
    async mounted() {
        await this.getGuns()
    }
}
</script>
