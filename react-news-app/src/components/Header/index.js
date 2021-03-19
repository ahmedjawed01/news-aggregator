import React from "react";

// components
import { Spinner } from "react-bootstrap";

// styles
import "./style.scss";

const Header = ({ setSearchValue, searchNewsData, loader, getAllNews }) => {
  const onSubmit = (e) => {
    e.preventDefault();
    searchNewsData();
  };

  const handleSearchValue = (e) => {
    setSearchValue(e.target.value);
    if (e.target.value.length === 0) {
      getAllNews();
    } else {
      setSearchValue(e.target.value);
    }
  };

  return (
    <nav className="navbar navbar-light justify-content-between">
      <a className="navbar-brand">News Aggregator</a>
      <form className="form-inline">
        <input
          className="form-control mr-sm-2"
          type="search"
          placeholder="Search"
          aria-label="Search"
          onChange={(e) => handleSearchValue(e)}
        />
        <button
          onClick={onSubmit}
          className="btn btn-outline-primary my-2 my-sm-0"
        >
          {loader ? (
            <>
              <span
                className="spinner-border login-txt spinner-border-sm mr-2"
                role="status"
                aria-hidden="true"
              ></span>
              <span className="login-txt">Searching</span>
            </>
          ) : (
            <span>Search</span>
          )}
        </button>
      </form>
    </nav>
  );
};

export default Header;
