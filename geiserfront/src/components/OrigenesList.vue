<template>
    <div>
        <Origenes v-bind:origen_detail="origen_detail" v-on:updateOrigenesList="updatedOrigenes"/>
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
                        <tr v-bind:key="origen.id" v-for="origen in origenesList">
                            <td>{{origen.id}}</td>
                            <td>{{origen.nombre}}</td>
                            <td><button class="btn-sm btn-danger" v-on:click="borrarOrigen(origen)">Borrar</button></td>
                            <td><button class="btn-sm btn-primary" v-on:click="editarOrigen(origen)">Editar</button></td>
                        </tr>
                    </tbody>
                </table>
        </div>
        <modal name="edit-origen" height="auto">
            <b-form id="formOrigenEditar" @submit.prevent="checkFormOrigen" @submit="$emit('updateOrigenesList')">
                <p>
                    <label>Nombre</label>
                    <b-form-input class="ml-2" required type="text" name="nombreEditarOrigen" id="nombreEditarOrigen" v-model="nombre"/>
                </p>
                <p>
                    <input class="btn-primary btn-sm" type="submit" value="Guardar"/>
                </p>
            </b-form>
            <p>
                <button class="btn-sm btn-primary" v-on:click="cerrarModalOrigen">Cerrar</button>
            </p>
        </modal>
    </div>
</template>

<script>
    import axios from 'axios';
    import {TokenService} from "../storage/service";
    import Origenes from "./Origenes";

    export default {
        name: "OrigenesList",
        components: {
            Origenes

        },

        data() {
            return {
                origenesList:[],
                origen_detail:null,
                nombre:"",
                idOrigenEdit:0
            }
        },
        methods: {
            getOrigenes() {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.get(this.$serverApiOrigenes, axiosConfig)
                    .then(res => {
                        this.origenesList = res.data;
                        console.log(this.origenesList);
                    })
                    .catch(err => console.log(err))
            },
            updatedOrigenes() {
                this.timer = setTimeout(() => {
                    let axiosConfig = {
                        headers: {
                            'Authorization': 'Token ' + this.token
                        }
                    };
                    axios.get(this.$serverApiOrigenes, axiosConfig)
                        .then(res => this.origenesList = res.data)
                        .catch(err => console.log(err))
                }, 600);
            },
            borrarOrigen(origenDelete) {
                this.$confirm("Estás seguro?")
                    .then(() => {
                        let axiosConfig = {
                            headers: {
                                'Authorization': 'Token ' + this.token
                            }
                        };
                        axios.delete(this.$serverApiOrigenes + origenDelete.id, axiosConfig)
                            .then(res => console.log(res.data))
                            .catch(err => console.log(err));
                        this.updatedOrigenes();
                    });
            },
            editarOrigen(origenEditar) {
                this.nombre = origenEditar.nombre;
                this.idOrigenEdit = origenEditar.id;
                this.$modal.show('edit-origen');
            },
            cerrarModalOrigen() {
                this.$modal.hide('edit-origen');
            },
            checkFormOrigen() {
                 let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.put(this.$serverApiOrigenes + this.idOrigenEdit + "/", {
                    nombre: this.nombre
                }, axiosConfig)
                    .then(res => {
                        this.$alert("El origen se editó correctamente");
                        this.cerrarModalOrigen();
                        this.updatedOrigenes();
                        console.log(res);
                    })
                    .catch( res => {
                        this.$alert("Hubo un problema al editar el origen, verifica que tengas acceso");
                        console.log(res);
                    })
            }
        },
        created() {
            this.token = TokenService.getToken();
            this.getOrigenes()

        }
    }
</script>

<style scoped>

</style>