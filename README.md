# Nosie Mask Detection

# Download data via

Copy and paste code in terminal to download dataset 

curl 'https://storage.googleapis.com/kaggle-data-sets/778086/1339204/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220218%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220218T153921Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=8011b4924121a60ba97ad7f295d636dc64708ee0c90deb495efd31f778326f37e19cfdad82ff3301e89c675950820710676b964f2ece9d30d3090d39f3ed1fcfdc0289f67f2c7d55c6354e46c604f375ebc75d964eacca310cb261a900c04cf63a200c91cc2876b9f1fe6371dab870c0b9ce6e5474ac74a9ae99d14536145609b2debed9f629247f99b065d49396936d7abbc2fcecf82ee7e856ec1d0ba48e75231b3461a4c0c28a4529025939b79c57789bcc06008b886a568affad8601094805e6c717abdc139b152b7a1d05c60f598ae2466cfecd023f270536264ac6cf7720be0356c8e58f05436b28b2542bc2c78d428938ef9fbd2824c1d33a55abda5a' \
  -H 'authority: storage.googleapis.com' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-ch-ua: "Opera";v="83", "Chromium";v="97", ";Not A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'referer: https://www.kaggle.com/' \
  -H 'accept-language: en-US,en;q=0.9' \
  --compressed -o data.zip
  
  After successfully downloading dataset we can now unzip and extract by using unzip data.zip
  
