<template>
    <div>
        <Servicios v-bind:servicio_detail="servicio_detail" v-on:updateServiciosList="updatedServicios"/>
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
                        <tr v-bind:key="servicio.id" v-for="servicio in serviciosList">
                            <td>{{servicio.id}}</td>
                            <td>{{servicio.nombre}}</td>
                            <td><button class="btn-sm btn-danger" v-on:click="borrarServicio(servicio)">Borrar</button></td>
                            <td><button class="btn-sm btn-primary" v-on:click="editarServicio(servicio)">Editar</button></td>
                        </tr>
                    </tbody>
                </table>
        </div>
        <modal name="edit-servicio" height="auto">
            <b-form id="formServicioEditar" @submit.prevent="checkFormServicio" @submit="$emit('updateServiciosList')">
                <p>
                    <label>Nombre</label>
                    <b-form-input class="ml-2" required type="text" name="nombreEditarServicio" id="nombreEditarServicio" v-model="nombre"/>
                </p>
                <p>
                    <input class="btn-primary btn-sm" type="submit" value="Guardar"/>
                </p>
            </b-form>
            <p>
                <button class="btn-sm btn-primary" v-on:click="cerrarModalServicio">Cerrar</button>
            </p>
        </modal>
    </div>
</template>

<script>
    import axios from 'axios';
    import {TokenService} from "../storage/service";
    import Servicios from "./Servicios";

    export default {
        name: "ServiciosList",
        components: {
            Servicios

        },

        data() {
            return {
                serviciosList:[],
                servicio_detail:null,
                nombre:"",
                idServicioEdit:0
            }
        },
        methods: {
            getServicios() {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.get(this.$serverApiServicios, axiosConfig)
                    .then(res => {
                        this.serviciosList = res.data;
                        console.log(this.serviciosList);
                    })
                    .catch(err => console.log(err))
            },
            updatedServicios() {
                this.timer = setTimeout(() => {
                    let axiosConfig = {
                        headers: {
                            'Authorization': 'Token ' + this.token
                        }
                    };
                    axios.get(this.$serverApiServicios, axiosConfig)
                        .then(res => this.serviciosList = res.data)
                        .catch(err => console.log(err))
                }, 600);
            },
            borrarServicio(servicioDelete) {
                this.$confirm("Estás seguro?")
                    .then(() => {
                        let axiosConfig = {
                            headers: {
                                'Authorization': 'Token ' + this.token
                            }
                        };
                        axios.delete(this.$serverApiServicios + servicioDelete.id, axiosConfig)
                            .then(res => console.log(res.data))
                            .catch(err => console.log(err));
                        this.updatedServicios();
                    });
            },
            editarServicio(servicioEditar) {
                this.nombre = servicioEditar.nombre;
                this.idServicioEdit = servicioEditar.id;
                this.$modal.show('edit-servicio');
            },
            cerrarModalServicio() {
                this.$modal.hide('edit-servicio');
            },
            checkFormServicio() {
                 let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.put(this.$serverApiServicios + this.idServicioEdit + "/", {
                    nombre: this.nombre
                }, axiosConfig)
                    .then(res => {
                        this.$alert("El servicio se editó correctamente");
                        this.cerrarModalServicio();
                        this.updatedServicios();
                        console.log(res);
                    })
                    .catch( res => {
                        this.$alert("Hubo un problema al editar el servicio, verifica que tengas acceso");
                        console.log(res);
                    })
            }
        },
        created() {
            this.token = TokenService.getToken();
            this.getServicios()

        }
    }
</script>

<style scoped>

</style>