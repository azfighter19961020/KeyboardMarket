<template>
	<html lang="zh-Hant-TW">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
	<div id="app">
		<headerComponent></headerComponent>
		<div id="carousel" style="width: 70%;height: 480px;margin:0 auto;">
			<b-carousel
			v-model="slide"
			:interval="4000"
			controls
			indicators
			background="#ababab"
			img-width="728"
			img-height="480"
			style="text-shadow: 1px 1px 2px #333;"
			@sliding-start="onSlideStart"
			@sliding-end="onSlideEnd">
				<b-carousel-slide img-src="https://github.com/charlie11438/market_django/blob/main/market/frontend/static/image/Car1.png?raw=true" style="width:100%;height:480px;">
					<h1>夏季IPAD特賣</h1>
				</b-carousel-slide>
				<b-carousel-slide img-src="https://github.com/charlie11438/market_django/blob/main/market/frontend/static/image/Car2.png?raw=true" style="width:100%;height:480px;">
					<h1>鍵盤特賣中</h1>
				</b-carousel-slide>
				<b-carousel-slide img-src="https://github.com/charlie11438/market_django/blob/main/market/frontend/static/image/Car3.png?raw=true" style="width:100%;height:480px;">
					<h1>藍芽耳機特賣中</h1>
				</b-carousel-slide>
			</b-carousel>
		</div>
		<b-container id="products" fluid="lg" class="container-fluid">
			<b-row>
				<b-col v-for="product in products" :key="product.id">
					<a :href="'/#/productDetail/' + product.id"><img :src="'http://localhost:8000' + product.img" alt="" style="width:200px;height: 200px;"></a>
					<h4 class="productTitle">{{ product.name }}</h4>
					<h5 class="productPrice">$ {{product.price}}</h5>
					<div>
						<b-button variant="info" @click="addCart(product.id)">
							加入購物車
						</b-button>
					</div>
				</b-col>
			</b-row>
		</b-container>
	</div>


    </html>
</template>

<script>
  import { getallproduct } from '@/apis/product.js'
  import { STATUS_OK } from '@/apis/constant.js'
  import { addCartData } from '@/apis/cart.js'
  export default{
    name:"indexPage",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        slide:0,
        sliding:null,
        isLogin: false,
        products:[]
      }
    },
    created(){
      getallproduct().then((response) => {
        if(response.data.code == STATUS_OK){
          this.products = response.data.data
        }else{
          this.$fire({type:'error',text:response.data.data})
        }
      })
    },
    methods:{
      addCart(product_id){
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        if(username != null && token != null){
          var data = {
            "pid":product_id,
            "amount":1,
            "username":username
          }
          addCartData(data,token).then((response) => {
            if(response.data.code == STATUS_OK){
              console.log(response.data)
              this.$fire({type:"success",text:"加入購物車成功!"})
            }else{
              this.$fire({type:"error",text:response.data.data})
            }
          })
        }else{
          this.$fire({type:"error",text:"請登入!"}).then(() => {
            window.location.href = "/#/login"
            window.location.reload()
          })
        }
      },
      onSlideStart(){
        this.sliding = true
      },
      onSlideEnd(){
        this.sliding = false
      }
    }
  }
</script>