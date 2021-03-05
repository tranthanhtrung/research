import React, { useEffect } from 'react'
import { useSelector } from 'react-redux'

import './../assets/css/index.css'
import bomd1 from './../assets/images/bomb/ball2.png'
import bomd2 from './../assets/images/bomb/ball3.png'
import bomd3 from './../assets/images/bomb/ball4.png'

const img = [bomd1, bomd2, bomd3]

const Bomb = () => {
  const { bombs } = useSelector(state => state.bomb)
  return (
    <>
      {bombs.map((pos, index) => {
        return (
          <div
            key={index}
            className='bomd'
            style={{
              width: 50,
              height: 50,
              position: 'absolute',
              transition: `left 0.3s, right 0.3s, top 0.3s, bottom 0.3s`,
              transitionTimingFunction: 'cubic-bezier(.5,.5,.5,.5)',
              background: `url(${img[pos.typeBomb]})`,
              backgroundSize: 'cover',
              left: `${pos.x}px`,
              top: `${pos.y}px`
            }}
          />
        )
      })}
    </>
  )
}

export default Bomb
