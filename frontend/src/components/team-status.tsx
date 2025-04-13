import React from 'react';

export function TeamStatusCard(props: {teamName: string, gold: number}) {
  return (
    <div className="team-status-bar">
      <span className="team-name">{props.teamName}</span>
      <span className="team-gold">${props.gold}</span>
    </div>
  );
}