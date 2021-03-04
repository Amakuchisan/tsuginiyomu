import React, { useState } from 'react';
import './App.css';
import { Atodeyomu } from './components/Atodeyomu'
import { Hotentory } from './components/Hotentory'
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

import { Suggestion } from "./pb/learner/learner_pb";

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

export const UserContext = React.createContext({} as initialContext)
export const EntryContext = React.createContext({} as initialEntryContext)

function App() {
  const [user, setUser] = useState<User>(initialUserValue);
  const [entries, setEntries] = useState({} as Suggestion[]);

  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <EntryContext.Provider value={{ entries, setEntries }}>
          <Welcome />
        </EntryContext.Provider>
      </UserContext.Provider>
      {user.HatenaID && (
        <h2>ようこそ{user.HatenaID}さん</h2>
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
            <Hotentory />
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
