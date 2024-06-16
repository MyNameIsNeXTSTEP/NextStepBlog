# **Coupling distance**
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
*16.10.2024* | *2-3 min. reading*  

---
## Introduction

There are well known things in software programming such as [coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) and [cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)).
Let's talk a bit about first one, and there's a distance in coupling, for example, when in object oriented programming consumers of your classes receive some data straight and then process it separately so the original class and its surroundings do not know anything about it, and that's considered a **bad design**:

## Example

```ts
class SubscriptionPlan {
  constructor (
    private planType: string,
    private durationWeeks: number,
  ) {
    this.planType = planType;
    this.durationWeeks = durationWeeks;
  };
  showPlan() {
    return {
      'subscriptionType': this.planType,
      'durationWeeks': this.durationWeeks,
    }
  }
};

const subscriptionObj = new SubscriptionPlan('pro', 4).showPlan();
// in reality it'd be extra or third party code, not just innocent log
console.log(
  'updated subscription plan:\n',
  {
    subscription: subscriptionObj.subscriptionType,
    durationMonths: Math.abs(subscriptionObj.durationWeeks / 4),
    chargingFeeDollars: 2.99,
  }
);
```

Here the `subscriptionObj` is:

```
{
  "subscription": "pro",  
  "durationWeeks": 4
}
```

And the last log:

```
{
  "subscription": "pro",
  "durationMonths": 1,
  "chargingFeeDollars": 2.99
}
```

So what do we see here ?  
The instance of `SubscriptionPlan` gives us created subscription, but then some code transformed it and yet added something extra.

So it happened in **unclear, untraceable, dirty manner** and here the distance is 2:  
1. Extracting from `subscriptionObj` properties  
2. Add new properties based on previous and recalculated

> That means the originally formulated data was changed out of the objects composition scope, or any other design that would keep objects back to back and lead us through the process of changes smoothly.  
> And in this type of code the flow of control is takes away form us, context is getting corrupted, the maintanance is getting lower.

## Conclusion

**The less the coupling distance is - the better !**

P.S.  
And speaking about the design, firstly, it would be much much better to implement even this small example in the way, where clients of our objects couldn't extract sensitive data straight, but rather use them as sources of abstractions, and the actual transformations would appear only on those levels and cleanly traceable, elegant and pure.

In the sample above, it might be another method in the class that would give us appropriate object representation (months and fee) or another class that would take instance of the current one and transform the data accordingly, wherever it needed to work with another API, which takes only those fields.