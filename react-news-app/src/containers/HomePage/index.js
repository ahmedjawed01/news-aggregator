import React, { useState, useEffect } from "react";

// components
import Header from "../../components/Header";
import { toast } from "react-toastify";

// services
import { getNews, searchNewsAPI } from "../../store/service/news.service";

// styles
import "./style.scss";
import "react-toastify/dist/ReactToastify.css";

const HomePage = () => {
  const [news, setNews] = useState("");
  const [searchValue, setSearchValue] = useState("");
  const [loader, setLoader] = useState(false);

  React.useEffect(() => {
    getAllNews();
  }, []);

  const getAllNews = async () => {
    try {
      const response = await getNews();
      setNews(response.data);
    } catch (error) {
      toast.error(error.response);
    }
  };

  const searchNewsData = async () => {
    setLoader(true);
    try {
      const response = await searchNewsAPI(searchValue);
      setNews(response.data)
    } catch (error) {
      toast.error(error.response);
    }
    setLoader(false);
  }

  return (
    <>
      <Header setSearchValue={setSearchValue} searchNewsData={searchNewsData} getAllNews={getAllNews} loader={loader} />
      <div className="p-5 page-container">
        <h1 className="pb-4 Header">News</h1>
        {news.length ? 
        <>
        {news && news.map((item, index) => (
          <div key={index} className="p-5 news-card">
            <div className="d-flex align-items-center">
              <a href={item.link} target="_blank" className="mb-0 mt-0">{item.headline}</a>
            </div>
            <div className="d-flex align-items-center">
              <h2 className="pr-4 source">Source</h2>
              <p className="mb-0 mt-0">{item.source}</p>
            </div>
          </div>
        ))}
        </> :
        <p className="text-center">Not Result Found</p>}
      </div>
    </>
  );
};

export default HomePage;
