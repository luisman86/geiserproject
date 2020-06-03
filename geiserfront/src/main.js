import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import VueSimpleAlert from 'vue-simple-alert'
import VModal from 'vue-js-modal'

Vue.config.productionTip = false
Vue.prototype.$serverApiClientes = 'http://3.101.43.5:8000/api/clientes/'
Vue.prototype.$serverApiLogin = 'http://3.101.43.5:8000/auth/'
Vue.prototype.$serverApiStatus = 'http://3.101.43.5:8000/api/status/'
Vue.prototype.$serverApiOrigenes = 'http://3.101.43.5:8000/api/origenes/'
Vue.prototype.$serverApiServicios = 'http://3.101.43.5:8000/api/servicios/'
// Vue.prototype.$serverApiClientes = 'http://localhost:8000/api/clientes/'
// Vue.prototype.$serverApiLogin = 'http://localhost:8000/auth/'
// Vue.prototype.$serverApiStatus = 'http://localhost:8000/api/status/'
// Vue.prototype.$serverApiOrigenes = 'http://localhost:8000/api/origenes/'
// Vue.prototype.$serverApiServicios = 'http://localhost:8000/api/servicios/'
Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.use(VueSimpleAlert)
Vue.use(VModal)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



const routes = [
    {
        path: '/inicio',
        name: 'Inicio',
        component: () => import('./components/ListClientes.vue')
    },
    {
        path: '/status',
        name: 'Status',
        component: () => import('./components/StatusList.vue')
    },
    {
        path: '/origenes',
        name: 'Origenes',
        component: () => import('./components/OrigenesList.vue')
    },
    {
        path: '/servicios',
        name: 'Servicios',
        component: () => import('./components/ServiciosList.vue')
    }

]

const router = new VueRouter({
    mode: 'history',
    routes
})

new Vue({
     router,
  render: h => h(App)
}).$mount('#app')
