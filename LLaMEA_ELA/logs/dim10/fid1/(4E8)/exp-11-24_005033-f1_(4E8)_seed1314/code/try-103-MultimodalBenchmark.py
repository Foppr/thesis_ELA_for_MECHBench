import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal recursive structure with self-similarity
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Multi-scale harmonic oscillations with fractal-like behavior
            scale_factor = 1.0 + 0.5 * np.sin(0.2 * i)
            harmonic = np.sin(scale_factor * xi) * np.cos(2 * xi) + \
                      0.3 * np.sin(3 * scale_factor * xi) * np.cos(4 * xi) + \
                      0.1 * np.sin(5 * scale_factor * xi)
            
            # Adaptive conditioning based on position and dimension
            condition = 1.0 + 0.3 * np.abs(xi) * (1 + 0.2 * np.sin(0.1 * i))
            
            # Recursive fractal component with diminishing returns
            fractal_component = 0.0
            for k in range(1, min(5, self.dim - i + 1)):
                if i + k < self.dim:
                    fractal_component += 0.1 * np.sin(2**k * xi) * np.cos(3**k * x[i+k]) / (k**1.5)
            
            result += condition * harmonic + fractal_component
            
        # Multi-scale cross-dimensional coupling with recursive structure
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited scope for computational efficiency
                # Recursive coupling strength based on dimension indices
                coupling_strength = (1 + 0.2 * np.sin(0.3 * (i + j))) * \
                                  (1 + 0.1 * np.cos(0.5 * i)) * \
                                  (1 + 0.1 * np.sin(0.4 * j))
                
                # Fractal coupling with multi-scale interaction
                cross_coupling += coupling_strength * \
                                np.sin(x[i] * x[j]) * \
                                np.exp(-0.05 * (x[i]**2 + x[j]**2)) * \
                                (1 + 0.05 * np.sin(2 * (x[i] + x[j])))
        
        # Add multi-scale periodicity with varying frequencies
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency pattern
            freq = 1.0 + 0.5 * np.sin(0.1 * i) + 0.3 * np.sin(0.2 * i**2)
            periodicity += freq * np.sin(freq * xi) * np.cos(2 * freq * xi)
            
        # Combine components with fractal weights
        result = 0.6 * result + 0.3 * cross_coupling + 0.4 * periodicity
        
        # Add penalty for distance from origin with fractal scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal-like penalty with varying exponents
            exponent = 2.0 + 0.5 * np.sin(0.3 * i)
            if xi >= 0:
                penalty += 0.1 * xi**exponent
            else:
                penalty += 0.15 * np.abs(xi)**(exponent + 0.5)
                
        result += penalty
        
        return result