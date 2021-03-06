import { useContext, useState } from 'react';
import { EntryContext } from '../App';
import { GetSuggestionRequest, Suggestion } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Atodeyomu = (props: any) => {
    const [isLoading, setIsLoading] = useState("探す");
    const { entries, setEntries } = useContext(EntryContext);
    // const [entries, setEntries] = useState({} as Suggestion[]);
    const compare = (n1: Suggestion, n2: Suggestion) => {
        let r = 0;
        if (n1.getScore() < n2.getScore()) { r = 1; }
        else if (n1.getScore() > n2.getScore()) { r = -1; }

        return r;
    };

    const getSuggestion = () => {
        const request = new GetSuggestionRequest();
        if (props.HatenaID) {
            request.setHatenaId(props.HatenaID);
            setIsLoading("検索中...");

            const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
            client.getSuggestion(request, {}, (err, ret) => {
                if (err || ret === null) {
                    setIsLoading("エラーが発生");
                    throw err;
                }
                const suggestions = ret.getSuggestionsList();
                setEntries(suggestions.sort(compare));
                setIsLoading("探す");
            });
        }
    }

    const onClick = () => {
        getSuggestion();
    };

    return (
        <header className="Atodeyomu">
            <h2>あとで読むから次に読む記事を探す</h2>
            <button onClick={onClick}>{isLoading}</button>
            { entries.length > 0 && (
                <ol>
                    {entries.map(entry => (
                        <li key={entry.getLink()}>
                            <a href={entry.getLink()}>
                                {entry.getTitle()}
                            </a>
                        </li>
                    ))}
                </ol>
            )}
        </header>
    )
}
