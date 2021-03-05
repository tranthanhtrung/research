import React, { useEffect } from 'react'
import { useDispatch } from 'react-redux'

import imgStart from './../assets/images/start.png'
import imgLogo from './../assets/images/logo.png'
import imgBackground from './../assets/images/background.png'

import Ball from './Ball'
import Bomd from './Bomb'

const Game = (props) => {
  const dispatch = useDispatch()

  useEffect(() => {
    setInterval(() => {
      dispatch({type: 'GENERATE'})
    }, 1000)
    setInterval(() => {
      dispatch({type: 'RUNNING'})
    }, 300)
  }, [dispatch])

  return (
    <div style={{
      overflow: 'hidden',
      position: 'relative',
      margin: '30px auto',
      width: 600,
      height: 600,
      background: `url(${imgBackground})`,
      backgroundSize: '600px 600px'
    }}>
      <Bomd/>
      <Ball/>

    </div>
  )
}

// <img className="img-logo" alt={"logo game"} src={imgLogo}/>
// <img className="btn-start" alt={"start game"} src={imgStart}/>
// <Bomd/>
export default Game
