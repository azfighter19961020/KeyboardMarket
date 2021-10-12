<template>
	<html lang="zh-Hant-TW">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="icon" type="image/x-con" href="@/assets/favicon.ico">
		<div id="app">
			<headerComponent></headerComponent>
			<div id="resetHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
				<h3>重置密碼</h3>
			</div>
			<div id="resetForm">
				<b-form @submit="onSubmit" style="width: 100%;">
					<b-form-group
					id="username+group"
					label="用戶名:"
					label-for="username"
					style="margin:10px;"
					>
						<b-form-input
						id="username"
						placeholder="請輸入用戶名"
						v-model="username"
						required
						>
						</b-form-input>
					</b-form-group>
					<b-button type="submit" variant="info" style="width: 80px;margin: 10px;">發送重置連結</b-button>
					<div id="result">
						<p>{{ resetText }}</p>
					</div>
				</b-form>
			</div>
		</div>
	</html>
</template>

<script>
  import { createReset } from '@/apis/reset.js'
  import { STATUS_OK } from '@/apis/constant.js'
  export default{
    name:"createResetPage",
    components:{
      'headerComponent':() => import('@/components/header.vue')
    },
    data(){
      return {
        username:"",
        resetText:""
      }
    },
    methods:{
      onSubmit(e){
        e.preventDefault()
        createReset(this.username).then((response) => {
          if(response.data.code == STATUS_OK){
            this.resetText = "重置信發送成功，請至當初登記信箱查收"
          }else{
            this.resetText = response.data.data
          }
        })
      }
    }
  }
</script>