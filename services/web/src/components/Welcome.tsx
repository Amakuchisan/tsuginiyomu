import React, { useContext, useState } from 'react';
import { CreateUserRequest } from "../pb/manager/manager_pb";
import { ManagerClient } from "../pb/manager/ManagerServiceClientPb";
import { UserContext } from '../App';

export const Welcome = () => {
  const { user, setUser } = useContext(UserContext)
  const [message, setMessage] = useState('');
  const [wordcloud, setWordcloud] = useState("");

  const onClick = () => {
    const request = new CreateUserRequest();
    request.setHatenaid(user.inputText);

    const client = new ManagerClient(`http://${window.location.hostname}:8080`, {}, {});
    console.log("createUser")
    client.createUser(request, {}, (err, ret) => {
      if (err || ret === null) {
        throw err;
      }
      setUser({ ...user, HatenaID: ret.getHatenaid() });
      const img = ret.getWordcloud_asB64()
      console.log(img)
      setWordcloud(window.atob(img))
    });
  };

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({ ...user, inputText: e.target.value });
  };

  return (
    <header className="App-header">
      <div>
        はてなID :&nbsp;
          <input
          type="text"
          value={user.inputText}
          onChange={onChange}
        />

        <button onClick={onClick}>Send</button>
        <p>{message}</p>
        {wordcloud && (
          <div className="wordcloud">
            <img src={`data:;image/png;base64,${wordcloud}`} alt="wordcloud" />
          </div>
        )}
      </div>
    </header>
  )
}
