import java.util.*

fun main(){
    //val array = sortArray(intArrayOf(5,2,3,1))
    println(Arrays.toString(sortArray(intArrayOf(5,2,3,1))))
    println(Arrays.toString(sortArray(intArrayOf(5,1,1,2,0,0))))
}

fun sortArray(nums: IntArray): IntArray{
    for(i in 0..(nums.size - 1)){
        for(j in 0..(nums.size - 2 - i )){
            if(nums[j] > nums[j + 1]){
                var temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
            }
        }
    }
    //nums.forEach { println(it) }
    return nums.toList().toIntArray()
}