<template>
    <div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <b-form id="formServicio" @submit.prevent="checkFormServicios" @submit="$emit('updateServiciosList')">
                            <p>
                                <label>Nombre</label>
                                <b-form-input class="ml-2" required type="text" name="nombreServicio" id="nombreServicio" v-model="nombre"/>
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
        name: "Servicios",
        components: {
        },

        data() {
            return {
                nombre:null,
            }
        },
        methods: {
            checkFormServicios() {
                 let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.post(this.$serverApiServicios, {
                    nombre: this.nombre
                }, axiosConfig)
                    .then(res => {
                        this.$alert("El servicio se agregó correctamente");
                        console.log(res);
                    })
                    .catch( res => {
                        this.$alert("Hubo un problema al agregar un servicio, verifica que tengas acceso");
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