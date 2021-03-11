import React, { useState } from 'react';
import './App.css';
import { Atodeyomu } from './components/Atodeyomu'
import { Hotentory } from './components/Hotentry'
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

import { Suggestion, LearnRequest } from "./pb/learner/learner_pb";
import { LearnerClient } from "./pb/learner/LearnerServiceClientPb";

// react-tabs
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

export type User = {
  HatenaID: string,
  wordcloud: string,
};

const initialUserValue = {
  HatenaID: '',
  wordcloud: '',
};

type initialContext = {
  user: User,
  setUser: React.Dispatch<React.SetStateAction<User>>
};

type initialEntryContext = {
  entries: Suggestion[],
  setEntries: React.Dispatch<React.SetStateAction<Suggestion[]>>
};

type initialHotEntryContext = {
  hotentries: Suggestion[],
  setHotEntries: React.Dispatch<React.SetStateAction<Suggestion[]>>
};

export const UserContext = React.createContext({} as initialContext)
export const EntryContext = React.createContext({} as initialEntryContext)
export const HotEntryContext = React.createContext({} as initialHotEntryContext)

const App = () => {
  const [user, setUser] = useState<User>(initialUserValue);
  const [entries, setEntries] = useState({} as Suggestion[]);
  const [hotentries, setHotEntries] = useState({} as Suggestion[]);
  const [learnMessage, setLearnMessage] = useState('データを学習する');

  const onClickLearn = () => {
    if (!user.HatenaID) {
      return
    }
    const request = new LearnRequest();
    request.setHatenaId(user.HatenaID);
    setLearnMessage("学習中...")

    const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
    client.learn(request, {}, (err, ret) => {
      if (err || ret === null) {
        setLearnMessage("エラー")
        throw err;
      }
      // if (ret.getLearned()) {
      //   console.log("学習が終わりました！");
      // } else {
      //   console.log("学習に失敗しました！");
      // }
      console.log("学習が終わりました！");
      setLearnMessage("データを学習する")
    });
  };

  const initEntries = () => {
    setEntries({} as Suggestion[]);
    setHotEntries({} as Suggestion[]);
  }

  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <Welcome initEntries={initEntries}/>
      </UserContext.Provider>
      {user.HatenaID && (
        <div className="Learn">
          <h2 className="message">ようこそ{user.HatenaID}さん</h2>
          <button onClick={onClickLearn}>{learnMessage}</button>
        </div>
      )}
      {!user.HatenaID && (
        <h2>ログインしてください</h2>
      )}
      <div className="Tab">
        {/* react-tab */}
        <Tabs>
          <TabList>
            <Tab>あとで読むから探す</Tab>
            <Tab>ホットエントリーから探す</Tab>
          </TabList>
          <TabPanel>
            <EntryContext.Provider value={{ entries, setEntries }}>
              <Atodeyomu HatenaID={user.HatenaID} />
            </EntryContext.Provider>
          </TabPanel>
          <TabPanel>
            <HotEntryContext.Provider value={{ hotentries, setHotEntries }}>
              <Hotentory HatenaID={user.HatenaID} />
            </HotEntryContext.Provider>
          </TabPanel>
        </Tabs>
        {/* react-tab */}
      </div>
      <UserContext.Provider value={{ user, setUser }}>
        <Wordcloud />
      </UserContext.Provider>
    </div>
  );
}

export default App;
