import numpy as np

class FractalChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate fractal pattern using iterative function system
        self.fractal_pattern = np.zeros(dim)
        for i in range(dim):
            self.fractal_pattern[i] = np.sin(i * np.pi / 4) * np.cos(i * np.pi / 3)
        
        # Precompute temporal chaos sequence
        self.chaos_seq = np.zeros(dim)
        x = 0.5
        for i in range(dim):
            x = 3.9 * x * (1 - x)
            self.chaos_seq[i] = x
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal geometric component
        fractal_comp = np.sum(self.fractal_pattern * np.sin(2 * np.pi * x_norm))
        
        # Temporal chaos component
        chaos_comp = np.sum(self.chaos_seq * np.cos(2 * np.pi * x_norm))
        
        # Multi-scale noise with varying amplitudes
        noise_comp = 0
        for i in range(1, 6):
            noise_comp += (1/i) * np.sum(np.sin(i * x_norm) * np.random.uniform(0.1, 1.0, self.dim))
        
        # Self-similar scaling component
        scale_comp = np.sum(np.power(np.abs(x_norm), 1.5)) * np.random.uniform(0.5, 1.5)
        
        # Combine all components with adaptive weights
        return 0.25 * fractal_comp + 0.35 * chaos_comp + 0.30 * noise_comp + 0.10 * scale_comp