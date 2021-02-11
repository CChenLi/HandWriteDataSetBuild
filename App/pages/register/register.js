const app = getApp();

Page({
  data: {
  showTopTips: false,
   
  radioItems: [
  { name: '学生', value: '1', checked: true },
  { name: '导师', value: '0' }
  ],
  checkboxItems: [
  { name: '美本', value: '0', checked: true },
  { name: '美妍', value: '1' },
  { name: '加本', value: '2' },
  { name: '加妍', value: '3' },
  { name: '澳本', value: '4' },
  { name: '澳妍', value: '5' }
  ],
   
  date: "2021-01-01",
  time: "00:00",
   
  countryCodes: ["+86", "+80", "+84", "+87"],
  countryCodeIndex: 0,
   
  countries: ["中国", "美国", "英国"],
  countryIndex: 0,
   
  accounts: ["WeChat", "QQ", "Email"],
  accountIndex: 0,
   
  isAgree: false
  },
  showTopTips: function () {
  var that = this;
  this.setData({
  showTopTips: true
  });
  setTimeout(function () {
  that.setData({
  showTopTips: false
  });
  }, 3000);
  },
  radioChange: function (e) {
  console.log('radio发生change事件，携带value值为：', e.detail.value);
   
  var radioItems = this.data.radioItems;
  for (var i = 0, len = radioItems.length; i < len; ++i) {
  radioItems[i].checked = radioItems[i].value == e.detail.value;
  }
   
  this.setData({
  radioItems: radioItems
  });
  },
  checkboxChange: function (e) {
  console.log('checkbox发生change事件，携带value值为：', e.detail.value);
   
  var checkboxItems = this.data.checkboxItems, values = e.detail.value;
  for (var i = 0, lenI = checkboxItems.length; i < lenI; ++i) {
  checkboxItems[i].checked = false;
   
  for (var j = 0, lenJ = values.length; j < lenJ; ++j) {
  if (checkboxItems[i].value == values[j]) {
  checkboxItems[i].checked = true;
  break;
  }
  }
  }
   
  this.setData({
  checkboxItems: checkboxItems
  });
  },
  bindDateChange: function (e) {
  this.setData({
  date: e.detail.value
  })
  },
  bindTimeChange: function (e) {
  this.setData({
  time: e.detail.value
  })
  },
  bindCountryCodeChange: function (e) {
  console.log('picker country code 发生选择改变，携带值为', e.detail.value);
   
  this.setData({
  countryCodeIndex: e.detail.value
  })
  },
  bindCountryChange: function (e) {
  console.log('picker country 发生选择改变，携带值为', e.detail.value);
   
  this.setData({
  countryIndex: e.detail.value
  })
  },
  bindAccountChange: function (e) {
  console.log('picker account 发生选择改变，携带值为', e.detail.value);
   
  this.setData({
  accountIndex: e.detail.value
  })
  },
  bindAgreeChange: function (e) {
  this.setData({
  isAgree: !!e.detail.value.length
  });
  }
  });