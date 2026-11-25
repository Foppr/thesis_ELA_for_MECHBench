import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Sinusoidal oscillations with Gaussian RBFs
        sinusoidal = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    rbf_sum += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2 * np.pi * (x[i] + x[j]))
            sinusoidal += np.sin(3 * x[i]) * np.cos(2 * x[i]) * rbf_sum
        
        # Polynomial interactions with dynamic exponents
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 2 + 0.5 * np.sin(0.5 * i)
                exp_j = 2 + 0.5 * np.sin(0.5 * j)
                poly_interaction += (x[i]**exp_i) * (x[j]**exp_j) * np.cos(0.1 * (i - j))
        
        # Localized attractor fields with dynamic positioning
        attractor = 0
        for i in range(self.dim):
            # Dynamic attractor positions based on dimension
            attractor_pos = 2 * np.sin(0.3 * i) + 0.5 * np.cos(0.7 * i)
            dist_to_attr = np.abs(x[i] - attractor_pos)
            attractor += np.exp(-0.1 * dist_to_attr**2) * np.sin(5 * x[i])
        
        # Dynamic conditioning factor
        condition_factor = 1.0 + 0.3 * np.sin(0.2 * np.sum(x)) + 0.2 * np.cos(0.1 * self.dim)
        
        # Cross-dimensional coupling with frequency modulation
        coupling = 0
        for i in range(self.dim):
            freq_mod = 1 + 0.4 * np.sin(0.1 * i + np.sum(x))
            coupling += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] / 2) * np.exp(-0.1 * x[i]**2)
        
        # Global shift using chaotic dynamics
        global_shift = 0
        logistic_val = 0.5
        for _ in range(10):
            logistic_val = 4 * logistic_val * (1 - logistic_val)
        for i in range(self.dim):
            global_shift += 0.2 * np.sin(3 * x[i]) * logistic_val
        
        # Combined function with varying weights
        return sphere + condition_factor * (0.3 * sinusoidal + 0.1 * poly_interaction + 0.05 * coupling + 0.03 * attractor) + global_shift