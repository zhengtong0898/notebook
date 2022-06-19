### 记录对OpenAPI的理解
- **OpenAPI是一个规范**  
  > OpenAPI提出了一组关键字, 用于描述`Restfull API`的各接口作用.      
  > 与`github actions`工作流文件一样, 都是由属于描述性文件.  

- **OpenAPI描述文件的作用**
  > `swagger-ui` 可以通过 `openapi` 描述文件生成一个可视化(WEB)的接口清单, 并支持`execute`快速向接口提交数据、获取数据.   
  > `Postman` 可以通过 `openapi` 描述文件将所有接口清单导入 `Postman`, 然后就可以快乐的进行接口测试了.   
  > `测开` 可以通过 `openapi` 描述文件将所有接口提取出来, 快速组织起来沉淀到自动化测试用例集中.  

- **OpenAPI是如何自动生成的**  
  > 在 `Django Rest Framework` 里面, `drf-yasg`是一个库专门用来生成`Swagger/OpenAPI 2.0`接口清单,   
  > `drf-yasg` 从 `路由(urlpatterns)` 中提取所有接口以及类型(GET、POST、PUT、PATCH、DELETE等),   
  > `drf-yasg` 从 `序列化(serializers)` 中提取接口`request parameters`和`response struct`.
  > `drf-yasg` 从 `模型(models)` 中提取每个字段的约束(最大长度、必填、字符串、复杂度等).  
  > `drf-yasg` 从 `验证(Valications)` 中验证模型的约束.  
  > 所以, 这就是`def-yasg`生成`openapi`的依据.  


### 参考资料
- [x] [OpenAPI官网介绍](https://oai.github.io/Documentation/start-here.html)
- [x] [Swagger官网对OpenAPI3.0的介绍](https://swagger.io/specification/)
- [x] [B站视频介绍OpenAPI2.0的介绍](https://www.bilibili.com/video/BV1iV411e7hx)
- [x] [OpenAPI2.0和OpenAPI3.0的区别](https://blog.stoplight.io/difference-between-open-v2-v3-v31)  
- [x] [drf-yasg: Swagger generator(OpenAPI2.0): Django-rest-framework](https://drf-yasg.readthedocs.io/en/stable/readme.html)
- [x] [B站drf-yasg安装教程](https://www.bilibili.com/video/BV1VQ4y1v7Ug)
- [x] [drf-spectacular: OpenAPI3.0 generator: Django-rest-framework](https://drf-spectacular.readthedocs.io/en/latest/)
- [x] [API Mock Servers and Contract Testing](https://github.com/stoplightio/prism)  
- [ ] openapi如何启动mock服务?  
