import React from 'react';
import CircularProgress from '@material-ui/core/CircularProgress';

class SnippetList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      page: 1,
    };
  }

  fetchSnippets() {
    const { page } = this.state;
    const url_query = '?page=' + page;

    history.replaceState({}, "", url_query);

    this.setState({isLoaded: false}, () => {
      $.ajax({
        method: "GET",
        url: "/api/snippets/" + url_query,
      }).done(data => {
        this.setState({
          snippets: data.results,
          previous: data.previous,
          next: data.next,
          isLoaded: true,
        });
      }).fail(error => {
        this.setState({
          error: error.responseJSON.detail,
          isLoaded: true,
        });
      });
    });
  }

  componentDidMount() {
    this.fetchSnippets();
  }

  render() {
    const { isLoaded, snippets } = this.state;

    return (
      <div>
      {isLoaded && 
        <div>{ JSON.stringify(snippets) }</div>
      }{!isLoaded &&
        <CircularProgress />
      }
      </div>
    );
  }
}

export default SnippetList;