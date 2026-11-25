import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial chaos component with higher-order terms and nonlinearity
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_scaled[i]**5 + 0.7 * x_scaled[i]**4 - 0.4 * x_scaled[i]**3 + 0.2 * x_scaled[i]**2 - 0.1 * x_scaled[i])
        
        # Modified radial cosine oscillation with multiple frequencies and dynamic amplitude
        r = np.sqrt(np.sum(x_scaled**2))
        radial_cos = (np.cos(10.0 * r) + 0.5 * np.cos(20.0 * r)) * np.exp(-0.5 * r**2)
        
        # Enhanced directional gradient modulation with multiple angular dependencies
        grad_mod = 1.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            grad_mod *= (1.0 + 0.6 * np.sin(7.0 * angle) * np.cos(3.0 * angle))
        
        # Multi-scale interaction terms with varying coupling strengths and phase shifts
        interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            interaction += np.sin(4.0 * x_scaled[i] + 3.0 * x_scaled[j] + 1.5 * x_scaled[k]) * np.cos(3.5 * x_scaled[i])
        
        # Enhanced cross-dimensional coupling with adaptive weighting and additional harmonic terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term += weight * (np.sin(5.0 * (x_scaled[i] + x_scaled[j])) + 0.3 * np.cos(8.0 * (x_scaled[i] - x_scaled[j])))
        
        # Additional chaotic component for increased complexity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15.0 * x_scaled[i]) * np.cos(12.0 * x_scaled[(i+1) % self.dim])
        
        # Combine all components with optimized weighting
        result = 0.6 * poly_term + 0.4 * radial_cos * grad_mod + 0.25 * interaction + 0.15 * cross_term + 0.1 * chaotic
        
        return result