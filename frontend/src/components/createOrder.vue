<template>
	<html lang="zh-Hant-TW">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
	<div id="app">
		<headerComponent></headerComponent>
		<div id="createHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
			<h3>結帳</h3>
		</div>
		<div id="carts" style="margin-top: 15px;">
			<b-row v-for="item in carts" :key="item.id">
				<b-col cols="2">
					<img :src="'http://localhost:8000' + item.product.img" style="width:150px;height: 150px;" alt="">
				</b-col>
				<b-col cols="3">
					<h4>{{ item.product.name }}</h4>
				</b-col>
				<b-col cols="3">
					<b-form-spinbutton id="product_id_spin" v-model="item.amount" min="1" max="100" @change="fixAmount(item.id)"></b-form-spinbutton>
				</b-col>
				<b-col cols="2">
					<h4>${{ item.product.price * item.amount }}</h4>
				</b-col>
				<b-col cols="2">
					<b-button variant="danger" @click="deleteCart(item.id)">刪除</b-button>
				</b-col>
			</b-row>
			<hr>
			<b-row>
				<b-col cols="8"></b-col>
				<b-col cols="2">
					<h5>共計 {{ itemCount }} 件</h5>
				</b-col>
				<b-col cols="2">
					<h5>總計: {{ total }}</h5>
				</b-col>
			</b-row>
			<hr>
			<b-row>
				<b-col cols="10"></b-col>
				<b-col cols="2"><b-button variant="info" @click="checkout">確認結帳</b-button></b-col>
			</b-row>
		</div>
	</div>
	</html>
</template>

<script>
  import { getCartData,fixCartData,deleteCartData } from '@/apis/cart.js'
  import { createOrderData } from '@/apis/order.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name: 'createOrderPage',
    data(){
      return {
        isLogin:false,
        carts:[]
      }
    },
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    computed: {
      total: function(){
        var sum = 0
        this.carts.forEach((item) => {
          sum += item.amount * item.product.price
        })
        return sum
      },
      itemCount: function(){
        var sum = 0
        this.carts.forEach((item) => {
          sum += item.amount
        })
        return sum
      }
    },
    methods:{
      checkout(){
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        createOrderData(username,token).then((response) => {
          if(response.data.code == STATUS_OK){
            window.localStorage.setItem('orderID',response.data.data.orderid)
            console.log(response.data.data.links.approve)
            window.location.href = response.data.data.links.approve
          }else{
            this.$fire({type:"error",text:response.data.data})
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
      deleteCart(cid){
        var token = window.localStorage.getItem('token')
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
      }
    },
    created(){
      var username = window.localStorage.getItem('username')
      var token = window.localStorage.getItem('token')
      if(username != null && token != null){
        getCartData(username,token).then((response) => {
          if(response.data.code == STATUS_OK){
            this.carts = response.data.data
          }else{
            this.$fire({type:"error",text:response.data.data})
          }
        })
      }
    }

  }
</script>