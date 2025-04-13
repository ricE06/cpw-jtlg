import React from 'react';

export function ChallengeList(props: {loc: string}) {
  return (
    <div>
      <h2>{props.loc}</h2>
      <div className="challenge-list">
        <ChallengeCard challengeTitle="Challenge 1" />
        <ChallengeCard challengeTitle="Challenge 2" />
        <ChallengeCard challengeTitle="Challenge 3" />
        <ChallengeCard challengeTitle="Challenge 4" />
        <ChallengeCard challengeTitle="Challenge 5" />
      </div>
    </div>
  );
}

export function ChallengeCard(props: {challengeTitle: string}) {
  return (
    <div className="challenge-card">
      <h3>{props.challengeTitle}</h3>
      <p>Spend an hour fighting React.</p>
      <button>Go!</button>
    </div>
  );
}

// TODO add new card component with full description + game logic, image submission