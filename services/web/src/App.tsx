import React, { useState } from 'react';
import './App.css';
import { Atodeyomu } from './components/Atodeyomu'
import { Hotentory } from './components/Hotentory'
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

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

export const UserContext = React.createContext({} as initialContext)

function App() {
  const [user, setUser] = useState<User>(initialUserValue);
  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <Welcome />
      </UserContext.Provider>
      <div className="Tab">
        {/* react-tab */}
        <Tabs>
          <TabList>
            <Tab>あとで読むから探す</Tab>
            <Tab>ホットエントリーから探す</Tab>
          </TabList>
          <TabPanel>
            <Atodeyomu />
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
