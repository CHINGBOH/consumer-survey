const typeData = {
  impulsive: {
    icon: '💰',
    name: '冲动消费型',
    risk: '⭐⭐⭐⭐⭐ 高风险',
    desc: '看到优惠就心动，办完卡就后悔的"月光女孩"',
    tips: [
      '永远不要当天办卡，给自己3天冷静期',
      '不要被"打折力度"迷惑，先查市场价',
      '拒绝"不做疗程没效果"的说法',
      '警惕"你的皮肤问题很严重"',
      '不要办超过1年的长期卡'
    ]
  },
  rational: {
    icon: '🌸',
    name: '理性护肤型',
    risk: '⭐ 低风险',
    desc: '做足功课再下单，会比价会看成分的"精明消费者"',
    tips: [
      '不要过度谨慎，错过好项目',
      '警惕"性价比陷阱"，便宜不一定好',
      '建立自己的"白名单"店家',
      '学会"适度妥协"，80分就可以行动',
      '关注"长期价值"而非"单次价格"'
    ]
  },
  scientific: {
    icon: '🔬',
    name: '科学美容型',
    risk: '⭐⭐ 中低风险',
    desc: '追求效果、懂原理、愿意尝试新技术的"成分党"',
    tips: [
      '警惕"成分迷信"，成分好≠产品好',
      '不要过度叠加猛药',
      '警惕"技术崇拜"，新技术不一定更好',
      '不要忽视"皮肤屏障"',
      '警惕"速效陷阱"'
    ]
  },
  result: {
    icon: '🎯',
    name: '效果至上型',
    risk: '⭐⭐⭐⭐ 中高风险',
    desc: '想快速见效、愿意冒险、预算充足的"效果主义者"',
    tips: [
      '警惕"速效"承诺，7天美白99%是激素',
      '不要叠加多个猛项目',
      '警惕"独家技术"',
      '不要忽视术后护理',
      '一定要去正规机构'
    ]
  },
  newbie: {
    icon: '👶',
    name: '美容小白型',
    risk: '⭐⭐⭐ 中风险',
    desc: '刚入门、缺乏经验、容易被忽悠的"美容新手"',
    tips: [
      '先学基础知识再花钱',
      '不要相信美容师的"专业诊断"',
      '从基础项目开始',
      '不要办卡！不要办卡！不要办卡！',
      '警惕"深层清洁"推销'
    ]
  }
}

Page({
  data: {
    typeInfo: {}
  },

  onLoad(options) {
    const type = options.type || 'rational'
    this.setData({
      typeInfo: typeData[type]
    })
  },

  restart() {
    wx.reLaunch({
      url: '/pages/index/index'
    })
  },

  share() {
    wx.showShareMenu({
      withShareTicket: true,
      menus: ['shareAppMessage', 'shareTimeline']
    })
  },

  onShareAppMessage() {
    return {
      title: '我是' + this.data.typeInfo.name + '，测测你是哪种类型？',
      path: '/pages/index/index'
    }
  }
})
