<template>
    <div>
        <Status v-bind:status_detail="status_detail" v-on:updateStatusList="updatedStatus"/>
        <br/>
        <br/>
        <div class="row d-flex justify-content-center">
            <table class="table">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-bind:key="status.id" v-for="status in statusList">
                            <td>{{status.id}}</td>
                            <td>{{status.nombre}}</td>
                            <td><button class="btn-sm btn-danger" v-on:click="borrarStatus(status)">Borrar</button></td>
                            <td><button class="btn-sm btn-primary" v-on:click="editarStatus(status)">Editar</button></td>
                        </tr>
                    </tbody>
                </table>
        </div>
        <modal name="edit-status" height="auto">
            <b-form id="formStatusEditar" @submit.prevent="checkFormStatus" @submit="$emit('updateStatusList')">
                <p>
                    <label>Nombre</label>
                    <b-form-input class="ml-2" required type="text" name="nombreEditar" id="nombreEditar" v-model="nombre"/>
                </p>
                <p>
                    <input class="btn-primary btn-sm" type="submit" value="Guardar"/>
                </p>
            </b-form>
            <p>
                <button class="btn-sm btn-primary" v-on:click="cerrarModal">Cerrar</button>
            </p>
        </modal>
    </div>
</template>

<script>
    import axios from 'axios';
    import {TokenService} from "../storage/service";
    import Status from "./Status";

    export default {
        name: "StatusList",
        components: {
            Status
        },

        data() {
            return {
                statusList:[],
                status_detail:null,
                nombre:"",
                idStatusEdit:0
            }
        },
        methods: {
            getStatus() {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.get(this.$serverApiStatus, axiosConfig)
                    .then(res => {
                        this.statusList = res.data;
                        console.log(this.statusList);
                    })
                    .catch(err => console.log(err))
            },
            updatedStatus() {
                this.timer = setTimeout(() => {
                    let axiosConfig = {
                        headers: {
                            'Authorization': 'Token ' + this.token
                        }
                    };
                    axios.get(this.$serverApiStatus, axiosConfig)
                        .then(res => this.statusList = res.data)
                        .catch(err => console.log(err))
                }, 600);
            },
            borrarStatus(statusDelete) {
                this.$confirm("Estás seguro?")
                    .then(() => {
                        let axiosConfig = {
                            headers: {
                                'Authorization': 'Token ' + this.token
                            }
                        };
                        axios.delete(this.$serverApiStatus + statusDelete.id, axiosConfig)
                            .then(res => console.log(res.data))
                            .catch(err => console.log(err));
                        this.updatedStatus();
                    });
            },
            editarStatus(statusEditar) {
                this.nombre = statusEditar.nombre;
                this.idStatusEdit = statusEditar.id;
                this.$modal.show('edit-status');
            },
            cerrarModal() {
                this.$modal.hide('edit-status');
            },
            checkFormStatus() {
                 let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.put(this.$serverApiStatus + this.idStatusEdit + "/", {
                    nombre: this.nombre
                }, axiosConfig)
                    .then(res => {
                        this.$alert("El status se editó correctamente");
                        this.cerrarModal();
                        this.updatedStatus();
                        console.log(res);
                    })
                    .catch( res => {
                        this.$alert("Hubo un problema al editar el status, verifica que tengas acceso");
                        console.log(res);
                    })
            }
        },
        created() {
            this.token = TokenService.getToken();
            this.getStatus()

        }
    }
</script>

<style scoped>

</style>