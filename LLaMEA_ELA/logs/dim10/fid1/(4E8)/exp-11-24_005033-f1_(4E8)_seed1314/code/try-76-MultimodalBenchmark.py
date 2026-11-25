import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with fractal-like recursive interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 3.0 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.02 * np.sum(x**4)
        
        # Dynamic elliptic conditioning with fractal scaling
        ellipsoid_term = 0.0
        for i in range(self.dim):
            ellipsoid_term += (10**(2*i/(self.dim-1)) * x[i]**2)
        result += 0.1 * ellipsoid_term
        
        # Introduce recursive fractal coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with recursive scaling
                scale = 1.0 / (1.0 + np.abs(x[i] - x[j]))
                result += 0.05 * np.sin(20 * x[i]) * np.cos(20 * x[j]) * scale * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add recursive chaotic component with self-similar structure
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(30 * x[i]) * np.cos(35 * x[i]) * np.sin(40 * x[i])
        result += 0.08 * chaos_term
        
        # Enhanced cross-dimensional couplings with non-separable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(15 * (x[i] + x[j])) * np.cos(15 * (x[i] - x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial coupling with adaptive exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(10 * (x[i] + x[j]))
        result += 0.03 * poly_coupling
        
        # Adaptive gradient modulation with recursive penalty
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.cos(15 * x[i]) * np.sin(20 * x[i]))
        result += 0.15 * (grad_mod**2) * np.exp(-0.01 * np.sum(x**2))
        
        # Add a novel basin attraction component with multiple local minima
        basin_term = 0.0
        for k in range(5):
            phase = k * np.pi / 5
            basin_term += np.sum(np.sin(10 * (x + phase)) * np.cos(12 * (x + phase)))
        result += 0.04 * basin_term
        
        return result