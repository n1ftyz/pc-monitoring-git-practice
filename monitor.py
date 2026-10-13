from config import CPU_LIMIT, GPU_LIMIT, RAM_LIMIT


def analyze(cpu, gpu, ram):
    return {
        "cpu": cpu >= CPU_LIMIT,
        "gpu": gpu >= GPU_LIMIT,
        "ram": ram >= RAM_LIMIT,
    }