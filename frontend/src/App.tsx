import React from 'react';
import './App.css';
import { ChallengeCard, ChallengeList } from './components/challenge-card';
import { TeamStatusCard } from './components/team-status';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Jet Lag The Game: MA$$ACHUSETTS</h1>
      </header>
      <TeamStatusCard teamName="Losers of the Custody Battle" gold={100} />
      <ChallengeList loc="Simmons" />
    </div>
  );
}

export default App;
