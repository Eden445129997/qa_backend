"""
ForeignKey
    on_delete(外键)
        CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
        PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
        SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
        SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
        SET(): 自定义一个值，该值当然只能是对应的实体了
DateTimeField
    auto_now
    auto_now_add
        1 auto_now 与 auto_now_add 的比较
        auto_now=True 表示某个字段（或者对象）第一次保存的时候，由系统生成的。自动继承了不可更改的属性 editable=False，所以一旦设定就不可以更改、不可以再次重载（override），因此在后台 admin 中也不会显示出来。通常可以用在注册时间、生成时间等字段。
        auto_now_add=False 是字段每次修改的时候，最新的时间都会保存进去。

"""