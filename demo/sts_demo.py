#!/usr/bin/env python
# coding=utf-8
import json
import os

from sts.sts import Sts


#if __name__ == '__main__':
def getKey():
    config = {
        # 临时密钥有效时长，单位是秒
        'duration_seconds': 1800,
        'secret_id': os.environ['COS_SECRET_ID'],
        # 固定密钥
        'secret_key': os.environ['COS_SECRET_KEY'],
        # 设置网络代理
        # 'proxy': {
        #     'http': 'xx',
        #     'https': 'xx'
        # },
        # 换成你的 bucket
        'bucket': 'petbaby-1302683643',
        # 换成 bucket 所在地区
        'region': 'ap-beijing',
        # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
        # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
        'allow_prefix': 'exampleobject',
        # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
        'allow_actions': [
            # 简单上传
            'name/cos:PutObject',
            'name/cos:PostObject',
            # 分片上传
            'name/cos:InitiateMultipartUpload',
            'name/cos:ListMultipartUploads',
            'name/cos:ListParts',
            'name/cos:UploadPart',
            'name/cos:CompleteMultipartUpload'
        ],

    }


    sts = Sts(config)
    response = sts.get_credential()
    #print('get data : ' + json.dumps(dict(response), indent=4))
    return(response)
