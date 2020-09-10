<template>
    <div class="registration-form" id="app">
        <v-btn v-show="!show_gun_form" class="white--text" color="#3f47d5" v-on:click="show_gun_form=true">Register New Firearm</v-btn>
        <v-dialog v-model="show_gun_form">
            <v-card style="margin-left: 0px">
                <v-col
                    md="4"
                >
                    <v-text-field
                        v-model="manufacturer"
                        :counter="40"
                        label="Manufacturer"
                        filled
                        required
                    ></v-text-field>
                </v-col>

                <v-col
                    md="4"
                >
                    <v-text-field
                        v-model="model"
                        :counter="20"
                        label="Model"
                        filled
                        required
                    ></v-text-field>
                </v-col>

                <v-col
                    md="4"
                >
                    <v-text-field
                        v-model="caliber"
                        :counter="15"
                        label="Caliber"
                        filled
                        required
                    ></v-text-field>
                </v-col>

                <v-col
                    md="4"
                >
                    <v-text-field
                        v-model="current_owner"
                        :counter="40"
                        label="First and Last Name"
                        filled
                        required
                    ></v-text-field>
                </v-col>
                <v-card-actions>
                    <v-btn v-show="show_gun_form" style="margin-bottom: 5px" @click="SubmitForm()">Submit</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    export default {
        name: "RegistrationForm",
        data() {
            return {
                show_gun_form: false,
                manufacturer: "",
                model: "",
                caliber: "",
                current_owner: "",
            }
        },
        methods: {
            async SubmitForm() {
                const newGun = {
                    manufacturer: this.manufacturer,
                    model: this.model,
                    caliber: this.caliber,
                    current_owner: this.current_owner
                }

                try {
                    let resp = await this.$axios.post('/api/guns/', newGun)
                    this.$emit('firearm-submitted')
                    let that = this
                    _.forOwn(newGun, function(value, key) {
                        that[key] = ''
                    })
                } catch {
                    console.log('post request failed')
                }
                this.show_gun_form = false
            }
        }
    }
</script>

<style>

</style>
