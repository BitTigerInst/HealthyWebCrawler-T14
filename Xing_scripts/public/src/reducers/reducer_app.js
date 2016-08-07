import { FETCH_APP } from '../actions/index';

export default function (state = [], action) {
  switch (action.type) {
    case FETCH_APP:
      return action.payload.data;
      //return state.concat([action.payload.data]);
  }

  return state;
}