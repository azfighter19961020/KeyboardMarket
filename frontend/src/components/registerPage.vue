<template>
	<html lang="zh-Hant-TW">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="icon" type="image/x-con" href="@/assets/favicon.ico"> 
		<div id="app">
			<headerComponent></headerComponent>
			<div id="registerHeader" style="width:100%;height:100px;background-image: linear-gradient(to right,#C9C9C9,#F2FFFF,#00E6E6);padding-top: 40px;">
				<h3>註冊</h3>
			</div>
			<div id="registerForm" style="width:50%;height: 500px;">
				<b-form @submit="onSubmit" @reset="onReset">
					<b-form-group
					id="username_group"
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
						<div v-show="!isValid">
							{{ usernameErrMsg }}
						</div>
					</b-form-group>
					<b-form-group
					id="password_group"
					label="密碼:"
					label-for="password"
					style="margin: 10px;"
					>
						<b-form-input
						id="password"
						placeholder="請輸入密碼"
						type="password"
						v-model="password"
						required
						>
						</b-form-input>
						<div v-show="!isValid">
							{{ passwordErrMsg }}
						</div>
					</b-form-group>
					<b-form-group
					id="password1_group"
					label="請確認密碼:"
					label-for="password1"
					style="margin:10px;"
					>
						<b-form-input
						id="password1"
						placeholder="請再次輸入密碼"
						type="password"
						v-model="password1"
						required
						>
						</b-form-input>
						<div v-show="!isValid">
							{{ password1ErrMsg }}
						</div>
					</b-form-group>
					<b-form-group
					id="email_group"
					label="電話:"
					label-for="phone"
					style="margin: 10px;"
					>
						<b-form-input
						id="phone"
						placeholder="請輸入電話"
						v-model="phone"
						required
						>
						</b-form-input>
						<div v-show="!isValid">
							{{ phoneErrMsg }}
						</div>
					</b-form-group>
					<b-form-group
					id="email_group"
					label="電子郵件:"
					label-for="email"
					style="margin: 10px;"
					>
						<b-form-input
						id="email"
						placeholder="請輸入E-mail"
						type="email"
						v-model="email"
						required
						>
						</b-form-input>
						<div v-show="!isValid">
							{{ emailErrMsg }}
						</div>
					</b-form-group>
					<b-form-group
					id="address_group"
					label="地址:"
					label-for="address"
					style="margin:10px;"
					>
						<b-form-input
						id="address"
						placeholder="請輸入地址"
						v-model="address"
						required
						>
						</b-form-input>
						<div v-show="!isValid">
							{{ addressErrMsg }}
						</div>
					</b-form-group>
					<vue-recaptcha
					ref="recaptcha"
					@verify="captchaVerified"
					@expired="captchaExpired"
					sitekey="6LcMB7kcAAAAAI_6uZG77-bK-Qn_rJWx3F1u4Y2o"
					:loadRecaptchaScript="true"
					>
					</vue-recaptcha>
					<b-button type="submit" variant="info" style="width:80px;margin:10px;">註冊</b-button>
					<b-button type="reset" variant="danger" style="width:80px;margin:10px;">清空</b-button>
				</b-form>
			</div>
		</div>
	</html>
</template>


<script>
  import { CREATED } from '@/apis/constant.js'
  import { register } from '@/apis/users.js'
  import VueRecaptcha from 'vue-recaptcha'
  export default{
    name:"registerPage",
    components:{
      'headerComponent':() => import('@/components/header.vue'),
      VueRecaptcha
    },
    data(){
      return {
        isLogin:false,
        username:"",
        password:"",
        password1:"",
        email:"",
        phone:"",
        address:"",
        usernameErrMsg:"",
        passwordErrMsg:"",
        password1ErrMsg:"",
        emailErrMsg:"",
        phoneErrMsg:"",
        addressErrMsg:"",
        isValid:true,
        captchaVerify:false,
        recaptchaToken:""
      }
    },
    methods: {
      captchaExpired(){
        this.captchaVerify = false
      },
      captchaVerified(recaptchaToken){
        this.captchaVerify = true
        this.recaptchaToken = recaptchaToken
      },
      onSubmit(e){
        e.preventDefault()
        if(!this.captchaVerify){
          this.$fire({type:"error",text:"請通過recaptcha驗證"})
        }
        this.isValid = true
        this.$refs.recaptcha.reset()
        this.usernameErrMsg = this.passwordErrMsg = this.password1ErrMsg = this.emailErrMsg = this.phoneErrMsg = this.addressErrMsg = ""
        let UsernameValidation = /[!@#$%^&*()\-_+=|\\{}[]"'\/.,]/
        let emailValidation =  /^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$/
        if(UsernameValidation.test(this.username)){
          this.usernameErrMsg = "用戶名包含特殊字元"
          this.isValid = false
        }
        if(!emailValidation.test(this.email)){
          this.emailErrMsg = "電子信箱格式不正確"
          this.isValid = false
        }
        if(this.password != this.password1){
          this.passwordErrMsg = "密碼不一致"
          this.isValid = false
        }
        if(this.password.length < 6){
          this.passwordErrMsg = "密碼長度過短"
          this.isValid = false
        }
        if(this.phone.length != 10){
          this.phoneErrMsg = "電話錯誤"
          this.isValid = false
        }
        if(this.isValid){
          var data = {
            "username":this.username,
            "email":this.email,
            "password":this.password,
            "password1":this.password1,
            "phone":this.phone,
            "address":this.address,
            "recaptchaToken":this.recaptchaToken
          }
          console.log(CREATED)
          register(data).then((response) => {
            console.log(response.data.code)
            if(response.data.code == CREATED){
              window.localStorage.setItem('username',this.username)
              window.localStorage.setItem('token',response.data.data.token)
              this.$alert("註冊成功").then(() => {
                window.location.href = "/#/index"
                window.location.reload()
              })
            }else{
              this.$fire({type:'error',text:response.data.data})
            }
          })
        }
        
      },
      onReset(){
        this.username = this.password = this.password1 = this.email = this.phone = this.address = this.usernameErrMsg = this.passwordErrMsg = this.password1ErrMsg = this.emailErrMsg = this.phoneErrMsg = this.addressErrMsg = ""
        this.isValid = true
      }
    }
  }
</script>