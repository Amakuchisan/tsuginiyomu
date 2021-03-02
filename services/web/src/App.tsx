import React, { useState } from 'react';
import './App.css';
import { Atodeyomu } from './components/Atodeyomu'
import { Hotentory } from './components/Hotentory'
import { Welcome } from './components/Welcome'
import { Wordcloud } from './components/Wordcloud'

// react-tabs
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

type User = {
  inputText: string,
  HatenaID: string,
};

type initialContext = {
  user: User,
  setUser: React.Dispatch<React.SetStateAction<User>>
};

const initialValue = {
  inputText: '',
  HatenaID: '',
};

export const UserContext = React.createContext({} as initialContext)
export const HatenaIDContext = React.createContext('' as User["HatenaID"])

function App() {
  const [user, setUser] = useState<User>(initialValue);
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
      <HatenaIDContext.Provider value={user.HatenaID}>
        <Wordcloud />
      </HatenaIDContext.Provider>
    </div>
  );
}

export default App;
