import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced conditioning
        result = 0.1 * np.sum(x**2)
        
        # Chaotic radial basis functions with logistic map modulation
        for i in range(self.dim):
            # Logistic map for chaotic center distribution
            center = 4.0 * np.sin(i * 0.7) * np.cos(i * 0.3) * 3.0
            width = 0.5 + 0.8 * np.abs(np.sin(i * 0.4))
            result += 3.0 * np.exp(-0.5 * ((x[i] - center)**2) / (width**2))
        
        # High-order polynomial cross-terms with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic degree modulation
                degree_i = 3 + (i * j) % 4
                degree_j = 2 + (i + j) % 5
                coupling = np.sin(i * 0.6 + j * 0.4) * 0.5 + 1.0
                result += coupling * (x[i]**degree_i) * (x[j]**degree_j) * np.cos(0.3 * (x[i] + x[j]))
        
        # Multi-scale sine-based structure with frequency chaos
        for i in range(self.dim):
            freq1 = 2.0 + 3.0 * np.sin(i * 0.5)
            freq2 = 1.5 + 2.5 * np.cos(i * 0.3)
            result += 2.0 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Dynamic conditioning with chaotic distance modulation
        dist = np.sqrt(np.sum(x**2))
        condition_factor = 1.0 + 0.5 * np.sin(dist * 0.4) * np.exp(-0.3 * dist)
        result *= condition_factor
        
        # Enhanced boundary penalty with chaotic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.6:
                scale = 2.0 + 1.5 * np.sin(i * 0.8)
                boundary_penalty += scale * (np.abs(x[i]) - 4.6)**4
        result += boundary_penalty
        
        # Higher-order nonlinearity with chaotic modulation
        for i in range(self.dim):
            mod = 0.2 + 0.1 * np.sin(i * 0.9)
            result += mod * x[i]**4
        
        # Add chaotic noise term to increase landscape complexity
        noise_term = 0.05 * np.sum(np.sin(x * 7.0) * np.cos(x * 3.0))
        result += noise_term
        
        return result