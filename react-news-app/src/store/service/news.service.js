import axios from "axios";
import Config from "../../config/index";


// getNews
const getNews = async () => {
    const url = `${Config.baseUrl}/news`;
    const result = await axios.get(url);
    return result;
};

// searchNews
/**
 * 
 *  
 * @param search_value 
 */
 const searchNewsAPI = async (search_value) => {
    const url = `${Config.baseUrl}/news?q=${search_value}`;
    const result = await axios.get(url);
    return result;
};


export { getNews, searchNewsAPI };