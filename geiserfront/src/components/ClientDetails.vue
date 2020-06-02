<template>
    <div class="">
        <div class="row d-flex justify-content-center">
            <p class="mb-3">Nombre: {{client_detail.nombre}}</p>
        </div>
        <div class="row d-flex justify-content-center">
            <p>Apellido Paterno: {{client_detail.apellido_paterno}}</p>
        </div>
        <div class="row d-flex justify-content-center">
            <p>Apellido Materno: {{client_detail.apellido_materno}}</p>
        </div>
        <div class="row d-flex justify-content-center">
            <b-form id="direcciones" @submit.prevent="addDireccion" @submit="$emit('updated', client_detail)">
                <p>
                    <label>Calle</label>
                    <b-form-input id="calle" required name="calle" v-model="calle" type="text"/>
                </p>
                <p>
                    <label>Num Ext</label>
                    <b-form-input id="numExt" required name="numExt" v-model="num_ext" type="text"/>
                </p>
                <p>
                    <label>Fraccionamiento</label>
                    <b-form-input id="fraccionamiento" required name="fraccionamiento" v-model="fraccionamiento" type="text"/>
                </p>
                <input class="btn-primary btn-sm" type="submit" value="Guardar"/>
            </b-form>
        </div>
        <br/>
        <div class="row d-flex justify-content-center">
            <button class="btn-sm btn-danger" v-on:click="clientDelete(client_detail)" @click="$emit('updateDelete')">Borrar Cliente</button>
        </div>
    </div>
</template>

<script>
    import {TokenService} from "../storage/service";
    import axios from 'axios';

    export default {
        name: "ClientDetails",
        props: {
            client_detail: {}
        },
        data() {
            return {
                calle : null,
                num_ext : null,
                fraccionamiento : null
            }
        },
        methods: {
            clientDelete() {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.delete(this.$serverApiClientes + this.client_detail.id, axiosConfig)
                    .then(res => console.log(res.data))
                    .catch(err => console.log(err))
            },
            addDireccion() {
                var postData = {
                calle: this.calle,
                num_ext: this.num_ext,
                fraccionamiento: this.fraccionamiento
            }
            let axiosConfig = {
                headers: {
                    'Authorization': 'Token ' + this.token
                }
            }
            console.log(this.token)
            axios.post(this.$serverApiClientes + this.client_detail.id + '/direccion_cliente/', postData, axiosConfig)
                .then(res => console.log(res.data))
                .catch(err => console.log(err))
            }
        },
        created() {
            this.token = TokenService.getToken();
        }
    }
</script>

<style scoped>

</style>