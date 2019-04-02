# sqInRect(5, 3) should return [3, 2, 1, 1]
#   sqInRect(3, 5) should return [3, 2, 1, 1]
#   or (Haskell)
#   squaresInRect  5  3 `shouldBe` Just [3,2,1,1]
#   squaresInRect  3  5 `shouldBe` Just [3,2,1,1]
def sqInRect(x, y)
	if x == y
		return nil
	end
	result = []

    while y != x do
        if y > x
            y -= x
            result.append(x)
        elsif x > y
            x -= y
            result.append(y)
        end 
    end
    
    result.append(y)
    
    return result
end

# Refactor
def sqInRect(l, w)
	rects = []

	while l > 0 do
		w,l = [w, l].minmax
		rects << w
		l -= w
	end
	rects.size > 1 ? rects : nil
end 