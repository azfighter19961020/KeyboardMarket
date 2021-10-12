import axios from 'axios'
import {host,port} from '@/apis/constant.js'

export function getallproduct(){
  return axios.get(`http://${host()}:${port()}/product`)
}

export function getallcategory(){
  return axios.get(`http://${host()}:${port()}/product/category`)
}

export function getcproduct(cid){
  return axios.get(`http://${host()}:${port()}/product/${cid}`)
}

export function getDetail(pid){
  return axios.get(`http://${host()}:${port()}/product/detail/${pid}`)
}