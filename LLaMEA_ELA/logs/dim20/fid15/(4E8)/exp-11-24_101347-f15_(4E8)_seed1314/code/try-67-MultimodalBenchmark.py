import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_scaled[i]**4 + 0.5 * x_scaled[i]**3 - 0.3 * x_scaled[i]**2 + 0.1 * x_scaled[i])
        
        # Radial cosine oscillation with variable frequency
        r = np.sqrt(np.sum(x_scaled**2))
        radial_cos = np.cos(8.0 * r) * np.exp(-r**2)
        
        # Directional gradient modulation with angular dependence
        grad_mod = 1.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            grad_mod *= (1.0 + 0.4 * np.sin(5.0 * angle))
        
        # Multi-scale interaction terms with varying coupling strengths
        interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            interaction += np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j]) * np.cos(2.5 * x_scaled[k])
        
        # Cross-dimensional coupling with exponential weighting
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term += weight * np.sin(4.0 * (x_scaled[i] + x_scaled[j]))
        
        # Combine all components with dynamic weighting
        result = 0.7 * poly_term + 0.5 * radial_cos * grad_mod + 0.3 * interaction + 0.2 * cross_term
        
        return result