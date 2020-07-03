# 一、hashmap中put()和get()
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
遍历HashMap链表中的每个元素，并对每个key进行hash计算，最后通过get方法获取其对应的值对象。

本文参考：简书https://www.jianshu.com/p/4aa3bb16f36c；作者：gogoingmonkey


# 二、headsort堆排序
## 1.概述
堆排序与归并排序一样，但不同于插入排序的是，堆排序的时间复杂度是O(nlgn)。而与插入排序相同，和归并排序不同的是，堆排序同样具有空间原址性：任何时候只需要常数个额外的元素空间存储临时数据。因此，堆排序是集合了归并排序和插入排序的算法。
## 2.堆的简介
## 2.1什么是堆
（二叉）堆是一个数组，可以近似为一个完全二叉树，书上的每一个节点对应数组中的一个元素。除了最低层外，该树是完全充满的，而且是从左向右填充。
## 2.2最大堆和最小堆
### 2.2.1最大堆
在最大堆中，除了根结点以外，所有节点满足父节点 >= 儿子节点。也就是说，某个节点的值，至多和自己父节点一样大。因此，堆中最大的元素存放在根结点中；并且，在任一子树中，该子树包含的所有节点的值 <= 该节点的值
作用：堆排序
### 2.2.1最小堆
在最小堆中，除了根结点以外，所有节点满足父节点 <= 儿子节点。因此，堆中最小的元素存放在根结点中；并且，在任一子树中，该子树包含的所有节点的值 >= 该节点的值
作用：构造优先队列
## 3.堆排序
堆排序的算法实现，均为伪代码
### 3.1堆排序算法
<code><pre>
HEAPSORT(A){
    Build-Max-Heap(A)
    for i = A.length to 2
        swip A[1] with A[i]
        A.heap-size = A.heap-size -  1
        Max-Heapify(A, 1)
}
</code></pre>
<code><pre>
'''
    初始化最大堆
'''
Build-Max-Heap(A){
    A.heap-size = A.length
    for i = Floor(A.length/2) to 1
        Max-Heapify(A, i)
}
</code></pre>
<code><pre>
'''
    调整堆
'''
Max-Heapify(A, 1){
    l = Left(i)
    r = Right(i)
    if l <= A.heap-size and A[l] > a[i]
        largest = l
    else largest = i
    
    if r <= A.heap-size and A[r]>A[largest]
        largest = r

    if largest != i
        swip A[i] and A[largest]
        Max-Heapify(A, largest)
}
</code></pre>