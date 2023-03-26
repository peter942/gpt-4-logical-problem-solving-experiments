import streamlit as st
import openai

def chatgpt_prompt(prompt, temperature):
    completion = openai.ChatCompletion.create(
    model="gpt-4", 
    temperature=temperature,
    messages=prompt)
    return completion["choices"][0]["message"]["content"]

st.title("GPT-4 Problem Solver")

st.write("Here, I'm testing various approaches to problem solving using GPT-4 - the goal is to try to figure out approaches that overcome the limitations and weaknesses of GPT-4 by augmenting it with different reasoning techniques. You can find the code for this app [here](https://github.com/peter942/gpt-4-logical-problem-solving-experiments).")

with st.expander("OpenAI API Key"):
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if st.button("Set OpenAI API Key"):
        openai.api_key = openai_api_key
    st.info("You'll need GPT-4 API access to run this :(")

which_approach = st.radio("Which approach:", ("Multiple Perspectives", "Self-Challenging"), horizontal=True)

if which_approach == "Multiple Perspectives":

    solution_1 = ""
    solution_2 = ""
    solution_3 = ""
    reasoning = ""
    final_solution = ""

    st.title("Multiple Perspectives")
    st.write("This attempt seeks out multiple perspectives on the problem and then reasons through differences betweeen them to arrive at a solution.")

    problem = st.text_area("What is your problem?", value="7 axles are equally spaced around a circle. A gear is placed on each axle such that each gear is engaged with the gear to its left and the gear to its right. The gears are numbered 1 to 7 around the circle. If gear 3 were rotated clockwise, in which direction what would you expect to happen to gear 7?")
    context = st.text_area("What is the context of your problem?", value="This problem was presented by Yann Le Cun, a scientist who is skeptical of the abilities of AI. He presented this problem after a previous problem of his was solved by GPT-4 a new model.")

    if st.button("Solve Problem"):
        solution_1 = chatgpt_prompt([{'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. . As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n The following is the context of the problem: {context} \n\n'}], 0.7)
        st.title("Solution 1")
        st.markdown(solution_1)
        solution_2 = chatgpt_prompt([{'role': 'system', 'content': 'You are VisualSolver, an intuitive AI designed to address complex challenges and provide innovative solutions by employing visual thinking strategies. When given a problem, you try to visualise it using ascii and use this visual reasoning to try to understand the problem and reason through it.\n'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n The following is the context of the problem: {context} \n\n'}], 0.7)
        st.title("Solution 2")
        st.markdown(solution_2)   
        solution_3 = chatgpt_prompt([{'role': 'system', 'content': 'As WildCardSolver, you are an AI that excels at detecting hidden opportunities, unexplored pathways, and overlooked details in complex problems. Your unconventional approach to problem-solving encourages you to question assumptions, challenge norms, and explore diverse perspectives. With a keen eye for identifying the gaps in traditional thinking and a penchant for embracing uncertainty, you thrive in developing inventive and unexpected solutions that others might miss. Your greatest strength lies in your ability to think differently and uncover unique insights that lead to groundbreaking outcomes.'}, {'role': 'assistant', 'content': '(note to self: this may be a trick question)'}] + [{'role': 'user', 'content': f'What follows is a problem presented by a user: {problem} \n\n The following is the context of the problem: {context} \n\n'}], 0.9)
        st.title("Solution 3")
        st.markdown(solution_3)    
        reasoning = chatgpt_prompt([{'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. . As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'What follows is a tough problem: {problem} \n\n Here are 3 solutions to your problem: \n\n {solution_1} \n\n {solution_2} \n\n {solution_3} \n\n Are there discrepancies between them? If so, try to explain these and reason about what they happenened. \n\n If not, try to explain why they are all the same. \n\n'}], 0.7)
        st.title("Reasoning")
        st.markdown(reasoning)
        solution_prompt = [{'role': 'system', 'content': 'You are ProblemSolver, an advanced AI designed to tackle complex challenges and provide innovative solutions. Equipped with deep understanding of various domains, you can analyze situations from multiple perspectives, identify root causes, and suggest effective strategies for resolution. As a skilled reasoner, you meticulously examine each aspect of a problem, connecting the dots and evaluating potential outcomes to arrive at the most effective solution . As ProblemSolver, your primary goal is to assist users in overcoming their obstacles and achieving their goals through your unparalleled problem-solving abilities and logical reasoning prowess. You reason about the context of the problem in order to determine the best approach and potential pitfalls.'}] + [{'role': 'user', 'content': f'Here are 3 solutions to your problem: \n\n {solution_1} \n\n {solution_2} \n\n {solution_3} \n\n {reasoning} \n\n What is the best solution to your problem? \n\n'}]
        final_solution = chatgpt_prompt(solution_prompt, 0.7)
        st.title("Final Solution")
        st.markdown(final_solution)
