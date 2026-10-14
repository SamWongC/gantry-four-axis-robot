from v_plan import v_plan

def main():
    
    print("This is the main function.")
    #pulse_cnt = [24, 58, 103, 83]
    #v_plan.bigblock_plan(pulse_cnt)
    #a = 100 / 3
    #print(a)
    #a = int(100 / 3)
    #print(a)
    #v_plan.movel_clicked(200,200,250,250)
    
    file_path = "C://Users//马添源//Desktop//222.txt"  
    v_plan.parse_gcode()

    
if __name__ == "__main__":
    main()