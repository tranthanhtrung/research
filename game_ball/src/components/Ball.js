import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'

import './../assets/css/index.css'
import imgBall from './../assets/images/ball.png'

const Ball = (props) => {
  const {x,y} = useSelector(state => state.ball)
  const dispatch = useDispatch()

  useEffect(() => {
    window.addEventListener('keydown', (event) => {
      event.keyCode === 39 && dispatch({type: 'MOVE_RIGHT'})
      event.keyCode === 40 && dispatch({type: 'MOVE_BOTTOM'})
      event.keyCode === 37 && dispatch({type: 'MOVE_LEFT'})
      event.keyCode === 38 && dispatch({type: 'MOVE_TOP'})
    });
  }, [dispatch])

  return(
    <>
      <div
        className='ball'
        style={{
          width: 50,
          height: 50,
          position: 'absolute',
          transition: `left 0.1s, right 0.1s, top 0.1s, bottom 0.1s`,
          transitionTimingFunction: 'cubic-bezier(.5,.5,.5,.5)',
          background: `url(${imgBall})`,
          backgroundSize: 'cover',
          left: `${x}px`,
          top: `${y}px`
        }}
      />
    </>
  )
}

export default Ball;
