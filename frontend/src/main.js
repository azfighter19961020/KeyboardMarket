import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSimpleAlert from "vue-simple-alert"
import VueSocialSharing from 'vue-social-sharing'

Vue.use(VueSocialSharing)
Vue.use(VueSimpleAlert)
Vue.config.productionTip = false
Vue.use(BootstrapVue)

new Vue({
  render: h => h(App),
  router // 新增router到這邊
}).$mount('#app')
