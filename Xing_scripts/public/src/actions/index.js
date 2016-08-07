import axios from 'axios';

const ROOT_URL = '/search';

export const FETCH_APP = 'FETCH_APP';

export function fetchApp(data) {  
  const url = `${ROOT_URL}?${data}`; 
  const request = axios.get(url);

  return {
    type: FETCH_APP,
    payload: request
  };
}