import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic sine modulations with radial basis functions
        chaotic_mod = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    rbf_sum += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(4 * np.pi * (x[i] + x[j]))
            chaotic_mod += np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i]) * rbf_sum
        
        # Enhanced polynomial couplings with dynamic coefficients
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.5 + 0.5 * np.sin(0.3 * (i + j) + np.sum(x))
                poly_coupling += coeff * (x[i]**3) * (x[j]**4) * np.cos(0.2 * (i - j))
        
        # Time-varying harmonic components with frequency modulation
        harmonic = 0
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(0.2 * self.dim + i + np.sum(x))
            harmonic += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] / 3) * np.exp(-0.08 * x[i]**2)
        
        # Global shift using logistic map dynamics
        global_shift = 0
        for i in range(self.dim):
            logistic_val = 4 * 0.5 * (1 - 0.5)  # Initial logistic map value
            for _ in range(5):
                logistic_val = 4 * logistic_val * (1 - logistic_val)
            global_shift += 0.15 * np.sin(7 * x[i]) * logistic_val
        
        # Radial basis function with dynamic scaling
        rbf_dynamic = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    rbf_sum += np.exp(-0.3 * dist**2) * np.sin(3 * np.pi * dist)
            rbf_dynamic += rbf_sum
        
        # Dynamic scaling factor based on dimensionality and position
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 1) + 0.05 * np.cos(np.sum(x)**2)
        
        # Combined function with enhanced fitness characteristics
        return sphere + scale_factor * (0.2 * chaotic_mod + 0.03 * harmonic + 0.02 * poly_coupling + 0.01 * rbf_dynamic) + global_shift