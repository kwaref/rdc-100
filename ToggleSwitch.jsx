import React from 'react'
import './toggleSwitch.css'

export const ToggleSwitch = () => {
	return (
		<label className='switch'>
			<input type='checkbox' />
			<span className='slider round'></span>
		</label>
	)
}
