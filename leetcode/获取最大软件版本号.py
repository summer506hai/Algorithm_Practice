# -*— coding:utf-8 --*
'''
<主版本>.<次版本>.<增量版本>-<里程碑版本>
<主版本>.<次版本>.<增量版本> ：基于数字比较
里程碑版本 ： 基于字符串比较

'''

#SB式写法
def main():
    version_a = input()
    version_b = input()
    try:
        num_a_1 = version_a.split(".")[0]
    except Exception:
        num_a_1 = -1
    try:
        num_a_2 = version_a.split(".")[1]
    except Exception:
        num_a_2 = -1
    try:
        a_3 = version_a.split(".")[2]
        if "-" in a_3:
            num_a_3 = a_3.split("-")[0]
        else:
            num_a_3 = a_3
    except Exception:
        num_a_3 = -1
    try:
        str_a_4 = version_a.split("-")[1]
    except Exception:
        str_a_4 = ""
    try:
        num_b_1 = version_b.split(".")[0]
    except Exception:
        num_b_1 = -1

    try:
        num_b_2 = version_b.split(".")[1]
    except Exception:
        num_b_2 = -1
    try:
        b_3 = version_b.split(".")[2]
        if "-" in b_3:
            num_b_3 = b_3.split("-")[0]
        else:
            num_b_3 = b_3
    except Exception:
        num_b_3 = -1

    try:
        str_b_4 = version_b.split("-")[1]
    except Exception:
        str_b_4 = ""


    if int(num_a_1) > int(num_b_1):
        return version_a
    elif int(num_a_1) < int(num_b_1):
        return version_b
    else:
        if int(num_a_2) > int(num_b_2):
            return version_a
        elif int(num_a_2) < int(num_b_2):
            return version_b
        else:
            if int(num_a_3) > int(num_b_3):
                return version_a
            elif int(num_a_3) < int(num_b_3):
                return version_b
            else:
                if str_a_4 > str_b_4:
                    return version_a
                elif str_a_4 < str_a_4:
                    return version_b
                else:
                    return version_a


if __name__ == "__main__":
    print(main())


'''
优化后
'''
def parse_version(version):
    parts_str = version.split("-")
    if len(parts_str) > 0:
        parts = parts_str[0].split(".")
        alpha = parts_str[1]
    else:
        parts = version.split(".")
        alpha = ""
    while len(parts) < 3:
        parts.append(-1)
    nums = [int(part) for part in parts[:3]]
    # alpha = parts[3] if len(parts) > 3 else ""
    # print(nums,alpha)
    return nums, alpha

def compare_versions(version_a, version_b):
    nums_a, alpha_a = parse_version(version_a)
    nums_b, alpha_b = parse_version(version_b)
    for num_a, num_b in zip(nums_a, nums_b):
        if num_a != num_b:
            return version_a if num_a > num_b else version_b
    if alpha_a != alpha_b:
        return version_a if alpha_a > alpha_b else version_b
    return version_a

def main():
    version_a = input()
    version_b = input()
    result = compare_versions(version_a, version_b)
    print(result)

if __name__ == "__main__":
    main()

