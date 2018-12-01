import React from 'react';
import ReactDOM from 'react-dom';
import Game from './Game';
import CssBaseline from '@material-ui/core/CssBaseline';
import SnippetList from './SnippetList';

const tictactoe = document.getElementById('tictactoe');
const css_baseline = document.getElementById('css-baseline');
const snippet_list = document.getElementById('snippet-list');

if (tictactoe) {
  ReactDOM.render(
    <Game />,
    tictactoe
  );
}

if (css_baseline) {
  ReactDOM.render(
    <CssBaseline />,
    css_baseline
  );
}

if (snippet_list) {
  ReactDOM.render(
    <SnippetList />,
    snippet_list
  );
}