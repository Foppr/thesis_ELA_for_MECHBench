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
            
            # Enhanced multi-scale harmonic oscillations with modified coefficients
            scale_factor = 1.0 + 0.7 * np.sin(0.25 * i)
            harmonic = 1.2 * np.sin(scale_factor * xi) * np.cos(2.5 * xi) + \
                      0.4 * np.sin(3.5 * scale_factor * xi) * np.cos(4.2 * xi) + \
                      0.15 * np.sin(5.3 * scale_factor * xi)
            
            # Enhanced adaptive conditioning with stronger position dependence
            condition = 1.0 + 0.4 * np.abs(xi) * (1 + 0.3 * np.sin(0.15 * i))
            
            # Enhanced recursive fractal component with stronger coupling
            fractal_component = 0.0
            for k in range(1, min(6, self.dim - i + 1)):
                if i + k < self.dim:
                    fractal_component += 0.15 * np.sin(2**(k+1) * xi) * np.cos(3**(k+1) * x[i+k]) / (k**1.7)
            
            result += condition * harmonic + fractal_component
            
        # Enhanced multi-scale cross-dimensional coupling with stronger interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling scope
                # Enhanced coupling strength with more complex pattern
                coupling_strength = (1 + 0.3 * np.sin(0.35 * (i + j))) * \
                                  (1 + 0.15 * np.cos(0.55 * i)) * \
                                  (1 + 0.15 * np.sin(0.45 * j))
                
                # Enhanced fractal coupling with stronger interaction
                cross_coupling += coupling_strength * \
                                np.sin(x[i] * x[j]) * \
                                np.exp(-0.07 * (x[i]**2 + x[j]**2)) * \
                                (1 + 0.08 * np.sin(2.5 * (x[i] + x[j])))
        
        # Enhanced multi-scale periodicity with increased complexity
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced fractal frequency pattern
            freq = 1.2 + 0.6 * np.sin(0.15 * i) + 0.4 * np.sin(0.25 * i**2)
            periodicity += freq * np.sin(freq * xi) * np.cos(2.5 * freq * xi)
            
        # Combine components with adjusted weights
        result = 0.7 * result + 0.4 * cross_coupling + 0.5 * periodicity
        
        # Enhanced penalty for distance from origin with modified fractal scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced fractal-like penalty with varying exponents
            exponent = 2.2 + 0.6 * np.sin(0.35 * i)
            if xi >= 0:
                penalty += 0.15 * xi**exponent
            else:
                penalty += 0.2 * np.abs(xi)**(exponent + 0.7)
                
        result += penalty
        
        return result