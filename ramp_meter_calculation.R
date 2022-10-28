d<- c(7200, 960, 600, 600)
d<- d/1.2 # d is not divided by 1.2 if running for 120% demand
b<- 2100*3

od<- matrix()

turn_ratio<- c(0.99, 0.99, 0.85, 0.01)
A<- rbind(c(turn_ratio[1], 
        turn_ratio[1]*turn_ratio[2],
        turn_ratio[1]*turn_ratio[2]*turn_ratio[3],
        turn_ratio[1]*turn_ratio[2]*turn_ratio[3]*turn_ratio[4]),
      c(0, 
        turn_ratio[2],
        turn_ratio[2]*turn_ratio[3],
        turn_ratio[2]*turn_ratio[3]*turn_ratio[4]),
      c(0,
        0,
        turn_ratio[3],
        turn_ratio[3]*turn_ratio[4]),
      c(0,
        0,
        0,
        turn_ratio[4]))
x1<- d[1]
s1<- A[1,1]*x1+A[2,2]*d[2]

if(b < s1){
  cat("Ramp metering is needed at 1 and that the rate should be:", d[2]-(s1-b), "\n")
  if(d[2]-(s1-b) < 0){
    x2<- 0
    cat("Since the number is negative, ramp 1 should be closed")
  }else{
    x2<- d[2]-(s1-b)
  }
}else{
  cat("No ramp metering is needed")
}

s2<- x1*A[1,2] + x2*A[2,2] + d[3]
if(b < s2){
  cat("Ramp metering is needed at 2 and that the rate should be:", d[3]-(s2-b), "\n")
  if(d[3]-(s2-b) < 0){
    x3<- 0
    cat("Since the number is negative, ramp 2 should be closed")
  }else{
    x3<- d[3]-(s2-b)
  }
}else{
  cat("No ramp metering is needed")
}

s3<- x1*A[1,3]+x2*A[2,3]+x3*A[3,3]+d[4]
if(b < s3){
  cat("Ramp metering is needed at 3 and that the rate should be:", d[4]-(s3-b), "\n")
  if(d[4]-(s3-b) < 0){
    x4<- 0
    cat("Since the number is negative, ramp 3 should be closed")
  }
}else{
  cat("No ramp metering is needed")
}



