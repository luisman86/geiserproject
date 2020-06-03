<template>
  <div class="">
      <div class="col-md-12 mb-5" v-if="createNew">
        <CreateClient v-on:updateList="updatedClients"/>
      </div>
    <div class="row d-flex justify-content-center">
        <div class="col-md-5 text-center nicefont">
            <h4>Bienvenido a Geiser</h4>
            <form @submit.prevent="createdNew()">
                <input type="submit" class="btn-sm btn-primary" id="createdNew" value="Crear nuevo cliente"/>
            </form>
            <p v-bind:key="cliente.id" v-for="cliente in clientes">
                {{cliente.nombre}}
                <br/>
                Direcciones:
                <br/>
                <span v-bind:key="direccion.id" v-for="direccion in cliente.direcciones">
                    {{direccion.calle}}
                    {{direccion.num_ext}}
                    {{direccion.fraccionamiento}}
                </span>
                <br/>
                <button class="btn-sm btn-primary mt-2 mb-3" v-on:click="clientDetail(cliente)">Details</button>
            </p>
        </div>
    </div>
      <div class="row d-flex justify-content-center">
            <ClientDetails v-bind:client_detail="client_detail" v-on:updated="updatedClients" v-on:updateDelete="updatedClients"/>
      </div>
  </div>
</template>

<script>
    import axios from 'axios';
    import ClientDetails from './ClientDetails';
    import CreateClient from './CreateClient'

    export default {
        name: 'App',
        components: {
            ClientDetails,
            CreateClient,
        },
        data() {
            return {
                clientes: [],
                client_detail: Object,
                createNew: "",
            }
        },
        methods: {
            getClientes() {
                axios.get(this.$serverApiClientes)
                    .then(res => this.clientes = res.data)
                    .catch(err => console.log(err))
            },
            clientDetail(cliente) {
                this.client_detail = cliente;
                console.log(this.client_detail)
            },
            createdNew() {
            this.createNew = !this.createNew
            },
            updatedClients() {
                this.timer = setTimeout(() => {
                    axios.get(this.$serverApiClientes)
                        .then(res => this.clientes = res.data)
                        .catch(err => console.log(err))
                }, 600);
            }
        },
        created() {
            this.getClientes();
            this.createNew = false;
        }
    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');
    .nicefont{
        font-size:26px;
        font-family: 'Alatsi', sams-serif;
    }
</style>