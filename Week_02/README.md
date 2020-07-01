# 一、hashmap哈希表的put和get方法分析
## 1.概述
HashMap是基于哈希表的实现Map接口的双列集合，数据结构是数组（哈希表）+链表（解决冲突）。其中key唯一、value可重复，允许存储null键和null值。

## 2.hashmap数据结构
### 2.1初始化
haspmap的底层是一个数组，每项数组中都是一个链表。每次新建一个hashmap，都会初始化一个数组。源代码如下：
<pre><code>
public HashMap(int initialCapacity, float loadFactor) {
    if (initialCapacity < 0)
        throw new IllegalArgumentException("Illegal initial capacity: " +
                                           initialCapacity);
    if (initialCapacity > MAXIMUM_CAPACITY)
        initialCapacity = MAXIMUM_CAPACITY;
    if (loadFactor <= 0 || Float.isNaN(loadFactor))
        throw new IllegalArgumentException("Illegal load factor: " +
                                           loadFactor);

    // Find a power of 2 >= initialCapacity
    int capacity = 1;
    while (capacity < initialCapacity)
        capacity <<= 1;

    this.loadFactor = loadFactor;
    threshold = (int)Math.min(capacity * loadFactor, MAXIMUM_CAPACITY + 1);
    //创建一个空数组，用来存放哈希表；
    //
    table = new Entry[capacity];
    useAltHashing = sun.misc.VM.isBooted() &&
            (capacity >= Holder.ALTERNATIVE_HASHING_THRESHOLD);
    init();
}
</code></pre>
数组的数据结构是：key、value和指向下一个引用的Next
<code><pre>
static class Entry<K,V> implements Map.Entry<K,V> {
    final K key;
    V value;
    Entry<K,V> next;
    final int hash;
    ……
}
</code></pre>

### 2.2存储put()
<pre><code>
public V put(K key, V value) {
    //其允许存放null键和null值，当其key为null时，调用putForNullKey方法，放入到table[0]的这个位置
    if (key == null)
        return putForNullKey(value);
    //通过调用hash函数对key进行哈希，得到哈希之后的数值。
    int hash = hash(key);
    //根据上一步骤中求出的hash得到在数组中是索引i
    int i = indexFor(hash, table.length);
    //如果i处的Entry不为null，则通过其next指针不断遍历e元素的下一个元素。
    for (Entry<K,V> e = table[i]; e != null; e = e.next) {
        Object k;
        if (e.hash == hash && ((k = e.key) == key || key.equals(k))) {
            V oldValue = e.value;
            e.value = value;
            e.recordAccess(this);
            return oldValue;
        }
    }

    modCount++;
    addEntry(hash, key, value, i);
    return null;
}
</code></pre>

### 2.3读取get()
<pre><code>
public V get(Object key) {
    if (key == null)
        return getForNullKey();

    //计算key的hashcode，找到数组中对应的元素
    Entry<K,V> entry = getEntry(key);
    //查看是否有链表
    return null == entry ? null : entry.getValue();
}

//解决hash冲突
final Entry<K,V> getEntry(Object key) {
    //计算数组对应的位置，遍历列表
    int hash = (key == null) ? 0 : hash(key);
    for (Entry<K,V> e = table[indexFor(hash, table.length)];
         e != null;
         e = e.next) {
        Object k;
        //通过key.equals()查找对应记录
        if (e.hash == hash &&
            ((k = e.key) == key || (key != null && key.equals(k))))
            return e;
    }
    return null;
}
</code></pre>

## 3.常见的面试题
1. 两个对象的hashcode相同，会发生什么？
hashcode相同，说明两个对象HashMap数组的同一位置上，遍历链表中的每个元素，通过key的equals方法来判断是否为同一个key。如果是同一个key，则新的value会覆盖旧的value，并且返回旧的value（修改）。如果不是同一个key，则存储在该位置上的链表的链头（添加）。
2. 如果两个键的hashcode相同，如何取值？
遍历HashMap链表中的每个元素，并对每个key进行hash计算，最后##通过get方法获取其对应的值对象。

本文参考：简书https://www.jianshu.com/p/4aa3bb16f36c；作者：gogoingmonkey


# 二、headsort堆排序
## 1.概述

## 2.堆的简介
## 3.堆排序