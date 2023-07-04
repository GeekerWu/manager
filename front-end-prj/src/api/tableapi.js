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
  gettable:'/get_table',
  search:'/search_table',
}

export function gettable () {
  return axios({
    url: api.gettable,
    method: 'get',
  })
}

export function search (parameter) {
  return axios({
    url: api.search,
    method: 'post',
    data: parameter
  })
}



