import React, { useContext } from 'react';

import { CreateWordCloudRequest } from "../pb/learner/learner_pb";
import { LearnerClient } from "../pb/learner/LearnerServiceClientPb";
import { WordcloudContext } from '../App';
import userEvent from '@testing-library/user-event';

export const Wordcloud = () => {
    const { user, setWordcloud } = useContext(WordcloudContext)

    const updateWordcloud = () => {
        const request = new CreateWordCloudRequest();
        if (user.HatenaID) {
            request.setHatenaId(user.HatenaID);

            const client = new LearnerClient(`http://${window.location.hostname}:8080/learner`, {}, {});
            client.createWordCloud(request, {}, (err, ret) => {
                if (err || ret === null) {
                    throw err;
                }
                setWordcloud(window.atob(ret.getWordcloud_asB64()))
            });
        }
    }
    const onClick = () => {
        updateWordcloud();
    };

    return (
        <header className="wordcloud">
            <h2>{user.HatenaID}さんのワードクラウドを作成する</h2>

            <button onClick={onClick}>画像を更新する</button>
            {user.wordcloud && (
                <div className="wordcloud">
                    <img src={`data:;image/png;base64,${user.wordcloud}`} alt="wordcloud" />
                </div>
            )};
        </header>
    )
}
