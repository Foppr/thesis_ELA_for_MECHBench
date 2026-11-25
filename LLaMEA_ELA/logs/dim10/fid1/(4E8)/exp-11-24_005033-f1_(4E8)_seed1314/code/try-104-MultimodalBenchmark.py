import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic sine-wave component with modified frequencies
        result = np.sum(np.sin(12 * x) * np.cos(18 * x)) + 0.6 * np.sum(np.sin(30 * x**2))
        
        # Dynamic conditioning with altered exponential scaling
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (15**(i / self.dim) * x[i]**2)
        result += 0.25 * condition_term
        
        # Chaotic coupling terms with modified interaction strengths
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = np.sin(35 * (x[i] + x[j])) * np.cos(30 * (x[i] - x[j]))
                chaos_coupling += coupling / (1.0 + distance**2.5)
        result += 0.15 * chaos_coupling
        
        # Modified basin structure with different harmonic phases
        basin_term = 0.0
        for k in range(6):
            phase = k * np.pi / 3
            basin_term += np.sum(np.sin(6 * (x + phase)) * np.cos(8 * (x + phase)))
        result += 0.2 * basin_term
        
        # Adaptive gradient modulation with modified non-separable interactions
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.sin(25 * x[i]) * np.cos(30 * x[i]))
        result += 0.12 * (grad_mod**1.3) * np.exp(-0.03 * np.sum(x**2))
        
        # Modified polynomial coupling with different exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**5 + x[j]**5) * np.sin(15 * (x[i] + x[j]))
        result += 0.07 * poly_coupling
        
        # Adjusted saddle-point attraction with modified harmonic potential
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.sin(10 * x[i]) * np.cos(15 * x[i])
        result += 0.1 * saddle_term
        
        return result