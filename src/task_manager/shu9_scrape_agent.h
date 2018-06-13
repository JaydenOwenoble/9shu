#ifndef __SHU9_SCRAPE_AGENT_H__
#define __SHU9_SCRAPE_AGENT_H__

#include "interfaces/scrape_agent.h"


class Shu9ScrapeAgent : public IScrapeAgent
{
  public:
    // Implement IScrapeAgent
    const char* scrapeHtmls(const char* req);
    const char* getQuality();
};


#endif