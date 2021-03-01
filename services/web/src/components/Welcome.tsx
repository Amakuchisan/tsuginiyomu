import React, { useContext, useState } from 'react';
import { UserContext } from '../App';

export const Welcome = () => {
  const { user, setUser } = useContext(UserContext)
  const [message, setMessage] = useState('');

  const onClick = () => {
    setUser({...user, HatenaID: user.inputText });
    setMessage(`Hello ${user.inputText} !!`)
    // setMessage(`Hello ${user.HatenaID} !!`)
  };

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({ ...user, inputText: e.target.value });
  };

  return (
    <header className="App-header">
      <div>
        はてなID :
          <input
          type="text"
          value={user.inputText}
          onChange={onChange}
        />

        <button onClick={onClick}>Send</button>
        <p>{message}</p>
      </div>
    </header>
  )
}
