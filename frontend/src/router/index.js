import Vue from 'vue'
import Router from 'vue-router'
import helloPage from '@/components/HelloWorld.vue'
import indexPage from '@/components/indexPage.vue'
import loginPage from '@/components/loginPage.vue'
import registerPage from '@/components/registerPage.vue'
import orderPage from '@/components/orderPage.vue'
import productDetail from '@/components/productDetail.vue'
import orderDetail from '@/components/orderDetail.vue'
import selfPage from '@/components/self.vue'
import productsPage from '@/components/productsPage.vue'
import createOrderPage from '@/components/createOrder.vue'
import orderCreated from '@/components/orderCreated.vue'
import orderCanceled from '@/components/orderCanceled.vue'
import createReset from '@/components/createResetPage.vue'
import resetPage from '@/components/resetPage.vue'
import favoritePage from '@/components/favoritePage.vue'


// 讓vue可以正常使用Router套件
Vue.use(Router)

/*
新增routes常數列表，包含多個Map
每個Map包含不同的path
格式為：
{
  path:'URL路徑，例如index為/index',
  name:'Path名稱',
  component: 組件名稱，例如index的組件為indexPage.vue，就是引入並且填indexPage
}
*/
const routes = [
  {
    path: "/hello",
    name: "helloPage",
    component: helloPage
  },
  {
    path: "/index",
    name: "indexPage",
    component: indexPage,
    meta: {
      title: '首頁'
    },
  },
  {
    path: "/login",
    name: "loginPage",
    component: loginPage,
    meta: {
      title: '登入'
    },
  },
  {
    path: "/register",
    name: "registerPage",
    component: registerPage,
    meta: {
      title: '註冊'
    }
  },
  {
    path: "/order",
    name: "orderPage",
    component: orderPage,
    meta: {
      title: '訂單'
    },
  },
  {
    path: "/productDetail/:pid",
    name: "productDetailPage",
    component: productDetail,
    meta:{
      title: '商品詳情'
    }
  },
  {
    path: "/orderDetail/:oid",
    name: "orderDetailPage",
    component: orderDetail,
    meta: {
      title: "訂單詳情"
    }
  },
  {
    path: "/self",
    name: "selfPage",
    component:selfPage,
    meta: {
      title: "個人頁面"
    }
  },
  {
    path: "/products/:cid",
    name: "productsPage",
    component: productsPage,
    meta: {
      title: "分類商品"
    }
  },
  {
    path: "/createorder",
    name: "createOrderPage",
    component: createOrderPage,
    meta: {
      title: "創建訂單"
    }
  },
  {
    path: "/orderCreated",
    name:"createPaypalPage",
    component: orderCreated,
    meta: {
      title: "付款建立"
    }
  },
  {
    path: "/orderCanceled",
    name: "cancalOrderPage",
    component: orderCanceled,
    meta: {
      title: "付款取消"
    }
  },
  {
    path: "/createreset",
    name: "createResetPage",
    component: createReset,
    meta: {
      title: "重置密碼"
    }
  },
  {
    path: "/reset",
    name: "resetPage",
    component: resetPage,
    meta: {
      title: "重置"
    }
  },
  {
    path: "/favorite",
    name: "favoritePage",
    component: favoritePage,
    meta: {
      title: "按讚好物"
    }
  }
]

/*
新增Router物件，
base為基本路徑，
routes則為上面新增的常數路徑列表
*/
var router = new Router({
  routes
})

router.beforeEach((to,from,next) => {
  if(to.meta.title){
    document.title = to.meta.title
  }
  next()
})

/*
預設index.js引入會返回router物件
*/
export default router
