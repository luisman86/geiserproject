<template>
    <div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <b-form id="formStatus" @submit.prevent="checkFormStatus" @submit="$emit('updateStatusList')">
                            <p>
                                <label>Nombre</label>
                                <b-form-input class="ml-2" required type="text" name="nombre" id="nombre" v-model="nombre"/>
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
    import {TokenService} from "../storage/service";

    export default {
        name: "Status",
        components: {
        },

        data() {
            return {
                nombre:null,
            }
        },
        methods: {
            checkFormStatus() {
                 let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.post(this.$serverApiStatus, {
                    nombre: this.nombre
                }, axiosConfig)
                    .then(res => {
                        this.$alert("El status se agregó correctamente");
                        console.log(res);
                    })
                    .catch( res => {
                        this.$alert("Hubo un problema al agregar un status, verifica que tengas acceso");
                        console.log(res);
                    })
            },
        },
        created() {
            this.token = TokenService.getToken();

        }
    }
</script>

<style scoped>

</style>