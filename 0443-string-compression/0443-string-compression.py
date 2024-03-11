class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        placeholder = seeker =  0
        current_count = 0
        while seeker < len(chars):
            if chars[seeker] != chars[placeholder]:
                if current_count > 1:
                    add_chars = list(str(current_count))
                    for i in range(len(add_chars)):
                        placeholder+=1
                        chars[placeholder] = add_chars[i]

            

                placeholder+=1
                chars[placeholder] = chars[seeker]
                current_count = 1
            else:
                current_count += 1

            seeker+=1

        if current_count > 0:
            if current_count > 1:
                    add_chars = list(str(current_count))
                    for i in range(len(add_chars)):
                        placeholder+=1
                        chars[placeholder] = add_chars[i]


        return placeholder+1

        