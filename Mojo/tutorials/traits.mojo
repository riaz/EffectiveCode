trait SomeTrait:
    fn say_hello(self):...
# implementing a trait
@value
struct SomeStruct:
    fn say_hello(self):
        print("Hello World")

# function that uses the trait as a argument
fn func_with_trait[T: SomeTrait] (x:T):
    x.say_hello()

# using trait function
fn using_trait_func():
    var instance = SomeStruct()
    
    # we can pass the struct to the above function that uses the trait
    func_with_trait(instance)

fn main():
    using_trait_func()