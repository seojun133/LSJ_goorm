farms = ['제일농장', '우리농장', '한국농장']
animals = ['닭', '소', '돼지']

farm_data = {
    '제일농장': [100, 50, 80],
    '우리농장': [50, 10, 20],
    '한국농장': [200, 100, 150]
}

for farm in farms:
    print(f"**** {farm} ****")
    for animal, count in zip(animals, farm_data[farm]):
        print(f"{animal}, {count}마리입니다.")
    print()