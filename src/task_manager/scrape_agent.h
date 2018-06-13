#ifndef __IF_SCRAPE_AGENT_H__
#define __IF_SCRAPE_AGENT_H__


enum ScrapeStatus
{
    SCRAPE_OK,
    SCRAPE_FAIL
};


/** Scrape agent interface
 * function: By this interface you can control one scrape.
 */
class IScrapeAgent
{
  public:
    /** Scrape htmls
     * function: Get a batch of htmls by a batch of requests.
     * desc: This is a block function. */
    virtual ScrapeStatus scrapeHtmls(const char* req) = 0;

    /** Get the capacity of scrape. */
    virtual const char* getQuality() = 0;
};


#endif
