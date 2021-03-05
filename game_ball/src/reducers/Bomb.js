const initalState = {
  bombs: []
}

const EQUATIONS = [
  {a: 0, b:0, c:0, x: 100, y: 0, oscillation: 40},
  {a: 0, b:0, c:0, x: 100, y: 600, oscillation: -40},
  {a: 0, b:0, c:0, x: 300, y: 0, oscillation: 40},
  {a: 0, b:0, c:0, x: 300, y: 600, oscillation: -40},
  {a: 0, b:0, c:0, x: 450, y: 0, oscillation: 40},
  {a: 0, b:0, c:0, x: 450, y: 600, oscillation: -40},
  {a: 1.2, b:-60, c:0, x: 0, oscillation: 40},
  {a: 1.2, b:-60, c:0, x: 600, oscillation: -40},
  {a: -2, b:1000, c:0, x: 0, oscillation: 40},
  {a: -2, b:1000, c:0, x: 600, oscillation: -40},
  {a: 0, b:100, c:0, x: 0, y: 100, oscillation: 40},
  {a: 0, b:100, c:0, x: 600, y: 100, oscillation: -40},
  {a: 0, b:400, c:0, x: 0, y: 400, oscillation: 40},
  {a: 0, b:400, c:0, x: 600, y: 400, oscillation: -40},
  {a: 0.00625, b:-3.75, c:612.5, x: 0, oscillation: 40},
  {a: 0.00625, b:-3.75, c:612.5, x: 600, oscillation: -40},
  {a: -0.00375, b:2.25, c:112.5, x: 0, oscillation: 40},
  {a: -0.00375, b:2.25, c:112.5, x: 600, oscillation: -40},
]

export default (state = initalState, {type} = {}) => {
  switch (type) {
    case 'GENERATE':
      const typeBomb = Math.round(Math.random()*10)%3
      const {x, y, a, b, c, oscillation} = EQUATIONS[Math.round(Math.random()*100)%18]

      return {...state, bombs: [...state.bombs, {x, y, a, b, c, typeBomb, oscillation}]}
    case 'RUNNING':
      const bombs = state.bombs.map((bomb) => {
        return ganeratePos(bomb)
      })
      return {...state, bombs}
    default:
      return state
  }
}

const ganeratePos = ({x, y, a, b, c, typeBomb, oscillation}) => {
  if (a+b+c === 0)
    return {x, y: y + oscillation, a, b, c, typeBomb, oscillation}
  if (a+c ===0)
    return {x: x + oscillation, y, a, b, c, typeBomb, oscillation}
  if (c === 0)
    return {x: x + oscillation, y: a*(x+oscillation) + b, a, b, c, typeBomb, oscillation}
  return {x: x + oscillation, y: a*(x+oscillation)**2 + b*(x+oscillation) + c, a, b, c, typeBomb, oscillation}
}
