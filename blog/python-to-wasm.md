# Converting my python library to wasm

Webassembly is a developing technology that allows a compilation target that can be executed anywhere. This means that when you compile a program, you can run it in javascript, python, or the command line.

I am the owner and maintainer of [mathgenerator](https://github.com/lukew3/mathgenerator), a library for generating math exercises. I originally wrote this in Python, mostly because it was what I was most familiar with, and thought that it would be easiest for outside contributors to add on to. These are valid reasons for choosing Python, but at this point, I think that it is important for this to be available as a js library for the browser, so that static sites can use the generator. Webassembly libraries can be used from just about any runtime, so if somebody wanted to use this on their Ruby or Go server, that would be possible without a hacky python intermediary.

## Beginning
I jumped into this project with little knowledge of Webassembly (sometimes abbreviated WASM) at the beginning of this project. I found great explanations of wasm like [this one by Lin Clark](https://www.youtube.com/watch?v=HktWin_LPf4) and became hopeful. I also had little knowledge about compiled languages, with only about a semester's worth of C++ experience.

My first attempt consisted of me trying to learn how to use [emscripten](https://emscripten.org/) to build from C++ code. However, emscripten works by generating a wasm binary and js code to interact with that binary. However, if we want to target runtimes other than javascript, this is not an adequate option. 

My next attempt consisted of using Rust and wasm-bindgen/wasm-pack.

## Challenges
### Kwargs
Compiled languages don't have python kwargs where you have an optional parameter. Therefore, if I wanted to include default and customizable generators, I would have to make multiple functions for each generator. I decided to have a regular generator function that would generate with defaults and another function with the same name but `_args` appended to it. 

### Random
At this stage in development, WASM doesn't have access to the system's random source, so random has to be imported from system calls. Luckily, the Rust getrandom crate handles this as long as you add 
```
getrandom = { version = "0.2", features = ["js"] }
```
to your `Cargo.toml`.

