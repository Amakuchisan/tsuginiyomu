import { useContext, useState } from 'react';
import Select from 'react-select';
import { HotEntryContext } from '../App';
import { GetHotentrySuggestionRequest, Suggestion } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Hotentory = (props: any) => {

    const [selectedOption, setSelectedOption] = useState({ value: 'all', label: '総合' });
    const { hotentries, setHotEntries } = useContext(HotEntryContext);
    const [message, setMessage] = useState("カテゴリを選んでください");

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

    const compare = (n1: Suggestion, n2: Suggestion) => {
        let r = 0;
        if (n1.getScore() < n2.getScore()) { r = 1; }
        else if (n1.getScore() > n2.getScore()) { r = -1; }

        return r;
    };

    const getHotentrySuggestion = (category: string) => {
        const request = new GetHotentrySuggestionRequest();
        if (props.HatenaID) {
            request.setHatenaId(props.HatenaID);
            request.setCategory(category);
            setMessage("検索中...")

            const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
            client.getHotentrySuggestion(request, {}, (err, ret) => {
                if (err || ret === null) {
                    setMessage("エラーが発生");
                    throw err;
                }
                const suggestions = ret.getSuggestionsList();
                setHotEntries(suggestions.sort(compare));
                setMessage("カテゴリを選んでください");
            });
        }
    }


    const onChange = (option: any) => {
        setSelectedOption(option);
        getHotentrySuggestion(option.value);
    }

    return (
        <header className="Hotentry">
            <h2>ホットエントリーから次に読む記事を探す</h2>
            <h3>{message}</h3>

            <div className="Category">
                <Select
                    options={options}
                    onChange={onChange}
                    defaultValue={selectedOption}
                />
            </div>

            { hotentries.length > 0 && (
                <ul>
                    {hotentries.map(entry => (
                        <li key={entry.getTitle()}>
                            <a href={entry.getLink()}>
                                {entry.getTitle()}
                            </a> ({entry.getScore().toFixed(2)})
                        </li>
                    ))}
                </ul>
            )}
        </header>
    )
}
