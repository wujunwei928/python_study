#encoding=utf-8
# 如果上面不指定utf-8编码, 默认是ASCII编码, 下面分词会报错

import jieba

# 类别占比
leibie_zhanbi = {
	"质量" : 0.3686868687,
	"配送及时" : 0.1060606061,
	"配送及时,质量" : 0.0429292929,
	"不满意" : 0.0378787879,
	"售后处理客服态度专业性" : 0.0353535354,
	"质量,售后处理客服态度专业性" : 0.0277777778,
	"质量,退换货环节" : 0.0252525253,
	"包装" : 0.0202020202,
	"未按照指定要求送达" : 0.0176767677,
	"质量,配送及时" : 0.0176767677,
	"配送及时,售后处理客服态度专业性" : 0.0176767677,
	"价格" : 0.0151515152,
	"发票" : 0.0126262626,
	"质量,包装" : 0.0101010101,
	"包装,质量" : 0.0101010101,
	"配送及时,售后响应速度" : 0.0101010101,
	"赠品" : 0.0101010101,
	"配送及时,包装" : 0.0101010101,
	"退换货环节" : 0.0101010101,
	"质量,价格" : 0.0075757576,
	"质量,售后响应速度" : 0.0075757576,
	"质量,退换货环节,售后处理客服态度专业性" : 0.0075757576,
	"配送及时,未按照指定要求送达" : 0.0075757576,
	"安装及时性" : 0.0050505051,
	"赠品,质量" : 0.0050505051,
	"发票,售后处理客服态度专业性" : 0.0050505051,
	"安装费用,安装及时性" : 0.0050505051,
	"配送人员态度" : 0.0050505051,
	"配送及时,发票" : 0.0050505051,
	"未按照指定要求送达,质量" : 0.0050505051,
	"配送及时,配送人员态度" : 0.0050505051,
	"赠品,售后响应速度" : 0.0050505051,
	"包装,退换货环节" : 0.0050505051,
	"发票,售后响应速度" : 0.0050505051,
	"安装费用" : 0.0050505051,
	"售后响应速度" : 0.0050505051,
	"质量,配送及时,售后响应速度" : 0.0025252525,
	"配送及时,价格" : 0.0025252525,
	"赠品,配送及时" : 0.0025252525,
	"配送及时,安装专业性态度,售后响应速度" : 0.0025252525,
	"质量,发票,退换货环节" : 0.0025252525,
	"配送及时,赠品" : 0.0025252525,
	"配送及时,售后处理客服态度专业性,退换货环节,质量" : 0.0025252525,
	"包装,未按照指定要求送达" : 0.0025252525,
	"赠品,退换货环节" : 0.0025252525,
	"配送及时,质量,退换货环节" : 0.0025252525,
	"质量,包装,退换货环节" : 0.0025252525,
	"配送及时,质量,退换货环节,售后响应速度" : 0.0025252525,
	"价格,发票" : 0.0025252525,
	"配送及时,配送人员态度,售后处理客服态度专业性" : 0.0025252525,
	"质量,未按照指定要求送达" : 0.0025252525,
	"包装,价格,配送及时" : 0.0025252525,
	"包装,售后响应速度" : 0.0025252525,
	"售后处理客服态度专业性,未按照指定要求送达" : 0.0025252525,
	"配送及时,售后响应速度,发票" : 0.0025252525,
	"价格,配送及时,售后处理客服态度专业性" : 0.0025252525,
	"配送及时,售后响应速度,售后处理客服态度专业性" : 0.0025252525,
	"价格,未按照指定要求送达" : 0.0025252525,
	"发票,退换货环节" : 0.0025252525,
	"安装专业性态度,售后处理客服态度专业性,质量" : 0.0025252525,
	"质量,发票" : 0.0025252525,
	"退换货环节,质量" : 0.0025252525,
	"安装专业性态度,售后处理客服态度专业性,价格" : 0.0025252525,
	"未按照指定付款方式付款" : 0.0025252525,
	"质量,配送及时,售后处理客服态度专业性" : 0.0025252525,
	"安装专业性态度,安装费用" : 0.0025252525,
	"价格,配送及时,发票" : 0.0025252525,
	"未按照指定要求送达,配送人员态度" : 0.0025252525,
	"未按照指定要求送达,售后处理客服态度专业性" : 0.0025252525,
	"质量,退换货环节," : 0.0025252525,
	"售后响应速度,安装及时" : 0.0025252525,
	"安装专业性态度" : 0.0025252525,
	"质量,赠品" : 0.0025252525,
	"配送及时,未按照指定要求送达,配送人员态度" : 0.0025252525,
	"配送及时,未按照指定要求送达,售后处理客服态度专业性" : 0.0025252525,
};


# 词库
ciku_fp = open("ciku.txt", "r");
ciku = {}
for line in ciku_fp:
	lineArr = line.strip().split("=")
	ciku[lineArr[0]] = lineArr[1]


# 质量词占比
zhiliang_fp = open("zhiliangci_zhanbi.txt", "r")
zhiliang = {}
for line in zhiliang_fp:
	lineArr = line.strip().split("=")
	zhiliang[ lineArr[0] ] = lineArr[1]


# 归类词 在质量中的占比
# ①: 读取文件获取分词
gui_lei_ci = open("gui_lei_ci.txt", "r");
gailv_1 = 1;
for line in gui_lei_ci:
	ciyu = line.strip()
	if zhiliang.has_key(ciyu):
		# python比php严格, 如果不转成float 报错: can't multiply sequence by non-int of type 'float'
		gailv_1 *= float(zhiliang[ciyu])
		# print type(zhiliang[ciyu])   # <type 'str'>
print gailv_1

# ②: 结巴分词直接获取分词
seg_list = jieba.cut("将近20天没收到货,电话打了好几家的,这几次都是给各种电话,如寄件人,公司电话,尾号1911,问了半天用不再公司来回复我,不是客服负责处理快件送不到的问题吗,就是这么蒙混吗", cut_all=False)	# 精确模式
gailv_2 = 1
for ciyu in seg_list:
	if zhiliang.has_key(ciyu):
		gailv_2 *= float(zhiliang[ciyu])
print gailv_2

# ③: 读取多条评论获取分词
pinglun_fp = open('pinglun.txt', 'r')
for line in pinglun_fp:
	pinglun = line.strip()
	gailv_3 = 1
	seg_list = jieba.cut(pinglun)
	for ciyu in seg_list:
		if zhiliang.has_key(ciyu):
			gailv_3 *= float(zhiliang[ciyu])
	print gailv_3