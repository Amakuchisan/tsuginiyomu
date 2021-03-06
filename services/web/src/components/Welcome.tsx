import React, { useContext, useState } from 'react';

import { UserContext } from '../App';
import { CreateUserRequest } from "../pb/manager/manager_pb";
import { ManagerClient } from "../pb/manager/ManagerServiceClientPb";
import { LearnRequest } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Welcome = (props: any) => {
  const { user, setUser } = useContext(UserContext)
  const [inputText, setInputText] = useState('');

  const onClick = async () => {
    if (!inputText) {
      return;
    }
    const isExisted = await exist_user();
    if (!isExisted) {
      // 存在しないユーザは登録しない
      setInputText('');
      return;
    }
    const request = new CreateUserRequest();
    request.setHatenaid(inputText);

    const client = new ManagerClient(`http://${window.location.hostname}:8080/manager`, {}, {});
    client.createUser(request, {}, (err, ret) => {
      if (err || ret === null) {
        throw err;
      }
      setUser({ ...user, HatenaID: ret.getHatenaid(), wordcloud: window.atob(ret.getWordcloud_asB64()) });
      props.initEntries();
    });
  };

  const exist_user = () => {
    return new Promise(resolve => {
      const request = new LearnRequest();
      request.setHatenaId(inputText);
      const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
      client.existsHatenaID(request, {}, (err, ret) => {
        if (err || ret === null) {
          alert("サーバエラーが発生");
          throw err;
        }
        if (!ret.getExisted()) {
          alert("存在しないはてなIDです");
        }
        resolve(ret.getExisted());
      });
    });
  }

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value);
  };

  return (
    <header className="App-header">
      <div className="user_input">
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
