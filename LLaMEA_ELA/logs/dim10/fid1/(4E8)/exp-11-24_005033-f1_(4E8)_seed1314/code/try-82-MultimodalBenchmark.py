import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with enhanced fractal interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 2.5 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.03 * np.sum(x**4)
        
        # Dynamic elliptic conditioning with improved scaling
        ellipsoid_term = 0.0
        for i in range(self.dim):
            ellipsoid_term += (10**(2*i/(self.dim-1)) * x[i]**2)
        result += 0.15 * ellipsoid_term
        
        # Enhanced recursive fractal coupling terms with modified scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + 0.5 * np.abs(x[i] - x[j]))
                result += 0.07 * np.sin(20 * x[i]) * np.cos(20 * x[j]) * scale * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Enhanced chaotic component with modified frequency interactions
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(35 * x[i]) * np.cos(40 * x[i]) * np.sin(45 * x[i])
        result += 0.12 * chaos_term
        
        # Improved cross-dimensional couplings with stronger non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(20 * (x[i] + x[j])) * np.cos(20 * (x[i] - x[j])) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Enhanced polynomial coupling with variable exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**4 + x[j]**4) * np.sin(12 * (x[i] + x[j]))
        result += 0.04 * poly_coupling
        
        # Refined adaptive gradient modulation with stronger penalty
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.cos(20 * x[i]) * np.sin(25 * x[i]))
        result += 0.2 * (grad_mod**2) * np.exp(-0.02 * np.sum(x**2))
        
        # Enhanced basin attraction component with more distinct local minima
        basin_term = 0.0
        for k in range(7):
            phase = k * np.pi / 7
            basin_term += np.sum(np.sin(12 * (x + phase)) * np.cos(15 * (x + phase)))
        result += 0.06 * basin_term
        
        return result