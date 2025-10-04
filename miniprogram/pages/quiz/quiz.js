const app = getApp()

const questions = [
  {q:"你的年龄段？",t:"💡 不同年龄段的皮肤需求差异很大",o:["18-22岁（学生党/职场新人）","23-28岁（职场打拼中）","29-35岁（轻熟女）","36岁以上"],s:[{newbie:1},{rational:1},{scientific:1},{result:1}]},
  {q:"你遇到过以下哪些"坑"？",t:"🚨 这些都是常见套路",o:["被推销办大额年卡/疗程卡","效果远不如承诺的好","做完皮肤反而变差","还好，没遇到过"],s:[{impulsive:3},{result:2},{scientific:2},{rational:3}]},
  {q:"当美容师说"你的皮肤需要深层清洁"时，你会？",t:"💡 正常皮肤1-2周做一次就够了",o:["立刻答应，听专业的","问清楚为什么需要，怎么做","拒绝，觉得是推销","回家查资料再决定"],s:[{newbie:3},{rational:3},{scientific:2},{rational:2}]},
  {q:"看到"限时优惠，今天办卡立减3000元"，你会？",t:"🎭 "限时优惠"永远都有",o:["心动！立刻办（怕错过优惠）","先体验一次，满意再说","回家考虑几天","直接拒绝（肯定是套路）"],s:[{impulsive:5},{rational:3},{rational:2},{scientific:2}]},
  {q:"你对美容知识的了解程度？",t:"📚 知识是最好的避坑武器",o:["完全小白（不懂成分、不懂项目）","略懂一点（知道基础概念）","比较了解（会看成分表，懂原理）","很专业（能分辨真假，知道避坑）"],s:[{newbie:5},{impulsive:2,newbie:2},{scientific:4},{rational:4}]},
  {q:"你最想改善的皮肤问题是？",t:"💡 对症下药很重要",o:["痘痘/粉刺/闭口","暗沉/肤色不均","细纹/松弛/抗衰","敏感/泛红"],s:[{newbie:1},{rational:1},{result:2},{scientific:1}]},
  {q:"你更看重？",t:"⚠️ 承诺"一次见效"的项目要谨慎",o:["快速见效（哪怕有一定风险）","温和安全（慢慢改善也没关系）","性价比（效果和价格都要考虑）","科学有效（相信数据和原理）"],s:[{result:5},{rational:3},{rational:2},{scientific:3}]},
  {q:"你会为了优惠办理年卡/疗程卡吗？",t:"💡 办卡前一定要签合同，问清退款条款",o:["会，算下来很划算","不会，怕店家跑路","看情况，信得过的店才办","只办小额的（3000元以内）"],s:[{impulsive:4},{rational:3},{rational:2},{scientific:1}]}
]

Page({
  data: {
    currentIndex: 0,
    currentQuestion: questions[0],
    selectedOption: null,
    answers: [],
    progress: 12.5
  },

  onLoad() {
    this.scores = {impulsive:0, rational:0, scientific:0, result:0, newbie:0}
  },

  onSelectOption(e) {
    this.setData({
      selectedOption: parseInt(e.detail.value)
    })
  },

  prevQuestion() {
    if (this.data.currentIndex > 0) {
      const newIndex = this.data.currentIndex - 1
      const answers = this.data.answers
      this.setData({
        currentIndex: newIndex,
        currentQuestion: questions[newIndex],
        selectedOption: answers[newIndex] !== undefined ? answers[newIndex] : null,
        progress: (newIndex + 1) / 8 * 100
      })
    }
  },

  nextQuestion() {
    if (this.data.selectedOption === null) return

    // 记录答案和分数
    const answers = this.data.answers
    answers[this.data.currentIndex] = this.data.selectedOption
    
    const score = questions[this.data.currentIndex].s[this.data.selectedOption]
    for (let k in score) {
      this.scores[k] += score[k]
    }

    if (this.data.currentIndex < 7) {
      const newIndex = this.data.currentIndex + 1
      this.setData({
        currentIndex: newIndex,
        currentQuestion: questions[newIndex],
        selectedOption: answers[newIndex] !== undefined ? answers[newIndex] : null,
        answers: answers,
        progress: (newIndex + 1) / 8 * 100
      })
    } else {
      // 计算结果
      let max = 0
      let type = 'rational'
      for (let k in this.scores) {
        if (this.scores[k] > max) {
          max = this.scores[k]
          type = k
        }
      }
      
      app.globalData.userType = type
      wx.redirectTo({
        url: '/pages/result/result?type=' + type
      })
    }
  }
})
