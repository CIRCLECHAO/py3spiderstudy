#*encoding=utf-8
from pyquery import PyQuery as pq

html = """
<div id="mainsrp-itemlist"><div class="m-itemlist" data-spm="14">
  <div class="grid g-clearfix">
    <div class="items">
      
<div class="item J_MouserOnverReq item-ad  " data-category="auctions" data-index="0">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552801603455" class="pic-link J_ClickStat J_ItemPicA" data-nid="552801603455" data-recommend-nav="" href="https://click.simba.taobao.com/cc_im?p=iPad&amp;s=853497975&amp;k=513&amp;e=Nt%2BdVo86JXV62Y7Uf1SS3gF6xK9nE%2FsvNhBmw3K720SG0krIAi4h1yDT%2FVvd90F6gNRWkwREPzxuzfzH0mjaRhAlcid1amHjsYkjeYu71MqWwzc2fRoqUQy22txm%2BleSzWQuLmZS6KDytAl9VshU%2Bx97Ruli6jn0mJfOpMPd5Ntp4hOOcEa0CnANy%2BblWLV9y%2FhKWlvMD1q9dwhZjplArpFB1lbBXvRA%2BjpZhunlf%2B11OFV%2BdHLC7WJeGfrt29hrT%2BJfHJYsahEvbai6VnYgndH0qAgRBdvFyW08QSYFGzMzaP7aUZXHw3p8lzQ4deU%2FhmJejUurbtsbdLTV8kzzRSVfxT5OCmsFQLe3REz80ElUXLkTzB8Cs4zGALJCCSEjZJGKmR4V3nsSm7z3PCSQRf7CGw0ALTej7gszQ8msvTNZqD0hxp9z3rAV0RskKUZ2C5EukTEY5cP78IjuRQ4n7X9SZjueUcy2zuFj7JrBTfsUZfPuXt%2BN0a9iEuKm25Oi#detail" data-href="https://click.simba.taobao.com/cc_im?p=iPad&amp;s=853497975&amp;k=513&amp;e=Nt%2BdVo86JXV62Y7Uf1SS3gF6xK9nE%2FsvNhBmw3K720SG0krIAi4h1yDT%2FVvd90F6gNRWkwREPzxuzfzH0mjaRhAlcid1amHjsYkjeYu71MqWwzc2fRoqUQy22txm%2BleSzWQuLmZS6KDytAl9VshU%2Bx97Ruli6jn0mJfOpMPd5Ntp4hOOcEa0CnANy%2BblWLV9y%2FhKWlvMD1q9dwhZjplArpFB1lbBXvRA%2BjpZhunlf%2B11OFV%2BdHLC7WJeGfrt29hrT%2BJfHJYsahEvbai6VnYgndH0qAgRBdvFyW08QSYFGzMzaP7aUZXHw3p8lzQ4deU%2FhmJejUurbtsbdLTV8kzzRSVfxT5OCmsFQLe3REz80ElUXLkTzB8Cs4zGALJCCSEjZJGKmR4V3nsSm7z3PCSQRf7CGw0ALTej7gszQ8msvTNZqD0hxp9z3rAV0RskKUZ2C5EukTEY5cP78IjuRQ4n7X9SZjueUcy2zuFj7JrBTfsUZfPuXt%2BN0a9iEuKm25Oi#detail" target="_blank" trace="msrp_auction" traceidx="0" trace-index="0" trace-nid="552801603455" trace-num="44" trace-price="4138.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552801603455" class="J_ItemPic img" src="//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i4/12657496/TB2z79EueGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg_230x230.jpg_.webp" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i4/12657496/TB2z79EueGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg" alt="Apple/苹果 iPad Pro 10">
            </a>
      </div>

  


      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552801603455" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>4138.00</strong>
      </div>
      <div class="deal-cnt">539人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552801603455" class="J_ClickStat" data-nid="552801603455" href="https://click.simba.taobao.com/cc_im?p=iPad&amp;s=853497975&amp;k=513&amp;e=Nt%2BdVo86JXV62Y7Uf1SS3gF6xK9nE%2FsvNhBmw3K720SG0krIAi4h1yDT%2FVvd90F6gNRWkwREPzxuzfzH0mjaRhAlcid1amHjsYkjeYu71MqWwzc2fRoqUQy22txm%2BleSzWQuLmZS6KDytAl9VshU%2Bx97Ruli6jn0mJfOpMPd5Ntp4hOOcEa0CnANy%2BblWLV9y%2FhKWlvMD1q9dwhZjplArpFB1lbBXvRA%2BjpZhunlf%2B11OFV%2BdHLC7WJeGfrt29hrT%2BJfHJYsahEvbai6VnYgndH0qAgRBdvFyW08QSYFGzMzaP7aUZXHw3p8lzQ4deU%2FhmJejUurbtsbdLTV8kzzRSVfxT5OCmsFQLe3REz80ElUXLkTzB8Cs4zGALJCCSEjZJGKmR4V3nsSm7z3PCSQRf7CGw0ALTej7gszQ8msvTNZqD0hxp9z3rAV0RskKUZ2C5EukTEY5cP78IjuRQ4n7X9SZjueUcy2zuFj7JrBTfsUZfPuXt%2BN0a9iEuKm25Oi#detail" target="_blank" trace="msrp_auction" traceidx="0" trace-index="0" trace-nid="552801603455" trace-num="44" trace-price="4138.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸 平板电脑 2018新款<span class="H">iPad</span>苹果pro9.7
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
        <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="100340983" data-nid="552801603455" target="_blank" href="https://click.simba.taobao.com/cc_im?p=iPad&amp;s=853497975&amp;k=481&amp;e=tQwhF2v%2BDb162Y7Uf1SS3gF6xK9nE%2FsvNhBmw3K720SG0krIAi4h1yDT%2FVvd90F6gNRWkwREPzxNW2H8phwemBAlcid1amHjsYkjeYu71MqWwzc2fRoqUQy22txm%2BleSzWQuLmZS6KDytAl9VshU%2Bx97Ruli6jn0mJfOpMPd5Ntp4hOOcEa0CnANy%2BblWLV9y%2FhKWlvMD1q9dwhZjplArpFB1lbBXvRA%2BjpZhunlf%2B11OFV%2BdHLC7WJeGfrt29hrT%2BJfHJYsahEvbai6VnYgndH0qAgRBdvFyW08QSYFGzMzaP7aUZXHw3p8lzQ4deU%2FhmJejUurbtsbdLTV8kzzRSVfxT5OCmsFQLe3REz80ElUXLkTzB8Cs4zGALJCCSEjZJGKmR4V3nv6NSxWragstvv9FOriv1088jdXVwmAsESNFUTjqTGk094YCxv083n7Bscmwupou6mXeY2mpz0%2BQJz%2BoEMIaIZm">
            <span class="dsrs">
                    <span class="dsr morethan"></span>
                    <span class="dsr morethan"></span>
                    <span class="dsr morethan"></span>
                </span>
          <span>领域数码通讯</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552801603455">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//re.taobao.com/search?keyword=iPad&amp;refpid=420432_1006&amp;frcatid=&amp;" target="_blank" title="掌柜热卖宝贝" trace="srpservice" traceidx="0"><span class="icon-service-remai"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="1">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_536758244128" class="pic-link J_ClickStat J_ItemPicA" data-nid="536758244128" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=536758244128&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=536758244128&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="1" trace-index="1" trace-nid="536758244128" trace-num="44" trace-price="2686.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_536758244128" class="J_ItemPic img" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/268451883/TB1hLXBz5OYBuNjSsD4XXbSkFXa_!!0-item_pic.jpg_230x230.jpg_.webp" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/268451883/TB1hLXBz5OYBuNjSsD4XXbSkFXa_!!0-item_pic.jpg" alt="【128G3期免息】Apple/苹果 iPad mini 4 7.9英寸 wifi 平板电脑 正品国行3/6/12期分期 三际数码官方旗舰店">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=536758244128">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=536758244128" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2686.00</strong>
      </div>
      <div class="deal-cnt">540人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_536758244128" class="J_ClickStat" data-nid="536758244128" href="//detail.tmall.com/item.htm?id=536758244128&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="1" trace-index="1" trace-nid="536758244128" trace-num="44" trace-price="2686.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          【128G3期免息】Apple/苹果 <span class="H">iPad</span> mini 4 7.9英寸 wifi 平板电脑 正品国行3/6/12期分期 三际数码官方旗舰店
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="268451883" data-nid="536758244128" href="//store.taobao.com/shop/view_shop.htm?user_number_id=268451883" target="_blank">
        <span class="dsrs">
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
            </span>
        <span>三际数码官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">山东 济南</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_536758244128">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="3"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="三际数码官方旗舰店" data-display="inline" data-item="536758244128" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E4%B8%89%E9%99%85%E6%95%B0%E7%A0%81%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="2">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_521889234742" class="pic-link J_ClickStat J_ItemPicA" data-nid="521889234742" data-recommend-nav="" href="//item.taobao.com/item.htm?id=521889234742&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=521889234742&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="2" trace-index="2" trace-nid="521889234742" trace-num="44" trace-price="5558.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_521889234742" class="J_ItemPic img" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2430166508/TB262m0ihWYBuNjy1zkXXXGGpXa_!!2430166508.jpg_230x230.jpg_.webp" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2430166508/TB262m0ihWYBuNjy1zkXXXGGpXa_!!2430166508.jpg" alt="新款Apple/苹果 iPad pro 12.9寸 64g 256G Wifi 4G 平板电脑国行">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=521889234742">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=521889234742" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>5558.00</strong>
      </div>
      <div class="deal-cnt">107人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_521889234742" class="J_ClickStat" data-nid="521889234742" href="//item.taobao.com/item.htm?id=521889234742&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="2" trace-index="2" trace-nid="521889234742" trace-num="44" trace-price="5558.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          新款Apple/苹果 <span class="H">iPad</span> pro 12.9寸 64g 256G Wifi 4G 平板电脑国行
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2430166508" data-nid="521889234742" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2430166508" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>麦克团mactuancom</span>
      </a>
    
  


        </div>
        <div class="location">北京</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_521889234742">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="6"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="麦克团mactuancom" data-display="inline" data-item="521889234742" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E9%BA%A6%E5%85%8B%E5%9B%A2mactuancom&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="3">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_573597186496" class="pic-link J_ClickStat J_ItemPicA" data-nid="573597186496" data-recommend-nav="" href="//item.taobao.com/item.htm?id=573597186496&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=573597186496&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="3" trace-index="3" trace-nid="573597186496" trace-num="44" trace-price="1750.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_573597186496" class="J_ItemPic img" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i3/2244854683/TB24.fuHWmWBuNjy1XaXXXCbXXa_!!2244854683.jpg_230x230.jpg_.webp" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i3/2244854683/TB24.fuHWmWBuNjy1XaXXXCbXXa_!!2244854683.jpg" alt="Apple/苹果 iPad mini4平板电脑插卡7.9寸三网4G版WIFI 迷你4">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=573597186496">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=573597186496" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1750.00</strong>
      </div>
      <div class="deal-cnt">76人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_573597186496" class="J_ClickStat" data-nid="573597186496" href="//item.taobao.com/item.htm?id=573597186496&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="3" trace-index="3" trace-nid="573597186496" trace-num="44" trace-price="1750.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> mini4平板电脑插卡7.9寸三网4G版WIFI 迷你4
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2244854683" data-nid="573597186496" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2244854683" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>创业新辉煌588</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_573597186496">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="创业新辉煌588" data-display="inline" data-item="573597186496" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%88%9B%E4%B8%9A%E6%96%B0%E8%BE%89%E7%85%8C588&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="4">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_41780562505" class="pic-link J_ClickStat J_ItemPicA" data-nid="41780562505" data-recommend-nav="" href="//item.taobao.com/item.htm?id=41780562505&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=41780562505&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="4" trace-index="4" trace-nid="41780562505" trace-num="44" trace-price="1828.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_41780562505" class="J_ItemPic img" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i2/898225/TB2PU9bkHArBKNjSZFLXXc_dVXa_!!898225.jpg_230x230.jpg_.webp" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i2/898225/TB2PU9bkHArBKNjSZFLXXc_dVXa_!!898225.jpg" alt="Apple/苹果 iPad 2018款iPad air3 平板电脑 ipad2018新款9.7">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=41780562505">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=41780562505" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1828.00</strong>
      </div>
      <div class="deal-cnt">389人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_41780562505" class="J_ClickStat" data-nid="41780562505" href="//item.taobao.com/item.htm?id=41780562505&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="4" trace-index="4" trace-nid="41780562505" trace-num="44" trace-price="1828.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> 2018款<span class="H">iPad</span> air3 平板电脑 <span class="H">ipad</span>2018新款9.7
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="898225" data-nid="41780562505" href="//store.taobao.com/shop/view_shop.htm?user_number_id=898225" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>ygsd</span>
      </a>
    
  


        </div>
        <div class="location">北京</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_41780562505">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="8"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-fuwu"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="ygsd" data-display="inline" data-item="41780562505" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=ygsd&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="5">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552807369048" class="pic-link J_ClickStat J_ItemPicA" data-nid="552807369048" data-recommend-nav="" href="//item.taobao.com/item.htm?id=552807369048&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=552807369048&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="5" trace-index="5" trace-nid="552807369048" trace-num="44" trace-price="3368.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552807369048" class="J_ItemPic img" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/898225/TB2.RDJB4GYBuNjy0FnXXX5lpXa_!!898225.jpg_230x230.jpg_.webp" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/898225/TB2.RDJB4GYBuNjy0FnXXX5lpXa_!!898225.jpg" alt="新款Apple/苹果 iPad Pro 10.5寸 9.7 平板 wifi 4G 港版国行现货">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552807369048">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552807369048" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3368.00</strong>
      </div>
      <div class="deal-cnt">186人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552807369048" class="J_ClickStat" data-nid="552807369048" href="//item.taobao.com/item.htm?id=552807369048&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="5" trace-index="5" trace-nid="552807369048" trace-num="44" trace-price="3368.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          新款Apple/苹果 <span class="H">iPad</span> Pro 10.5寸 9.7 平板 wifi 4G 港版国行现货
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="898225" data-nid="552807369048" href="//store.taobao.com/shop/view_shop.htm?user_number_id=898225" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>ygsd</span>
      </a>
    
  


        </div>
        <div class="location">北京</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552807369048">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="11"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-fuwu"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="ygsd" data-display="inline" data-item="552807369048" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=ygsd&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="6">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_538682674274" class="pic-link J_ClickStat J_ItemPicA" data-nid="538682674274" data-recommend-nav="" href="//item.taobao.com/item.htm?id=538682674274&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=538682674274&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="6" trace-index="6" trace-nid="538682674274" trace-num="44" trace-price="2800.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_538682674274" class="J_ItemPic img" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/773574749/TB26VhnkCCWBuNjy0FhXXb6EVXa_!!773574749.png_230x230.jpg_.webp" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/773574749/TB26VhnkCCWBuNjy0FhXXb6EVXa_!!773574749.png" alt="Apple/苹果 新款iPad Pro 12.9英寸平板电脑9.7 10.5美版国行">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=538682674274">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=538682674274" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2800.00</strong>
      </div>
      <div class="deal-cnt">74人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_538682674274" class="J_ClickStat" data-nid="538682674274" href="//item.taobao.com/item.htm?id=538682674274&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="6" trace-index="6" trace-nid="538682674274" trace-num="44" trace-price="2800.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 新款<span class="H">iPad</span> Pro 12.9英寸平板电脑9.7 10.5美版国行
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="773574749" data-nid="538682674274" href="//store.taobao.com/shop/view_shop.htm?user_number_id=773574749" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>laughing京</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_538682674274">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="laughing京" data-display="inline" data-item="538682674274" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=laughing%E4%BA%AC&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="7">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_547848493836" class="pic-link J_ClickStat J_ItemPicA" data-nid="547848493836" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=547848493836&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=547848493836&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="7" trace-index="7" trace-nid="547848493836" trace-num="44" trace-price="1968.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_547848493836" class="J_ItemPic img" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i2/1764629552/TB1VlRSoxSYBuNjSspjXXX73VXa_!!0-item_pic.jpg_230x230.jpg_.webp" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i2/1764629552/TB1VlRSoxSYBuNjSspjXXX73VXa_!!0-item_pic.jpg" alt="低至1968起/2017款/Apple/苹果 Ipad平板电脑苹果9.7英寸 air2升级版 32/128Gwifi 国行正品 12期分期">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=547848493836">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=547848493836" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1968.00</strong>
      </div>
      <div class="deal-cnt">262人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_547848493836" class="J_ClickStat" data-nid="547848493836" href="//detail.tmall.com/item.htm?id=547848493836&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="7" trace-index="7" trace-nid="547848493836" trace-num="44" trace-price="1968.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          低至1968起/2017款/Apple/苹果 <span class="H">Ipad</span>平板电脑苹果9.7英寸 air2升级版 32/128Gwifi 国行正品 12期分期
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1764629552" data-nid="547848493836" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1764629552" target="_blank">
        <span class="dsrs">
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
            </span>
        <span>环球机库官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">江苏 扬州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_547848493836">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="15"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="环球机库官方旗舰店" data-display="inline" data-item="547848493836" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%8E%AF%E7%90%83%E6%9C%BA%E5%BA%93%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="8">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552925823079" class="pic-link J_ClickStat J_ItemPicA" data-nid="552925823079" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=552925823079&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=552925823079&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="8" trace-index="8" trace-nid="552925823079" trace-num="44" trace-price="4538.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552925823079" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/2616970884/O1CN011IOuZHW8yKRmwdS_!!2616970884.jpg" alt="Apple/苹果 iPad Pro 10.5英寸64G/256G轻薄平板电脑wifi 开发票 全国13仓就近发货" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/2616970884/O1CN011IOuZHW8yKRmwdS_!!2616970884.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552925823079">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552925823079" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>4538.00</strong>
      </div>
      <div class="deal-cnt">870人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552925823079" class="J_ClickStat" data-nid="552925823079" href="//detail.tmall.com/item.htm?id=552925823079&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="8" trace-index="8" trace-nid="552925823079" trace-num="44" trace-price="4538.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸64G/256G轻薄平板电脑wifi 开发票 全国13仓就近发货
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2616970884" data-nid="552925823079" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2616970884" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>苏宁易购官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">江苏 南京</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552925823079">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="17"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="苏宁易购官方旗舰店" data-display="inline" data-item="552925823079" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E8%8B%8F%E5%AE%81%E6%98%93%E8%B4%AD%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="9">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_522542463386" class="pic-link J_ClickStat J_ItemPicA" data-nid="522542463386" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=522542463386&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=522542463386&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="9" trace-index="9" trace-nid="522542463386" trace-num="44" trace-price="2699.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_522542463386" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2616970884/TB1Yhk0qByWBuNkSmFPXXXguVXa_!!0-item_pic.jpg" alt="Apple/苹果 iPad mini4 7.9英寸平板电脑128GWiFi版迷你平板电脑" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2616970884/TB1Yhk0qByWBuNkSmFPXXXguVXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=522542463386">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=522542463386" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2699.00</strong>
      </div>
      <div class="deal-cnt">906人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_522542463386" class="J_ClickStat" data-nid="522542463386" href="//detail.tmall.com/item.htm?id=522542463386&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="9" trace-index="9" trace-nid="522542463386" trace-num="44" trace-price="2699.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> mini4 7.9英寸平板电脑128GWiFi版迷你平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2616970884" data-nid="522542463386" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2616970884" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>苏宁易购官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">江苏 南京</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_522542463386">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="19"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="苏宁易购官方旗舰店" data-display="inline" data-item="522542463386" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E8%8B%8F%E5%AE%81%E6%98%93%E8%B4%AD%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="10">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552789216451" class="pic-link J_ClickStat J_ItemPicA" data-nid="552789216451" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=552789216451&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=552789216451&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="10" trace-index="10" trace-nid="552789216451" trace-num="44" trace-price="4599.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552789216451" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/1669409267/TB1pLn5BhuTBuNkHFNRXXc9qpXa_!!0-item_pic.jpg" alt="Apple/苹果 iPad Pro 10.5英寸 平板电脑 64G/256G Wifi版 轻薄" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/1669409267/TB1pLn5BhuTBuNkHFNRXXc9qpXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552789216451">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552789216451" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>4599.00</strong>
      </div>
      <div class="deal-cnt">470人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552789216451" class="J_ClickStat" data-nid="552789216451" href="//detail.tmall.com/item.htm?id=552789216451&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="10" trace-index="10" trace-nid="552789216451" trace-num="44" trace-price="4599.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸 平板电脑 64G/256G Wifi版 轻薄
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1669409267" data-nid="552789216451" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1669409267" target="_blank">
        <span class="dsrs">
                <span class="dsr equalthan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>卓辰数码旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">浙江 杭州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552789216451">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="21"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="2">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="卓辰数码旗舰店" data-display="inline" data-item="552789216451" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%8D%93%E8%BE%B0%E6%95%B0%E7%A0%81%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="11">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552647276387" class="pic-link J_ClickStat J_ItemPicA" data-nid="552647276387" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=552647276387&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=552647276387&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="11" trace-index="11" trace-nid="552647276387" trace-num="44" trace-price="6333.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552647276387" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/TB1An8PRFXXXXbUXVXXXXXXXXXX_!!0-item_pic.jpg" alt="Apple/苹果 12.9 英寸 iPad Pro" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/TB1An8PRFXXXXbUXVXXXXXXXXXX_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552647276387">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552647276387" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>6333.00</strong>
      </div>
      <div class="deal-cnt"></div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552647276387" class="J_ClickStat" data-nid="552647276387" href="//detail.tmall.com/item.htm?id=552647276387&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="11" trace-index="11" trace-nid="552647276387" trace-num="44" trace-price="6333.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 12.9 英寸 <span class="H">iPad</span> Pro
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1917047079" target="_blank">applestore官方旗舰店</a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552647276387">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="24"><span class="icon-service-tianmao"></span></a>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="applestore官方旗舰店" data-display="inline" data-item="552647276387" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=applestore%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="12">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552644716383" class="pic-link J_ClickStat J_ItemPicA" data-nid="552644716383" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=552644716383&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=552644716383&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="12" trace-index="12" trace-nid="552644716383" trace-num="44" trace-price="5143.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552644716383" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/TB1An8PRFXXXXbUXVXXXXXXXXXX_!!0-item_pic.jpg" alt="Apple/苹果 10.5 英寸 iPad Pro" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/TB1An8PRFXXXXbUXVXXXXXXXXXX_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552644716383">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552644716383" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>5143.00</strong>
      </div>
      <div class="deal-cnt"></div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552644716383" class="J_ClickStat" data-nid="552644716383" href="//detail.tmall.com/item.htm?id=552644716383&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="12" trace-index="12" trace-nid="552644716383" trace-num="44" trace-price="5143.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 10.5 英寸 <span class="H">iPad</span> Pro
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1917047079" target="_blank">applestore官方旗舰店</a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552644716383">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="25"><span class="icon-service-tianmao"></span></a>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="applestore官方旗舰店" data-display="inline" data-item="552644716383" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=applestore%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="13">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_547699700735" class="pic-link J_ClickStat J_ItemPicA" data-nid="547699700735" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=547699700735&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=547699700735&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="13" trace-index="13" trace-nid="547699700735" trace-num="44" trace-price="2058.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_547699700735" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/1669409267/TB1P60GmHZnBKNjSZFhXXc.oXXa_!!0-item_pic.jpg" alt="Apple/苹果 Ipad 2017款 9.7英寸 平板电脑 32G/128G Wifi版" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/1669409267/TB1P60GmHZnBKNjSZFhXXc.oXXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=547699700735">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=547699700735" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2058.00</strong>
      </div>
      <div class="deal-cnt">378人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_547699700735" class="J_ClickStat" data-nid="547699700735" href="//detail.tmall.com/item.htm?id=547699700735&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="13" trace-index="13" trace-nid="547699700735" trace-num="44" trace-price="2058.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">Ipad</span> 2017款 9.7英寸 平板电脑 32G/128G Wifi版
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1669409267" data-nid="547699700735" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1669409267" target="_blank">
        <span class="dsrs">
                <span class="dsr equalthan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>卓辰数码旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">浙江 杭州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_547699700735">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="26"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="2">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="卓辰数码旗舰店" data-display="inline" data-item="547699700735" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%8D%93%E8%BE%B0%E6%95%B0%E7%A0%81%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="14">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_553551949493" class="pic-link J_ClickStat J_ItemPicA" data-nid="553551949493" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=553551949493&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=553551949493&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="14" trace-index="14" trace-nid="553551949493" trace-num="44" trace-price="5788.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_553551949493" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/197232874/TB1DXhpCASWBuNjSszdXXbeSpXa_!!0-item_pic.jpg" alt="赠电动牙刷【2年保修】Apple/苹果 iPad Pro 10.5英寸平板电脑" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/197232874/TB1DXhpCASWBuNjSszdXXbeSpXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=553551949493">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=553551949493" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>5788.00</strong>
      </div>
      <div class="deal-cnt">76人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_553551949493" class="J_ClickStat" data-nid="553551949493" href="//detail.tmall.com/item.htm?id=553551949493&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="14" trace-index="14" trace-nid="553551949493" trace-num="44" trace-price="5788.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          赠电动牙刷【2年保修】Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="197232874" data-nid="553551949493" href="//store.taobao.com/shop/view_shop.htm?user_number_id=197232874" target="_blank">
        <span class="dsrs">
                <span class="dsr equalthan"></span>
                <span class="dsr equalthan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>绿森数码官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">浙江 杭州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_553551949493">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="29"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-tmallzhisongonly" title="天猫直送，天猫保障的配送服务。规则见详情页。"></span>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="2">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="3">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="绿森数码官方旗舰店" data-display="inline" data-item="553551949493" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%BB%BF%E6%A3%AE%E6%95%B0%E7%A0%81%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="15">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_542753672513" class="pic-link J_ClickStat J_ItemPicA" data-nid="542753672513" data-recommend-nav="" href="//item.taobao.com/item.htm?id=542753672513&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=542753672513&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="15" trace-index="15" trace-nid="542753672513" trace-num="44" trace-price="3199.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_542753672513" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/319889882/TB2tLIqrYSYBuNjSspiXXXNzpXa_!!319889882.jpg" alt="Apple/苹果 iPad pro 大屏苹果12.9寸平板电脑 ipadpro wifi 4G港" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/319889882/TB2tLIqrYSYBuNjSspiXXXNzpXa_!!319889882.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=542753672513">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=542753672513" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3199.00</strong>
      </div>
      <div class="deal-cnt">92人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_542753672513" class="J_ClickStat" data-nid="542753672513" href="//item.taobao.com/item.htm?id=542753672513&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="15" trace-index="15" trace-nid="542753672513" trace-num="44" trace-price="3199.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> pro 大屏苹果12.9寸平板电脑 <span class="H">ipad</span>pro wifi 4G港
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="319889882" data-nid="542753672513" href="//store.taobao.com/shop/view_shop.htm?user_number_id=319889882" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>飞翔数码馆</span>
      </a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_542753672513">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="飞翔数码馆" data-display="inline" data-item="542753672513" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E9%A3%9E%E7%BF%94%E6%95%B0%E7%A0%81%E9%A6%86&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="16">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_570849344177" class="pic-link J_ClickStat J_ItemPicA" data-nid="570849344177" data-recommend-nav="" href="//item.taobao.com/item.htm?id=570849344177&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=570849344177&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="16" trace-index="16" trace-nid="570849344177" trace-num="44" trace-price="1275.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_570849344177" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/2617114334/TB2iwh7x5CYBuNkHFCcXXcHtVXa_!!2617114334.jpg" alt="Apple/苹果 ipad mini 3平板电脑7.9英寸wifi插卡版3g2g迷你3 64g" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/2617114334/TB2iwh7x5CYBuNkHFCcXXcHtVXa_!!2617114334.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=570849344177">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=570849344177" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1275.00</strong>
      </div>
      <div class="deal-cnt">259人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_570849344177" class="J_ClickStat" data-nid="570849344177" href="//item.taobao.com/item.htm?id=570849344177&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="16" trace-index="16" trace-nid="570849344177" trace-num="44" trace-price="1275.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">ipad</span> mini 3平板电脑7.9英寸wifi插卡版3g2g迷你3 64g
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2617114334" data-nid="570849344177" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2617114334" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>优品电讯1</span>
      </a>
    
  


        </div>
        <div class="location">广东 惠州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_570849344177">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="优品电讯1" data-display="inline" data-item="570849344177" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E4%BC%98%E5%93%81%E7%94%B5%E8%AE%AF1&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="17">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_570016032807" class="pic-link J_ClickStat J_ItemPicA" data-nid="570016032807" data-recommend-nav="" href="//item.taobao.com/item.htm?id=570016032807&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=570016032807&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="17" trace-index="17" trace-nid="570016032807" trace-num="44" trace-price="3400.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_570016032807" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2561411244/TB2frjvsNGYBuNjy0FnXXX5lpXa_!!2561411244.jpg" alt="Apple/苹果 iPad Pro 10.5英寸9.7平板电脑2017 2018新款iPad" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2561411244/TB2frjvsNGYBuNjy0FnXXX5lpXa_!!2561411244.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=570016032807">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=570016032807" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3400.00</strong>
      </div>
      <div class="deal-cnt">70人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_570016032807" class="J_ClickStat" data-nid="570016032807" href="//item.taobao.com/item.htm?id=570016032807&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="17" trace-index="17" trace-nid="570016032807" trace-num="44" trace-price="3400.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸9.7平板电脑2017 2018新款<span class="H">iPad</span>
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2561411244" data-nid="570016032807" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2561411244" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>youjinglongye</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_570016032807">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="youjinglongye" data-display="inline" data-item="570016032807" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=youjinglongye&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="18">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_560436394138" class="pic-link J_ClickStat J_ItemPicA" data-nid="560436394138" data-recommend-nav="" href="//item.taobao.com/item.htm?id=560436394138&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=560436394138&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="18" trace-index="18" trace-nid="560436394138" trace-num="44" trace-price="2799.99" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_560436394138" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/591479855/TB2bpXfn1uSBuNjSsziXXbq8pXa_!!591479855.png" alt="2017款Apple/苹果 iPad Pro一二代12.9/10.5/9.7平板电脑美版国行" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/591479855/TB2bpXfn1uSBuNjSsziXXbq8pXa_!!591479855.png_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=560436394138">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=560436394138" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2799.99</strong>
      </div>
      <div class="deal-cnt">81人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_560436394138" class="J_ClickStat" data-nid="560436394138" href="//item.taobao.com/item.htm?id=560436394138&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="18" trace-index="18" trace-nid="560436394138" trace-num="44" trace-price="2799.99" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          2017款Apple/苹果 <span class="H">iPad</span> Pro一二代12.9/10.5/9.7平板电脑美版国行
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="591479855" data-nid="560436394138" href="//store.taobao.com/shop/view_shop.htm?user_number_id=591479855" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>goheyboy</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_560436394138">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="goheyboy" data-display="inline" data-item="560436394138" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=goheyboy&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="19">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_547482776077" class="pic-link J_ClickStat J_ItemPicA" data-nid="547482776077" data-recommend-nav="" href="//item.taobao.com/item.htm?id=547482776077&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=547482776077&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="19" trace-index="19" trace-nid="547482776077" trace-num="44" trace-price="1688.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_547482776077" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/25483223/TB2hHb2iL9TBuNjy1zbXXXpepXa_!!25483223.jpg" alt="Apple/苹果 iPad 2018款 32 128G wifi 4G 新iPad Air 4 未激活" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i4/25483223/TB2hHb2iL9TBuNjy1zbXXXpepXa_!!25483223.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=547482776077">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=547482776077" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1688.00</strong>
      </div>
      <div class="deal-cnt">64人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_547482776077" class="J_ClickStat" data-nid="547482776077" href="//item.taobao.com/item.htm?id=547482776077&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="19" trace-index="19" trace-nid="547482776077" trace-num="44" trace-price="1688.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> 2018款 32 128G wifi 4G 新<span class="H">iPad</span> Air 4 未激活
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="25483223" data-nid="547482776077" href="//store.taobao.com/shop/view_shop.htm?user_number_id=25483223" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>糊涂在线</span>
      </a>
    
  


        </div>
        <div class="location">四川 成都</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_547482776077">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="糊涂在线" data-display="inline" data-item="547482776077" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%B3%8A%E6%B6%82%E5%9C%A8%E7%BA%BF&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="20">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_566928246245" class="pic-link J_ClickStat J_ItemPicA" data-nid="566928246245" data-recommend-nav="" href="//item.taobao.com/item.htm?id=566928246245&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=566928246245&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="20" trace-index="20" trace-nid="566928246245" trace-num="44" trace-price="1610.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_566928246245" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/319889882/TB27r4isb9YBuNjy0FgXXcxcXXa_!!319889882.jpg" alt="Apple/苹果 iPad 2018款 9.7英寸 平板电脑 Wifi版新款32G/128G" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/319889882/TB27r4isb9YBuNjy0FgXXcxcXXa_!!319889882.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=566928246245">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=566928246245" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1610.00</strong>
      </div>
      <div class="deal-cnt">220人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_566928246245" class="J_ClickStat" data-nid="566928246245" href="//item.taobao.com/item.htm?id=566928246245&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="20" trace-index="20" trace-nid="566928246245" trace-num="44" trace-price="1610.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> 2018款 9.7英寸 平板电脑 Wifi版新款32G/128G
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="319889882" data-nid="566928246245" href="//store.taobao.com/shop/view_shop.htm?user_number_id=319889882" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>飞翔数码馆</span>
      </a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_566928246245">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="飞翔数码馆" data-display="inline" data-item="566928246245" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E9%A3%9E%E7%BF%94%E6%95%B0%E7%A0%81%E9%A6%86&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="21">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_573504301725" class="pic-link J_ClickStat J_ItemPicA" data-nid="573504301725" data-recommend-nav="" href="//item.taobao.com/item.htm?id=573504301725&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=573504301725&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="21" trace-index="21" trace-nid="573504301725" trace-num="44" trace-price="1120.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_573504301725" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/1590377402/TB2BNSoEKSSBuNjy0FlXXbBpVXa_!!1590377402.jpg" alt="Apple/苹果ipad mini2平板电脑 迷你全新7.9英寸特价插卡wifi超薄" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/1590377402/TB2BNSoEKSSBuNjy0FlXXbBpVXa_!!1590377402.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=573504301725">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=573504301725" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1120.00</strong>
      </div>
      <div class="deal-cnt">377人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_573504301725" class="J_ClickStat" data-nid="573504301725" href="//item.taobao.com/item.htm?id=573504301725&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="21" trace-index="21" trace-nid="573504301725" trace-num="44" trace-price="1120.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果<span class="H">ipad</span> mini2平板电脑 迷你全新7.9英寸特价插卡wifi超薄
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1590377402" data-nid="573504301725" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1590377402" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>guangzhou_0753</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_573504301725">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="guangzhou_0753" data-display="inline" data-item="573504301725" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=guangzhou_0753&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="22">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_566736097933" class="pic-link J_ClickStat J_ItemPicA" data-nid="566736097933" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=566736097933&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=566736097933&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="22" trace-index="22" trace-nid="566736097933" trace-num="44" trace-price="2288.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_566736097933" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i3/1708919206/TB1710nzXOWBuNjy0FiXXXFxVXa_!!0-item_pic.jpg" alt="【12期分期】Apple/苹果 iPad 2018款 平板电脑9.7英寸32G/128G" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i3/1708919206/TB1710nzXOWBuNjy0FiXXXFxVXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=566736097933">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=566736097933" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2288.00</strong>
      </div>
      <div class="deal-cnt">129人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_566736097933" class="J_ClickStat" data-nid="566736097933" href="//detail.tmall.com/item.htm?id=566736097933&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="22" trace-index="22" trace-nid="566736097933" trace-num="44" trace-price="2288.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          【12期分期】Apple/苹果 <span class="H">iPad</span> 2018款 平板电脑9.7英寸32G/128G
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1708919206" data-nid="566736097933" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1708919206" target="_blank">
        <span class="dsrs">
                <span class="dsr equalthan"></span>
                <span class="dsr equalthan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>禾木林数码专营店</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_566736097933">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="41"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="禾木林数码专营店" data-display="inline" data-item="566736097933" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%A6%BE%E6%9C%A8%E6%9E%97%E6%95%B0%E7%A0%81%E4%B8%93%E8%90%A5%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="23">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_567243251492" class="pic-link J_ClickStat J_ItemPicA" data-nid="567243251492" data-recommend-nav="" href="//item.taobao.com/item.htm?id=567243251492&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=567243251492&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="23" trace-index="23" trace-nid="567243251492" trace-num="44" trace-price="2430.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_567243251492" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/3270656771/TB2Dm1Lg1uSBuNjSsplXXbe8pXa_!!3270656771.jpg" alt="Apple/苹果 iPad Pro 10.5英寸 9.7英寸平板电脑 苹果新款iPad" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/3270656771/TB2Dm1Lg1uSBuNjSsplXXbe8pXa_!!3270656771.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=567243251492">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=567243251492" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2430.00</strong>
      </div>
      <div class="deal-cnt">67人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_567243251492" class="J_ClickStat" data-nid="567243251492" href="//item.taobao.com/item.htm?id=567243251492&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="23" trace-index="23" trace-nid="567243251492" trace-num="44" trace-price="2430.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸 9.7英寸平板电脑 苹果新款<span class="H">iPad</span>
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="3270656771" data-nid="567243251492" href="//store.taobao.com/shop/view_shop.htm?user_number_id=3270656771" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>如龙数码城</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_567243251492">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="如龙数码城" data-display="inline" data-item="567243251492" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%A6%82%E9%BE%99%E6%95%B0%E7%A0%81%E5%9F%8E&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="24">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_557362749658" class="pic-link J_ClickStat J_ItemPicA" data-nid="557362749658" data-recommend-nav="" href="//item.taobao.com/item.htm?id=557362749658&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=557362749658&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="24" trace-index="24" trace-nid="557362749658" trace-num="44" trace-price="3959.01" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_557362749658" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/1963365327/TB2tv5pnQyWBuNjy0FpXXassXXa_!!1963365327.jpg" alt="Apple/苹果 新款ipad pro12.9寸pro  4G版 12.9pro 二代 平板电脑" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/1963365327/TB2tv5pnQyWBuNjy0FpXXassXXa_!!1963365327.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=557362749658">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=557362749658" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3959.01</strong>
      </div>
      <div class="deal-cnt">52人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_557362749658" class="J_ClickStat" data-nid="557362749658" href="//item.taobao.com/item.htm?id=557362749658&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="24" trace-index="24" trace-nid="557362749658" trace-num="44" trace-price="3959.01" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 新款<span class="H">ipad</span> pro12.9寸pro  4G版 12.9pro 二代 平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1963365327" data-nid="557362749658" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1963365327" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>宝诗丽1314</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_557362749658">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="宝诗丽1314" data-display="inline" data-item="557362749658" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%AE%9D%E8%AF%97%E4%B8%BD1314&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="25">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_539337968924" class="pic-link J_ClickStat J_ItemPicA" data-nid="539337968924" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=539337968924&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=539337968924&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="25" trace-index="25" trace-nid="539337968924" trace-num="44" trace-price="2628.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_539337968924" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1764629552/TB1LDPhlOCYBuNkHFCcXXcHtVXa_!!0-item_pic.jpg" alt="低至2598起/Apple/苹果 iPad mini 4 128G 7.9英寸迷你4平板游戏平板 4G版 3/6/12期分期 正品国行 全国联保" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1764629552/TB1LDPhlOCYBuNkHFCcXXcHtVXa_!!0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=539337968924">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=539337968924" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2628.00</strong>
      </div>
      <div class="deal-cnt">233人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_539337968924" class="J_ClickStat" data-nid="539337968924" href="//detail.tmall.com/item.htm?id=539337968924&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="25" trace-index="25" trace-nid="539337968924" trace-num="44" trace-price="2628.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          低至2598起/Apple/苹果 <span class="H">iPad</span> mini 4 128G 7.9英寸迷你4平板游戏平板 4G版 3/6/12期分期 正品国行 全国联保
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1764629552" data-nid="539337968924" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1764629552" target="_blank">
        <span class="dsrs">
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
            </span>
        <span>环球机库官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">江苏 扬州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_539337968924">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="43"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="环球机库官方旗舰店" data-display="inline" data-item="539337968924" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%8E%AF%E7%90%83%E6%9C%BA%E5%BA%93%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="26">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_565378069102" class="pic-link J_ClickStat J_ItemPicA" data-nid="565378069102" data-recommend-nav="" href="//item.taobao.com/item.htm?id=565378069102&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=565378069102&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="26" trace-index="26" trace-nid="565378069102" trace-num="44" trace-price="4180.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_565378069102" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1856213115/TB2gWKUC3mTBuNjy1XbXXaMrVXa_!!1856213115.jpg" alt="Apple/苹果iPad Pro 10.5寸插卡4G 苹果平板 ipad 新款pro12.9寸" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1856213115/TB2gWKUC3mTBuNjy1XbXXaMrVXa_!!1856213115.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=565378069102">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=565378069102" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>4180.00</strong>
      </div>
      <div class="deal-cnt">97人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_565378069102" class="J_ClickStat" data-nid="565378069102" href="//item.taobao.com/item.htm?id=565378069102&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="26" trace-index="26" trace-nid="565378069102" trace-num="44" trace-price="4180.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果<span class="H">iPad</span> Pro 10.5寸插卡4G 苹果平板 <span class="H">ipad</span> 新款pro12.9寸
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1856213115" data-nid="565378069102" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1856213115" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>纯色心情1951</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_565378069102">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-fuwu"></span>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="纯色心情1951" data-display="inline" data-item="565378069102" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%BA%AF%E8%89%B2%E5%BF%83%E6%83%851951&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="27">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_566559466243" class="pic-link J_ClickStat J_ItemPicA" data-nid="566559466243" data-recommend-nav="" href="//item.taobao.com/item.htm?id=566559466243&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=566559466243&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="27" trace-index="27" trace-nid="566559466243" trace-num="44" trace-price="1650.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_566559466243" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/2676434646/TB26C.7tfiSBuNkSnhJXXbDcpXa_!!2676434646.jpg" alt="Apple/苹果 iPad Air2平板电脑 2017升级款3网4G9.7英寸WIFI全新" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i4/2676434646/TB26C.7tfiSBuNkSnhJXXbDcpXa_!!2676434646.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=566559466243">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=566559466243" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1650.00</strong>
      </div>
      <div class="deal-cnt">364人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_566559466243" class="J_ClickStat" data-nid="566559466243" href="//item.taobao.com/item.htm?id=566559466243&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="27" trace-index="27" trace-nid="566559466243" trace-num="44" trace-price="1650.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Air2平板电脑 2017升级款3网4G9.7英寸WIFI全新
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2676434646" data-nid="566559466243" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2676434646" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>莫长琴</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_566559466243">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="莫长琴" data-display="inline" data-item="566559466243" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E8%8E%AB%E9%95%BF%E7%90%B4&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="28">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_530916542482" class="pic-link J_ClickStat J_ItemPicA" data-nid="530916542482" data-recommend-nav="" href="//item.taobao.com/item.htm?id=530916542482&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=530916542482&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="28" trace-index="28" trace-nid="530916542482" trace-num="44" trace-price="2250.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_530916542482" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/138183191/TB2cCU0lxGYBuNjy0FnXXX5lpXa_!!138183191.jpg" alt="Apple/苹果 iPad pro 10.5寸 Pro 12.9寸 4G版 商务 平板电脑" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/138183191/TB2cCU0lxGYBuNjy0FnXXX5lpXa_!!138183191.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=530916542482">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=530916542482" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2250.00</strong>
      </div>
      <div class="deal-cnt">105人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_530916542482" class="J_ClickStat" data-nid="530916542482" href="//item.taobao.com/item.htm?id=530916542482&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="28" trace-index="28" trace-nid="530916542482" trace-num="44" trace-price="2250.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> pro 10.5寸 Pro 12.9寸 4G版 商务 平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="138183191" data-nid="530916542482" href="//store.taobao.com/shop/view_shop.htm?user_number_id=138183191" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>刘胜将军</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_530916542482">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="48"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="刘胜将军" data-display="inline" data-item="530916542482" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%88%98%E8%83%9C%E5%B0%86%E5%86%9B&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="29">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_547214698912" class="pic-link J_ClickStat J_ItemPicA" data-nid="547214698912" data-recommend-nav="" href="//item.taobao.com/item.htm?id=547214698912&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=547214698912&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="29" trace-index="29" trace-nid="547214698912" trace-num="44" trace-price="1950.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_547214698912" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/475027050/TB2H5hQhNSYBuNjSsphXXbGvVXa_!!475027050.jpg" alt="正品Apple/苹果 iPad 2018款 9.7英寸平板电脑32G/128G 新款iPad" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/475027050/TB2H5hQhNSYBuNjSsphXXbGvVXa_!!475027050.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=547214698912">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=547214698912" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1950.00</strong>
      </div>
      <div class="deal-cnt">71人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_547214698912" class="J_ClickStat" data-nid="547214698912" href="//item.taobao.com/item.htm?id=547214698912&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="29" trace-index="29" trace-nid="547214698912" trace-num="44" trace-price="1950.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          正品Apple/苹果 <span class="H">iPad</span> 2018款 9.7英寸平板电脑32G/128G 新款<span class="H">iPad</span>
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="475027050" data-nid="547214698912" href="//store.taobao.com/shop/view_shop.htm?user_number_id=475027050" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>860803华晶</span>
      </a>
    
  


        </div>
        <div class="location">浙江 杭州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_547214698912">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="50"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="860803华晶" data-display="inline" data-item="547214698912" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=860803%E5%8D%8E%E6%99%B6&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="30">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_554352080996" class="pic-link J_ClickStat J_ItemPicA" data-nid="554352080996" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=554352080996&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=554352080996&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="30" trace-index="30" trace-nid="554352080996" trace-num="44" trace-price="2628.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_554352080996" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/3339867181/TB2ONR4J29TBuNjy0FcXXbeiFXa_!!3339867181-0-item_pic.jpg" alt="【12期分期】 Apple/苹果 iPad mini 4 平板电脑苹果7.9英寸 128G wifi正品 迷你4游戏平板 4G版" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/3339867181/TB2ONR4J29TBuNjy0FcXXbeiFXa_!!3339867181-0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=554352080996">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=554352080996" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2628.00</strong>
      </div>
      <div class="deal-cnt">165人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_554352080996" class="J_ClickStat" data-nid="554352080996" href="//detail.tmall.com/item.htm?id=554352080996&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="30" trace-index="30" trace-nid="554352080996" trace-num="44" trace-price="2628.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          【12期分期】 Apple/苹果 <span class="H">iPad</span> mini 4 平板电脑苹果7.9英寸 128G wifi正品 迷你4游戏平板 4G版
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="3339867181" data-nid="554352080996" href="//store.taobao.com/shop/view_shop.htm?user_number_id=3339867181" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>岗隆数码专营店</span>
      </a>
    
  


        </div>
        <div class="location">江苏 无锡</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_554352080996">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="52"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="岗隆数码专营店" data-display="inline" data-item="554352080996" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%B2%97%E9%9A%86%E6%95%B0%E7%A0%81%E4%B8%93%E8%90%A5%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="31">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_563361679776" class="pic-link J_ClickStat J_ItemPicA" data-nid="563361679776" data-recommend-nav="" href="//item.taobao.com/item.htm?id=563361679776&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=563361679776&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="31" trace-index="31" trace-nid="563361679776" trace-num="44" trace-price="3484.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_563361679776" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/747184945/TB234hfj6nD8KJjSspbXXbbEXXa_!!747184945.png" alt="Apple/苹果 iPad Pro 10.5英寸 平板电脑 2017 2018新款iPad美版" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/747184945/TB234hfj6nD8KJjSspbXXbbEXXa_!!747184945.png_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=563361679776">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=563361679776" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3484.00</strong>
      </div>
      <div class="deal-cnt">51人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_563361679776" class="J_ClickStat" data-nid="563361679776" href="//item.taobao.com/item.htm?id=563361679776&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="31" trace-index="31" trace-nid="563361679776" trace-num="44" trace-price="3484.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5英寸 平板电脑 2017 2018新款<span class="H">iPad</span>美版
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="747184945" data-nid="563361679776" href="//store.taobao.com/shop/view_shop.htm?user_number_id=747184945" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>背着大象奔驰的蚂蚁</span>
      </a>
    
  


        </div>
        <div class="location">四川 成都</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_563361679776">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="背着大象奔驰的蚂蚁" data-display="inline" data-item="563361679776" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E8%83%8C%E7%9D%80%E5%A4%A7%E8%B1%A1%E5%A5%94%E9%A9%B0%E7%9A%84%E8%9A%82%E8%9A%81&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="32">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_567197203365" class="pic-link J_ClickStat J_ItemPicA" data-nid="567197203365" data-recommend-nav="" href="//item.taobao.com/item.htm?id=567197203365&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=567197203365&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="32" trace-index="32" trace-nid="567197203365" trace-num="44" trace-price="2288.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_567197203365" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/20267119/TB2KOxpyOOYBuNjSsD4XXbSkFXa_!!20267119.jpg" alt="Apple/苹果 iPad 2018款 iPad6支持苹果手写笔 9.7寸未拆封未激活" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/20267119/TB2KOxpyOOYBuNjSsD4XXbSkFXa_!!20267119.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=567197203365">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=567197203365" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2288.00</strong>
      </div>
      <div class="deal-cnt">50人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_567197203365" class="J_ClickStat" data-nid="567197203365" href="//item.taobao.com/item.htm?id=567197203365&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="32" trace-index="32" trace-nid="567197203365" trace-num="44" trace-price="2288.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> 2018款 <span class="H">iPad</span>6支持苹果手写笔 9.7寸未拆封未激活
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="20267119" data-nid="567197203365" href="//store.taobao.com/shop/view_shop.htm?user_number_id=20267119" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>bvfdew</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_567197203365">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <a href="//www.taobao.com/go/act/jpmj.php" target="_blank" trace="srpservice" traceidx="55"><span class="icon-service-jinpaimaijia"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="bvfdew" data-display="inline" data-item="567197203365" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=bvfdew&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="33">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_554902582555" class="pic-link J_ClickStat J_ItemPicA" data-nid="554902582555" data-recommend-nav="" href="//item.taobao.com/item.htm?id=554902582555&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=554902582555&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="33" trace-index="33" trace-nid="554902582555" trace-num="44" trace-price="1905.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_554902582555" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/1826072582/TB2wW3zgGmWBuNjy1XaXXXCbXXa_!!1826072582.jpeg" alt="Apple/苹果 iPad 2018款平板电脑苹果全新正品9.7英寸128g 32g 4g" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i1/1826072582/TB2wW3zgGmWBuNjy1XaXXXCbXXa_!!1826072582.jpeg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=554902582555">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=554902582555" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1905.00</strong>
      </div>
      <div class="deal-cnt">102人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_554902582555" class="J_ClickStat" data-nid="554902582555" href="//item.taobao.com/item.htm?id=554902582555&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="33" trace-index="33" trace-nid="554902582555" trace-num="44" trace-price="1905.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> 2018款平板电脑苹果全新正品9.7英寸128g 32g 4g
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1826072582" data-nid="554902582555" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1826072582" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>cyipad7022</span>
      </a>
    
  


        </div>
        <div class="location">四川 成都</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_554902582555">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="cyipad7022" data-display="inline" data-item="554902582555" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=cyipad7022&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="34">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_568457254445" class="pic-link J_ClickStat J_ItemPicA" data-nid="568457254445" data-recommend-nav="" href="//item.taobao.com/item.htm?id=568457254445&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=568457254445&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="34" trace-index="34" trace-nid="568457254445" trace-num="44" trace-price="3325.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_568457254445" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/2561411244/TB2QJwXnQOWBuNjSsppXXXPgpXa_!!2561411244.jpg" alt="2017新款Apple/苹果 iPad Pro 12.9 二代 256GB 平板电脑" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/2561411244/TB2QJwXnQOWBuNjSsppXXXPgpXa_!!2561411244.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=568457254445">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=568457254445" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3325.00</strong>
      </div>
      <div class="deal-cnt">48人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_568457254445" class="J_ClickStat" data-nid="568457254445" href="//item.taobao.com/item.htm?id=568457254445&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="34" trace-index="34" trace-nid="568457254445" trace-num="44" trace-price="3325.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          2017新款Apple/苹果 <span class="H">iPad</span> Pro 12.9 二代 256GB 平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="2561411244" data-nid="568457254445" href="//store.taobao.com/shop/view_shop.htm?user_number_id=2561411244" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>youjinglongye</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_568457254445">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="youjinglongye" data-display="inline" data-item="568457254445" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=youjinglongye&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="35">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_567412509044" class="pic-link J_ClickStat J_ItemPicA" data-nid="567412509044" data-recommend-nav="" href="//detail.tmall.com/item.htm?id=567412509044&amp;ns=1&amp;abbucket=4" data-href="//detail.tmall.com/item.htm?id=567412509044&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="35" trace-index="35" trace-nid="567412509044" trace-num="44" trace-price="2318.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_567412509044" class="J_ItemPic img" data-src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/263726286/TB2H3XMG1uSBuNjSsplXXbe8pXa_!!263726286-0-item_pic.jpg" alt="12期分期/送壳膜支架/现货速发Apple/苹果 iPad 2018款 9.7英寸wifi新款平板电脑能良官方旗舰店 正品国行" src="//g-search2.alicdn.com/img/bao/uploaded/i4/i1/263726286/TB2H3XMG1uSBuNjSsplXXbe8pXa_!!263726286-0-item_pic.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=567412509044">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=567412509044" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2318.00</strong>
      </div>
      <div class="deal-cnt">267人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_567412509044" class="J_ClickStat" data-nid="567412509044" href="//detail.tmall.com/item.htm?id=567412509044&amp;ns=1&amp;abbucket=4" target="_blank" trace="msrp_auction" traceidx="35" trace-index="35" trace-nid="567412509044" trace-num="44" trace-price="2318.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          12期分期/送壳膜支架/现货速发Apple/苹果 <span class="H">iPad</span> 2018款 9.7英寸wifi新款平板电脑能良官方旗舰店 正品国行
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="263726286" data-nid="567412509044" href="//store.taobao.com/shop/view_shop.htm?user_number_id=263726286" target="_blank">
        <span class="dsrs">
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
                <span class="dsr lessthan"></span>
            </span>
        <span>能良数码官方旗舰店</span>
      </a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_567412509044">
        <ul class="icons">
        
                <li class="icon " data-index="0">
                                    <a href="//www.tmall.com/" target="_blank" title="尚天猫，就购了" trace="srpservice" traceidx="59"><span class="icon-service-tianmao"></span></a>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="能良数码官方旗舰店" data-display="inline" data-item="567412509044" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E8%83%BD%E8%89%AF%E6%95%B0%E7%A0%81%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="36">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_573483807081" class="pic-link J_ClickStat J_ItemPicA" data-nid="573483807081" data-recommend-nav="" href="//item.taobao.com/item.htm?id=573483807081&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=573483807081&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="36" trace-index="36" trace-nid="573483807081" trace-num="44" trace-price="1280.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_573483807081" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/1037322546/TB2MkQyDkyWBuNjy0FpXXassXXa_!!1037322546.jpg" alt="Apple/苹果ipad mini 3平板电脑7.9英寸wifi迷你3插卡64g分期免息" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/1037322546/TB2MkQyDkyWBuNjy0FpXXassXXa_!!1037322546.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=573483807081">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=573483807081" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1280.00</strong>
      </div>
      <div class="deal-cnt">222人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_573483807081" class="J_ClickStat" data-nid="573483807081" href="//item.taobao.com/item.htm?id=573483807081&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="36" trace-index="36" trace-nid="573483807081" trace-num="44" trace-price="1280.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果<span class="H">ipad</span> mini 3平板电脑7.9英寸wifi迷你3插卡64g分期免息
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1037322546" data-nid="573483807081" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1037322546" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>美足8689</span>
      </a>
    
  


        </div>
        <div class="location">广东 东莞</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_573483807081">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="美足8689" data-display="inline" data-item="573483807081" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%BE%8E%E8%B6%B38689&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="37">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_566956582094" class="pic-link J_ClickStat J_ItemPicA" data-nid="566956582094" data-recommend-nav="" href="//item.taobao.com/item.htm?id=566956582094&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=566956582094&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="37" trace-index="37" trace-nid="566956582094" trace-num="44" trace-price="3300.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_566956582094" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/272364127/TB2EeXeh1GSBuNjSspbXXciipXa_!!272364127.jpg" alt="Apple/苹果 iPad 2018款 9.7寸 支持Apple Pencil~" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i4/272364127/TB2EeXeh1GSBuNjSspbXXciipXa_!!272364127.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=566956582094">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=566956582094" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3300.00</strong>
      </div>
      <div class="deal-cnt">71人付款</div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_566956582094" class="J_ClickStat" data-nid="566956582094" href="//item.taobao.com/item.htm?id=566956582094&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="37" trace-index="37" trace-nid="566956582094" trace-num="44" trace-price="3300.00" trace-pid="">
          Apple/苹果 <span class="H">iPad</span> 2018款 9.7寸 支持Apple Pencil~
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="272364127" data-nid="566956582094" href="//store.taobao.com/shop/view_shop.htm?user_number_id=272364127" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>安琪糖糖</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_566956582094">
        <ul class="icons">
        
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="安琪糖糖" data-display="inline" data-item="566956582094" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%AE%89%E7%90%AA%E7%B3%96%E7%B3%96&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="38">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_545277998267" class="pic-link J_ClickStat J_ItemPicA" data-nid="545277998267" data-recommend-nav="" href="//item.taobao.com/item.htm?id=545277998267&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=545277998267&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="38" trace-index="38" trace-nid="545277998267" trace-num="44" trace-price="1199.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_545277998267" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/73773056/TB2.L7.b8cXBuNjt_biXXXpmpXa_!!73773056.png" alt="Apple苹果 iPad4 四代 4代 WIFI 4G 版 平板电脑 包邮 保修半年" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i3/73773056/TB2.L7.b8cXBuNjt_biXXXpmpXa_!!73773056.png_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=545277998267">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=545277998267" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>1199.00</strong>
      </div>
      <div class="deal-cnt">98人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_545277998267" class="J_ClickStat" data-nid="545277998267" href="//item.taobao.com/item.htm?id=545277998267&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="38" trace-index="38" trace-nid="545277998267" trace-num="44" trace-price="1199.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple苹果 <span class="H">iPad</span>4 四代 4代 WIFI 4G 版 平板电脑 包邮 保修半年
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="73773056" data-nid="545277998267" href="//store.taobao.com/shop/view_shop.htm?user_number_id=73773056" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>碧空剑</span>
      </a>
    
  


        </div>
        <div class="location">辽宁 沈阳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_545277998267">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="碧空剑" data-display="inline" data-item="545277998267" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E7%A2%A7%E7%A9%BA%E5%89%91&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="39">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_554035015014" class="pic-link J_ClickStat J_ItemPicA" data-nid="554035015014" data-recommend-nav="" href="//item.taobao.com/item.htm?id=554035015014&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=554035015014&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="39" trace-index="39" trace-nid="554035015014" trace-num="44" trace-price="4279.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_554035015014" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/3006130747/TB2I6UnDVOWBuNjy0FiXXXFxVXa_!!3006130747.jpg" alt="Apple/苹果 iPad Pro 10.5寸 12.9寸二代 2017 2018新款 美版日版" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/3006130747/TB2I6UnDVOWBuNjy0FiXXXFxVXa_!!3006130747.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=554035015014">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=554035015014" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>4279.00</strong>
      </div>
      <div class="deal-cnt">31人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_554035015014" class="J_ClickStat" data-nid="554035015014" href="//item.taobao.com/item.htm?id=554035015014&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="39" trace-index="39" trace-nid="554035015014" trace-num="44" trace-price="4279.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> Pro 10.5寸 12.9寸二代 2017 2018新款 美版日版
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="3006130747" data-nid="554035015014" href="//store.taobao.com/shop/view_shop.htm?user_number_id=3006130747" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>一帆数码2013</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_554035015014">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="一帆数码2013" data-display="inline" data-item="554035015014" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E4%B8%80%E5%B8%86%E6%95%B0%E7%A0%812013&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="40">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_552464035326" class="pic-link J_ClickStat J_ItemPicA" data-nid="552464035326" data-recommend-nav="" href="//item.taobao.com/item.htm?id=552464035326&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=552464035326&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="40" trace-index="40" trace-nid="552464035326" trace-num="44" trace-price="2799.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_552464035326" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1069744797/TB2Qp6yquuSBuNjSsplXXbe8pXa_!!1069744797.jpg" alt="Apple/苹果 新款iPad Pro 12.9寸10.5寸 ipadpro12.9二代平板电脑" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i2/1069744797/TB2Qp6yquuSBuNjSsplXXbe8pXa_!!1069744797.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=552464035326">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=552464035326" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2799.00</strong>
      </div>
      <div class="deal-cnt">55人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_552464035326" class="J_ClickStat" data-nid="552464035326" href="//item.taobao.com/item.htm?id=552464035326&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="40" trace-index="40" trace-nid="552464035326" trace-num="44" trace-price="2799.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 新款<span class="H">iPad</span> Pro 12.9寸10.5寸 <span class="H">ipad</span>pro12.9二代平板电脑
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="1069744797" data-nid="552464035326" href="//store.taobao.com/shop/view_shop.htm?user_number_id=1069744797" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>波波逛街99</span>
      </a>
    
  


        </div>
        <div class="location">广东 广州</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_552464035326">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="波波逛街99" data-display="inline" data-item="552464035326" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E6%B3%A2%E6%B3%A2%E9%80%9B%E8%A1%9799&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="41">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_531392316105" class="pic-link J_ClickStat J_ItemPicA" data-nid="531392316105" data-recommend-nav="" href="//item.taobao.com/item.htm?id=531392316105&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=531392316105&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="41" trace-index="41" trace-nid="531392316105" trace-num="44" trace-price="2178.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_531392316105" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/100340983/TB2fN0gl8yWBuNkSmFPXXXguVXa_!!100340983.jpg" alt="Apple/苹果 iPad mini4 wifi 7.9英寸 平板电脑 苹果迷你4代 全新" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i3/100340983/TB2fN0gl8yWBuNkSmFPXXXguVXa_!!100340983.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=531392316105">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=531392316105" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2178.00</strong>
      </div>
      <div class="deal-cnt">45人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_531392316105" class="J_ClickStat" data-nid="531392316105" href="//item.taobao.com/item.htm?id=531392316105&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="41" trace-index="41" trace-nid="531392316105" trace-num="44" trace-price="2178.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> mini4 wifi 7.9英寸 平板电脑 苹果迷你4代 全新
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="100340983" data-nid="531392316105" href="//store.taobao.com/shop/view_shop.htm?user_number_id=100340983" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>领域数码通讯</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_531392316105">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-fuwu"></span>
                              </li>
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="1">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="2">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="领域数码通讯" data-display="inline" data-item="531392316105" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E9%A2%86%E5%9F%9F%E6%95%B0%E7%A0%81%E9%80%9A%E8%AE%AF&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="42">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_562602390914" class="pic-link J_ClickStat J_ItemPicA" data-nid="562602390914" data-recommend-nav="" href="//item.taobao.com/item.htm?id=562602390914&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=562602390914&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="42" trace-index="42" trace-nid="562602390914" trace-num="44" trace-price="3245.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_562602390914" class="J_ItemPic img" data-src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/127187360/TB2DKFfcGLN8KJjSZFKXXb7NVXa_!!127187360.png" alt="Apple/苹果 iPad pro 大屏苹果12.9寸平板电脑 ipadpro wifi 4G美" src="//g-search3.alicdn.com/img/bao/uploaded/i4/i2/127187360/TB2DKFfcGLN8KJjSZFKXXb7NVXa_!!127187360.png_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=562602390914">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=562602390914" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>3245.00</strong>
      </div>
      <div class="deal-cnt">31人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_562602390914" class="J_ClickStat" data-nid="562602390914" href="//item.taobao.com/item.htm?id=562602390914&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="42" trace-index="42" trace-nid="562602390914" trace-num="44" trace-price="3245.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple/苹果 <span class="H">iPad</span> pro 大屏苹果12.9寸平板电脑 <span class="H">ipad</span>pro wifi 4G美
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="127187360" data-nid="562602390914" href="//store.taobao.com/shop/view_shop.htm?user_number_id=127187360" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>每天多赚一块钱</span>
      </a>
    
  


        </div>
        <div class="location">上海</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_562602390914">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="每天多赚一块钱" data-display="inline" data-item="562602390914" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E6%AF%8F%E5%A4%A9%E5%A4%9A%E8%B5%9A%E4%B8%80%E5%9D%97%E9%92%B1&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

        
<div class="item J_MouserOnverReq  " data-category="auctions" data-index="43">
  <div class="pic-box J_MouseEneterLeave J_PicBox">
    <div class="pic-box-inner">
      <div class="pic">
        <a id="J_Itemlist_PLink_566900056921" class="pic-link J_ClickStat J_ItemPicA" data-nid="566900056921" data-recommend-nav="" href="//item.taobao.com/item.htm?id=566900056921&amp;ns=1&amp;abbucket=4#detail" data-href="//item.taobao.com/item.htm?id=566900056921&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="43" trace-index="43" trace-nid="566900056921" trace-num="44" trace-price="2150.00" trace-recommend-nav="" trace-risk="" trace-pid="">
                <img id="J_Itemlist_Pic_566900056921" class="J_ItemPic img" data-src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/677955778/TB2x2qecRjTBKNjSZFDXXbVgVXa_!!677955778.jpg" alt="Apple苹果 iPad Pro 一代 9.7寸 12.9寸平板电脑 Wi-Fi 4G 插卡版" src="//g-search1.alicdn.com/img/bao/uploaded/i4/i1/677955778/TB2x2qecRjTBKNjSZFDXXbVgVXa_!!677955778.jpg_230x230.jpg_.webp">
            </a>
      </div>

    <div class="similars">
    <a class="btn disabled" target="_blank">
        <s class="shim"></s>
        <s class="bar"></s>
        <span class="text">找同款</span>
    </a>

    <a class="btn " target="_blank" href="/search?type=similar&amp;app=i2i&amp;rec_type=1&amp;uniqpid=&amp;nid=566900056921">
        <s class="shim"></s>
        <span class="text">找相似</span>
    </a>
  </div>




      <div class="report">
        <a href="//jubao.taobao.com/index.htm?itemId=566900056921" target="_blank" title="举报该宝贝">
          <span class="icon-btn-report"></span>
        </a>
      </div>

    </div>

    
  </div>
  

  <div class="ctx-box J_MouseEneterLeave J_IconMoreNew">

    <div class="row row-1 g-clearfix">
    
      <div class="price g_price g_price-highlight">
        <span>¥</span><strong>2150.00</strong>
      </div>
      <div class="deal-cnt">33人付款</div>
        <div class="ship icon-service-free"></div>
    
    </div>

    <div class="row row-2 title">
      <a id="J_Itemlist_TLink_566900056921" class="J_ClickStat" data-nid="566900056921" href="//item.taobao.com/item.htm?id=566900056921&amp;ns=1&amp;abbucket=4#detail" target="_blank" trace="msrp_auction" traceidx="43" trace-index="43" trace-nid="566900056921" trace-num="44" trace-price="2150.00" trace-pid="">
          <span class="baoyou-intitle icon-service-free"></span>
          Apple苹果 <span class="H">iPad</span> Pro 一代 9.7寸 12.9寸平板电脑 Wi-Fi 4G 插卡版
      </a>
    </div>

    
      <div class="row row-3 g-clearfix">
        <div class="shop">
    
  
    
      <a class="shopname J_MouseEneterLeave J_ShopInfo" data-userid="677955778" data-nid="566900056921" href="//store.taobao.com/shop/view_shop.htm?user_number_id=677955778" target="_blank">
        <span class="dsrs">
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
                <span class="dsr morethan"></span>
            </span>
        <span>司狼通讯</span>
      </a>
    
  


        </div>
        <div class="location">广东 深圳</div>
      </div>
    

    <div class="row row-4 g-clearfix">
      <div class="feature-icons icon-has-more" id="J_Itemlist_Icons_566900056921">
        <ul class="icons">
        
                <li class="icon J_IconPopup J_MouseEneterLeave" data-index="0">
                                    <span class="icon-service-baoxian"></span>
                              </li>
                <li class="icon " data-index="1">
                                    <span class="icon-fest-gongyibaobei" title="公益宝贝"></span>
                              </li>
            </ul>
      </div>

        <div class="wangwang">
          <span class="ww-light ww-small" data-nick="司狼通讯" data-display="inline" data-item="566900056921" data-icon="small" data-encode="true"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%8F%B8%E7%8B%BC%E9%80%9A%E8%AE%AF&amp;site=cntaobao&amp;fromid=cntaobao" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
        </div>
    </div>

  </div>

  
</div>

      </div>

    

    <div class="items" id="J_itemlistCont">

    </div>
  </div>
</div>
</div>
"""
# 直接返回所有匹配的元素（html格式） 还会自动补全
doc = pq(html)  # 可以传入网址以及本地文件

lls = doc('#mainsrp-itemlist .items .item').items()
for item in lls:
    ll = {
        'price': item.find('.price').text(),
    }
    print(ll)


# # print(doc('li'))
# # print(type(doc('li')) )
# # 本地文件 filename
# # doc = pq(filename='test.html')
# # print(doc('li'))
# # 网址 url
# # doc = pq(url='http://www.baidu.com')
# # print(doc('div'))
# # 父节点 祖先节点 子节点 子孙节点
# li = doc(".item-01")
# # container = li.parent()
# # print(container)
# # container = li.parents()
# # print(container)
# # container = li.children()
# # print(container)
# container = li.find('a')  # 必须传参
# print(container)
# # 兄弟节点
# sib = li.siblings()
# print(sib)
# # 遍历items()
# for lis in sib.items():
#     print(lis)
# # 属性attr 只返回第一个匹配的 文本text()
# print(li.children('a').attr('href'))
# print(li.text())
# print('\n')
# # 修改class属性 可以多个对象操作
# li.add_class('added')
# print(li)
# li.remove_class('added')
# print(li)
# # attr text html
# li.children('a').attr('href', 'www.baidu.com')  # 一个参数是获取 两个参数是赋值
# print(li)
# li.text("哈哈")
# print(li)
# li.html("hehe")
# print(li)
# # remove()移除元素
# print('\n')
# # doc.find('li').remove()
# # print(doc)
# # 伪类选择器 跟css一样
# print(doc.find('li:first-child'))
