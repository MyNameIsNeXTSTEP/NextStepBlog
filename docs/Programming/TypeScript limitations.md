# **TypeScript limitations**

<span class='translation_button'>[Read in RUS (translated by ChatGPT)](/Programming/TypeScript limitations-rus)</span>

<link href="/stylesheets/tags.css" rel="stylesheet" type="text/css"/>
<div class="tags">
    <div class='tag'>
        <a href="/tags#Programming">Programming</a>
    </div>
    <div class='tag'>
        <a href="/tags#Typescript">Typescript</a>
    </div>
    <div class='tag'>
        <a href="/tags#OOP">OOP</a>
    </div>
</div>
*17.02.2024* | *3-4 min. reading*  

Or how did i tried to code TS overloads not without the help of ChatGPT.
[ChatGPT messages share link](https://chat.openai.com/share/7c7c7517-9e9d-4b5e-816c-0f6def3060b)

As i have started studying such thing as overoads some time ago, i had an idea to implement it in some way in typescipt. My goal was to somehow introduce the easy to use overloading code in TS, without too much mannual handling as i saw in examples while preparing, researching the field.

<img
    src="/assets/just-try-to-realise-ts-meme.jpeg"
    width="100%"
/>

The whole idea was to do something like the Java has, but for TS considering that TS "support" method overloading only on compile-time having the same name methods in class, but with different signatures and the one method so called **entry point** or **entry method**. Alse it means that programmer should take the typechecking in first place on:
```ts
class TestClass {
    someMethod(obj: TypeOne): void; // "overloaded" signature method
    someMethod(obj: TypeTwo): void; // "overloaded" signature method
    someMethod(obj: TypeOneOrTwo): void { // the entry method
        // need to check type entrance agaist our predicates
        if (obj && _check_obj_type_matching_somehow_)) {
            // do something 
        }
        else { // may have another `else if` type matching check
            // do something
        }
    }
};
```

So the issue to make it work was to somehow be able to check that the provided object is one of the subtypes of a union type, and here i faced the core problem.
In JS/TS there are [ECMAScript Data Types and Values](https://tc39.es/ecma262/#sec-ecmascript-data-types-and-values) against which only we can check the actual type of something, for exmaple, using the **typeof** keyword.

Buy the general purpuse is to check the type of incoming object in overloaded entrance method against the **custom defined** types. We can achive it by several approaches.
First - is to mannualy check the presence of incoming object properties in type guard:
```ts
type TypeOne = {
    name: string;
    id: number;
};

function isTypeOne(obj: any): obj is TypeOne {
    return (
        'name' in obj && 'id' in obj &&
        typeof (obj as TypeOne).name === 'string' &&
        typeof (obj as TypeOne).id === 'number'
    );
}
```

And that includes the worst scenarion of handling multiple fields of bigger object mathicng their types explicitly, but mannualy. It can be done in the form of automatic properties checking using **Object.keys** and map it through collected value types from the object signature - but it's really cumbersome.
Also we may use the TS **version 4.9** [satisfies](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html) operator to check for type, but it's not working as it seemd to be:
```ts
type TypeOne = {
    name: string;
    id: number;
};

var obj = { id: 1, name: 2};

if (obj satisfies TypeOne) {
  console.log(1) // 1 will be logged
} else {
  console.log(2)
}
```

Because *"The new satisfies operator lets us validate that the type of an expression matches some type, without changing the resulting type of that expression."* (c).
So it only will show you type error alert at compile-time in IDE, but the code still will be executed with no errors.

After a while i realised that the appropriate solution could be something that only correspondse to this two points:

- Type checking must be dynamic, which means the ability to use generics and be able match every types by one action.
- If checking for properties presence and their data types it should automative

Struggling and surfing the web, playing with code i did not manage to succeed to find any answers to fit my goals. The main factor was that using union types and checkng it's subtype against it neither in the form generic nor straight always gives the error:
```ts
type TypeOne = {
    name: string;
    id: number;
};
type TypeTwo = …
type TypeThree = …

type TMerged =
    | TypeOne
    | TypeTwo
    | TypeThree

// Create a map object that registers each type check function
const typeCheckMap: TypeCheckMap = {
    'TypeOne': isTypeOne,
    'TypeTwo': isTypeTwo,
    // Add other types as necessary
};

// Generic type guard function
function isType<T>(obj: TMerged, typeName: keyof typeof typeCheckMap): obj is T {
    const typeChecker = typeCheckMap[typeName];
    if (!typeChecker) {
        throw new Error(`Type check for '${typeName}' not found.`);
    }
    return typeChecker(obj);
}

// ERROR:
// A type predicate's type must be assignable to its parameter's type.
//  Type 'T' is not assignable to type 'TMerged'.
//    Type 'T' is not assignable to type 'TypeTwo'
```

The reason is the field types required in **TypeOne** but not existing in **TypeTwo** f.e. are conflicting. TypeScript cannot handle the fact that type predicate can be assignable and substitute to the super-type **TMerged**.

And here's the ChatGPT. After several question i finally realised the problem - it's the TS disability to validate data types in run-time and also the core type-matching principle, it's [structural](https://www.typescriptlang.org/docs/handbook/type-compatibility.html), so no compatibility between inner types of the union type affects the matching directly between the super-time and it's subtype, i.e. type **TMerged** is not assignable to type **TypeTwo** f.e. due to their structural differencies. Even extanding one another the problem doesn't go away.

So the conclusion is - the only way today to normally use the methid overloading in TS is still the semi-mannual checking of types.