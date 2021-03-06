import React, { useContext, useState } from 'react';

import { UserContext } from '../App';
import { EntryContext, HotEntryContext } from '../App';
import { CreateUserRequest } from "../pb/manager/manager_pb";
import { ManagerClient } from "../pb/manager/ManagerServiceClientPb";
import { Suggestion, LearnRequest } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Welcome = () => {
  const { user, setUser } = useContext(UserContext)
  const { entries, setEntries } = useContext(EntryContext)
  const { hotentries, setHotEntries } = useContext(HotEntryContext)
  const [inputText, setInputText] = useState('');
  const [learnMessage, setLearnMessage] = useState('データを学習する');

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
      setEntries({} as Suggestion[]);
      setHotEntries({} as Suggestion[]);
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

  const onClickLearn = () => {
    if (!user.HatenaID) {
      return
    }
    const request = new LearnRequest();
    request.setHatenaId(inputText);
    setLearnMessage("学習中...")

    const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
    client.learn(request, {}, (err, ret) => {
      if (err || ret === null) {
        setLearnMessage("エラー")
        throw err;
      }
      if (ret.getLearned()) {
        console.log("学習が終わりました！");
      } else {
        console.log("学習に失敗しました！");
      }
      setLearnMessage("データを学習する")
    });
  };

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

      {user.HatenaID && (
        <div className="Learner-button">
          <button onClick={onClickLearn}>{learnMessage}</button>
        </div>
      )}
    </header>
  )
}
