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
  searchevent:'/search_event',
  update_event:'/update_event',
  play_event:'/play_event',
}

export function play_event (parameter) {
  return axios({
    url: api.play_event,
    method: 'post',
    data: parameter
  })
}
export function searchevent (parameter) {
  return axios({
    url: api.searchevent,
    method: 'post',
    data: parameter
  })
}
export function update_event (parameter) {
  return axios({
    url: api.update_event,
    method: 'post',
    data: parameter
  })
}



