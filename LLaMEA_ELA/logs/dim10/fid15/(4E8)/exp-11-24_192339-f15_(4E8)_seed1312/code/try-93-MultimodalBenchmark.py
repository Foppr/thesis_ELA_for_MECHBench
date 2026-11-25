import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential wells
        exp_potential = 0
        for i in range(self.dim):
            exp_potential += np.exp(-0.5 * (x[i] - 2)**2) + np.exp(-0.5 * (x[i] + 2)**2)
        
        # Trigonometric wave interference
        wave_interference = 0
        for i in range(self.dim):
            wave_sum = 0
            for j in range(self.dim):
                if i != j:
                    wave_sum += np.sin(2 * np.pi * (x[i] - x[j])) * np.cos(3 * np.pi * (x[i] + x[j]))
            wave_interference += np.sin(5 * x[i]) * np.cos(4 * x[i]) * wave_sum
        
        # Adaptive noise modulation
        noise_mod = 0
        for i in range(self.dim):
            noise_level = 0.1 * (1 + 0.5 * np.sin(0.3 * self.dim + i + np.sum(x)))
            noise_mod += noise_level * np.sin(7 * x[i]) * np.cos(6 * x[i])
        
        # Dynamic scaling based on position and dimension
        dynamic_scale = 1.0 + 0.2 * np.sin(0.5 * np.sum(x)) * np.cos(0.4 * self.dim)
        
        # Saddle point structure with polynomial coupling
        saddle_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += (x[i]**2 - x[j]**2) * np.sin(0.1 * (i + j)) * np.cos(0.2 * (x[i] + x[j]))
        
        # Global shift using sinusoidal modulation
        global_shift = 0
        for i in range(self.dim):
            shift_val = 0.3 * np.sin(0.2 * self.dim + i + np.sum(x))
            global_shift += shift_val * (x[i] - 1)**3
        
        # Final combined function
        return dynamic_scale * (0.5 * exp_potential + 0.3 * wave_interference + 0.2 * saddle_term) + noise_mod + global_shift