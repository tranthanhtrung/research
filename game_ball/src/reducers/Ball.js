const initalState = {
  x: 275,
  y: 275
}
const RANGE = 20

export default (state = initalState, {type} = {}) => {
  switch (type) {
    case 'MOVE_LEFT':
      return {...state, x: observeBoundaries(state.x, state.x - RANGE)}
    case 'MOVE_RIGHT':
      return {...state, x: observeBoundaries(state.x, state.x + RANGE)}
    case 'MOVE_TOP':
      return {...state, y: observeBoundaries(state.y, state.y - RANGE)}
    case 'MOVE_BOTTOM':
      return {...state, y: observeBoundaries(state.y, state.y + RANGE)}
    default:
      return state
  }
}

const observeBoundaries = (oldPos, newPos) => {
  if (newPos < 0 || newPos + 50 > 600 )
    return oldPos
  return newPos
}
