# Python Logical Problems – I/O, Data Types, Conditionals, Loops
# 1️
# . ATM Transaction Validator
# Problem Statement
# An ATM processes N withdrawal requests sequentially. Each request has an amount. Rules:
# ● Withdrawal amount must be a multiple of 100
# ● Account balance must never go negative
# ● For each transaction, print SUCCESS or FAILED
# Input
# InitialBalance
# N
# amount1
# amount2
# ...
# amountN
# Output
# SUCCESS
# FAILED
# SUCCESS
# ...
# FinalBalance
# Sample Input:
# 5000
# 4
# 1200
# 155
# 2000
# 2500
# Sample Output:
# SUCCESS
# FAILED
# SUCCESS
# FAILED
# 1800
# Hint:
# Update balance only if both conditions are satisfied.
# 2️
# . Smart Electricity Billing
# Problem Statement
# Electricity bill is calculated slab-wise:
# ● First 100 units → ₹3/unit
# ● Next 100 units → ₹5/unit
# ● Remaining → ₹8/unit
# If usage > 300 units, add 10% surcharge.
# Input:
# units
# Output:
# total_bill
# Sample Input
# 350:
# Sample Output:
# 1540
# Hint:
# Apply slabs incrementally, then apply surcharge conditionally.
# 3️
# . Password Strength Evaluator
# Problem Statement
# Given a password string:
# ● Must contain at least 1 digit
# ● Must contain at least 1 uppercase
# ● Length ≥ 8
# Print STRONG or WEAK.
# Input:
# password
# Output:
# STRONG
# Sample Input:
# Pass1234
# Sample Output:
# STRONG
# Hint:
# Loop through characters and count conditions manually.
# 4️
# . Traffic Signal Simulation
# Problem Statement
# A signal cycles every second:
# ● 1–30 → RED
# ● 31–45 → YELLOW
# ● 46–90 → GREEN
# Given a time T, print the signal color.
# Input:
# T
# Output:
# RED / YELLOW / GREEN
# Sample Input:
# 44
# Sample Output:
# YELLOW
# Hint:
# Use modulo arithmetic and range checks.
# 5️
# . Salary Deduction System
# Problem Statement
# Employee salary rules:
# ● Basic salary given
# ● If late days > 5 → deduct 5%
# ● If late days > 10 → deduct 10%
# ● If absent days > 2 → deduct additional 5%
# Input:
# salary
# late_days
# absent_days
# Output:
# final_salary
# Sample Input:
# 50000
# 8
# 1
# Sample Output:
# 47500
# Hint:
# Apply deductions cumulatively, not exclusively.
# 6️
# . Prime Range Analyzer
# Problem Statement
# Print count of prime numbers between A and B (inclusive).
# Input:
# A
# B
# Output:
# prime_count
# Sample Input:
# 10
# 30
# Sample Output:
# 6
# Hint:
# Check divisibility up to √n.
# 7️
# . Online Order Discount Engine
# Problem Statement
# Total order amount:
# ● ≥ 5000 → 20% discount
# ● ≥ 3000 → 10%
# ● ≥ 1000 → 5%
# ● Else → No discount
# Print final payable amount.
# Input:
# amount
# Output:
# payable_amount
# Sample Input:
# 3200
# Sample Output:
# 2880
# Hint:
# Apply only one highest applicable discount.
# 8️
# . Binary to Decimal Converter (Without Built-in)
# Problem Statement
# Given a binary number, convert to decimal.
# Input:
# binary_number
# Output:
# decimal_number
# Sample Input:
# 101101
# Sample Output:
# 45
# Hint:
# Process digits from right to left using powers of 2.
# 9️
# .Mobile Battery Drain Simulator
# Problem Statement
# Battery starts at 100%. Each app drains fixed % per minute. Stop when battery ≤ 0. Print minutes used.
# Input:
# drain_per_minute
# Output:
# minutes
# Sample Input
# 7
# Sample Output
# 15
# Hint:
# Use a loop until battery <= 0.
# 10. Exam Result Processor
# Problem Statement
# Input marks for 5 subjects:
# ● If any mark < 35 → FAIL
# ● Else average ≥ 75 → DISTINCTION
# ● Else PASS
# Input
# m1 m2 m3 m4 m5
# Output
# FAIL / PASS / DISTINCTION
# Sample Input
# 80 78 74 90 88
# Sample Output
# DISTINCTION
# Hint:
# First validate failure condition, then classify.
# 11. Number Compression Counter
# Problem Statement
# Given a number, count how many times it can be divided by 2 until it becomes odd.
# Input
# number
# Output
# count
# Sample Input
# 40
# Sample Output
# 3
# Hint:
# Use a loop and modulo check.
# 12️ . Vowel Frequency Analyzer
# Problem Statement
# Count total vowels in a given sentence (case-insensitive).
# Input
# sentence
# Output
# vowel_count
# Sample Input
# I Love Python
# Sample Output
# 4
# Hint:
# Normalize case before comparison.
# 13️ . Train Ticket Fare Calculator
# Problem Statement
# Fare rules:
# ● Distance × ₹2/km
# ● Senior citizen → 30% discount
# ● Child (<12) → 50% discount
# Input
# distance
# age
# Output
# fare
# Sample Input
# 200
# 65
# Sample Output
# 280
# Hint:
# Calculate base fare first, then apply age-based rule.
# 14️ . Number Pattern Validator
# Problem Statement
# Check if digits of a number are strictly increasing left to right.
# Input
# number
# Output
# YES / NO
# Sample Input
# 13579
# Sample Output
# YES
# Hint:
# Compare adjacent digits.
# 15️ . Smart Door Lock System
# Problem Statement
# User gets 3 attempts to enter correct PIN.
# ● Correct → ACCESS GRANTED
# ● All wrong → LOCKED
# Input
# correct_pin
# attempt1
# attempt2
# attempt3
# Output
# ACCESS GRANTED / LOCKED
# Sample Input
# 4321
# 1111
# 2222
# 4321
# Sample Output
# ACCESS GRANTED
# Hint:
# Exit loop early on success.
# 16️ . Water Tank Overflow Detector
# Problem Statement
# Tank capacity is 1000L. Inflow every minute given. Stop when overflow occurs and print minute number.
# Input
# N
# inflow1 inflow2 ... inflowN
# Output
# overflow_minute
# Sample Input
# 5
# 200 300 250 400 100
# Sample Output
# 4
# Hint :
# Accumulate volume gradually.
# 17️ . Armstrong Number Checker
# Problem Statement
# Check if a number equals sum of cubes of its digits.
# Input
# number
# Output
# YES / NO
# Sample Input
# 153
# Sample Output
# YES
# Hint:
# Extract digits using modulo and division.
# 18️ . Bus Seat Allocation
# Problem Statement
# Bus has 40 seats. For each booking request:
# ● If seats available → CONFIRMED
# ● Else → WAITLISTED
# Input
# N
# request1
# request2
# ...
# Output
# CONFIRMED / WAITLISTED
# Sample Input
# 3
# 15
# 10
# 20
# Sample Output
# CONFIRMED
# CONFIRMED
# WAITLISTED
# Hint:
# Track remaining seats.
# 19️ . Number Mirror Validator
# Problem Statement
# Reverse a number and check if original equals reversed.
# Input
# number
# Output
# PALINDROME / NOT PALINDROME
# Sample Input
# 1221
# Sample Output
# PALINDROME
# Hint:
# Build reverse using arithmetic.
# 20️ . Digital Lock Countdown
# Problem Statement
# Given a number, repeatedly subtract sum of its digits until result is a single digit.
# Input
# number
# Output
# final_digit
# Sample Input
# 987
# Sample Output
# 6
# Hint:
# Nested loops: digit sum inside reduction loop.