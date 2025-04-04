import sys
import os
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.assessment import Assessment
from app.models.user import User
from datetime import datetime

# Create a test user instance
test_user = User(
    username='testuser',
    email='test@example.com',
    password_hash='test_hash',  # This would normally be hashed
    is_active=True,
    is_admin=True
)
# --- Data Pools for Generation ---

first_names = [
    "Alex", "Morgan", "Jordan", "Taylor", "Casey", "Riley", "Jamie", "Skyler",
    "Dakota", "Remi", "Rowan", "Charlie", "Finley", "Emerson", "Avery", "Kai",
    "Blake", "Drew", "Cameron", "Sage", "Quinn", "Reese", "Peyton", "Sawyer",
    "Devin", "Micah", "Logan", "Chris", "Sam", "Liam", "Olivia", "Noah", "Emma",
    "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia", "James", "Amelia",
    "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Martin", "Jackson", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson",
    "Carter", "Mitchell", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans"
]

departments_positions = {
    "Engineering": ["Software Engineer", "Senior Software Engineer", "Tech Lead", "Engineering Manager", "DevOps Engineer", "QA Engineer", "Systems Architect"],
    "Product": ["Product Manager", "Associate Product Manager", "Senior Product Manager", "Product Owner", "UX Researcher"],
    "Design": ["UI/UX Designer", "Graphic Designer", "Senior Designer", "Design Lead", "Interaction Designer"],
    "Analytics": ["Data Scientist", "Data Analyst", "Business Intelligence Analyst", "Machine Learning Engineer", "Data Engineer"],
    "Marketing": ["Marketing Specialist", "Content Strategist", "SEO Manager", "Digital Marketing Manager", "Social Media Coordinator"],
    "Sales": ["Sales Development Representative", "Account Executive", "Sales Manager", "Customer Success Manager", "Sales Operations Analyst"],
    "HR": ["HR Generalist", "Recruiter", "Talent Acquisition Specialist", "HR Manager", "Compensation Analyst"],
    "Finance": ["Accountant", "Financial Analyst", "Senior Financial Analyst", "Controller", "Finance Manager"],
    "Operations": ["Operations Coordinator", "Operations Manager", "Supply Chain Analyst", "Logistics Manager"]
}

review_periods = [f"Q{q} {y}" for y in [2023, 2024] for q in [1, 2, 3, 4]]

strength_phrases = [
    "Excellent communication skills", "Strong technical aptitude", "Great team player",
    "Proactive problem-solver", "Highly adaptable", "Detail-oriented",
    "Strong leadership potential", "Creative thinking", "Customer-focused",
    "Efficient time management", "Mentors junior team members", "Data-driven decision maker",
    "Excellent presentation skills", "Strong analytical abilities", "Takes initiative",
    "Collaborates effectively across teams", "Deep domain knowledge", "Manages complexity well",
    "Delivers high-quality results consistently", "Positive attitude", "Quick learner",
    "Strategic thinking", "Stakeholder management", "User empathy", "Code quality focus",
    "Infrastructure automation", "Security best practices", "Financial modeling", "Talent sourcing",
    "Process optimization", "Campaign management", "Negotiation skills"
]

improvement_phrases = [
    "Could improve time management", "Needs to enhance presentation skills",
    "Could be more proactive in communication", "Needs deeper technical understanding in X area",
    "Could improve documentation practices", "Needs to delegate more effectively",
    "Could focus more on strategic goals", "Needs to manage stakeholder expectations better",
    "Could improve handling of constructive feedback", "Needs to develop cross-functional collaboration",
    "Could enhance reporting clarity", "Needs to improve prioritization skills",
    "Could benefit from assertiveness training", "Needs to increase speed of delivery",
    "Could improve attention to detail on routine tasks", "Needs more experience with tool Y",
    "Could engage more in team discussions", "Needs to build confidence in area Z",
    "Could work on meeting deadlines more consistently", "Needs to refine requirements gathering"
]

goal_phrases = [
    "Lead a major project", "Mentor junior developers/colleagues", "Improve cross-team collaboration",
    "Launch new product feature", "Optimize data processing pipeline", "Publish research/blog post",
    "Implement CI/CD improvements", "Enhance security protocols", "Achieve X% sales target",
    "Improve customer satisfaction scores", "Develop a new training module", "Complete certification Z",
    "Streamline reporting process", "Reduce operational costs by Y%", "Improve team velocity",
    "Gain expertise in technology X", "Take on more leadership responsibilities", "Present at a conference",
    "Improve design system adoption", "Develop new marketing campaign strategy", "Refine onboarding process",
    "Master financial forecasting model", "Increase lead generation by W%"
]

comment_templates = [
    "{name} consistently exceeds expectations. Strengths in {strength1} and {strength2} are particularly notable.",
    "A solid performance from {name} this period. Key contributions include {goal1}.",
    "{name} is a valuable member of the team, demonstrating strong {strength1}.",
    "Performance meets expectations. {name} should focus on {improvement1} while continuing to leverage {strength1}.",
    "Excellent progress shown by {name}, particularly in achieving {goal1}.",
    "{name} has shown significant growth. Areas like {strength1} are strong, while {improvement1} is an area for development.",
    "Highly effective performer. {name}'s work on {goal1} has been impactful. Continue fostering {strength2}.",
    "Good contributions this quarter. {name} is working towards {goal2} and improving {improvement1}.",
    "{name} demonstrates potential. Key strengths include {strength1}. Next steps involve focusing on {goal1} and addressing {improvement1}.",
    "Reliable and consistent performer. {name}'s {strength1} makes them a dependable team member. Agreed focus on {goal2} for next period."
]

# --- Generation Logic ---

synthetic_assessments = []
used_names = set()

# Add the original 5
original_assessments = [
    Assessment(
        employee_name='John Doe',
        position='Senior Software Engineer',
        department='Engineering',
        review_period='Q1 2024',
        performance_rating=4.5,
        strengths='Strong technical skills, excellent problem-solving abilities, great team player',
        areas_for_improvement='Could improve documentation practices',
        goals='Lead a major project in Q2, mentor junior developers',
        comments='John has consistently delivered high-quality work and shown great leadership potential',
        author=test_user
    ),
    Assessment(
        employee_name='Jane Smith',
        position='Product Manager',
        department='Product',
        review_period='Q1 2024',
        performance_rating=4.8,
        strengths='Exceptional stakeholder management, strong product vision, excellent communication',
        areas_for_improvement='Could focus more on technical details',
        goals='Launch new product feature in Q2, improve cross-team collaboration',
        comments='Jane has been instrumental in driving product success and building strong relationships with stakeholders',
        author=test_user
    ),
    Assessment(
        employee_name='Mike Johnson',
        position='UI/UX Designer',
        department='Design',
        review_period='Q1 2024',
        performance_rating=4.2,
        strengths='Creative design solutions, attention to detail, user-centered approach',
        areas_for_improvement='Could improve time management',
        goals='Lead design system improvements, mentor junior designers',
        comments='Mike consistently delivers visually stunning and user-friendly designs that exceed expectations',
        author=test_user
    ),
    Assessment(
        employee_name='Sarah Williams',
        position='Data Scientist',
        department='Analytics',
        review_period='Q1 2024',
        performance_rating=4.9,
        strengths='Advanced analytical skills, innovative problem-solving, excellent research capabilities',
        areas_for_improvement='Could improve presentation skills',
        goals='Publish research paper, optimize data processing pipeline',
        comments='Sarah\'s work has significantly improved our data-driven decision-making processes',
        author=test_user
    ),
    Assessment(
        employee_name='Robert Brown',
        position='DevOps Engineer',
        department='Engineering',
        review_period='Q1 2024',
        performance_rating=4.7,
        strengths='Infrastructure automation expertise, strong security knowledge, excellent troubleshooting',
        areas_for_improvement='Could improve documentation',
        goals='Implement CI/CD improvements, enhance security protocols',
        comments='Robert has been crucial in maintaining our infrastructure reliability and security',
        author=test_user
    ),
    Assessment(
        employee_name='Dakota Smith',
        position='UI/UX Designer',
        department='Design',
        review_period='Q2 2024',
        performance_rating=4.3,
        strengths='Creative thinking, excellent presentation skills, campaign management',
        areas_for_improvement='Needs to increase speed of delivery',
        goals='Master financial forecasting model',
        comments='Highly effective performer. Dakota\'s work on master financial forecasting model has been impactful. Continue fostering campaign management.',
        author=test_user
    ),
    Assessment(
        employee_name='Micah Clark',
        position='Sales Operations Analyst',
        department='Sales',
        review_period='Q4 2024',
        performance_rating=4.3,
        strengths='Detail-oriented, infrastructure automation, campaign management',
        areas_for_improvement='Needs more experience with tool y',
        goals='Master financial forecasting model, increase lead generation by w%',
        comments='Performance meets expectations. Micah should focus on needs more experience with tool y while continuing to leverage detail-oriented.',
        author=test_user
    ),
    Assessment(
        employee_name='Finley Moore',
        position='Senior Software Engineer',
        department='Engineering',
        review_period='Q2 2024',
        performance_rating=4.0,
        strengths='Talent sourcing',
        areas_for_improvement='Needs to build confidence in area z, could engage more in team discussions',
        goals='Master financial forecasting model',
        comments='Finley is a valuable member of the team, demonstrating strong talent sourcing.',
        author=test_user
    ),
    Assessment(
        employee_name='Sophia Johnson',
        position='Supply Chain Analyst',
        department='Operations',
        review_period='Q4 2024',
        performance_rating=4.8,
        strengths='Collaborates effectively across teams, great team player',
        areas_for_improvement='Needs deeper technical understanding in x area, needs to develop cross-functional collaboration',
        goals='Lead a major project',
        comments='Sophia has shown significant growth. Areas like great team player are strong, while needs to develop cross-functional collaboration is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Emerson Baker',
        position='Associate Product Manager',
        department='Product',
        review_period='Q4 2024',
        performance_rating=4.9,
        strengths='Strong analytical abilities',
        areas_for_improvement='None noted this period.',
        goals='Achieve x% sales target, lead a major project',
        comments='Reliable and consistent performer. Emerson\'s strong analytical abilities makes them a dependable team member. Agreed focus on lead a major project for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Remi Perez',
        position='Sales Development Representative',
        department='Sales',
        review_period='Q3 2023',
        performance_rating=3.9,
        strengths='Excellent presentation skills, financial modeling',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Improve team velocity',
        comments='Remi has shown significant growth. Areas like excellent presentation skills are strong, while needs to build confidence in area z is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Amelia Walker',
        position='Operations Manager',
        department='Operations',
        review_period='Q4 2023',
        performance_rating=4.4,
        strengths='Proactive problem-solver, deep domain knowledge',
        areas_for_improvement='Could enhance reporting clarity',
        goals='Improve customer satisfaction scores',
        comments='Amelia is a valuable member of the team, demonstrating strong deep domain knowledge.',
        author=test_user
    ),
    Assessment(
        employee_name='Lucas Evans',
        position='Talent Acquisition Specialist',
        department='HR',
        review_period='Q1 2024',
        performance_rating=3.1,
        strengths='Collaborates effectively across teams, strong leadership potential, strong analytical abilities',
        areas_for_improvement='Needs more experience with tool y',
        goals='Improve design system adoption',
        comments='Excellent progress shown by Lucas, particularly in achieving improve design system adoption.',
        author=test_user
    ),
    Assessment(
        employee_name='Noah Williams',
        position='Digital Marketing Manager',
        department='Marketing',
        review_period='Q4 2024',
        performance_rating=4.3,
        strengths='Code quality focus, proactive problem-solver',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Increase lead generation by w%, develop new marketing campaign strategy',
        comments='Noah is a valuable member of the team, demonstrating strong proactive problem-solver.',
        author=test_user
    ),
    Assessment(
        employee_name='Peyton Taylor',
        position='SEO Manager',
        department='Marketing',
        review_period='Q3 2024',
        performance_rating=3.8,
        strengths='Efficient time management',
        areas_for_improvement='Needs to refine requirements gathering, needs more experience with tool y',
        goals='Lead a major project',
        comments='A solid performance from Peyton this period. Key contributions include lead a major project.',
        author=test_user
    ),
    Assessment(
        employee_name='Benjamin Clark',
        position='DevOps Engineer',
        department='Engineering',
        review_period='Q1 2023',
        performance_rating=4.2,
        strengths='Collaborates effectively across teams, efficient time management',
        areas_for_improvement='Needs to improve prioritization skills, needs to delegate more effectively',
        goals='Lead a major project, mentor junior developers/colleagues',
        comments='Benjamin demonstrates potential. Key strengths include collaborates effectively across teams. Next steps involve focusing on lead a major project and addressing needs to improve prioritization skills.',
        author=test_user
    ),
    Assessment(
        employee_name='Isabella King',
        position='Product Manager',
        department='Product',
        review_period='Q2 2023',
        performance_rating=4.3,
        strengths='Strong analytical abilities',
        areas_for_improvement='Needs to improve prioritization skills, could enhance reporting clarity',
        goals='Mentor junior developers/colleagues',
        comments='A solid performance from Isabella this period. Key contributions include mentor junior developers/colleagues.',
        author=test_user
    ),
    Assessment(
        employee_name='Micah Brown',
        position='Business Intelligence Analyst',
        department='Analytics',
        review_period='Q3 2023',
        performance_rating=3.8,
        strengths='Code quality focus, detail-oriented',
        areas_for_improvement='Needs to manage stakeholder expectations better, needs to enhance presentation skills',
        goals='Lead a major project',
        comments='Micah has shown significant growth. Areas like code quality focus are strong, while needs to manage stakeholder expectations better is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Sawyer Turner',
        position='Systems Architect',
        department='Engineering',
        review_period='Q3 2023',
        performance_rating=4.5,
        strengths='Excellent presentation skills',
        areas_for_improvement='Could improve documentation practices',
        goals='Refine onboarding process',
        comments='Sawyer has shown significant growth. Areas like excellent presentation skills are strong, while could improve documentation practices is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Jordan King',
        position='Sales Development Representative',
        department='Sales',
        review_period='Q2 2023',
        performance_rating=3.9,
        strengths='Stakeholder management',
        areas_for_improvement='Could engage more in team discussions, could be more proactive in communication',
        goals='Complete certification z',
        comments='Reliable and consistent performer. Jordan\'s stakeholder management makes them a dependable team member. Agreed focus on complete certification z for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Dakota Turner',
        position='HR Generalist',
        department='HR',
        review_period='Q2 2024',
        performance_rating=4.1,
        strengths='Excellent presentation skills',
        areas_for_improvement='Needs to develop cross-functional collaboration, needs to delegate more effectively',
        goals='Improve design system adoption, streamline reporting process',
        comments='A solid performance from Dakota this period. Key contributions include improve design system adoption.',
        author=test_user
    ),
    Assessment(
        employee_name='Chris White',
        position='Account Executive',
        department='Sales',
        review_period='Q3 2024',
        performance_rating=4.0,
        strengths='Manages complexity well, delivers high-quality results consistently',
        areas_for_improvement='Needs to delegate more effectively, needs to build confidence in area z',
        goals='Master financial forecasting model',
        comments='Highly effective performer. Chris\'s work on master financial forecasting model has been impactful. Continue fostering manages complexity well.',
        author=test_user
    ),
    Assessment(
        employee_name='Isabella Robinson',
        position='Content Strategist',
        department='Marketing',
        review_period='Q4 2024',
        performance_rating=4.5,
        strengths='Mentors junior team members, proactive problem-solver',
        areas_for_improvement='Could improve attention to detail on routine tasks, could work on meeting deadlines more consistently',
        goals='Achieve x% sales target',
        comments='Isabella has shown significant growth. Areas like proactive problem-solver are strong, while could improve attention to detail on routine tasks is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Cameron Phillips',
        position='Operations Manager',
        department='Operations',
        review_period='Q2 2024',
        performance_rating=4.6,
        strengths='Strategic thinking, infrastructure automation',
        areas_for_improvement='Focus remains on leveraging strengths.',
        goals='Lead a major project',
        comments='Highly effective performer. Cameron\'s work on lead a major project has been impactful. Continue fostering infrastructure automation.',
        author=test_user
    ),
    Assessment(
        employee_name='Chris Young',
        position='Design Lead',
        department='Design',
        review_period='Q4 2024',
        performance_rating=4.8,
        strengths='Positive attitude, excellent communication skills',
        areas_for_improvement='None noted this period.',
        goals='Refine onboarding process',
        comments='Chris is a valuable member of the team, demonstrating strong positive attitude.',
        author=test_user
    ),
    Assessment(
        employee_name='Sam Roberts',
        position='Sales Operations Analyst',
        department='Sales',
        review_period='Q1 2024',
        performance_rating=3.9,
        strengths='Code quality focus, excellent presentation skills, quick learner',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Increase lead generation by w%, master financial forecasting model',
        comments='Excellent progress shown by Sam, particularly in achieving increase lead generation by w%.',
        author=test_user
    ),
    Assessment(
        employee_name='Alexander Thomas',
        position='Compensation Analyst',
        department='HR',
        review_period='Q3 2024',
        performance_rating=4.6,
        strengths='Customer-focused',
        areas_for_improvement='Needs deeper technical understanding in x area, could improve time management',
        goals='Lead a major project, take on more leadership responsibilities',
        comments='Highly effective performer. Alexander\'s work on take on more leadership responsibilities has been impactful. Continue fostering customer-focused.',
        author=test_user
    ),
    Assessment(
        employee_name='Harper Johnson',
        position='QA Engineer',
        department='Engineering',
        review_period='Q2 2023',
        performance_rating=4.0,
        strengths='Manages complexity well',
        areas_for_improvement='Needs to develop cross-functional collaboration',
        goals='Gain expertise in technology x',
        comments='Highly effective performer. Harper\'s work on gain expertise in technology x has been impactful. Continue fostering manages complexity well.',
        author=test_user
    ),
    Assessment(
        employee_name='Avery Rodriguez',
        position='Accountant',
        department='Finance',
        review_period='Q1 2023',
        performance_rating=3.4,
        strengths='Code quality focus',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Enhance security protocols, implement ci/cd improvements',
        comments='Highly effective performer. Avery\'s work on enhance security protocols has been impactful. Continue fostering code quality focus.',
        author=test_user
    ),
    Assessment(
        employee_name='Lucas Scott',
        position='Social Media Coordinator',
        department='Marketing',
        review_period='Q3 2023',
        performance_rating=5.0,
        strengths='Creative thinking',
        areas_for_improvement='Could be more proactive in communication',
        goals='Improve team velocity',
        comments='Highly effective performer. Lucas\'s work on improve team velocity has been impactful. Continue fostering creative thinking.',
        author=test_user
    ),
    Assessment(
        employee_name='Dakota Lee',
        position='Finance Manager',
        department='Finance',
        review_period='Q4 2023',
        performance_rating=3.3,
        strengths='Talent sourcing',
        areas_for_improvement='Could enhance reporting clarity',
        goals='Launch new product feature',
        comments='A solid performance from Dakota this period. Key contributions include launch new product feature.',
        author=test_user
    ),
    Assessment(
        employee_name='Chris Campbell',
        position='Machine Learning Engineer',
        department='Analytics',
        review_period='Q3 2024',
        performance_rating=4.2,
        strengths='Strong leadership potential',
        areas_for_improvement='Needs to enhance presentation skills, could be more proactive in communication',
        goals='Master financial forecasting model',
        comments='Performance meets expectations. Chris should focus on needs to enhance presentation skills while continuing to leverage strong leadership potential.',
        author=test_user
    ),
    Assessment(
        employee_name='Henry Smith',
        position='Customer Success Manager',
        department='Sales',
        review_period='Q2 2024',
        performance_rating=4.4,
        strengths='Positive attitude, takes initiative, talent sourcing',
        areas_for_improvement='Needs to delegate more effectively',
        goals='Increase lead generation by w%, launch new product feature',
        comments='Henry consistently exceeds expectations. Strengths in takes initiative and talent sourcing are particularly notable.',
        author=test_user
    ),
    Assessment(
        employee_name='Taylor Adams',
        position='UI/UX Designer',
        department='Design',
        review_period='Q3 2024',
        performance_rating=4.6,
        strengths='Positive attitude, deep domain knowledge',
        areas_for_improvement='Focus remains on leveraging strengths.',
        goals='Take on more leadership responsibilities',
        comments='Reliable and consistent performer. Taylor\'s deep domain knowledge makes them a dependable team member. Agreed focus on take on more leadership responsibilities for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Skyler Young',
        position='Systems Architect',
        department='Engineering',
        review_period='Q4 2023',
        performance_rating=3.9,
        strengths='Strong analytical abilities',
        areas_for_improvement='Could focus more on strategic goals, needs to improve prioritization skills',
        goals='Improve customer satisfaction scores',
        comments='Performance meets expectations. Skyler should focus on needs to improve prioritization skills while continuing to leverage strong analytical abilities.',
        author=test_user
    ),
    Assessment(
        employee_name='Sawyer Rodriguez',
        position='Accountant',
        department='Finance',
        review_period='Q4 2024',
        performance_rating=4.6,
        strengths='Deep domain knowledge, stakeholder management',
        areas_for_improvement='Could benefit from assertiveness training, could improve attention to detail on routine tasks',
        goals='Publish research/blog post',
        comments='Good contributions this quarter. Sawyer is working towards publish research/blog post and improving could benefit from assertiveness training.',
        author=test_user
    ),
    Assessment(
        employee_name='Blake Martinez',
        position='Content Strategist',
        department='Marketing',
        review_period='Q4 2023',
        performance_rating=4.0,
        strengths='Data-driven decision maker, great team player',
        areas_for_improvement='Needs to improve prioritization skills, needs to develop cross-functional collaboration',
        goals='Optimize data processing pipeline',
        comments='Blake demonstrates potential. Key strengths include great team player. Next steps involve focusing on optimize data processing pipeline and addressing needs to develop cross-functional collaboration.',
        author=test_user
    ),
    Assessment(
        employee_name='Sam Johnson',
        position='Logistics Manager',
        department='Operations',
        review_period='Q2 2023',
        performance_rating=4.0,
        strengths='Excellent presentation skills, manages complexity well',
        areas_for_improvement='Could benefit from assertiveness training, needs to delegate more effectively',
        goals='Develop a new training module',
        comments='A solid performance from Sam this period. Key contributions include develop a new training module.',
        author=test_user
    ),
    Assessment(
        employee_name='Benjamin Thomas',
        position='Systems Architect',
        department='Engineering',
        review_period='Q3 2024',
        performance_rating=4.6,
        strengths='Highly adaptable, delivers high-quality results consistently',
        areas_for_improvement='Focus remains on leveraging strengths.',
        goals='Lead a major project',
        comments='Performance meets expectations. Benjamin should focus on ongoing development while continuing to leverage highly adaptable.',
        author=test_user
    ),
    Assessment(
        employee_name='Drew Anderson',
        position='Associate Product Manager',
        department='Product',
        review_period='Q4 2024',
        performance_rating=4.1,
        strengths='Positive attitude, campaign management',
        areas_for_improvement='Could work on meeting deadlines more consistently, could improve time management',
        goals='Optimize data processing pipeline, refine onboarding process',
        comments='Good contributions this quarter. Drew is working towards optimize data processing pipeline and improving could improve time management.',
        author=test_user
    ),
    Assessment(
        employee_name='Olivia King',
        position='HR Generalist',
        department='HR',
        review_period='Q1 2024',
        performance_rating=4.6,
        strengths='Code quality focus, strong analytical abilities, detail-oriented',
        areas_for_improvement='Needs more experience with tool y',
        goals='Master financial forecasting model, improve design system adoption',
        comments='Reliable and consistent performer. Olivia\'s code quality focus makes them a dependable team member. Agreed focus on improve design system adoption for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Casey Smith',
        position='Accountant',
        department='Finance',
        review_period='Q4 2024',
        performance_rating=4.5,
        strengths='Manages complexity well, negotiation skills, delivers high-quality results consistently',
        areas_for_improvement='Could improve documentation practices',
        goals='Gain expertise in technology x, streamline reporting process',
        comments='Reliable and consistent performer. Casey\'s delivers high-quality results consistently makes them a dependable team member. Agreed focus on gain expertise in technology x for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Micah Jackson',
        position='Data Engineer',
        department='Analytics',
        review_period='Q2 2024',
        performance_rating=3.9,
        strengths='User empathy, strategic thinking, negotiation skills',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Publish research/blog post',
        comments='Performance meets expectations. Micah should focus on needs deeper technical understanding in x area while continuing to leverage user empathy.',
        author=test_user
    ),
    Assessment(
        employee_name='Emma Clark',
        position='Social Media Coordinator',
        department='Marketing',
        review_period='Q2 2023',
        performance_rating=4.7,
        strengths='Customer-focused, creative thinking, stakeholder management',
        areas_for_improvement='None noted this period.',
        goals='Improve design system adoption, streamline reporting process',
        comments='Emma demonstrates potential. Key strengths include customer-focused. Next steps involve focusing on streamline reporting process and addressing ongoing development.',
        author=test_user
    ),
    Assessment(
        employee_name='Drew Wilson',
        position='Controller',
        department='Finance',
        review_period='Q3 2024',
        performance_rating=4.7,
        strengths='Highly adaptable, excellent presentation skills, data-driven decision maker',
        areas_for_improvement='Needs to manage stakeholder expectations better',
        goals='Improve team velocity',
        comments='Performance meets expectations. Drew should focus on needs to manage stakeholder expectations better while continuing to leverage highly adaptable.',
        author=test_user
    ),
    Assessment(
        employee_name='Ava Harris',
        position='SEO Manager',
        department='Marketing',
        review_period='Q1 2024',
        performance_rating=3.8,
        strengths='Strong leadership potential, negotiation skills, user empathy',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Implement ci/cd improvements, launch new product feature',
        comments='Reliable and consistent performer. Ava\'s negotiation skills makes them a dependable team member. Agreed focus on implement ci/cd improvements for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Liam Anderson',
        position='Graphic Designer',
        department='Design',
        review_period='Q3 2023',
        performance_rating=4.3,
        strengths='Infrastructure automation, quick learner, strong analytical abilities',
        areas_for_improvement='Could improve attention to detail on routine tasks',
        goals='Reduce operational costs by y%, develop a new training module',
        comments='Good contributions this quarter. Liam is working towards reduce operational costs by y% and improving could improve attention to detail on routine tasks.',
        author=test_user
    ),
    Assessment(
        employee_name='Ava Hernandez',
        position='Accountant',
        department='Finance',
        review_period='Q2 2023',
        performance_rating=4.4,
        strengths='Customer-focused, stakeholder management, strategic thinking',
        areas_for_improvement='Could engage more in team discussions, needs to manage stakeholder expectations better',
        goals='Improve cross-team collaboration, implement ci/cd improvements',
        comments='Ava is a valuable member of the team, demonstrating strong strategic thinking.',
        author=test_user
    ),
    Assessment(
        employee_name='Sawyer Ramirez',
        position='Account Executive',
        department='Sales',
        review_period='Q2 2023',
        performance_rating=3.2,
        strengths='Strong leadership potential',
        areas_for_improvement='Needs to improve prioritization skills',
        goals='Launch new product feature',
        comments='Excellent progress shown by Sawyer, particularly in achieving launch new product feature.',
        author=test_user
    ),
    Assessment(
        employee_name='Amelia Parker',
        position='Accountant',
        department='Finance',
        review_period='Q4 2024',
        performance_rating=4.3,
        strengths='Takes initiative, data-driven decision maker, deep domain knowledge',
        areas_for_improvement='Could improve time management',
        goals='Refine onboarding process',
        comments='A solid performance from Amelia this period. Key contributions include refine onboarding process.',
        author=test_user
    ),
    Assessment(
        employee_name='Lucas Smith',
        position='Interaction Designer',
        department='Design',
        review_period='Q3 2023',
        performance_rating=4.9,
        strengths='Highly adaptable, data-driven decision maker, quick learner',
        areas_for_improvement='None noted this period.',
        goals='Enhance security protocols',
        comments='Lucas demonstrates potential. Key strengths include highly adaptable. Next steps involve focusing on enhance security protocols and addressing ongoing development.',
        author=test_user
    ),
    Assessment(
        employee_name='Oliver Hernandez',
        position='Software Engineer',
        department='Engineering',
        review_period='Q1 2024',
        performance_rating=4.2,
        strengths='Data-driven decision maker, collaborates effectively across teams, deep domain knowledge',
        areas_for_improvement='Needs to refine requirements gathering',
        goals='Complete certification z',
        comments='A solid performance from Oliver this period. Key contributions include complete certification z.',
        author=test_user
    ),
    Assessment(
        employee_name='Charlotte Campbell',
        position='QA Engineer',
        department='Engineering',
        review_period='Q4 2023',
        performance_rating=4.9,
        strengths='Talent sourcing',
        areas_for_improvement='None noted this period.',
        goals='Publish research/blog post',
        comments='Charlotte consistently exceeds expectations. Strengths in talent sourcing and talent sourcing are particularly notable.',
        author=test_user
    ),
    Assessment(
        employee_name='Finley Garcia',
        position='QA Engineer',
        department='Engineering',
        review_period='Q2 2024',
        performance_rating=3.9,
        strengths='Delivers high-quality results consistently',
        areas_for_improvement='Needs to improve prioritization skills, needs to develop cross-functional collaboration',
        goals='Achieve x% sales target',
        comments='Performance meets expectations. Finley should focus on needs to develop cross-functional collaboration while continuing to leverage delivers high-quality results consistently.',
        author=test_user
    ),
    Assessment(
        employee_name='James Clark',
        position='UI/UX Designer',
        department='Design',
        review_period='Q4 2024',
        performance_rating=4.2,
        strengths='Data-driven decision maker, process optimization',
        areas_for_improvement='Needs more experience with tool y',
        goals='Increase lead generation by w%, optimize data processing pipeline',
        comments='A solid performance from James this period. Key contributions include increase lead generation by w%.',
        author=test_user
    ),
    Assessment(
        employee_name='Avery King',
        position='Content Strategist',
        department='Marketing',
        review_period='Q3 2023',
        performance_rating=3.9,
        strengths='Strategic thinking, financial modeling',
        areas_for_improvement='Could enhance reporting clarity',
        goals='Enhance security protocols',
        comments='Avery consistently exceeds expectations. Strengths in financial modeling and strategic thinking are particularly notable.',
        author=test_user
    ),
    Assessment(
        employee_name='Riley Thomas',
        position='Sales Operations Analyst',
        department='Sales',
        review_period='Q4 2024',
        performance_rating=4.4,
        strengths='Security best practices, takes initiative',
        areas_for_improvement='Could improve documentation practices, could improve attention to detail on routine tasks',
        goals='Develop new marketing campaign strategy, launch new product feature',
        comments='Highly effective performer. Riley\'s work on develop new marketing campaign strategy has been impactful. Continue fostering security best practices.',
        author=test_user
    ),
    Assessment(
        employee_name='Benjamin Parker',
        position='Senior Designer',
        department='Design',
        review_period='Q2 2023',
        performance_rating=4.1,
        strengths='Highly adaptable',
        areas_for_improvement='Could improve documentation practices, could enhance reporting clarity',
        goals='Improve customer satisfaction scores',
        comments='Reliable and consistent performer. Benjamin\'s highly adaptable makes them a dependable team member. Agreed focus on improve customer satisfaction scores for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Isabella Johnson',
        position='Data Engineer',
        department='Analytics',
        review_period='Q3 2024',
        performance_rating=3.2,
        strengths='Excellent communication skills, financial modeling',
        areas_for_improvement='Could engage more in team discussions, could improve handling of constructive feedback',
        goals='Gain expertise in technology x, refine onboarding process',
        comments='Highly effective performer. Isabella\'s work on refine onboarding process has been impactful. Continue fostering excellent communication skills.',
        author=test_user
    ),
    Assessment(
        employee_name='Liam Baker',
        position='Data Engineer',
        department='Analytics',
        review_period='Q3 2023',
        performance_rating=3.5,
        strengths='Strong leadership potential',
        areas_for_improvement='Needs to manage stakeholder expectations better',
        goals='Mentor junior developers/colleagues',
        comments='Liam consistently exceeds expectations. Strengths in strong leadership potential and strong leadership potential are particularly notable.',
        author=test_user
    ),
    Assessment(
        employee_name='Morgan Baker',
        position='Product Manager',
        department='Product',
        review_period='Q2 2024',
        performance_rating=4.3,
        strengths='Highly adaptable',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Increase lead generation by w%, achieve x% sales target',
        comments='Morgan demonstrates potential. Key strengths include highly adaptable. Next steps involve focusing on increase lead generation by w% and addressing needs to build confidence in area z.',
        author=test_user
    ),
    Assessment(
        employee_name='Henry Evans',
        position='Operations Coordinator',
        department='Operations',
        review_period='Q2 2023',
        performance_rating=4.3,
        strengths='Talent sourcing',
        areas_for_improvement='Could focus more on strategic goals, needs to enhance presentation skills',
        goals='Gain expertise in technology x',
        comments='Henry is a valuable member of the team, demonstrating strong talent sourcing.',
        author=test_user
    ),
    Assessment(
        employee_name='Evelyn Phillips',
        position='DevOps Engineer',
        department='Engineering',
        review_period='Q1 2024',
        performance_rating=3.9,
        strengths='Creative thinking',
        areas_for_improvement='Needs to refine requirements gathering, could improve time management',
        goals='Increase lead generation by w%, reduce operational costs by y%',
        comments='Evelyn is a valuable member of the team, demonstrating strong creative thinking.',
        author=test_user
    ),
    Assessment(
        employee_name='Drew Gonzalez',
        position='Content Strategist',
        department='Marketing',
        review_period='Q2 2023',
        performance_rating=4.7,
        strengths='Campaign management',
        areas_for_improvement='None noted this period.',
        goals='Develop new marketing campaign strategy',
        comments='Drew has shown significant growth. Areas like campaign management are strong, while ongoing development is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Skyler Thompson',
        position='Social Media Coordinator',
        department='Marketing',
        review_period='Q4 2024',
        performance_rating=3.3,
        strengths='Mentors junior team members',
        areas_for_improvement='Needs more experience with tool y, needs to delegate more effectively',
        goals='Improve customer satisfaction scores',
        comments='A solid performance from Skyler this period. Key contributions include improve customer satisfaction scores.',
        author=test_user
    ),
    Assessment(
        employee_name='Morgan Nelson',
        position='Supply Chain Analyst',
        department='Operations',
        review_period='Q4 2023',
        performance_rating=4.3,
        strengths='Strategic thinking, manages complexity well',
        areas_for_improvement='Could focus more on strategic goals',
        goals='Improve customer satisfaction scores, lead a major project',
        comments='Good contributions this quarter. Morgan is working towards improve customer satisfaction scores and improving could focus more on strategic goals.',
        author=test_user
    ),
    Assessment(
        employee_name='Benjamin Evans',
        position='Supply Chain Analyst',
        department='Operations',
        review_period='Q2 2024',
        performance_rating=4.9,
        strengths='Mentors junior team members, proactive problem-solver',
        areas_for_improvement='None noted this period.',
        goals='Streamline reporting process, take on more leadership responsibilities',
        comments='Benjamin has shown significant growth. Areas like proactive problem-solver are strong, while ongoing development is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Sam Taylor',
        position='Machine Learning Engineer',
        department='Analytics',
        review_period='Q4 2024',
        performance_rating=4.0,
        strengths='Excellent communication skills',
        areas_for_improvement='Could work on meeting deadlines more consistently',
        goals='Improve design system adoption',
        comments='Sam has shown significant growth. Areas like excellent communication skills are strong, while could work on meeting deadlines more consistently is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Sophia Baker',
        position='QA Engineer',
        department='Engineering',
        review_period='Q1 2023',
        performance_rating=3.9,
        strengths='Creative thinking',
        areas_for_improvement='Could improve attention to detail on routine tasks',
        goals='Enhance security protocols, present at a conference',
        comments='Excellent progress shown by Sophia, particularly in achieving present at a conference.',
        author=test_user
    ),
    Assessment(
        employee_name='Noah Thomas',
        position='Talent Acquisition Specialist',
        department='HR',
        review_period='Q1 2024',
        performance_rating=3.5,
        strengths='Mentors junior team members, code quality focus',
        areas_for_improvement='Needs to develop cross-functional collaboration',
        goals='Achieve x% sales target',
        comments='Noah is a valuable member of the team, demonstrating strong mentors junior team members.',
        author=test_user
    ),
    Assessment(
        employee_name='Elijah Anderson',
        position='Graphic Designer',
        department='Design',
        review_period='Q1 2024',
        performance_rating=3.3,
        strengths='Deep domain knowledge, infrastructure automation',
        areas_for_improvement='Could engage more in team discussions, needs more experience with tool y',
        goals='Achieve x% sales target, streamline reporting process',
        comments='Elijah is a valuable member of the team, demonstrating strong infrastructure automation.',
        author=test_user
    ),
    Assessment(
        employee_name='Charlie Lewis',
        position='Data Analyst',
        department='Analytics',
        review_period='Q1 2023',
        performance_rating=4.3,
        strengths='Delivers high-quality results consistently, manages complexity well, security best practices',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Refine onboarding process',
        comments='Charlie has shown significant growth. Areas like delivers high-quality results consistently are strong, while needs deeper technical understanding in x area is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Emma Parker',
        position='Interaction Designer',
        department='Design',
        review_period='Q3 2023',
        performance_rating=3.5,
        strengths='Strong leadership potential, highly adaptable, strong technical aptitude',
        areas_for_improvement='Needs to manage stakeholder expectations better, needs to develop cross-functional collaboration',
        goals='Develop new marketing campaign strategy, increase lead generation by w%',
        comments='Good contributions this quarter. Emma is working towards develop new marketing campaign strategy and improving needs to develop cross-functional collaboration.',
        author=test_user
    ),
    Assessment(
        employee_name='Harper Roberts',
        position='Design Lead',
        department='Design',
        review_period='Q3 2023',
        performance_rating=4.6,
        strengths='Process optimization, mentors junior team members',
        areas_for_improvement='None noted this period.',
        goals='Improve cross-team collaboration, achieve x% sales target',
        comments='Harper has shown significant growth. Areas like mentors junior team members are strong, while ongoing development is an area for development.',
        author=test_user
    ),
    Assessment(
        employee_name='Emma Lopez',
        position='Associate Product Manager',
        department='Product',
        review_period='Q4 2023',
        performance_rating=4.4,
        strengths='Highly adaptable, mentors junior team members, proactive problem-solver',
        areas_for_improvement='Needs to refine requirements gathering, needs to enhance presentation skills',
        goals='Master financial forecasting model',
        comments='Excellent progress shown by Emma, particularly in achieving master financial forecasting model.',
        author=test_user
    ),
    Assessment(
        employee_name='Taylor Carter',
        position='Product Manager',
        department='Product',
        review_period='Q4 2024',
        performance_rating=4.1,
        strengths='User empathy, delivers high-quality results consistently',
        areas_for_improvement='Needs to refine requirements gathering',
        goals='Lead a major project',
        comments='Reliable and consistent performer. Taylor\'s delivers high-quality results consistently makes them a dependable team member. Agreed focus on lead a major project for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Noah Moore',
        position='Account Executive',
        department='Sales',
        review_period='Q3 2024',
        performance_rating=4.4,
        strengths='Highly adaptable',
        areas_for_improvement='Could work on meeting deadlines more consistently',
        goals='Present at a conference',
        comments='A solid performance from Noah this period. Key contributions include present at a conference.',
        author=test_user
    ),
    Assessment(
        employee_name='Jamie Martinez',
        position='Digital Marketing Manager',
        department='Marketing',
        review_period='Q1 2024',
        performance_rating=3.5,
        strengths='Quick learner, collaborates effectively across teams, strong technical aptitude',
        areas_for_improvement='Could work on meeting deadlines more consistently',
        goals='Improve customer satisfaction scores, implement ci/cd improvements',
        comments='Highly effective performer. Jamie\'s work on improve customer satisfaction scores has been impactful. Continue fostering quick learner.',
        author=test_user
    ),
    Assessment(
        employee_name='Charlie Turner',
        position='Compensation Analyst',
        department='HR',
        review_period='Q4 2023',
        performance_rating=4.7,
        strengths='Mentors junior team members',
        areas_for_improvement='Needs to enhance presentation skills',
        goals='Launch new product feature, develop new marketing campaign strategy',
        comments='Performance meets expectations. Charlie should focus on needs to enhance presentation skills while continuing to leverage mentors junior team members.',
        author=test_user
    ),
    Assessment(
        employee_name='Olivia Jones',
        position='Operations Coordinator',
        department='Operations',
        review_period='Q3 2024',
        performance_rating=4.7,
        strengths='Great team player, strategic thinking, detail-oriented',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Complete certification z',
        comments='A solid performance from Olivia this period. Key contributions include complete certification z.',
        author=test_user
    ),
    Assessment(
        employee_name='Lucas Davis',
        position='Tech Lead',
        department='Engineering',
        review_period='Q4 2023',
        performance_rating=4.0,
        strengths='Delivers high-quality results consistently, negotiation skills, strategic thinking',
        areas_for_improvement='Needs to refine requirements gathering, needs to develop cross-functional collaboration',
        goals='Lead a major project, develop new marketing campaign strategy',
        comments='Good contributions this quarter. Lucas is working towards develop new marketing campaign strategy and improving needs to refine requirements gathering.',
        author=test_user
    ),
    Assessment(
        employee_name='Reese Walker',
        position='Finance Manager',
        department='Finance',
        review_period='Q2 2023',
        performance_rating=5.0,
        strengths='Infrastructure automation, strong leadership potential, stakeholder management',
        areas_for_improvement='Could focus more on strategic goals',
        goals='Mentor junior developers/colleagues, develop new marketing campaign strategy',
        comments='Reese consistently exceeds expectations. Strengths in strong leadership potential and stakeholder management are particularly notable.',
        author=test_user
    ),
    Assessment(
        employee_name='Mia Nelson',
        position='HR Manager',
        department='HR',
        review_period='Q4 2024',
        performance_rating=4.6,
        strengths='Data-driven decision maker',
        areas_for_improvement='Focus remains on leveraging strengths.',
        goals='Enhance security protocols',
        comments='Mia demonstrates potential. Key strengths include data-driven decision maker. Next steps involve focusing on enhance security protocols and addressing ongoing development.',
        author=test_user
    ),
    Assessment(
        employee_name='Benjamin Martinez',
        position='Interaction Designer',
        department='Design',
        review_period='Q3 2024',
        performance_rating=4.2,
        strengths='User empathy',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Reduce operational costs by y%, increase lead generation by w%',
        comments='A solid performance from Benjamin this period. Key contributions include increase lead generation by w%.',
        author=test_user
    ),
    Assessment(
        employee_name='Reese Parker',
        position='Senior Designer',
        department='Design',
        review_period='Q2 2023',
        performance_rating=4.7,
        strengths='Process optimization, strategic thinking',
        areas_for_improvement='Needs deeper technical understanding in x area',
        goals='Gain expertise in technology x, refine onboarding process',
        comments='Performance meets expectations. Reese should focus on needs deeper technical understanding in x area while continuing to leverage strategic thinking.',
        author=test_user
    ),
    Assessment(
        employee_name='Alexander Lewis',
        position='Finance Manager',
        department='Finance',
        review_period='Q4 2024',
        performance_rating=3.2,
        strengths='Great team player, strong analytical abilities',
        areas_for_improvement='Needs to increase speed of delivery',
        goals='Streamline reporting process, achieve x% sales target',
        comments='Reliable and consistent performer. Alexander\'s great team player makes them a dependable team member. Agreed focus on achieve x% sales target for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Kai Robinson',
        position='Senior Financial Analyst',
        department='Finance',
        review_period='Q1 2024',
        performance_rating=3.6,
        strengths='Creative thinking',
        areas_for_improvement='Could engage more in team discussions, needs to develop cross-functional collaboration',
        goals='Develop new marketing campaign strategy, mentor junior developers/colleagues',
        comments='Kai is a valuable member of the team, demonstrating strong creative thinking.',
        author=test_user
    ),
    Assessment(
        employee_name='Cameron Allen',
        position='Customer Success Manager',
        department='Sales',
        review_period='Q4 2024',
        performance_rating=3.8,
        strengths='Strong technical aptitude',
        areas_for_improvement='Could improve attention to detail on routine tasks, could work on meeting deadlines more consistently',
        goals='Enhance security protocols',
        comments='Cameron is a valuable member of the team, demonstrating strong strong technical aptitude.',
        author=test_user
    ),
    Assessment(
        employee_name='Riley Scott',
        position='Operations Manager',
        department='Operations',
        review_period='Q2 2023',
        performance_rating=4.3,
        strengths='Strong leadership potential, excellent communication skills',
        areas_for_improvement='Could improve documentation practices',
        goals='Lead a major project',
        comments='Highly effective performer. Riley\'s work on lead a major project has been impactful. Continue fostering strong leadership potential.',
        author=test_user
    ),
    Assessment(
        employee_name='Finley Johnson',
        position='Associate Product Manager',
        department='Product',
        review_period='Q2 2023',
        performance_rating=4.1,
        strengths='Campaign management, financial modeling',
        areas_for_improvement='Could improve documentation practices, needs to build confidence in area z',
        goals='Reduce operational costs by y%',
        comments='Highly effective performer. Finley\'s work on reduce operational costs by y% has been impactful. Continue fostering financial modeling.',
        author=test_user
    ),
    Assessment(
        employee_name='William Mitchell',
        position='Data Engineer',
        department='Analytics',
        review_period='Q1 2023',
        performance_rating=4.0,
        strengths='Positive attitude, excellent communication skills',
        areas_for_improvement='Could benefit from assertiveness training, could work on meeting deadlines more consistently',
        goals='Enhance security protocols',
        comments='Reliable and consistent performer. William\'s excellent communication skills makes them a dependable team member. Agreed focus on enhance security protocols for next period.',
        author=test_user
    ),
    Assessment(
        employee_name='Logan Thompson',
        position='Graphic Designer',
        department='Design',
        review_period='Q3 2023',
        performance_rating=4.2,
        strengths='Infrastructure automation, negotiation skills, strong technical aptitude',
        areas_for_improvement='Needs to develop cross-functional collaboration',
        goals='Lead a major project, optimize data processing pipeline',
        comments='Good contributions this quarter. Logan is working towards lead a major project and improving needs to develop cross-functional collaboration.',
        author=test_user
    ),
    Assessment(
        employee_name='Casey Baker',
        position='UI/UX Designer',
        department='Design',
        review_period='Q4 2024',
        performance_rating=4.5,
        strengths='Campaign management, highly adaptable',
        areas_for_improvement='Could be more proactive in communication',
        goals='Optimize data processing pipeline',
        comments='Highly effective performer. Casey\'s work on optimize data processing pipeline has been impactful. Continue fostering campaign management.',
        author=test_user
    ),
    Assessment(
        employee_name='William Turner',
        position='Recruiter',
        department='HR',
        review_period='Q3 2024',
        performance_rating=3.3,
        strengths='Negotiation skills, data-driven decision maker, creative thinking',
        areas_for_improvement='Could benefit from assertiveness training, could work on meeting deadlines more consistently',
        goals='Master financial forecasting model, complete certification z',
        comments='Good contributions this quarter. William is working towards complete certification z and improving could work on meeting deadlines more consistently.',
        author=test_user
    ),
    Assessment(
        employee_name='Casey Thompson',
        position='Digital Marketing Manager',
        department='Marketing',
        review_period='Q3 2024',
        performance_rating=3.8,
        strengths='Infrastructure automation',
        areas_for_improvement='Could be more proactive in communication',
        goals='Enhance security protocols',
        comments='Good contributions this quarter. Casey is working towards enhance security protocols and improving could be more proactive in communication.',
        author=test_user
    ),
    Assessment(
        employee_name='Cameron Baker',
        position='Logistics Manager',
        department='Operations',
        review_period='Q3 2023',
        performance_rating=4.9,
        strengths='Excellent presentation skills, excellent communication skills',
        areas_for_improvement='Could benefit from assertiveness training, could work on meeting deadlines more consistently',
        goals='Lead a major project, present at a conference',
        comments='A solid performance from Cameron this period. Key contributions include lead a major project.',
        author=test_user
    ),
    Assessment(
        employee_name='Jordan Campbell',
        position='Compensation Analyst',
        department='HR',
        review_period='Q4 2024',
        performance_rating=4.8,
        strengths='Code quality focus, highly adaptable, campaign management',
        areas_for_improvement='Needs to delegate more effectively',
        goals='Achieve x% sales target, complete certification z',
        comments='Performance meets expectations. Jordan should focus on needs to delegate more effectively while continuing to leverage campaign management.',
        author=test_user
    ),
    Assessment(
        employee_name='Rowan Nelson',
        position='Machine Learning Engineer',
        department='Analytics',
        review_period='Q3 2023',
        performance_rating=3.2,
        strengths='Stakeholder management, data-driven decision maker',
        areas_for_improvement='Could improve handling of constructive feedback',
        goals='Reduce operational costs by y%',
        comments='Rowan demonstrates potential. Key strengths include stakeholder management. Next steps involve focusing on reduce operational costs by y% and addressing could improve handling of constructive feedback.',
        author=test_user
    ),
    Assessment(
        employee_name='Charlotte Lewis',
        position='Content Strategist',
        department='Marketing',
        review_period='Q1 2024',
        performance_rating=3.5,
        strengths='Excellent presentation skills, financial modeling, process optimization',
        areas_for_improvement='Needs to build confidence in area z',
        goals='Develop new marketing campaign strategy',
        comments='Charlotte demonstrates potential. Key strengths include excellent presentation skills. Next steps involve focusing on develop new marketing campaign strategy and addressing needs to build confidence in area z.',
        author=test_user
    ),
    Assessment(
        employee_name='Devin Thomas',
        position='UX Researcher',
        department='Product',
        review_period='Q1 2023',
        performance_rating=4.7,
        strengths='Deep domain knowledge, takes initiative, proactive problem-solver',
        areas_for_improvement='Could work on meeting deadlines more consistently, could benefit from assertiveness training',
        goals='Publish research/blog post',
        comments='Highly effective performer. Devin\'s work on publish research/blog post has been impactful. Continue fostering proactive problem-solver.',
        author=test_user
    )
]

for assessment in original_assessments:
    synthetic_assessments.append(assessment)
    used_names.add(assessment.employee_name)

# Generate 95 more
num_to_generate = 95
attempts = 0
max_attempts = num_to_generate * 3 # Limit attempts to avoid infinite loop if name pool is small

while len(synthetic_assessments) < 100 and attempts < max_attempts:
    attempts += 1

    # Generate Name
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    if name in used_names:
        continue # Avoid duplicate names
    used_names.add(name)

    # Select Department and Position
    department = random.choice(list(departments_positions.keys()))
    position = random.choice(departments_positions[department])

    # Select Review Period
    review_period = random.choice(review_periods)

    # Generate Rating (slightly skewed towards positive)
    rating_roll = random.random()
    if rating_roll > 0.7: # 30% chance of 4.5 - 5.0
        performance_rating = round(random.uniform(4.5, 5.0), 1)
    elif rating_roll > 0.2: # 50% chance of 3.8 - 4.4
        performance_rating = round(random.uniform(3.8, 4.4), 1)
    else: # 20% chance of 3.0 - 3.7
        performance_rating = round(random.uniform(3.0, 3.7), 1)

    # Generate Text Fields
    num_strengths = random.randint(1, 3)
    strengths = ", ".join(random.sample(strength_phrases, num_strengths)).capitalize()

    # Areas for improvement less likely for high ratings
    if performance_rating >= 4.6 and random.random() > 0.3: # 70% chance of no/minor improvements for top performers
        areas_for_improvement = random.choice(["None noted this period.", "Focus remains on leveraging strengths."])
    else:
        num_improvements = random.randint(1, 2)
        areas_for_improvement = ", ".join(random.sample(improvement_phrases, num_improvements)).capitalize()

    num_goals = random.randint(1, 2)
    goals = ", ".join(random.sample(goal_phrases, num_goals)).capitalize()

    # Generate Comments using templates
    selected_strength1 = random.choice(strengths.split(', ')).strip().lower()
    selected_strength2 = random.choice(strengths.split(', ')).strip().lower()
    while selected_strength1 == selected_strength2 and len(strengths.split(', ')) > 1: # Ensure two different strengths if possible
         selected_strength2 = random.choice(strengths.split(', ')).strip().lower()

    selected_improvement1 = random.choice(areas_for_improvement.split(', ')).strip().lower() if areas_for_improvement not in ["None noted this period.", "Focus remains on leveraging strengths."] else "ongoing development"
    selected_goal1 = random.choice(goals.split(', ')).strip().lower()
    selected_goal2 = random.choice(goals.split(', ')).strip().lower()
    while selected_goal1 == selected_goal2 and len(goals.split(', ')) > 1:
         selected_goal2 = random.choice(goals.split(', ')).strip().lower()

    comment_template = random.choice(comment_templates)
    comments = comment_template.format(
        name=first, # Use first name for personalization
        strength1=selected_strength1,
        strength2=selected_strength2,
        improvement1=selected_improvement1,
        goal1=selected_goal1,
        goal2=selected_goal2
    )

    # Create Assessment object (ensure author=test_user is used)
    assessment = Assessment(
        employee_name=name,
        position=position,
        department=department,
        review_period=review_period,
        performance_rating=performance_rating,
        strengths=strengths,
        areas_for_improvement=areas_for_improvement,
        goals=goals,
        comments=comments,
        author=test_user # Use the test_user variable
    )
    synthetic_assessments.append(assessment)

# --- Output the generated data in the desired format ---

print("# Start of generated assessment data")
print("assessments = [")

for i, assessment in enumerate(synthetic_assessments):
    # Properly escape single quotes within strings
    safe_strengths = assessment.strengths.replace("'", "\\'")
    safe_areas = assessment.areas_for_improvement.replace("'", "\\'")
    safe_goals = assessment.goals.replace("'", "\\'")
    safe_comments = assessment.comments.replace("'", "\\'")
    safe_name = assessment.employee_name.replace("'", "\\'")
    safe_position = assessment.position.replace("'", "\\'")
    safe_department = assessment.department.replace("'", "\\'")
    safe_review_period = assessment.review_period.replace("'", "\\'")

    print(f"    Assessment(")
    print(f"        employee_name='{safe_name}',")
    print(f"        position='{safe_position}',")
    print(f"        department='{safe_department}',")
    print(f"        review_period='{safe_review_period}',")
    print(f"        performance_rating={assessment.performance_rating},")
    print(f"        strengths='{safe_strengths}',")
    print(f"        areas_for_improvement='{safe_areas}',")
    print(f"        goals='{safe_goals}',")
    print(f"        comments='{safe_comments}',")
    # Ensure the author field correctly uses the variable `test_user`
    # If test_user is a string literal like "'System Generated'", it will print that.
    # If test_user is an object variable, it will print the variable name.
    # Adjust the following line based on how `test_user` is actually defined and needed in the output.
    # Assuming test_user is a variable name that should appear literally in the output:
    print(f"        author=test_user")
    # If test_user was intended to be a string *value* in the output, use:
    # print(f"        author='{assessment.author}'") # Assuming author holds a string value
    print(f"    ){',' if i < len(synthetic_assessments) - 1 else ''}")

print("]")
print(f"# Total assessments generated: {len(synthetic_assessments)}")
# --- End of generated assessment data ---