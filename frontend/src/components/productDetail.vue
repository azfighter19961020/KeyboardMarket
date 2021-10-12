<template>
	<html lang="zh-Hant-TW">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<b-container>
				<b-row align-h="center">
					<b-col cols="5">
						<img :src="'http://localhost:8000' + item.img" alt="" style="width: 200px;height: 200px;">
					</b-col>
					<b-col cols="5">
						<b-row>
							<h2>{{ item.name }}</h2>
						</b-row>
						<br>
						<b-row>
							<b-col cols="3">
                    <ShareNetwork
                    network="facebook"
                    :url="'http://127.0.0.1:8080/#/productDetail/' + item.id"
                    :quote="'我在鍵盤貿易發現了好棒的' + item.name + '!快來鍵盤貿易發現更多商品!'"
                    :hashtags="'keyboardmarket,鍵盤貿易,' + item.name"
                    >
                      <img src="@/assets/facebookShare.png" style="width:60px;height: 35px;" alt="">
                    </ShareNetwork>
               </b-col>
               <b-col cols="3">
                    <ShareNetwork
                    network="Line"
                    :url="'http://127.0.0.1:8080/#/productDetail/' + item.id"
                    :title="item.name + '鍵盤貿易'"
                    :description="'我在鍵盤貿易發現了好棒的' + item.name + '!快來鍵盤貿易發現更多商品!'"
                    >
                      <img src="@/assets/lineShare.png" alt="" style="width: 60px;height: 35px;">
                    </ShareNetwork>
               </b-col>
						</b-row>
						<br>
						<b-row>
							<h3>${{ item.price }}</h3>
						</b-row>
						<br>
						<b-row>
							<b-col cols="5">
								<b-form-spinbutton v-model="amount" min="1" :max="item.stored_amount"></b-form-spinbutton>
							</b-col>
							<b-col cols="3">
								<span style="color:red;">剩餘數量: {{ item.stored_amount }}</span>
							</b-col>
						</b-row>
						<br>
						<b-row>
							<b-col cols="3">
								<b-button variant="info" @click="addCart">加入購物車</b-button>
							</b-col>
              <b-col cols="3">
                <b-button variant="info" @click="addToFavorite">
                  {{ favoriteText }}
                </b-button>
              </b-col>
						</b-row>
					</b-col>
				</b-row>
				<br>
				<br>
				<br>
        <hr>
				<b-row v-html="item.info" align-h="center">
				</b-row>


			</b-container>
		</div>
	</html>
</template>

<script>
  import { getDetail } from '@/apis/product.js'
  import { getProductFavorite,addFavorite } from '@/apis/favorite.js'
  import { STATUS_OK } from '@/apis/constant.js'
  import { addCartData } from '@/apis/cart.js'
  export default{
    name:"productDetail",
    components: {
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        isLogin:false,
        amount: 1,
        item: {},
        favoriteText:""
      }
    },
    methods:{
      addToFavorite(){
        var pid = this.$route.params.pid
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        if(username == null || token == null){
          this.$fire({type:"error",text:"請登入!"}).then(() => {
            location.href = "/#/login"
          })
        }else{
          addFavorite(pid,token,username).then((response) => {
            if(response.data.code == STATUS_OK){
              this.favoriteText = response.data.data.status == 0 ? "按讚" : "已按讚"
            }
          })
        }
      },
      addCart(){
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        if(username != null && token != null){
          var data = {
            "pid":this.item.id,
            "amount":this.amount,
            "username":username
          }
          addCartData(data,token).then((response) => {
            if(response.data.code == STATUS_OK){
              this.$fire({type:"success","text":"加入購物車成功!"})
            }else{
              this.$fire({type:"error","text":response.data.data})
            }
          })
        }else{
          this.$fire({type:"error",text:"請登入!"}).then(() => {
            window.location.href = "/#/login"
            window.location.reload()
          })
        }
      }
    },
    created(){
      var pid = this.$route.params.pid
      getDetail(pid).then((response) => {
        if(response.data.code == STATUS_OK){
          this.item = response.data.data
          var token = window.localStorage.getItem("token")
          var username = window.localStorage.getItem("username")
          if(token == null || username == null){
            this.favoriteText = "登入以按讚"
          }else{
            getProductFavorite(pid,token,username).then((response) => {
              if(response.data.code == STATUS_OK){
                var status = response.data.data.status
                this.favoriteText = status == 0 ? "按讚" : "已按讚" 
              }
            })
          }

        }
        else{
          this.$fire({type:'error',text:response.data.data}).then(() => {
            window.location.href = "/#/index"
            window.location.reload
          })
        }
      })
    }
  }
</script>