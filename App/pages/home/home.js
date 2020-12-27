const app = getApp();

Page({
  data: {
    action1: 'Create Batch',
    action2: 'Batchs Created',
    action3: 'Upload',
    time: app.globalData.now
  },
  buttonHandler3(event) {
    const that = this;
    wx.showModal({
      title: "Upload",
      content: 'Do you wanna upload?',
      cancelColor: 'cancelColor',
      success (res) {
        if (res.confirm) {
          that.setData({
            action3: 'Uploaded'
          }, function () {
            wx.showToast({
              title: 'Upload Succeed',
              duration: 700
            });
          });
        } else if (res.cancel) {
          console.log('Uploaded canceled');
        }
      }
    });
  }
});