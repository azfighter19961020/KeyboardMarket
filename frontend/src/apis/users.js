import axios from 'axios'
import {host,port} from '@/apis/constant.js'

export function login(data){
  return axios.post(`http://${host()}:${port()}/login`,data)
}

export function register(data){
  return axios.post(`http://${host()}:${port()}/user`,data)
}

export function getdata(username,token){
  return axios.get(`http://${host()}:${port()}/user/${username}`,{
    headers: {
      "AUTHORIZATION":token
    }
  })
}

export function fixdata(data,token){
  return axios.put(`http://${host()}:${port()}/user`,data,{
    headers:{
      "AUTHORIZATION":token
    }
  })
}

export function uploadImage(data,token){
  return axios.post(`http://${host()}:${port()}/user/avatar`,data,{
    headers:{
      "AUTHORIZATION":token,
      processData: false,
      contentType: false
    }
  })
}