import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal recursive structure with self-similarity and chaotic components
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Multi-scale harmonic oscillations with fractal-like behavior and chaos
            scale_factor = 1.0 + 0.5 * np.sin(0.2 * i) * np.cos(0.1 * i**1.5)
            harmonic = (np.sin(scale_factor * xi) * np.cos(2 * xi) + 
                       0.3 * np.sin(3 * scale_factor * xi) * np.cos(4 * xi) + 
                       0.1 * np.sin(5 * scale_factor * xi) * np.sin(6 * xi) +
                       0.05 * np.sin(7 * scale_factor * xi**2) * np.cos(8 * xi**1.3))
            
            # Adaptive conditioning with dynamic scaling and chaotic modulation
            condition = 1.0 + 0.3 * np.abs(xi) * (1 + 0.2 * np.sin(0.1 * i)) * \
                       (1 + 0.1 * np.cos(0.05 * i**2))
            
            # Recursive fractal component with diminishing returns and chaotic coupling
            fractal_component = 0.0
            for k in range(1, min(6, self.dim - i + 1)):
                if i + k < self.dim:
                    fractal_component += (0.1 * np.sin(2**k * xi) * 
                                        np.cos(3**k * x[i+k]) * 
                                        np.exp(-0.1 * k) / (k**1.3)) + \
                                       (0.05 * np.sin(5**k * xi) * 
                                        np.cos(7**k * x[i+k]) * 
                                        np.sin(0.2 * k) / (k**1.7))
            
            # Add chaotic modulation to the fractal component
            chaos_mod = 0.05 * np.sin(10 * xi) * np.cos(15 * xi) * np.sin(0.3 * i)
            result += condition * harmonic + fractal_component + chaos_mod
            
        # Multi-scale cross-dimensional coupling with recursive structure and chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended scope for more complex coupling
                # Chaotic coupling strength based on dimension indices
                coupling_strength = (1 + 0.2 * np.sin(0.3 * (i + j))) * \
                                  (1 + 0.1 * np.cos(0.5 * i)) * \
                                  (1 + 0.1 * np.sin(0.4 * j)) * \
                                  (1 + 0.05 * np.sin(2 * i * j))
                
                # Fractal coupling with multi-scale interaction and chaotic modulation
                cross_coupling += coupling_strength * \
                                np.sin(x[i] * x[j]) * \
                                np.exp(-0.05 * (x[i]**2 + x[j]**2)) * \
                                (1 + 0.05 * np.sin(2 * (x[i] + x[j])) + 
                                 0.03 * np.cos(3 * (x[i] - x[j])))
        
        # Add multi-scale periodicity with varying frequencies and chaotic components
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency pattern with chaotic modulation
            freq = 1.0 + 0.5 * np.sin(0.1 * i) + 0.3 * np.sin(0.2 * i**2) + \
                   0.1 * np.cos(0.05 * i**3)
            periodicity += freq * np.sin(freq * xi) * np.cos(2 * freq * xi) + \
                          0.05 * np.sin(3 * freq * xi) * np.cos(4 * freq * xi)
            
        # Combine components with fractal weights and chaotic scaling
        result = 0.5 * result + 0.4 * cross_coupling + 0.3 * periodicity
        
        # Add penalty for distance from origin with fractal scaling and chaotic modulation
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal-like penalty with varying exponents and chaotic components
            exponent = 2.0 + 0.5 * np.sin(0.3 * i) + 0.2 * np.cos(0.1 * i**2)
            if xi >= 0:
                penalty += 0.1 * xi**exponent + 0.02 * np.sin(10 * xi) * np.cos(15 * xi)
            else:
                penalty += 0.15 * np.abs(xi)**(exponent + 0.5) + 0.03 * np.sin(8 * xi) * np.cos(12 * xi)
                
        # Add chaotic noise to the final result
        chaotic_noise = 0.05 * np.random.rand() * np.sin(np.sum(x)**2)
        
        result += penalty + chaotic_noise
        
        return result