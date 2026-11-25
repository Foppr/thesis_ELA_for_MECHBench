import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave component with frequency modulation
        result = np.sum(np.sin(15 * x) * np.cos(20 * x)) + 0.7 * np.sum(np.sin(35 * x**2))
        
        # Improved dynamic conditioning with logarithmic scaling
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (12**(i / self.dim) * x[i]**2)
        result += 0.3 * condition_term
        
        # Modified chaotic coupling with adaptive weights
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = np.sin(40 * (x[i] + x[j])) * np.cos(35 * (x[i] - x[j]))
                chaos_coupling += coupling / (1.0 + distance**2)
        result += 0.15 * chaos_coupling
        
        # Refined fractal-like basin structure with symmetric attraction points
        basin_term = 0.0
        for k in range(8):
            phase = k * np.pi / 4
            basin_term += np.sum(np.sin(7 * (x + phase)) * np.cos(9 * (x + phase)))
        result += 0.2 * basin_term
        
        # Enhanced gradient modulation with separable interactions
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.sin(30 * x[i]) * np.cos(35 * x[i]))
        result += 0.15 * (grad_mod**1.4) * np.exp(-0.02 * np.sum(x**2))
        
        # Adjusted polynomial coupling with higher-order terms
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**6 + x[j]**6) * np.sin(18 * (x[i] + x[j]))
        result += 0.08 * poly_coupling
        
        # Modified saddle-point attraction with enhanced harmonic potential
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.sin(12 * x[i]) * np.cos(18 * x[i])
        result += 0.11 * saddle_term
        
        return result