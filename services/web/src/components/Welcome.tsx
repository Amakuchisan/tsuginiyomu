import React, { useContext, useState } from 'react';
import { UserContext } from '../App';
import { EntryContext } from '../App';
import { CreateUserRequest } from "../pb/manager/manager_pb";
import { ManagerClient } from "../pb/manager/ManagerServiceClientPb";
import { Suggestion, LearnRequest } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Welcome = () => {
  const { user, setUser } = useContext(UserContext)
  const { entries, setEntries } = useContext(EntryContext)
  const [inputText, setInputText] = useState('');
  const [message, setMessage] = useState('データを学習する');

  const onClick = () => {
    const request = new CreateUserRequest();
    request.setHatenaid(inputText);

    const client = new ManagerClient(`http://${window.location.hostname}:8080/manager`, {}, {});
    client.createUser(request, {}, (err, ret) => {
      if (err || ret === null) {
        throw err;
      }
      setUser({ ...user, HatenaID: ret.getHatenaid(), wordcloud: window.atob(ret.getWordcloud_asB64()) });
      setEntries({} as Suggestion[])
    });
  };

  const onClickLearn = () => {
    if (!user.HatenaID) {
      return
    }
    const request = new LearnRequest();
    request.setHatenaId(inputText);
    setMessage("学習中...")

    const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
    client.learn(request, {}, (err, ret) => {
      if (err || ret === null) {
        throw err;
      }
      if (ret.getLearned()) {
        console.log("学習が終わりました！")
      } else {
        console.log("学習に失敗しました！")
      }
      setMessage("データを学習する")
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
        {user.HatenaID && (
          <div className="Learner-button">
            <button onClick={onClickLearn}>{message}</button>
          </div>
        )}
      </div>
    </header>
  )
}
