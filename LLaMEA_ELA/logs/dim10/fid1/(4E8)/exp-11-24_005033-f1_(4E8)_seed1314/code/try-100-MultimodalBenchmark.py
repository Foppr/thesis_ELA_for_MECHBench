import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic sine-wave component with dynamic frequency modulation
        result = np.sum(np.sin(10 * x) * np.cos(15 * x)) + 0.5 * np.sum(np.sin(25 * x**2))
        
        # Dynamic conditioning with exponential scaling
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (10**(i / self.dim) * x[i]**2)
        result += 0.2 * condition_term
        
        # Chaotic coupling terms with recursive sine interactions
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = np.sin(30 * (x[i] + x[j])) * np.cos(25 * (x[i] - x[j]))
                chaos_coupling += coupling / (1.0 + distance**2)
        result += 0.1 * chaos_coupling
        
        # Fractal-like basin structure with multiple attraction points
        basin_term = 0.0
        for k in range(8):
            phase = k * np.pi / 4
            basin_term += np.sum(np.sin(5 * (x + phase)) * np.cos(7 * (x + phase)))
        result += 0.15 * basin_term
        
        # Adaptive gradient modulation with non-separable interactions
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.sin(20 * x[i]) * np.cos(25 * x[i]))
        result += 0.1 * (grad_mod**1.5) * np.exp(-0.02 * np.sum(x**2))
        
        # Add high-order polynomial coupling with varying exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**4 + x[j]**4) * np.sin(12 * (x[i] + x[j]))
        result += 0.05 * poly_coupling
        
        # Saddle-point attraction with harmonic potential
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.sin(8 * x[i]) * np.cos(12 * x[i])
        result += 0.08 * saddle_term
        
        return result