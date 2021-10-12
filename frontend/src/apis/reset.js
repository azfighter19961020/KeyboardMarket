import { host,port } from '@/apis/constant.js'
import axios from 'axios'

export function createReset(username){
  return axios.post(`http://${host()}:${port()}/reset`,{
    "username":username
  })
}

export function resetValidate(token){
  return axios.get(`http://${host()}:${port()}/reset`,{
    params:{
      "token":token
    }
  })
}

export function resetPassword(password,token){
  return axios.put(`http://${host()}:${port()}/reset`,{
    "password":password,
    "token":token
  })
}