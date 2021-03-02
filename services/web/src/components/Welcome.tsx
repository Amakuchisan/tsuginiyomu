import React, { useContext, useState } from 'react';
import { CreateUserRequest } from "../pb/manager/manager_pb";
import { ManagerClient } from "../pb/manager/ManagerServiceClientPb";
import { UserContext } from '../App';

export const Welcome = () => {
  const { user, setUser } = useContext(UserContext)
  const [inputText, setInputText] = useState('');

  const onClick = () => {
    const request = new CreateUserRequest();
    request.setHatenaid(inputText);

    const client = new ManagerClient(`http://${window.location.hostname}:8080/manager`, {}, {});
    console.log("createUser")
    client.createUser(request, {}, (err, ret) => {
      if (err || ret === null) {
        throw err;
      }
      setUser({ ...user, HatenaID: ret.getHatenaid(), wordcloud: window.atob(ret.getWordcloud_asB64()) });
    });
  };

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value);
  };

  return (
    <header className="App-header">
      <div>
        はてなID :&nbsp;
          <input
          type="text"
          value={inputText}
          onChange={onChange}
        />

        <button onClick={onClick}>Send</button>
      </div>
    </header>
  )
}
