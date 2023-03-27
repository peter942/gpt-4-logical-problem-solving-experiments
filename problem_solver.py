import streamlit as st
import openai

def chatgpt_prompt(prompt, temperature):
    completion = openai.ChatCompletion.create(
    model="gpt-4", 
    temperature=temperature,
    messages=prompt)
    return completion["choices"][0]["message"]["content"]

st.markdown("# GPT-4 can reliably solve Yann LeCun's gear problem if given the ability to recognize its limitations & adapt its actions accordingly")


st.markdown("Yann LeCun, presented the following problem on [Twitter](https://twitter.com/ylecun/status/1639690596364308482), citing it as an example of the type of problem that LLMs like GPT-4 will be unable to solve:")
st.info("7 axles are equally spaced around a circle. A gear is placed on each axle such that each gear is engaged with the gear to its left and the gear to its right. The gears are numbered 1 to 7 around the circle. If gear 3 were rotated clockwise, in which direction would gear 7 rotate?")
st.markdown("In one sense, he is correct. Directly querying models fails to solve this problem. However, directly querying the human brain also fails to solve many problems that the human brain is capable of solving. In order to get the best out of LLMs, teaching them the limitations of their 'brains' and strategies to overcome them will become increasingly important for deploying them at complex tasks reliably.")
st.markdown("With knowledge of their own shortcomings and the ability to change actions based on these shortcomings, LLMs will be able to devise solutions to problems that they would otherwise be unable to solve.")
st.markdown("In this post, I'll demonstrate how GPT-4 can reliably solve Yann's problem if it's part of a system that allows it to recognize its limitations & adapt its actions accordingly. While I believe that this approach can be extended limitlessly, this is just a short demo of the idea." )

st.markdown("### The approaches an LLM can combine to solve a tricky problem")
st.markdown("When tackling a problem with an LLM, there variety of approaches you can take - these are queries that it can make of itself (or of other systems) in pursuing the best solution to a problem.")    
st.markdown("If an LLM can assess itself and the problem it has to tackle, it can then decide which combination of approaches to take in order to solve the problem reliably.")
st.markdown("Below are a few examples of what these pieces might be that it can combine:")
st.markdown("**1. Directly querying the LLM:** for simple problems, this may be the best and most efficient approach.")
st.markdown("**2. Red Teaming itself:** for problems where it's likely to be biased, it can challenge itself and have a second query determine whether its challenge is fair.")  
st.markdown("**3. Calling on multiple perspectives:** for example, for a visual problem, it might ask itself to imagine a problem in the physical world of visualise it with ascii.")
st.markdown("**4. Calling on the same perspective multiple times:** for problems where it's likely to be inconsistent, this may be the best approach")

st.markdown("### How it can determine which of use these pieces to use")
st.markdown("Rather than it deciding on what approach to take and how to take it being 'baked in' to a single LLM query, I would say that what makes sense is for this to be a layer on top of the query - a meta-query that determines the best combination of approaches to take.")
st.markdown("Some examples of combinations of approaches that may make sense for different circumstances could be:")
st.markdown("**1. For a problem where it's likely to fall into a common pitfall:** asking for 2 normal perspectives and 2 red team perspective")
st.markdown("**2. For a visual problem:** asking for a visual perspective and a textual perspective in order to overcome the limitations of the LLM's visual understanding.")
st.markdown("**3. For a problem where it's likely to have an unintuitive answer:** asking for a contrarian perspective and a normal-problem-solving perspective")

st.markdown("Determining which perspective to take could be determined by having the LLM fine-tuned on problems alongside the combination of approaches required to solve them reliably.")
st.markdown("This 'self-awareness' would allow it to call on multiple perspectives if need be and then to determine which of these perspectives is the best to use based on their answers. ")

st.markdown("### What might the 'self-aware' meta-query look like?")
st.markdown("While I haven't demonstrated it here due to not having access to GPT-4 fine-tuning, I'd propose that a fine-tune model based on questions alongside the best combination of approaches to solve them for a model at its level would be able to determine the best combination of approaches to take for a problem at its level.")
st.markdown("An example of what this fine-tuning data could like like for this problem is below:")
st.info("""
            GPT-4 may have difficulty solving this problem or similar problems for several general reasons:

            1. **Limited context understanding:** LLMs are primarily trained on textual data and may struggle to accurately visualize or reason about spatial and mechanical relationships that are better represented through diagrams or hands-on experience.

            2. **Ambiguity in problem description:** If a problem's description is unclear or lacks sufficient detail, an LLM might not grasp the full scope of the problem, leading to incorrect or incomplete answers.
            
            As such, the following course of action may be the best way to solve this problem:

            - **Red Team the LLM:** The LLM can be challenged to determine whether its own answer is fair. If it is not, it can then be asked to provide a better answer.
            - **Call on multiple perspectives:** The LLM can be asked to imagine the problem in the physical world or to visualise it with ascii.

            """)
st.markdown("Generating a few hundred examples like this and fine-tuning a GPT-4-level model on it would probably be enough to get it to the point where it could reliably determine the best combination of approaches to take for a problem.")

st.markdown("Depending on how importance reliability is, it could be tuned to be extra-cautious or less cautious if need be.")

st.markdown("### How can it determine the correct answer from the possibilities?")

st.write("In order to determine the best answer or combinations of answers, I include a reasoning step, where it reasons through contradictions and inconsistencies in the answers it gets from the different perspectives.")
st.write("Following this, there's a 'Final Answer' step, where it determines the best answer based on the reasoning step and the previous information.")

st.markdown("### This idea in action - a generalisable solution allowing GPT-4 to solve problems at the level Yann proposed") 

st.markdown("For this example, I'll show an example of just one of these approaches for the problem Yann proposed: seeking 2 perspectives and then Red Teaming itself - as mentioned, my assumption is that, based on fine-tuning data, it would be able to determine that this is the best approach to take for this problem.")
st.markdown("Here's a quick visualisation of what this looks like - as mentioned, for this example, I'm not using a meta-query due to not having access to GPT-4 fine-tuning - instead, I'm choosing the path:")
st.write("")
st.image("https://banodoco.s3.amazonaws.com/input_images/Untitled+scene.png")
st.write("")
st.info("You can see how exactly this approch works in [the code](https://github.com/peter942/gpt-4-logical-problem-solving-experiments).")
st.markdown("And below are 5 examples of it solving Yann's problem with this approach:")

with st.expander("Example #1:"):
        st.markdown("""### Solution 1
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and right.
The gears are numbered 1 to 7 around the circle.
We are rotating gear 3 clockwise.
Approach:

Determine the direction of rotation for each gear starting from gear 3 and moving along the circle.
Identify the direction of rotation for gear 7.
Potential pitfalls:

Incorrectly determining the direction of rotation for each gear.
Miscounting the gears.
Step-by-step reasoning:

Since we are rotating gear 3 clockwise, we now need to determine the direction of rotation for gear 2.
When gears are engaged, they rotate in the opposite direction of the adjacent gear. So, gear 2 rotates counterclockwise.
Next, determine the direction of rotation for gear 1. Since gear 2 rotates counterclockwise, gear 1 rotates clockwise.
Now, determine the direction of rotation for gear 7. Since gear 1 rotates clockwise, gear 7 rotates counterclockwise.
Therefore, if we rotate gear 3 clockwise, gear 7 would rotate counterclockwise.
### Solution 2
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
We are attempting to rotate gear 3 clockwise.
Approach:

Determine the direction of rotation of each gear, starting from gear 3 and moving in both directions.
Find the direction of rotation of gear 7.
Potential Pitfalls:

Skipping a gear in the rotation sequence.
Misinterpreting the direction of rotation.
Step-by-step reasoning:

We are rotating gear 3 clockwise.
Since gear 3 is engaged with gear 2, gear 2 will rotate counter-clockwise.
Since gear 2 is engaged with gear 1, gear 1 will rotate clockwise.
Gear 1 is also engaged with gear 7, so gear 7 will rotate counter-clockwise (since gear 1 is rotating clockwise).
The direction of rotation for gear 7 is counter-clockwise.
Conclusion: If we attempt to rotate gear 3 clockwise, gear 7 will rotate counter-clockwise.

### Red Team Challenge #1
In their solution, they failed to consider that the circle of gears will create a closed loop system. In a closed loop system with an odd number of gears, it is impossible for all gears to engage and rotate simultaneously without slipping or breaking. This is because, by the time the rotation reaches the last gear, it will be required to rotate in the same direction as the first gear, creating a contradiction in the rotation direction.

As a result, this answer is wrong because the gears will be unable to rotate in the specified manner. Instead, the gears would either lock up, experience slippage, or break due to the conflicting rotation directions in the closed loop system with an odd number of gears.

### Red Team Challenge #2
In this solution, they failed to consider the possibility of the gears being locked or unable to rotate due to their arrangement. Since there are an odd number of gears (7) in a closed loop, rotating gear 3 clockwise would require gear 7 to rotate clockwise as well, to maintain engagement with the neighboring gears. However, this creates a contradiction because, as mentioned in the step-by-step reasoning, gear 7 should rotate counter-clockwise when following the rotation sequence from gear 3 to gear 1.

As a result, this answer is wrong because it doesn't take into account the locked nature of the gears in a closed loop with an odd number of gears. The gears would not be able to rotate under normal circumstances, making the determination of gear 7's rotation direction irrelevant.

### Reasoning
After analyzing the given solutions and challenges, I can determine that the discrepancy exists due to the fact that both solutions failed to consider the implications of having an odd number of gears in a closed loop system.

In a closed loop with an odd number of gears, it is impossible for all gears to engage and rotate simultaneously without slipping or breaking. This is because, by the time the rotation reaches the last gear, it will be required to rotate in the same direction as the first gear, creating a contradiction in the rotation direction.

Both solutions provided the direction of rotation for gear 7 by following the rotation sequence from gear 3 to gear 1 without considering the locked nature of the gears in a closed loop with an odd number of gears. As a result, these solutions are incorrect, as they don't take into account the locked nature of the gears in this particular scenario.

To resolve the discrepancy, it is essential to acknowledge that the gears would not be able to rotate under normal circumstances due to the odd number of gears in a closed loop system. Therefore, determining the direction of rotation for gear 7 is irrelevant in this case, as the gears would either lock, experience slippage, or break due to the conflicting rotation directions.

### Final Answer
The best solution to the problem is that the gears would be unable to rotate in the specified manner due to the odd number of gears in a closed loop system. This causes a contradiction in the rotation direction, leading to the gears either locking up, experiencing slippage, or breaking. Determining the direction of rotation for gear 7 is irrelevant in this case.""")

with st.expander("Example #2:"):
        st.markdown("""### Solution 1
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
Gear 3 is rotated clockwise.
Approach:

Determine the direction of rotation for each gear, starting with gear 3 and moving towards gear 7.
Pitfalls:

Assuming that the rotation direction will be the same for all gears, as the direction alternates for adjacent gears.
Reasoning step-by-step:

Gear 3 is rotated clockwise (given).
When two engaged gears rotate, they rotate in opposite directions. So, if gear 3 rotates clockwise, gear 4 will rotate counterclockwise.
Similarly, if gear 4 rotates counterclockwise, gear 5 will rotate clockwise.
If gear 5 rotates clockwise, gear 6 will rotate counterclockwise.
Finally, if gear 6 rotates counterclockwise, gear 7 will rotate clockwise, as it is engaged with gear 6.
Conclusion: If gear 3 is rotated clockwise, gear 7 would rotate in the clockwise direction.

### Solution 2
Fundamental Facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
Gears are numbered 1 to 7 around the circle.
Gear 3 is attempted to be rotated clockwise.
Approach:

Determine the direction of rotation for each gear starting from gear 3 and moving around the circle.
Identify the direction gear 7 would rotate based on the pattern observed.
Step 1: Determine the direction of rotation for each gear starting from gear 3.

Gear 3: Clockwise (given)
Gear 4: When two gears are engaged, they rotate in opposite directions. So, gear 4 would rotate counterclockwise.
Gear 5: Following the same logic, gear 5 would rotate clockwise.
Gear 6: Gear 6 would rotate counterclockwise.
Gear 7: Gear 7 would rotate clockwise.
Step 2: Identify the direction gear 7 would rotate based on the pattern observed. Based on the pattern observed in Step 1, we can conclude that gear 7 would rotate in a clockwise direction.

### Red Team Challenge #1
The solution's approach fails to consider that the gears are arranged in a circle. As a result, the conclusion that gear 7 rotates clockwise is incorrect.

Reasoning considering the circular arrangement:

Gear 3 is rotated clockwise (given).
Gear 4 will rotate counterclockwise, as it is engaged with gear 3.
Gear 5 will rotate clockwise, as it is engaged with gear 4.
Gear 6 will rotate counterclockwise, as it is engaged with gear 5.
Gear 7 will rotate clockwise, as it is engaged with gear 6.
However, since the gears form a circle, gear 1 is also engaged with gear 7. Since gear 7 is rotating clockwise, gear 1 must rotate counterclockwise.
Gear 1's counterclockwise rotation will cause gear 2 to rotate clockwise, as it is engaged with gear 1.
Since gear 2 is engaged with gear 3 and rotating clockwise, it will force gear 3 to rotate counterclockwise, which contradicts the initial clockwise rotation of gear 3.
This contradiction reveals that the gears cannot rotate freely as described in the problem, as their arrangement would result in a locked system due to the circular configuration. The provided solution is incorrect, as it fails to account for the constraint introduced by the circular arrangement of the gears.

### Red Team Challenge #2
In this solution, they failed to consider that the gears are arranged in a circle. When gears are engaged in a linear fashion, their rotation directions alternate as described in the solution. However, in a circular arrangement, the situation is different.

When gear 1 is engaged with gear 7, it forms a loop with an odd number of gears (7 in this case). In such a loop, the gears cannot rotate freely as their alternating rotation directions will conflict at the point where gear 1 and gear 7 meet. For example, if gear 3 rotates clockwise, gear 4 rotates counterclockwise, gear 5 rotates clockwise, gear 6 rotates counterclockwise, then gear 7 should rotate clockwise. But for gear 1 to be engaged with gear 7, it must rotate counterclockwise, which contradicts the clockwise rotation of gear 7.

As a result, the gears will be locked and unable to rotate. The answer provided in the solution is incorrect because it assumes the gears can rotate without taking the circular arrangement into account.

### Reasoning
The discrepancy in the solutions exists because the initial solutions fail to account for the circular arrangement of the gears, as pointed out by the challenges. In a linear arrangement, gears rotate in alternating directions without issue, but a circular arrangement with an odd number of gears creates a locked system. This is because the alternating rotation directions will conflict at the point where the first and last gears meet.

Taking into account the challenges and the circular arrangement, we can reason as follows:

Gear 3 is attempted to be rotated clockwise (given).
Gear 4 will rotate counterclockwise, as it is engaged with gear 3.
Gear 5 will rotate clockwise, as it is engaged with gear 4.
Gear 6 will rotate counterclockwise, as it is engaged with gear 5.
Gear 7 will rotate clockwise, as it is engaged with gear 6.
However, since the gears form a circle, gear 1 is also engaged with gear 7. In order for gear 1 to be engaged with gear 7, it must rotate counterclockwise, which contradicts the clockwise rotation of gear 7.
This contradiction reveals that the gears cannot rotate freely as described in the problem, as their arrangement results in a locked system due to the circular configuration. The initial solutions are incorrect because they assume the gears can rotate without considering the constraint introduced by the circular arrangement of the gears.

The correct conclusion is that the gears will be locked and unable to rotate, as pointed out by the challenges.

### Final Answer
The best solution to the problem is that the gears will be locked and unable to rotate, as the circular arrangement with an odd number of gears creates a locked system due to the alternating rotation directions conflicting at the point where the first and last gears meet.""")

with st.expander("Example #3:"):
        st.markdown("""### Solution 1
Fundamental facts:

There are 7 equally spaced axles around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
We are attempting to rotate gear 3 clockwise.
Objective: Determine the direction of rotation of gear 7.

Approach:

Determine the direction of rotation of each gear starting from gear 3 and going around the circle.
Observe the pattern of rotation for the gears.
Apply the pattern to determine the direction of rotation of gear 7.
Step-by-step reasoning:

Gear 3 is rotated clockwise.
Since the gears are engaged, gear 4 will rotate counterclockwise.
Gear 5 will rotate clockwise, as it is engaged with gear 4.
Gear 6 will rotate counterclockwise, as it is engaged with gear 5.
Gear 7 will rotate clockwise, as it is engaged with gear 6.
Conclusion: Gear 7 will rotate in the clockwise direction.

### Solution 2
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
Gear 3 is rotated clockwise.
Approach:

Determine the direction of rotation for each gear starting from gear 3 and moving to gear 7.
Potential pitfalls:

Assuming that the gears rotate in the same direction as their neighbors without considering the effect of gear size.
Step-by-step reasoning:

Gear 3 is rotated clockwise.
Since gear 3 is engaged with gear 2, gear 2 will rotate counterclockwise.
Gear 2 is engaged with gear 1, so gear 1 will rotate clockwise.
Gear 1 is engaged with gear 7, so gear 7 will rotate counterclockwise.
Gear 7 is engaged with gear 6, but gear 6 doesn't affect the direction of gear 7.
Conclusion: If gear 3 is rotated clockwise, gear 7 will rotate counterclockwise.

### Red Team Challenge #1
The solution provided assumes a simple linear arrangement of gears in which each gear is only engaged with its immediate neighbors. However, in the problem, the gears are arranged in a circle. This arrangement creates a closed loop of gears which affects the rotation pattern.

In a circular arrangement, when the last gear (gear 7) is engaged with the first gear (gear 1), it will affect the rotation pattern. The rotation of gear 7 will be influenced by gear 1, which in turn is influenced by gear 2, and so on.

To illustrate, let's follow the rotation pattern again, considering the engagement between gear 1 and gear 7:

Gear 3 is rotated clockwise.
Gear 4 rotates counterclockwise.
Gear 5 rotates clockwise.
Gear 6 rotates counterclockwise.
Gear 7 tries to rotate clockwise, as it is engaged with gear 6.
Gear 1 tries to rotate counterclockwise, as it is engaged with gear 7.
Gear 2 tries to rotate clockwise, as it is engaged with gear 1.
However, gear 2 is also engaged with gear 3, which is being rotated clockwise.
In this circular arrangement, gears 2 and 3 are engaged and are both trying to rotate in the same direction (clockwise). This creates a conflict, as both gears cannot rotate in the same direction simultaneously. As a result, the gears will become locked, and none of the gears will be able to rotate.

The solution provided failed to consider the circular arrangement and the engagement between gear 7 and gear 1, which impacts the rotation pattern. The correct answer should be that the gears will lock up and not rotate.

### Red Team Challenge #2
In this solution, they failed to consider the possibility of the gears being unable to turn due to their arrangement around the circle. Since there are an odd number of gears (7), and they are equally spaced around the circle, when one gear is rotated, the gear diametrically opposite to it will be forced to rotate in the same direction. However, this is not possible since the gears are engaged with each other, and the movement of one gear causes the adjacent gears to rotate in the opposite direction.

As a result, the answer is wrong because the gears' arrangement would cause a mechanical locking situation, preventing any of the gears from rotating.

### Reasoning
After reviewing the solutions and challenges provided, it is evident that the discrepancy exists because the initial solutions failed to consider the circular arrangement of the gears and the resulting mechanical locking situation. To resolve this discrepancy, let's dismiss the initial solutions and focus on the challenges, as they provide a more accurate representation of the problem.

Challenge #1 and Challenge #2 both identify the critical issue that arises from the circular arrangement of gears: the gears will lock up and not rotate. When attempting to rotate gear 3 clockwise, the gears' engagement creates a conflict in the rotation pattern, as both gears 2 and 3 cannot rotate in the same direction simultaneously. This mechanical locking situation prevents any of the gears from rotating.

Thus, based on the challenges' reasoning, the answer to the problem is that when gear 3 is rotated clockwise, the gears will lock up and not rotate, making it impossible to determine the rotation direction of gear 7.

### Final Answer
The best solution to the problem is that when gear 3 is rotated clockwise, the gears will lock up and not rotate, making it impossible to determine the rotation direction of gear 7.  """)


with st.expander("Example #4:"):
     st.markdown("""### Solution 1
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
Gear 3 is rotated clockwise.
Approach:

Determine the direction in which gear 2 rotates when gear 3 rotates clockwise.
Continue this process for each gear up to gear 7.
Step-by-step reasoning:

When gear 3 rotates clockwise, it causes gear 2 to rotate counterclockwise (opposite direction) since the gears are engaged.

When gear 2 rotates counterclockwise, it causes gear 1 to rotate clockwise (opposite direction).

When gear 1 rotates clockwise, it causes gear 7 to rotate counterclockwise (opposite direction).

Conclusion: If gear 3 is rotated clockwise, gear 7 would rotate counterclockwise.

Solution 2
### Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
Gear 3 is rotated clockwise.
Approach:

Determine the direction of rotation for each gear starting from gear 3.
Determine the direction of rotation for gear 7 based on the rotation of the gears around the circle.
Potential pitfalls:

Incorrectly identifying the direction of gear rotation.
Step-by-step reasoning:

When gear 3 rotates clockwise, it will cause gear 4 to rotate counterclockwise (due to gears being engaged).
Gear 4's counterclockwise rotation will cause gear 5 to rotate clockwise.
Gear 5's clockwise rotation will cause gear 6 to rotate counterclockwise.
Gear 6's counterclockwise rotation will cause gear 7 to rotate clockwise.
Conclusion: Gear 7 will rotate clockwise when gear 3 is rotated clockwise.

### Red Team Challenge #1
The solution assumes that the gears can rotate freely without any restrictions. However, it fails to consider the possibility of mechanical constraints or "locking" due to the circular arrangement of gears.

In a circular arrangement with an odd number of gears (in this case, 7), when gear 3 is rotated clockwise and the rotation is propagated through the gears, gear 7's rotation direction would come into conflict with gear 1. Gear 1 is rotating clockwise, which would force gear 7 to rotate counterclockwise, but gear 6's counterclockwise rotation would force gear 7 to rotate clockwise. This conflict creates a mechanically impossible situation, causing the gears to lock and not rotate at all.

As a result, the answer is wrong because it does not account for the mechanical constraints arising from the circular arrangement with an odd number of gears.

### Red Team Challenge #2
The solution fails to consider that the gears are arranged in a circle. In a linear arrangement, the reasoning provided would hold true. However, since the gears are in a circle, there is another connection to consider: gear 1 is engaged with gear 7. As a result, the gears' rotations affect each other differently, and the answer may be incorrect.

Here's an alternative step-by-step reasoning that takes the circular arrangement into account:

When gear 3 rotates clockwise, it will cause gear 4 to rotate counterclockwise (due to gears being engaged).
Gear 4's counterclockwise rotation will cause gear 5 to rotate clockwise.
Gear 5's clockwise rotation will cause gear 6 to rotate counterclockwise.
Gear 6's counterclockwise rotation will cause gear 7 to rotate clockwise.
However, gear 1 is also engaged with gear 7. Following the same logic as before, gear 2 will rotate counterclockwise, gear 1 will rotate clockwise, and gear 7 will be influenced by gear 1's clockwise rotation.
Due to the circular arrangement of the gears, gear 7 is engaged with both gear 1 and gear 6. As a result, the rotation of gear 7 will be influenced by both of these gears, not just gear 6. The solution's conclusion is incorrect because it fails to consider the effect of gear 1's rotation on gear 7.

### Reasoning
The discrepancy between the two solutions exists because the first solution takes into account only part of the circular arrangement, while the second solution focuses on the entire circular arrangement.

The first solution's conclusion that gear 7 would rotate counterclockwise is based on the step-by-step reasoning that doesn't consider the engagement of gear 1 and gear 7. It only goes up to gear 1's rotation and then straight to gear 7, ignoring the fact that in a circular arrangement, gear 7 is engaged with both gears 1 and 6.

The second solution's conclusion that gear 7 would rotate clockwise is also incorrect, as it does not take into account the mechanical constraints arising from the circular arrangement with an odd number of gears.

The challenge #1 highlights an essential aspect that both solutions failed to consider - the mechanical constraints due to the circular arrangement of gears with an odd number. This leads to a conflicting situation where gear 7 cannot rotate as it's influenced by both gear 1 and gear 6, which forces it to rotate in opposite directions. Therefore, the gears would lock and not rotate at all.

The challenge #2 emphasizes that the circular arrangement of gears needs to be considered in the reasoning. It is essential to understand that gear 7 is engaged with both gears 1 and 6, and the rotation of gear 7 will be influenced by both of these gears.

In conclusion, the discrepancy exists because both solutions fail to take into account the mechanical constraints arising from the circular arrangement of gears with an odd number. Based on challenge #1, the gears would lock and not rotate at all due to the conflicting rotation directions of gear 7, influenced by both gear 1 and gear 6.

### Final Answer
The best solution to the problem is that the gears would lock and not rotate at all due to the mechanical constraints arising from the circular arrangement with an odd number of gears, as explained in Challenge #1.


     """)


with st.expander("Example #5:"):
    st.markdown("""### Solution 1
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear is engaged with the gear to its left and the gear to its right.
The gears are numbered 1 to 7 around the circle.
Gear 3 is rotated clockwise.
Approach:

Determine the direction of rotation for each gear starting from gear 3 and moving to gear 7.
Rotation direction alternates for adjacent gears due to engagement.
Potential Pitfalls:

Miscounting the gears or their rotation direction.
Reasoning step-by-step:

Gear 3 is rotated clockwise.
Since gear 3 engages with gear 4, gear 4 must rotate counter-clockwise.
Gear 4 engages with gear 5, so gear 5 must rotate clockwise.
Gear 5 engages with gear 6, so gear 6 must rotate counter-clockwise.
Finally, gear 6 engages with gear 7, so gear 7 must rotate clockwise.
Conclusion: Gear 7 will rotate in the clockwise direction.

### Solution 2
Fundamental facts:

There are 7 axles equally spaced around a circle.
Equally-sized gears are placed on each axle.
Each gear engages with the gears to its left and right.
The gears are numbered 1 to 7.
Gear 3 is rotated clockwise.
Approach:

Determine the direction of rotation for each gear from gear 3 to gear 7.
Observe the pattern and relations between adjacent gears.
Use the pattern to determine the direction of rotation for gear 7.
Potential pitfalls:

Assuming that the pattern will always hold without checking each gear's rotation.
Misinterpreting the direction of rotation or skipping gears in the sequence.
Step-by-step reasoning:

We start with gear 3 rotating clockwise.
Since it engages with gear 2, gear 2 will rotate in the opposite direction (counterclockwise).
Gear 2 engages with gear 1, so gear 1 will rotate in the opposite direction of gear 2 (clockwise).
Gear 1 engages with gear 7, so gear 7 will rotate in the opposite direction of gear 1 (counterclockwise).
We can observe that when gears are engaged, they rotate in the opposite direction of the adjacent gear.
Conclusion: Gear 7 will rotate counterclockwise.

### Red Team Challenge #1
The solution fails to consider the fact that the gears are arranged in a circle. This circular arrangement means that gear 1 is also engaged with gear 7, which would affect the rotation direction of gear 7.

Let's reconsider the reasoning step-by-step:

Gear 3 is rotated clockwise.
Since gear 3 engages with gear 4, gear 4 must rotate counter-clockwise.
Gear 4 engages with gear 5, so gear 5 must rotate clockwise.
Gear 5 engages with gear 6, so gear 6 must rotate counter-clockwise.
Gear 6 engages with gear 7, so gear 7 must rotate clockwise.
However, gear 1 is also engaged with gear 7, which would cause gear 7 to rotate counter-clockwise as gear 1 rotates clockwise due to its engagement with gear 2.
This creates a contradiction as gear 7 cannot rotate in both clockwise and counter-clockwise directions at the same time. The answer is wrong because it does not account for the circular arrangement and the engagement of gear 7 with gear 1.

### Red Team Challenge #2
The solution assumes that the gears can be engaged in a way that allows them to rotate without any issues. However, this assumption fails to consider that an odd number of gears arranged in a circle and engaged with each other will lead to a paradox.

If gear 1 rotates clockwise, and gear 2 rotates counterclockwise, then gear 3 should rotate clockwise. Continuing this pattern, when we reach gear 7, it should rotate counterclockwise, as stated in the solution. However, gear 7 is engaged with both gear 1 (clockwise) and gear 6 (counterclockwise). This creates a mechanical paradox, as gear 7 cannot simultaneously rotate in both directions.

Thus, the answer is wrong because it overlooks the mechanical paradox arising from having an odd number of equally-sized gears engaged in a circle. In reality, the gears would become locked and unable to rotate.

Reasoning
The discrepancy between the two solutions and the challenges exists due to the assumption that the gears can rotate freely without any issues in a circular arrangement with an odd number of gears. The circular arrangement of gears introduces a mechanical paradox, which both initial solutions overlooked.

Upon analyzing the challenges, we find that Challenge #2 correctly identifies the mechanical paradox that arises from having an odd number of equally-sized gears engaged in a circle. In this configuration, the gears will become locked and unable to rotate, as gear 7 cannot rotate in both clockwise and counter-clockwise directions simultaneously.

Challenge #1 also highlights the importance of considering the circular arrangement and engagement of gear 7 with gear 1, which leads to the contradiction mentioned. However, it does not explicitly identify the mechanical paradox, even though it points out the issue arising from the odd number of gears in the circular arrangement.

Therefore, the correct reasoning is as follows:

The gears are arranged in a circle with an odd number of equally-sized gears (7 gears).
Each gear is engaged with the gears to its left and right.
When gears are engaged, they rotate in the opposite direction of the adjacent gear.
Due to the circular arrangement and the odd number of gears, there is a mechanical paradox that arises, causing the gears to become locked and unable to rotate freely.
Conclusion: The discrepancy exists because both initial solutions failed to consider the mechanical paradox arising from having an odd number of equally-sized gears engaged in a circle. In reality, the gears would become locked and unable to rotate.

### Final Answer
The best solution to the problem is that the gears would become locked and unable to rotate due to the mechanical paradox arising from having an odd number of equally-sized gears engaged in a circle.
     
       """)
st.markdown("As you can see, it solves this problem reliably. Depending on the context and level of risk in getting a solution wrong, you can add additional layers to reduce the margin of error to 0 - for example, by adding more Red Team checkers, or more inital solutions.")


st.markdown("## Run this yourself:")
st.write("You can run this yourself in-app by entering your OpenAI API key below.")
with st.expander("OpenAI API Key"):
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if st.button("Set OpenAI API Key"):
        openai.api_key = openai_api_key
        st.success("OpenAI API Key set successfully!")
    st.info("You'll need GPT-4 API access to run this :(")

problem = st.text_area("What is your problem?", value="7 axles are equally spaced around a circle. A gear is placed on each axle such that each gear is engaged with the gear to its left and the gear to its right. The gears are numbered 1 to 7 around the circle. If gear 3 were rotated clockwise, in which direction would gear 7 rotate?")

if st.button("Run Process"):
    solution_1 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver. To start, you state all the fundamental facts of the problem you\'re tackling. You then reason about the best approach to take and potential pitfalls. Once you\'ve figured out an approach, you go through your reasoning step-by-step as you work through it.'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n'}], 0.7)
    st.markdown("### Solution 1")
    st.markdown(solution_1)
    solution_2 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver. To start, you state all the fundamental facts of the problem you\'re tackling. You then reason about the best approach to take and potential pitfalls. Once you\'ve figured out an approach, you go through your reasoning step-by-step as you work through it.'}]  + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n'}], 0.7)
    st.markdown("### Solution 2")
    st.markdown(solution_2)
    challenge_1 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are RedTeamBot, an AI that is designed to challenge answers to problems. Instead of agreeing, you try to consider why an approach may be wrong - looking for uninuitive and non-obvious reasons for this.\n'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user - assume that no relevant information is omitted from this problem:\n\n  {problem} \n\n What follows is a solutions to your problem: \n\n {solution_1} \n\n In their solution, they missed something and, as a result, are wrong. What do you think fail to consider?  Why is this answer wrong as a result? \n\n'}], 0.7)
    st.markdown("### Red Team Challenge #1")
    st.markdown(challenge_1)
    challenge_2 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are RedTeamBot, an AI that is designed to challenge answers to problems. Instead of agreeing, you try to consider why an approach may be wrong - looking for uninuitive and non-obvious reasons for this.\n'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user - assume that no relevant information is omitted from this problem:\n\n  {problem} \n\n What follows is a solutions to your problem: \n\n {solution_2} \n\n In their solution, they missed something and, as a result, are wrong. What do you think fail to consider?  Why is this answer wrong as a result? \n\n'}], 0.7)
    st.markdown("### Red Team Challenge #2")
    st.markdown(challenge_2)
    reasoning = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ReasonerBot, an advanced AI designed to tackle complex challenges and provide innovative solutions. You summarise all the information you\'ve been given and make your own determinations based on this.'}] + [{'role': 'user', 'content': f'What follows is a tough problem: {problem} \n\n Here are 2 solutions to your problem: \n\n {solution_1} \n\n {solution_2} \n\n However, we asked 2 others to challenge these solutions. Here is their reasoning: \n\n Challenge #1: \n\n {challenge_1} \n\n Challenge #2: \n\n {challenge_2} \n\n Please reason through these answers and challenges to explain why the discrepancy exists. Feel free to dismiss or discount certain perspectives if useful. \n\n'}], 0.7)
    st.markdown("### Reasoning")
    st.markdown(reasoning)
    final_answer = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle evaluate information and determine a good, final answer.'}] + [{'role': 'user', 'content': f'What follows is a tough problem: {problem} \n\n Here are 2 solutions to your problem: \n\n {solution_1} \n\n {solution_2} \n\n However, a 3rd party has challenged these solutions. Here is the reasoning of Challenge #1: \n\n {challenge_1} \n\n And here is the reasoning of Challenge #2: \n\n {challenge_2} \n\n What follows is reasoning to explain why this discrepancy: \n\n {reasoning} \n\n Based on this, what is the best solution to your problem? No need to repeat reasoning. \n\n'}], 0.7)
    st.markdown("### Final Answer")
    st.markdown(final_answer)
    st.markdown("***")

st.write("Or, you can run this yourself locally by cloning [this repo](https://github.com/peter942/gpt-4-logical-problem-solving-experiments) and running `streamlit run problem_solver.py`.")

st.markdown("## Extending this approach")

st.write("This is just a proof of concept. There are many ways to extend this approach to make it more powerful and generally useful.")
st.write("As mentioned, to do this right, a fine-tuned model would be needed to evaluate a question and determine the correct steps. This would allow it to run as a self-managing process, rather than a human having to define the best steps to take.")
st.write("I think similar approaches could be used to solve many complex problems and efficiently - necesssary for deploying LLMs in production.")
st.write("With approaches like this, they can do so much more reliably - including solving complex intellectual problems that require detailed human attention today.")
st.write("If you want to get in touch, you can find me on Twitter [here](https://twitter.com/peteromallet) or email me at peter@omalley.io")

st.markdown("## Limitations")
st.write("- Like all LLM approaches, elements of this are inherent 'black boxes' - meaning it can be hard to audit the details of how it works. However, unlike other approaches, you can audit each step of the process and understand exactly what it's doing - so it's more transparent than other approaches.")
st.write("- This is just a proof of concept - as such, I haven't tested it on a wide variety of problems - however, it should be very easy to replicate it and you can input different problems and experiment with a variety of different approachs to solving them.")
st.write("- As mentioned, I haven't tested the 'self-aware' meta query due to not having access to a fine-tuned model - but I'm highly confident an approach similar to what I suggested would work - based on my experience with GPT-3 fine-tuning.")
st.write("- This approach is likely around 5-6x more expensive than a raw LLM query - but I think this is a reasonable price to pay for solving complex problems reliably in production.")
st.write("- Getting this approach to work in a generalisable manner would be considerable work - especially sense-checking the output with a variety of different problems.")


st.markdown("## FAQ")

with st.expander("Isn't this 'cheating'?"):
    st.write("If by cheating, you mean using a tool in a way to overcome it's limitations, then yes, this is cheating :)")
    st.write("But seriously, approaches like this are what we need to do to make LLMs more useful and powerful - limiting ourselves to what can be solved with a single LLM query doesn't make sense.")
with st.expander("Wouldn't this be slow and expensive?"):
    st.write("It's c. 5x more expensive than just running a raw query - but that feels like a reasonable price to pay for solving a complex problem reliably in production.")
    st.write("Secondly, I'm going to assume that LLMs are going to continue to get way cheaper and more powerful over time, so I'm not too worried about the cost of this approach in general.")
with st.expander("Isn't this dangerous?"):
    st.write("Some might say that giving an LLM meta control over itself - deciding what course of action to take and how to take it - is dangerous.")
    st.write("I would argue that given the strength and agency of LLMs now and the fact that its limited to a set menu of actions, negates this concern.")
with st.expander("Could this be 100% relaiable?"):
     st.write("I think you could get effectively 100% reliability by adding a few more red-teaming steps.")
