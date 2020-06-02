import Vue from 'vue'
import VueRouter from 'vue-router'
import Status from '../components/Status.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/status',
        name: 'Status',
        component: Status
    }

]

const router = new VueRouter({
    routes
})

export default router