import React, { useContext, useState } from 'react';
import Select from 'react-select';
// import { HatenaIDContext } from '../App';

export const Hotentory = () => {
    // const HatenaID = useContext(HatenaIDContext)
    //   const [HatenaID, setHatenaID] = useState('sample');
    //   const [message, setMessage] = useState('');
    type option = {
        value: string,
        label: string,
    }

    const options = [
        { value: 'all', label: '総合' },
        { value: 'general', label: '一般' },
        { value: 'social', label: '世の中' },
        { value: 'economics', label: '政治と経済' },
        { value: 'life', label: '暮らし' },
        { value: 'knowledge', label: '学び' },
        { value: 'it', label: 'テクノロジー' },
        { value: 'fun', label: 'おもしろ' },
        { value: 'entertainment', label: 'エンタメ' },
        { value: 'game', label: 'アニメとゲーム' },
    ];

    const onClick = () => {
        console.log(selectedOption)
        // setMessage(`Hello ${HatenaID} !!`)
    };

    const onChange = (option: any) => {
        setSelectedOption(option.value)
    }

    const [selectedOption, setSelectedOption] = useState(null);

    return (
        <header className="wordcloud">
            <h2>ホットエントリーから次に読む記事を探す</h2>
            <h3>カテゴリを選んでください</h3>

            <div className="Category">
                <Select
                    options={options}
                    onChange={onChange}
                    defaultValue={selectedOption}
                />
            </div>

            <button onClick={onClick}>探す</button>
        </header>
    )
}
