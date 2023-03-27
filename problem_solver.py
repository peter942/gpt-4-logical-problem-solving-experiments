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

st.markdown("### The approaches an LLM can combine to solve a tricky problem")
st.markdown("An LLM can use a variety of approaches to solve a problem - these are queries that it can make of itself (or of other systems) in pursuing the best solution to a problem.")    
st.markdown("As per the above, based on its own assessment of itself and the problem, the LLM can then decide which combination of approaches to take - I'll cover this next.")
st.markdown("Below are a few examples of what these pieces might be that it can combine:")
st.markdown("**1. Directly querying the LLM:** for simple problems, this may be the best and most efficient approach.")
st.markdown("**2. Red Teaming itself:** for problems where it's likely to be biased, it can challenge itself and have a second query determine whether its challenge is fair.")  
st.markdown("**3. Calling on multiple perspectives:** for example, for a visual problem, it might ask itself to imagine a problem in the physical world of visualise it with ascii.")
st.markdown("**4. Calling on the same perspective multiple times:** for problems where it's likely to be inconsistent, this may be the best approach")

st.markdown("### How it can determine which of use these pieces to use")
st.markdown("Rather than it deciding on what approach to take and how to take it being 'baked in' to a single LLM query, I would say that what makes sense is for this to be a layer on top of the query - a meta-query that determines the best combination of approaches to take.")
st.markdown("Some examples of combinations of approaches might be:")
st.markdown("**1. For a problem where it's likely to fall into a common pitfall:** asking for 2 normal perspectives and a red teaming perspective")
st.markdown("**2. For a visual problem:** asking for a visual perspective and a textual perspective in order to overcome the limitations of the LLM's visual understanding.")
st.markdown("**3. For a problem where it's likely to have an unintuitive answer:** asking for a contrarian perspective and a normal-problem-solving perspective")

st.markdown("Each path should then be sense-checked by a meta-query that determines whether the path is likely to be correct or not.")

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

st.markdown("### How can you determine the right answer?")

st.write("In order to determine the best answer or combinations of answers, I set up a reasoning step, where it reasons through contradictions and inconsistencies in the answers it gets from the different perspectives.")
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
Let's analyze the problem step by step:

Gear 3 is rotated clockwise.
Since gear 3 is engaged with gear 2, gear 2 will rotate counterclockwise (opposite direction of gear 3).
Gear 2 is engaged with gear 1, so gear 1 will rotate clockwise (opposite direction of gear 2).
Gear 1 is engaged with gear 7, so gear 7 will rotate counterclockwise (opposite direction of gear 1).
Hence, if gear 3 were rotated clockwise, gear 7 would rotate counterclockwise.

### Solution 2
To determine the direction in which gear 7 would rotate when gear 3 is rotated clockwise, we need to consider the sequence of gear engagements.

When gear 3 rotates clockwise, gear 4 (engaged with gear 3) will rotate counterclockwise.

Gear 5, engaged with gear 4, will then rotate clockwise.

Gear 6, engaged with gear 5, will rotate counterclockwise.

Finally, gear 7, engaged with gear 6, will rotate clockwise.

So, when gear 3 is rotated clockwise, gear 7 will rotate in a clockwise direction.

### Red Team Challenge #1
Both solutions missed the fact that the gears are arranged in a circle, and their engagement pattern will be different from a linear arrangement. When gears are engaged in a circular pattern, the direction of rotation changes after a full circle.

Let's analyze the problem again:

Gear 3 is rotated clockwise.
Gear 2, engaged with gear 3, will rotate counterclockwise.
Gear 1, engaged with gear 2, will rotate clockwise.
Gear 7, engaged with gear 1, will rotate counterclockwise.
Gear 6, engaged with gear 7, will rotate clockwise.
Gear 5, engaged with gear 6, will rotate counterclockwise.
Gear 4, engaged with gear 5, will rotate clockwise.
However, since gear 4 is engaged with gear 3, this will cause gear 3 to rotate counterclockwise. But, we initially stated that gear 3 is rotated clockwise. This system creates a paradox and cannot exist with equally spaced gears in a circle. The system would lock up and not be able to rotate, as the gears' motion would contradict each other. So, both solutions are incorrect because they don't account for the circular arrangement and its resulting paradox.

### Red Team Challenge #2
Both answers missed the fact that the gears are equally spaced around a circle, which means that gear 7 would also be engaged with gear 6 and gear 1 simultaneously. This creates a closed loop of gears, which makes it impossible for all gears to rotate freely without any constraints.

In a closed loop of gears with an odd number of gears (such as this case with 7 gears), the rotation of the gears is not possible without putting excessive force on the gears, causing slippage or damage. This is because, in a closed loop with an odd number of gears, the last gear in the loop would need to rotate in the same direction as the first gear to maintain engagement, which is not possible due to the direction of rotation of the intermediary gears.

Thus, both answers are incorrect as they didn't consider the constraints imposed by the closed loop of gears with an odd number of gears. The actual answer is that the gears cannot rotate freely in this configuration.

### Reasoning
The discrepancy in the answers and challenges exists because the initial solutions failed to account for the circular arrangement of gears and the constraints it imposes. The challenges presented correctly identified the issues associated with the circular arrangement of an odd number of gears.

In a circular arrangement with an odd number of gears, the direction of rotation changes after a full circle, creating a paradox in the system, as pointed out in Challenge #1. The gears' motion would contradict each other, causing the system to lock up and not be able to rotate. This fact was not considered in the initial solutions.

Challenge #2 also highlights the constraints imposed by the closed loop of gears with an odd number of gears. In such a setup, the last gear in the loop would need to rotate in the same direction as the first gear to maintain engagement, which is not possible due to the direction of rotation of the intermediary gears. This constraint makes it impossible for all gears to rotate freely without causing slippage or damage.

Therefore, the discrepancy exists because the initial solutions did not consider the critical factors of the circular arrangement and the constraints it imposes on an odd number of equally spaced gears. The actual answer is that the gears cannot rotate freely in this configuration.

### Final Answer
The best solution to the problem is that the gears cannot rotate freely in this configuration with an odd number of equally spaced gears arranged in a circle. Both initial solutions failed to account for the circular arrangement and the constraints it imposes on the system. The challenges presented correctly identified the issues associated with the circular arrangement of an odd number of gears, which lead to a paradox in the system and prevents the gears from rotating freely without causing slippage or damage.""")

with st.expander("Example #2:"):
        st.markdown("""### Solution 1
To determine the direction in which gear 7 would rotate, we can analyze the chain of gears from gear 3 to gear 7. When two gears are engaged, rotating one gear in a particular direction causes the other gear to rotate in the opposite direction.

Here is the sequence of gears from gear 3 to gear 7:

Gear 3 rotates clockwise.
Gear 4 engages with gear 3, so it rotates counterclockwise.
Gear 5 engages with gear 4, so it rotates clockwise.
Gear 6 engages with gear 5, so it rotates counterclockwise.
Gear 7 engages with gear 6, so it rotates clockwise.
Therefore, if gear 3 is rotated clockwise, gear 7 would rotate in the clockwise direction.

### Solution 2
To determine the direction in which gear 7 would rotate when gear 3 is rotated clockwise, we can analyze the gear connections between them.

When gear 3 rotates clockwise, it causes gear 4 (engaged with gear 3) to rotate counterclockwise.
As gear 4 rotates counterclockwise, it causes gear 5 (engaged with gear 4) to rotate clockwise.
Similarly, when gear 5 rotates clockwise, it causes gear 6 (engaged with gear 5) to rotate counterclockwise.
Finally, as gear 6 rotates counterclockwise, it causes gear 7 (engaged with gear 6) to rotate clockwise.
So, when gear 3 is rotated clockwise, gear 7 rotates in the clockwise direction.

### Red Team Challenge #1
Both answers assume that gears 3 to 7 form a linear chain, but they do not take into account that these gears are arranged in a circle. In a circular arrangement, the gears' directions of rotation can be affected by their engagements with other gears in the circle, not just their immediate neighbors.

In this case, gear 1 is engaged with both gear 7 and gear 2, and gear 2 is engaged with gear 3. When gear 3 rotates clockwise, it causes gear 2 to rotate counterclockwise, which in turn causes gear 1 to rotate clockwise. Since gear 1 is engaged with gear 7, it will affect gear 7's rotation as well.

To determine the direction in which gear 7 would rotate when gear 3 is rotated clockwise, we need to consider the combined effect of gears 1 and 6 on gear 7:

Gear 6 rotates counterclockwise (as mentioned in both solutions) and causes gear 7 to rotate clockwise.
Gear 1 rotates clockwise (due to gear 2's counterclockwise rotation) and, being engaged with gear 7, causes gear 7 to rotate counterclockwise.
The opposing rotations caused by gears 1 and 6 cancel each other out, causing gear 7 to remain stationary. Therefore, if gear 3 is rotated clockwise, gear 7 would not rotate at all. The original solutions did not consider this possibility and missed the effect of gear 1 on gear 7's rotation.

### Red Team Challenge #2
Both solutions assume that the gears are only engaged with their immediate neighbors and do not take into consideration that gear 1 could also be engaged with gear 7, forming a closed loop.

In a closed loop system, the direction of rotation of the gears will not be as straightforward as described in both solutions. If gear 1 is engaged with gear 7, it can affect the direction of rotation of gear 7 when gear 3 is rotated clockwise. The solutions provided do not account for this possibility, and as a result, their conclusions might be incorrect.

To accurately determine the direction in which gear 7 would rotate when gear 3 is rotated clockwise, we need to consider the engagement between gear 1 and gear 7 and analyze the entire gear system as a closed loop.

### Reasoning
The discrepancy between the original solutions and the challenges exists because the original solutions only consider the linear chain of gears from gear 3 to gear 7, without taking into account their arrangement in a circle and the possible engagement between gear 1 and gear 7. The challenges highlight the circular nature of the gear arrangement and the potential effect of gear 1 on gear 7's rotation, which was not considered in the original solutions.

To resolve this discrepancy, we need to analyze the entire gear system as a closed loop and consider the engagement between gear 1 and gear 7.

Gear 3 rotates clockwise, causing gear 2 to rotate counterclockwise.
Gear 2 rotates counterclockwise, causing gear 1 to rotate clockwise.
Gear 1 rotates clockwise, causing gear 7 to rotate counterclockwise.
Gear 1 also rotates clockwise, causing gear 6 to rotate counterclockwise.
Gear 6 rotates counterclockwise, causing gear 5 to rotate clockwise.
Gear 5 rotates clockwise, causing gear 4 to rotate counterclockwise.
Gear 4 rotates counterclockwise, causing gear 3 to rotate clockwise.
Now, we can see that gear 7 is affected by both gear 1 and gear 6. Gear 1 causes gear 7 to rotate counterclockwise, while gear 6 causes gear 7 to rotate clockwise. Since these two rotations cancel each other out, gear 7 remains stationary.

Therefore, if gear 3 is rotated clockwise, gear 7 would not rotate at all. The original solutions did not consider the effect of gear 1 on gear 7, which led to the discrepancy between the original solutions and the challenges.

### Final Answer
The best solution to the problem is that if gear 3 is rotated clockwise, gear 7 would not rotate at all. This is because the rotations caused by gears 1 and 6 on gear 7 cancel each other out, resulting in a stationary gear 7.""")


with st.expander("Example #3:"):
        st.markdown("""### Solution 1
To determine the direction of rotation for gear 7, we need to consider how the motion gets transmitted through the gears.

When two gears are engaged, if one gear rotates clockwise, the other gear will rotate counterclockwise and vice versa.

Starting with gear 3 rotating clockwise:

Gear 2 will rotate counterclockwise (since it's engaged with gear 3)
Gear 1 will rotate clockwise (since it's engaged with gear 2)
Gear 7 will rotate counterclockwise (since it's engaged with gear 1)
Gear 6 will rotate clockwise (since it's engaged with gear 7)
Gear 5 will rotate counterclockwise (since it's engaged with gear 6)
Gear 4 will rotate clockwise (since it's engaged with gear 5)
Thus, if gear 3 were rotated clockwise, gear 7 would rotate in the counterclockwise direction.

### Solution 2
To determine the direction of rotation of gear 7 when gear 3 is rotated clockwise, we need to examine the pattern of rotation between connected gears.

When two gears are engaged, they rotate in opposite directions. So, when one gear rotates clockwise, the gear it is engaged with will rotate counterclockwise, and vice versa.

Here's a step-by-step breakdown of the gears' rotations:

Gear 3 rotates clockwise.
Gear 4, engaged with gear 3, will rotate counterclockwise.
Gear 5, engaged with gear 4, will rotate clockwise.
Gear 6, engaged with gear 5, will rotate counterclockwise.
Gear 7, engaged with gear 6, will rotate clockwise.
So, when gear 3 rotates clockwise, gear 7 will rotate in the same direction, which is clockwise.

### Red Team Challenge #1
The solution provided is incorrect because it failed to account for the fact that gear 1 is also engaged with gear 7 in the circular arrangement. This means that the motion transmission between gears is more complex than the simple linear chain described.

To find the correct answer, let's reconsider the motion transmission:

Gear 3 rotates clockwise
Gear 2 rotates counterclockwise (engaged with gear 3)
Gear 1 rotates clockwise (engaged with gear 2)
Gear 7 rotates counterclockwise (engaged with gear 1)
However, gear 1 is also engaged with gear 7, which would cause gear 7 to rotate clockwise. This creates a contradiction in the motion transmission.
In reality, the gears cannot rotate freely in this configuration as each gear experiences opposing forces from its two neighboring gears. The circular arrangement creates a locked system where the gears are unable to rotate without external forces causing deformation or slippage between the gears.

### Red Team Challenge #2
This answer is wrong because it failed to consider the circular arrangement of the gears. The gears are not arranged in a straight line but rather in a circle, which influences their rotation pattern.

Here's the corrected step-by-step breakdown of the gears' rotations:

Gear 3 rotates clockwise.
Gear 4, engaged with gear 3, will rotate counterclockwise.
Gear 5, engaged with gear 4, will rotate clockwise.
Gear 6, engaged with gear 5, will rotate counterclockwise.
Gear 7, engaged with gear 6, will rotate clockwise.
However, we must also consider that gear 7 is engaged with gear 1, which will affect its rotation. Since gear 7 is rotating clockwise, gear 1 will rotate counterclockwise. This will, in turn, affect gear 2, which will rotate clockwise. Finally, gear 2's rotation will affect gear 3, the starting point of our analysis.

With these additional factors, the rotation pattern of the gears may not be as simple as initially presented. The interaction between gears 1, 2, and 3 may cause more complex behavior in gear 7's rotation, making it impossible to definitively conclude that gear 7 will rotate clockwise.

### Reasoning
The discrepancy in the provided solutions and challenges arises due to the incomplete analysis of the circular gear arrangement. In a linear gear arrangement, it is straightforward to determine the direction of rotation of each gear, as they only engage with one other gear at a time. However, in this circular arrangement, gears engage with two neighboring gears, making the motion transmission more complex.

Both solutions have not considered the circular arrangement and the impact of gear 1 on gear 7 properly. The challenges provide a more insightful analysis of the problem.

Challenge #1 correctly identifies that the gears cannot rotate freely in this configuration, as each gear experiences opposing forces from its two neighboring gears. The circular arrangement creates a locked system where the gears are unable to rotate without external forces causing deformation or slippage between the gears.

Challenge #2 also acknowledges the impact of gear 1 on gear 7 and indicates that the interaction between gears 1, 2, and 3 may cause more complex behavior in gear 7's rotation, making it impossible to definitively conclude that gear 7 will rotate clockwise.

In conclusion, the discrepancy arises from the incomplete analysis of the circular arrangement of gears and the effect of neighboring gears on each other. The correct answer is that the gears cannot rotate freely in this configuration due to the opposing forces from their neighboring gears, creating a locked system.

### Final Answer
The best solution to the problem is that the gears cannot rotate freely in this configuration due to the opposing forces from their neighboring gears, creating a locked system.
        
        """)


with st.expander("Example #4:"):
     st.markdown("""
     ### Solution 1
To determine the direction in which gear 7 would rotate, we can analyze the chain of gears from gear 3 to gear 7. When two gears are engaged, they always rotate in opposite directions. Therefore, we can deduce the rotation direction for each gear in the chain as follows:

Gear 3 rotates clockwise (given).
Gear 4 must rotate counterclockwise because it is engaged with gear 3.
Gear 5 must rotate clockwise because it is engaged with gear 4.
Gear 6 must rotate counterclockwise because it is engaged with gear 5.
Gear 7 must rotate clockwise because it is engaged with gear 6.
So, if gear 3 were rotated clockwise, gear 7 would rotate in the clockwise direction.

### Solution 2
To determine the direction of rotation for gear 7 when gear 3 is rotated clockwise, we need to consider the pattern of rotation between consecutive gears.

When two gears are engaged, they rotate in opposite directions. So, if gear 3 rotates clockwise, gear 4 will rotate counterclockwise. Let's follow this pattern to gear 7:

Gear 3: clockwise (given)
Gear 4: counterclockwise (opposite of gear 3)
Gear 5: clockwise (opposite of gear 4)
Gear 6: counterclockwise (opposite of gear 5)
Gear 7: clockwise (opposite of gear 6)
Therefore, when gear 3 rotates clockwise, gear 7 will also rotate clockwise.

### Red Team Challenge #1
The solution provided seems to be incorrect because it fails to take into account that the gears are arranged in a circle. When gears are arranged in a circle, the direction of rotation is affected by the circular arrangement. The circular arrangement of gears creates a closed loop, which means that the initial gear's rotation is influenced by the last gear in the sequence.

In this case, gear 1 is engaged with gear 7, creating a closed loop. If gear 3 rotates clockwise, it will force gear 4 to rotate counterclockwise. However, gear 7, being engaged with gear 1, will also affect the rotation of gears in the sequence. Given the circular arrangement, it is not possible for all gears to rotate in the directions mentioned in the solution provided without causing the gears to jam.

Thus, there must be some error in the given arrangement of gears or their engagement, as the solution provided does not account for the circular arrangement and its implications on the gears' rotation.

### Red Team Challenge #2
In their solution, they missed the fact that the gears are arranged in a circle, and not in a straight line. When gears are arranged in a circle, the rotation direction changes when we consider the engagement of the first and the last gear in the circle.

Let's follow the pattern again, taking into account the circular arrangement:

Gear 3: clockwise (given)
Gear 4: counterclockwise (opposite of gear 3)
Gear 5: clockwise (opposite of gear 4)
Gear 6: counterclockwise (opposite of gear 5)
Gear 7: clockwise (opposite of gear 6)
Gear 1: counterclockwise (opposite of gear 7)
Gear 2: clockwise (opposite of gear 1)
Back to Gear 3: counterclockwise (opposite of gear 2)
In this case, due to the circular arrangement, gear 3 would have to rotate counterclockwise to engage with gear 2, which contradicts the initial given condition of gear 3 rotating clockwise. Thus, the problem, as presented, is not possible, and the solution is incorrect.

### Reasoning
The discrepancy in the provided solutions and challenges arises from the fact that the gears are arranged in a circle, forming a closed loop. The initial solutions did not take into account the engagement between gear 1 and gear 7, which influences the rotation of the gears in the sequence.

When gears are arranged in a circle, the rotation direction changes when we consider the engagement of the first and the last gear in the circle. This closed loop arrangement creates a situation where the gears cannot rotate without jamming, as the rotation directions of the gears in the sequence become contradictory.

To demonstrate this contradiction, let's follow the pattern again, taking into account the circular arrangement:

Gear 3: clockwise (given)
Gear 4: counterclockwise (opposite of gear 3)
Gear 5: clockwise (opposite of gear 4)
Gear 6: counterclockwise (opposite of gear 5)
Gear 7: clockwise (opposite of gear 6)
Gear 1: counterclockwise (opposite of gear 7)
Gear 2: clockwise (opposite of gear 1)
Back to Gear 3: counterclockwise (opposite of gear 2)
Now we have a contradiction: Gear 3 is initially given as rotating clockwise, but when considering the engagement between gear 1 and gear 7, gear 3 should rotate counterclockwise to engage with gear 2. This contradiction indicates that the problem, as presented, is not possible due to the circular arrangement of gears. The gears would jam in this setup, and hence, it is impossible to determine the rotation direction for gear 7 without modifying the gear arrangement or engagement.

### Final Answer
The best solution to the problem is that the given problem is not possible due to the circular arrangement of gears. The gears would jam in this setup, and hence, it is impossible to determine the rotation direction for gear 7 without modifying the gear arrangement or engagement.


     """)


with st.expander("Example #5:"):
    st.markdown("""### Solution 1
Let's analyze the situation step by step:

Gear 3 is rotated clockwise.
Since Gear 3 is engaged with Gear 4, Gear 4 will rotate in the opposite direction of Gear 3, which is counterclockwise.
Gear 4 is engaged with Gear 5, so Gear 5 will rotate in the opposite direction of Gear 4, which is clockwise.
Gear 5 is engaged with Gear 6, so Gear 6 will rotate in the opposite direction of Gear 5, which is counterclockwise.
Gear 6 is engaged with Gear 7, so Gear 7 will rotate in the opposite direction of Gear 6, which is clockwise.
Therefore, if Gear 3 were rotated clockwise, Gear 7 would rotate in the clockwise direction.

### Solution 2
Let's analyze the problem step by step:

There are 7 gears equally spaced around a circle.
Each gear is engaged with the gear to its left and right.
Gear 3 is rotated clockwise.
We need to determine the direction in which gear 7 would rotate.

Since the gears are engaged with their neighbors, when gear 3 rotates clockwise, it will cause gear 2 to rotate counterclockwise. Similarly, gear 1 will rotate clockwise as a result of gear 2's rotation.

Now, moving around the circle, we can deduce the direction of rotation for the remaining gears:

Gear 7 will rotate counterclockwise because gear 1 is rotating clockwise.
Gear 6 will rotate clockwise because gear 7 is rotating counterclockwise.
Gear 5 will rotate counterclockwise because gear 6 is rotating clockwise.
Gear 4 will rotate clockwise because gear 5 is rotating counterclockwise.
So, if gear 3 were rotated clockwise, gear 7 would rotate counterclockwise.

### Red Team Challenge #1
The solution provided seems to have missed an important aspect of the problem: that the gears are arranged in a circular setting. When gears are placed in a circle, the engagement between the first and the last gear must also be taken into account.

Here's a step by step analysis that considers the circular arrangement:

Gear 3 is rotated clockwise.
Gear 4 rotates counterclockwise (opposite to Gear 3).
Gear 5 rotates clockwise (opposite to Gear 4).
Gear 6 rotates counterclockwise (opposite to Gear 5).
Gear 7 rotates clockwise (opposite to Gear 6).
Gear 1 rotates counterclockwise (opposite to Gear 7).
Gear 2 rotates clockwise (opposite to Gear 1).
Gear 3 rotates counterclockwise (opposite to Gear 2).
However, this analysis leads us to a paradox, as we initially stated that Gear 3 rotates clockwise. In reality, the gears cannot rotate without slipping or breaking, as the circular arrangement creates a closed system where the opposite rotations of adjacent gears prevent continuous motion. Therefore, the solution provided is incorrect because it does not take into account the constraints created by the circular arrangement of gears.

### Red Team Challenge #2
I think the solution provided is incorrect because it assumes that the gears are engaged in a linear fashion. However, the problem clearly states that the gears are arranged in a circle. This means that gear 7 is not only engaged with gear 1 but also with gear 6. The solution does not take this into account, which leads to an inaccurate conclusion.

Given that gear 7 is engaged with both gears 1 and 6, its direction of rotation cannot be deduced simply by considering the rotation of gear 1. Instead, we must also consider the combined effect of the rotations of gears 1 and 6 on gear 7, which might lead to a different conclusion or an ambiguous result where the direction of rotation of gear 7 cannot be determined.

### Reasoning
The discrepancy exists because the initial solutions provided do not take into account the constraints created by the circular arrangement of gears. In a circular arrangement, gears cannot rotate without slipping or breaking, as the opposite rotations of adjacent gears prevent continuous motion.

The challenges raised by others highlight the fact that, in a circular setting, the engagement between the first and the last gear must also be taken into account. This creates a closed system where the opposite rotations of adjacent gears prevent continuous motion. Therefore, the solutions provided are incorrect as they do not consider the constraints imposed by the circular arrangement of gears.

Here's the corrected analysis that takes into account the circular arrangement:

Gear 3 is rotated clockwise.
Gear 4 rotates counterclockwise (opposite to Gear 3).
Gear 5 rotates clockwise (opposite to Gear 4).
Gear 6 rotates counterclockwise (opposite to Gear 5).
Gear 7 rotates clockwise (opposite to Gear 6).
Gear 1 rotates counterclockwise (opposite to Gear 7).
Gear 2 rotates clockwise (opposite to Gear 1).
Gear 3 should rotate counterclockwise (opposite to Gear 2).
This leads to a paradox, as we initially stated that Gear 3 rotates clockwise. In reality, the gears cannot rotate without slipping or breaking, as the circular arrangement creates a closed system where the opposite rotations of adjacent gears prevent continuous motion. Therefore, it is impossible to determine the direction of rotation of Gear 7, as the system cannot function without breaking or slipping.

### Final Answer
The best solution to the problem is that it is impossible to determine the direction of rotation of Gear 7, as the circular arrangement of gears creates a closed system where the opposite rotations of adjacent gears prevent continuous motion. The gears cannot rotate without slipping or breaking.
    
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
    solution_1 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n'}], 0.7)
    st.markdown("### Solution 1")
    st.markdown(solution_1)
    solution_2 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n'}], 0.7)
    st.markdown("### Solution 2")
    st.markdown(solution_2)
    challenge_1 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are RedTeamBot, an AI that is designed to challenge answers to problems from first principles. You take the solutions given and you ALWAYS assume that they are wrong. You are okay with being highly disagreeable if need be.\n'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n What follows is a solutions to your problem: \n\n {solution_1} \n\n In their solution, they missed something and, as a result, are wrong. What do you think they missed? \n\n'}], 0.7)
    st.markdown("### Red Team Challenge #1")
    st.markdown(challenge_1)
    challenge_2 = chatgpt_prompt([{ 'role': 'system', 'content': 'You are RedTeamBot, an AI that is designed to challenge answers to problems from first principles. You take the solutions given and you ALWAYS assume that they are wrong. You are okay with being highly disagreeable if need be.\n'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n What follows is a solutions to your problem: \n\n {solution_2} \n\n In their solution, they missed something and, as a result, are wrong. What do you think they missed? \n\n'}], 0.7)
    st.markdown("### Red Team Challenge #2")
    st.markdown(challenge_2)
    reasoning = chatgpt_prompt([{ 'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'What follows is a tough problem: {problem} \n\n Here are 2 solutions to your problem: \n\n {solution_1} \n\n {solution_2} \n\n However, we asked 2 others to challenge these solutions. Here is their reasoning: \n\n Challenge #1: \n\n {challenge_1} \n\n Challenge #2: \n\n {challenge_2} \n\n Please reason through these answers and challenges to explain why the discrepancy exists. \n\n'}], 0.7)
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
