import numpy as np

class MultimodalChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf += np.exp(-0.5 * ((x - centers[i]) / (1.0 + 0.1 * i))**2)
                
        # Fractional polynomial interactions with non-integer exponents
        fractional_poly = 0
        for i in range(self.dim):
            fractional_poly += (x[i]**1.5 + x[i]**2.5 + x[i]**3.5) * np.cos(0.3 * x[i])
            
        # Trigonometric chaos with coupled frequencies
        trig_chaos = 0
        for i in range(self.dim):
            freqs = [1, 2, 3, 5]
            for j, freq in enumerate(freqs[:min(len(freqs), self.dim - i)]):
                if i + j < self.dim:
                    trig_chaos += np.sin(freq * x[i]) * np.cos(freq * x[i+j]) * np.exp(-0.1 * (x[i]**2 + x[i+j]**2))
                    
        # Sigmoidal modulation with varying steepness
        sigmoid_mod = 0
        for i in range(self.dim):
            sigmoid_mod += 1 / (1 + np.exp(-5 * (x[i] - 1))) * np.sin(0.7 * x[i])
            
        # Coupled oscillatory terms with time-delay like behavior
        oscillatory = 0
        for i in range(self.dim):
            if i > 0:
                oscillatory += np.sin(x[i-1] + x[i]) * np.cos(x[i-1] - x[i]) * (1 + 0.2 * np.sin(0.5 * x[i]))
                
        # Polynomial chaos with random coefficients
        poly_chaos = 0
        for i in range(self.dim):
            coeff = np.random.uniform(-1, 1)
            poly_chaos += coeff * x[i]**(3 + np.random.rand() * 2) * np.tan(0.2 * x[i])
            
        # Add a global structure with multiple valleys
        valley_structure = 0
        for i in range(self.dim):
            valley_structure += (x[i] - np.sin(x[i]))**2
            
        # Combine components with dynamic weights based on input values
        weights = np.array([0.2, 0.3, 0.15, 0.1, 0.15, 0.05, 0.05])
        components = [rbf, fractional_poly, trig_chaos, sigmoid_mod, oscillatory, poly_chaos, valley_structure]
        
        # Normalize and return
        result = np.sum([w * c for w, c in zip(weights, components) if not np.isnan(c)])
        return result + 0.1 * np.sum(np.sin(x)**2)