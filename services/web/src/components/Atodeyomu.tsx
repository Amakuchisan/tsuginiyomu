// import React, { useState } from 'react';
import React, { useContext } from 'react';
import { EntryContext } from '../App';
import { GetSuggestionRequest, Suggestion } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";

export const Atodeyomu = (props: any) => {
    const {entries, setEntries} = useContext(EntryContext);
    // const [entries, setEntries] = useState({} as Suggestion[]);
    const compare = (n1: Suggestion, n2: Suggestion) => {
        let r = 0;
        if (n1.getScore() < n2.getScore()) { r = 1; }
        else if (n1.getScore() > n2.getScore()) { r = -1; }

        return r;
    };

    const getSuggestion = () => {
        console.log(props.HatenaID)
        const request = new GetSuggestionRequest();
        if (props.HatenaID) {
            request.setHatenaId(props.HatenaID);

            const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
            client.getSuggestion(request, {}, (err, ret) => {
                if (err || ret === null) {
                    throw err;
                }
                const suggestions = ret.getSuggestionsList();
                setEntries(suggestions.sort(compare))
            });
        }
    }

    const onClick = () => {
        getSuggestion();
    };

    return (
        <header className="wordcloud">
            <h2>あとで読むから次に読む記事を探す</h2>
            <button onClick={onClick}>探す</button>
            { entries.length > 0 && (
                <ul>
                    {entries.map(entry => (
                        <li key={entry.getTitle()}>
                            <a href={entry.getLink()}>
                                {entry.getTitle()}
                            </a>
                        </li>
                    ))}
                </ul>
            )}
        </header>
    )
}
