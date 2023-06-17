(defrule recommend-restaurant
  (user-cuisine $cuisine)
  (user-price-range $price-range)
  (user-location $location)
  =>
  (print "I recommend the following restaurants in Bauchi:")
  (loop-for-all-facts ((restaurant restaurant))
    (and
      (restaurant-cuisine restaurant = $cuisine)
      (restaurant-price-range restaurant = $price-range)
      (restaurant-location restaurant = $location)
      (restaurant-rating restaurant >= 4)
    )
    (print (restaurant-name restaurant))
  )
)
