#ifndef __IF_STORE_H__
#define __IF_STORE_H__


class IStore
{
  public:
    virtual bool saveRsps() = 0;
    virtual bool getReqs() = 0;
};


#endif
