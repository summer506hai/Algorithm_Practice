//给你一个整数 n（10 进制）和一个基数 k ，请你将 n 从 10 进制表示转换为 k 进制表示，计算并返回转换后各位数字的 总和 。
//转换后，各位数字应当视作是 10 进制数字，且它们的总和也应当按 10 进制表示返回。
//todo：只能进制转换么....
fun sumBase(n:Int, k:Int):Int {
    var myN : Float = n.toFloat()
    var y :Int = 0
    do {
        y += (myN % k.toFloat()).toInt()
        myN = myN / k
    }
    while (myN / k.toFloat() != 0.0f)
    return y
}

fun main(){
    println(sumBase(34,6))
    println(sumBase(42,2))
}