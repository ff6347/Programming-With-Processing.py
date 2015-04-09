# These are build in variables
# integer values
w = width
h = height
# now print to the console
# println adds a new line at the end of the text
print("The window is " + str(w) + " pixels wide")
println(" and " + str(h) + " pixels high")

# a string
devider = "\n-------------------\n"
println(devider)
# now change them with a build in function
size(400, 225)

# flaoting point values
ratio = ( width / height) # needs to be casted
msg = "Oh now your're doing a fancy format with a " + str(ratio) + " ratio?"
println(msg)
println(devider)


