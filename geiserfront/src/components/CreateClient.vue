<template>
    <div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <b-form id="formClient" @submit.prevent="checkForm" @submit="$emit('updateList')">
                            <p>
                                <label>Nombre</label>
                                <b-form-input class="ml-2" required type="text" name="nombre" id="nombre" v-model="nombre"/>
                            </p>
                            <p>
                                <label>Apellido Paterno</label>
                                <b-form-input class="ml-2" required type="text" name="ap_paterno" id="ap_paterno" v-model="apellido_paterno"/>
                            </p>
                            <p>
                                <label>Apellido Materno</label>
                                <b-form-input class="ml-2" required type="text" name="ap_materno" id="ap_materno" v-model="apellido_materno"/>
                            </p>
                            <p>
                                <input class="btn-primary btn-sm" type="submit" value="Guardar"/>
                            </p>
                        </b-form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "CreateClient",
        components: {

        },
        data() {
            return {
                nombre:null,
                apellido_paterno:null,
                apellido_materno:null
            }
        },
        methods: {
            checkForm() {
                axios.post(this.$serverApiClientes, {
                    nombre: this.nombre,
                    apellido_paterno: this.apellido_paterno,
                    apellido_materno: this.apellido_materno
                })
                    .then(res => console.log(res))
                    .catch( res => console.log(res))
            }
        }
    }
</script>

<style scoped>

</style>