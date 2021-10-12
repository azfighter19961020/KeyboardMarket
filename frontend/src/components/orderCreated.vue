<template>
	<html lang="zh-Hant-TW">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div class="info" style="margin:0 auto;width: 50%;height: 50%;text-align: center;">
				<img :src="successImage" alt="" style="width:300px;height: 300px;">
				<h4>{{ successText }}</h4>
			</div>
		</div>
	</html>
</template>

<script>
  import { captureOrder } from '@/apis/order.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name: "orderCreated",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        successImage:"",
        successText: ""
      }
    },
    created(){
      var orderid = window.localStorage.getItem("orderID")
      console.log(orderid)
      var token = window.localStorage.getItem("token")
      captureOrder(orderid,token).then((response) => {
        console.log(response)
        if(response.status == STATUS_OK){
          this.successImage = "https://i.imgur.com/mBolVrx.jpg"
          this.successText = "付款成功"
        }else{
          this.successImage = "https://i.imgur.com/EJjpUGf.png"
          this.successText = "付款失敗"
        }
      })
    }
  }
</script>