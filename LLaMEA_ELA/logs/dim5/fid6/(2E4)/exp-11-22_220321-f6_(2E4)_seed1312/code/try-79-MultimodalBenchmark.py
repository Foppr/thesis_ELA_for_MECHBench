import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.sigma = 1.5
        self.k = 3.0
        self.gamma = 0.7
        self.alpha = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function with chaotic modulation
        rb_func = 0.0
        for i in range(self.dim):
            # Add logistic map modulation for chaos
            chaos_factor = 4 * 0.5 * (1 - 0.5)  # Simplified chaotic base
            rb_func += np.exp(-self.sigma * (x[i] ** 2)) * (1 + 0.1 * np.sin(chaos_factor * x[i]))
            
        # Dynamic polynomial corrugation with adaptive exponents
        poly_corrugation = 0.0
        for i in range(self.dim):
            # Use dynamic exponents based on dimension
            exponent = 3 + (i % 4) + 0.5 * np.sin(0.5 * x[i])
            poly_corrugation += (x[i] ** exponent) * np.cos(self.k * x[i]) * np.exp(-0.1 * abs(x[i]))
            
        # Quaternion-inspired twist field with complex coupling
        twist_field = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex twist with sine and cosine interaction
                twist_field += np.sin(x[i] + x[j]) * np.cos(self.gamma * x[i] * x[j]) * \
                              np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive weighting based on dimension and values
                weight = 1.0 / (1 + np.exp(-0.5 * (x[i] - x[j])**2))
                cross_coupling += weight * (x[i]**2 + x[j]**2) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Asymmetric penalty with cubic and sigmoidal components
        penalty = 0.0
        for i in range(self.dim):
            # Combined penalty with dynamic scaling
            sig = 1 / (1 + np.exp(-x[i]))
            penalty += (sig - 0.5) ** 3 * np.exp(-0.2 * abs(x[i])) + \
                      self.alpha * np.sin(2 * x[i]) * np.cos(3 * x[i])
                      
        # Add a global scaling factor and combine components
        return 0.4 * rb_func + 0.3 * poly_corrugation + 0.2 * twist_field + 0.1 * cross_coupling + 0.5 * penalty