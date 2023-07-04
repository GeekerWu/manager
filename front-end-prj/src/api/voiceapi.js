import { axios } from '@/utils/request'

/**
 * login func
 * parameter: {
 *     username: '',
 *     password: '',
 *     remember_me: true,
 *     captcha: '12345'
 * }
 * @param parameter
 * @returns {*}
 */

const api = {
  loadinit:'/load_init',
  searchvoice:'/search_voice',
  getvoice:'/get_voice',
  playvoice:'/play_voice',
  savevoice:'/save_voice'
}
export function loadinit () {
  return axios({
    url: api.loadinit,
    method: 'get',
  })
}
export function savevoice (parameter) {
  return axios({
    url: api.savevoice,
    method: 'post',
    data: parameter
  })
}
export function searchvoice (parameter) {
  return axios({
    url: api.searchvoice,
    method: 'post',
    data: parameter
  })
}
export function getvoice (parameter) {
  return axios({
    url: api.getvoice,
    method: 'post',
    data: parameter
  })
}
export function playvoice (parameter) {
  return axios({
    url: api.playvoice,
    method: 'post',
    data: parameter
  })
}



