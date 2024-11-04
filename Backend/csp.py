from constraint import *
from typing import Dict, List, Tuple
import random

# Function to get time slots based on the provided slot dictionary and start times
def get_time_slots(slot_dict: Dict[str, int], start_times: Dict[str, int]) -> Tuple[List[str], Dict[str, int], Dict[str, str]]:
    subjects = []
    slot_time = {}
    mapping = {}
    for i in slot_dict:
        start = start_times[i]
        if i == 'Monday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"M{j + 1}")
                mapping[f"M{j + 1}"] = i.lower()
                slot_time[f"M{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Tuesday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"T{j + 1}")
                mapping[f"T{j + 1}"] = i.lower()
                slot_time[f"T{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Wednesday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"W{j + 1}")
                mapping[f"W{j + 1}"] = i.lower()
                slot_time[f"W{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Thursday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Th{j + 1}")
                mapping[f"Th{j + 1}"] = i.lower()
                slot_time[f"Th{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Friday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"F{j + 1}")
                mapping[f"F{j + 1}"] = i.lower()
                slot_time[f"F{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Saturday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Sa{j + 1}")
                mapping[f"Sa{j + 1}"] = i.lower()
                slot_time[f"Sa{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1
        elif i == 'Sunday':
            for j in range(int(slot_dict[i]) - 1):
                subjects.append(f"Su{j + 1}")
                mapping[f"Su{j + 1}"] = i.lower()
                slot_time[f"Su{j + 1}"] = start
                if start == 12:
                    start += 2
                else:
                    start += 1

    return subjects, slot_time, mapping

# Function to generate a timetable based on the provided constraints and courses
def generate(constraints: Dict[str, List[Dict[str, int]]], courses: List[Dict[str, int]]) -> Dict[str, List[Dict[str, str]]]:
    constraints_dict = {}
    start_times = {}
    end_times = {2: [], 3: []}
    offset = 0
    subject_hrs = {}
    subjects = []
    subject_data = {}
    consecutive_subjects = {}
    diff_consecutive_mode = True
    diff_non_consecutive_mode = True

    # Process working days constraints
    for course in constraints["working_days"]:
        constraints_dict[course["day"]] = course["total_hours"]
        start_times[course["day"]] = int(course["start_hr"])
        end_times[2].append((int(course["total_hours"]) - 2) + offset)
        for i in range(int(course["total_hours"]) - 3 + offset, int(course["total_hours"]) - 1 + offset):
            end_times[3].append(i)
        offset += int(course["total_hours"]) - 1

    # Process course data
    for item in courses:
        subject_hrs[item["name"]] = int(
            item['lectureno']) * int(item["duration"])
        subjects.append(item["name"])
        subject_data[item['name']] = {'start_hr': int(
            item['start_hr']), 'end_hr': int(item['end_hr'])}
        if item["duration"] != 1:
            consecutive_subjects[item["name"]] = item["duration"]

    if constraints['consecutive_subjects'][0] == "":
        diff_consecutive_mode = False

    if constraints['non_consecutive_subjects'][0] == "":
        diff_non_consecutive_mode = False

    time_slots, slot_time, mapping = get_time_slots(
        constraints_dict, start_times)

    Scheduling = Problem()
    Scheduling.addVariables(time_slots, subjects)

    # Constraint to ensure every subject is scheduled the required number of times
    def everySubject(*args: str) -> bool:
        Timetable = args
        for subject in subjects:
            if Timetable.count(subject) != subject_hrs[subject]:
                return False
        return True

    # Constraint to ensure consecutive subjects are scheduled together
    def sameConsecutive(*args: str) -> bool:
        Timetable = args
        for key, value in consecutive_subjects.items():
            index = Timetable.index(key)
            if (value == 2 and index in end_times[2]) or (value == 3 and index in end_times[3]):
                return False
            for i in range(value - 1):
                if Timetable[index + i + 1] != key:
                    return False
        return True

    # Constraint to ensure subjects are scheduled within the teacher's available hours
    def teacherTimings(*args: str) -> bool:
        Timetable = args
        for key, value in subject_data.items():
            indexes = [i for i, letter in enumerate(
                Timetable) if letter == key]
            for i in indexes:
                if slot_time[time_slots[i]] < value["start_hr"] or slot_time[time_slots[i]] >= value["end_hr"]:
                    return False
        return True

    # Constraint to ensure different consecutive subjects are scheduled together
    def diffConsecutive(*args: str) -> bool:
        Timetable = args
        for index, value in enumerate(constraints['consecutive_subjects']):
            indexes = [i for i, letter in enumerate(
                Timetable) if letter == value]
            for i in indexes:
                if index == 0:
                    if i == 0:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][1]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] != constraints['consecutive_subjects'][1]:
                            return False
                    else:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][1] or Timetable[i - 1] != constraints['consecutive_subjects'][1]:
                            return False
                else:
                    if i == 0:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][0]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] != constraints['consecutive_subjects'][0]:
                            return False
                    else:
                        if Timetable[i + 1] != constraints['consecutive_subjects'][0] or Timetable[i - 1] != constraints['consecutive_subjects'][0]:
                            return False
        return True

    # Constraint to ensure different non-consecutive subjects are not scheduled together
    def diffNonConsecutive(*args: str) -> bool:
        Timetable = args
        for index, value in enumerate(constraints['non_consecutive_subjects']):
            indexes = [i for i, letter in enumerate(
                Timetable) if letter == value]
            for i in indexes:
                if index == 0:
                    if i == 0:
                        if Timetable[i + 1] == constraints['non_consecutive_subjects'][1]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] == constraints['non_consecutive_subjects'][1]:
                            return False
                    else:
                        if Timetable[i + 1] == constraints['non_consecutive_subjects'][1] or Timetable[i - 1] == constraints['non_consecutive_subjects'][1]:
                            return False
                else:
                    if i == 0:
                        if Timetable[i + 1] == constraints['non_consecutive_subjects'][0]:
                            return False
                    elif i == len(Timetable) - 1:
                        if Timetable[i - 1] == constraints['non_consecutive_subjects'][0]:
                            return False
                    else:
                        if Timetable[i + 1] == constraints['non_consecutive_subjects'][0] or Timetable[i - 1] == constraints['non_consecutive_subjects'][0]:
                            return False
        return True

    Scheduling.addConstraint(everySubject, time_slots)
    Scheduling.addConstraint(sameConsecutive, time_slots)
    Scheduling.addConstraint(teacherTimings, time_slots)
    if diff_consecutive_mode:
        Scheduling.addConstraint(diffConsecutive, time_slots)
    if diff_non_consecutive_mode:
        Scheduling.addConstraint(diffNonConsecutive, time_slots)

    solution = Scheduling.getSolution()
    '''
    {'M1': 'CO',
    'M2': 'CO',
    'T1': 'AI',
    'T2': 'PSE',
    'T3': 'AI',
    'W1': 'DBMS',
    'W2': 'DBMS',
    'W3': 'DBMS',
    'W4': 'AI',
    'W5': 'PSE',
    'W6': 'PSE'}
    '''
    if solution is not None:
        resp_data = {'monday': [], 'tuesday': [], 'wednesday': [],
                     'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}
        for key, value in solution.items():
            resp_data[mapping[key]].append({
                'id': 1,
                'name': value,
                'type': 'custom',
                'startTime': f'2018-02-25T{str(slot_time[key]).zfill(2)}:00:00',
                'endTime': f'2018-02-25T{str(slot_time[key]+1).zfill(2)}:00:00'
            })
        return resp_data
    else:
        return None

# Function to generate a timetable using a genetic algorithm
def generate_timetable_genetic(constraints: Dict[str, List[Dict[str, int]]], courses: List[Dict[str, int]], population_size: int = 100, generations: int = 1000, mutation_rate: float = 0.01) -> Dict[str, List[Dict[str, str]]]:
    constraints_dict = {}
    start_times = {}
    end_times = {2: [], 3: []}
    offset = 0
    subject_hrs = {}
    subjects = []
    subject_data = {}
    consecutive_subjects = {}
    diff_consecutive_mode = True
    diff_non_consecutive_mode = True

    # Process working days constraints
    for course in constraints["working_days"]:
        constraints_dict[course["day"]] = course["total_hours"]
        start_times[course["day"]] = int(course["start_hr"])
        end_times[2].append((int(course["total_hours"]) - 2) + offset)
        for i in range(int(course["total_hours"]) - 3 + offset, int(course["total_hours"]) - 1 + offset):
            end_times[3].append(i)
        offset += int(course["total_hours"]) - 1

    # Process course data
    for item in courses:
        subject_hrs[item["name"]] = int(
            item['lectureno']) * int(item["duration"])
        subjects.append(item["name"])
        subject_data[item['name']] = {'start_hr': int(
            item['start_hr']), 'end_hr': int(item['end_hr'])}
        if item["duration"] != 1:
            consecutive_subjects[item["name"]] = item["duration"]

    if constraints['consecutive_subjects'][0] == "":
        diff_consecutive_mode = False

    if constraints['non_consecutive_subjects'][0] == "":
        diff_non_consecutive_mode = False

    time_slots, slot_time, mapping = get_time_slots(
        constraints_dict, start_times)

    def fitness(timetable: List[str]) -> int:
        score = 0
        if everySubject(*timetable):
            score += 1
        if sameConsecutive(*timetable):
            score += 1
        if teacherTimings(*timetable):
            score += 1
        if diff_consecutive_mode and diffConsecutive(*timetable):
            score += 1
        if diff_non_consecutive_mode and diffNonConsecutive(*timetable):
            score += 1
        return score

    def mutate(timetable: List[str]) -> List[str]:
        for i in range(len(timetable)):
            if random.random() < mutation_rate:
                timetable[i] = random.choice(subjects)
        return timetable

    def crossover(parent1: List[str], parent2: List[str]) -> List[str]:
        crossover_point = random.randint(0, len(parent1) - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    population = [[random.choice(subjects) for _ in range(len(time_slots))] for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        next_generation = population[:10]
        for _ in range(population_size - 10):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        population = next_generation

    best_timetable = population[0]
    if fitness(best_timetable) > 0:
        resp_data = {'monday': [], 'tuesday': [], 'wednesday': [],
                     'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}
        for index, value in enumerate(best_timetable):
            resp_data[mapping[time_slots[index]]].append({
                'id': 1,
                'name': value,
                'type': 'custom',
                'startTime': f'2018-02-25T{str(slot_time[time_slots[index]]).zfill(2)}:00:00',
                'endTime': f'2018-02-25T{str(slot_time[time_slots[index]]+1).zfill(2)}:00:00'
            })
        return resp_data
    else:
        return None
