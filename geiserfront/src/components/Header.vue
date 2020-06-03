<template>
    <div>
       <b-navbar type="dark" variant="dark">
           <b-navbar-brand class="text-white" href="#">Geiser</b-navbar-brand>

           <b-nav-item variant="dark" to="/inicio">Inicio</b-nav-item>
           <b-nav-item to="/status">Status</b-nav-item>
           <b-nav-item to="/origenes">Origenes</b-nav-item>
           <b-nav-item to="/servicios">Servicios</b-nav-item>

           <b-navbar-nav class="ml-auto">
               <b-nav-form @submit.prevent="login" v-if="token==null">
                   <b-form-input id="username" size="sm" class="mr-sm-2" v-model="username"
                                 placeholder="username" name="username"></b-form-input>
                   <b-form-input id="password" size="sm" class="mr-sm-2" v-model="password"
                                 type="password" placeholder="password" name="password"></b-form-input>

                   <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
               </b-nav-form>
               <b-nav-form @submit.prevent="logout" v-if="token!=null">
                   <b-button size="sm" class="my-2 my-sm-0" type="submit">Logout</b-button>
               </b-nav-form>
           </b-navbar-nav>
       </b-navbar>
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        name: "Header",
        components: {

        },
        data() {
            return {
                username : null,
                password: null,
                token: localStorage.getItem('user-token') || null
            }
        },
        methods: {
            login() {
                console.log(this.username)
                console.log(this.password)
                axios.post(this.$serverApiLogin, {
                    username: this.username,
                    password: this.password
                })
                    .then(resp => {
                        this.token = resp.data.token
                        console.log(this.token)
                        localStorage.setItem('user-token', resp.data.token)
                    })
                    .catch(err => {
                        localStorage.removeItem('user-token')
                        console.log(err)
                    })
            },
            logout() {
                this.token = null;
                localStorage.removeItem('user-token');
            }
        }
    }
</script>

<style scoped>

</style>