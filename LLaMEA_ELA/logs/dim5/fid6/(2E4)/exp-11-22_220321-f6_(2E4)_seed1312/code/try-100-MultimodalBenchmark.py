import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        radial = 1.0 + 0.5 * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Trigonometric wave components in each dimension
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(4.0 * x[i]) + np.cos(3.0 * x[i])
            
        # Polynomial penalty terms with varying exponents
        poly_penalty = 0.0
        for i in range(self.dim):
            poly_penalty += (x[i]**4 + x[i]**6) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-dimensional interaction with angular dependencies
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                cross_interaction += np.sin(2.0 * angle) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Sine-based correlation structure
        correlation = 0.0
        for i in range(self.dim):
            correlation += np.sin(1.5 * x[i]) * np.cos(1.5 * x[i])
            
        # Asymmetric scaling based on dimension index
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i]**3) * (1 + 0.2 * np.sin(i))
            
        # Final combination with global modulation
        return radial * (trig_sum + 0.5 * poly_penalty + 0.3 * cross_interaction + 0.4 * correlation + 0.2 * asymmetry)