<template>
		<div style="height: 150px;">
			<div id="header" style="height: 100px;">
				<b-navbar toggleable="lg" tyle="dark" variant="info" style="height: 100%">
					<b-navbar-brand href="/#/index">
						<img src="@/assets/logo_transparent.png" alt="鍵盤貿易logo">
					</b-navbar-brand>
					<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
					<b-collapse id="nav-collapse" is-nav>
						<b-navbar-nav>
							<b-nav-item href="/#/index">首頁</b-nav-item>
						</b-navbar-nav>
						<b-navbar-nav class="ml-auto">
							<b-nav-dropdown v-show="isLogin" right @show="loadCart">
								<template slot="button-content">
									<img src="@/assets/cart.svg" alt="購物車">
								</template>
								<b-dropdown-item style="width: 600px;" v-for="item in carts" :key="item.id">
									<b-row>
										<b-col cols="2">
											<img :src="'http://localhost:8000' + item.product.img" alt="" style="width: 100%;height: 100%">
										</b-col>
										<b-col cols="3">
											<div style="white-space:normal;word-wrap:break-word; word-break: break-all;width: 100%;height: 100%;">
												{{ item.product.name }}
											</div>
										</b-col>
										<b-col cols="3">
											<b-form-spinbutton id="product_id_spin" v-model="item.amount" min="1" max="100" @change="fixAmount(item.id)"></b-form-spinbutton>
										</b-col>
										<b-col cols="2">
											<h4>{{ item.product.price * item.amount }}</h4>
										</b-col>
										<b-col cols="2">
											<b-button variant="danger" @click="deleteCart(item.id)">
												刪除
											</b-button>
										</b-col>												
									</b-row>
								</b-dropdown-item>
								<hr>
								<b-dropdown-item style="padding-left: calc(100% - 100px)">
									<b-button variant="info" @click="createOrder">結帳</b-button>
								</b-dropdown-item>
								<hr>
							</b-nav-dropdown>
							<b-nav-item-dropdown text="會員" right>
								<b-dropdown-item href="/#/login" v-show="!isLogin">登入</b-dropdown-item>
								<b-dropdown-item href="/#/register" v-show="!isLogin">註冊</b-dropdown-item>
								<b-dropdown-item href="/#/self" v-show="isLogin">個人資料</b-dropdown-item>
                <b-dropdown-item href="/#/favorite" v-show="isLogin">按讚好物</b-dropdown-item>
								<b-dropdown-item href="/#/order" v-show="isLogin">訂單</b-dropdown-item>
								<b-dropdown-item v-show="isLogin" @click="logout">登出</b-dropdown-item>
							</b-nav-item-dropdown>
						</b-navbar-nav>
					</b-collapse>
				</b-navbar>				
			</div>
			<div id="catgoryNavigator" style="width: 100%;height: 100px;">
				<b-nav tabs fill>
					<b-nav-item v-for="item in categories" :key="item.value" @click="refresh(item.value)">
						{{ item.category }}
					</b-nav-item>
				</b-nav>
			</div>			
		</div>
</template>

<script>
  import { getallcategory } from '@/apis/product.js'
  import { getCartData,fixCartData,deleteCartData } from '@/apis/cart.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name:'kheader',
    data(){
      return {
        isLogin:false,
        username:"",
        categories:[],
        carts:[]
      }
    },
    mounted(){
      var username = window.localStorage.getItem('username')
      var token = window.localStorage.getItem('token')
      if(username != null && token != null){
        this.username = username
        this.isLogin = true
      }
      getallcategory().then((response) => {
        if(response.data.code == STATUS_OK){
          this.categories = response.data.data
        }else{
          this.$fire({type:'error',text:response.data.data})
        }
      })
    },
    methods: {
      createOrder(){
        window.location.href = "/#/createorder"
        window.location.reload()
      },
      deleteCart(cid){
        var token = window.localStorage.getItem("token")
        deleteCartData(cid,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.carts.forEach((item,index) => {
              if(item.id == cid){
                this.carts.splice(index,1)
              }
            })
            this.$bvToast.toast("刪除成功",{
              title:"購物車訊息",
              autoHideDelay:5000,
              appendToast:true
            })
          }else{
            this.$bvToast.toast(response.data.data,{
              title:"購物車訊息",
              autoHideDelay:5000,
              appendToast:true
            })
          }
        })
      },
      fixAmount(cid){
        var username = window.localStorage.getItem('username')
        var token = window.localStorage.getItem('token')
        var record = {}
        this.carts.forEach((item) => {
          if(item.id == cid){
            record = item
          }
        })
        var data = {
          "username":username,
          "pid":record.product.id,
          "amount":record.amount
        }
        fixCartData(data,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.$bvToast.toast("修改數量成功",{
              title: '購物車訊息',
              autoHideDelay: 5000,
              appendToast: true
            })
          }else{
            this.$bvToast.toast(response.data.data,{
              title:"購物車訊息",
              autoHideDelay:5000,
              appendToast: true
            })
          }
        })
      },
      refresh(value){
        window.location.href = "/#/products/" + value
        window.location.reload()
      },
      loadCart(){
        var username = window.localStorage.getItem('username')
        var token = window.localStorage.getItem('token')
        if(username != null && token != null){
          getCartData(username,token).then((response) => {
            if(response.data.code == STATUS_OK){
              this.carts = response.data.data
            }else{
              this.$fire({type:'error',text:response.data.data})
            }
          })
        }else{
          this.$fire({type:'error',text:"請登入！"}).then(() => {
            window.location.href = "/#/login"
            window.location.reload()
          })
        }
      },
      logout(){
        window.localStorage.removeItem('username')
        window.localStorage.removeItem('token')
        window.location.reload()
      }
    }
  }
</script>