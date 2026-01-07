import machine
for i in range(5):
    try:
        adc = machine.ADC(i)
        print(f"GPIO{i}: {adc.read_u16()} ({adc.read()})")
    except ValueError:
        print(f"GPIO{i}: INVALID")


