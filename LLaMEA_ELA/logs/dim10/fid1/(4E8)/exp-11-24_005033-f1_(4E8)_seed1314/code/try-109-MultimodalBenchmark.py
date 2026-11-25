import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal recursive structure with self-similarity and chaotic dynamics
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Multi-scale harmonic oscillations with chaotic sine-wave interactions
            scale_factor = 1.0 + 0.7 * np.sin(0.3 * i) * np.cos(0.2 * i**1.5)
            harmonic = (np.sin(scale_factor * xi) * np.cos(2 * xi) + 
                       0.4 * np.sin(3 * scale_factor * xi) * np.cos(4 * xi) + 
                       0.2 * np.sin(5 * scale_factor * xi) * np.cos(6 * xi) +
                       0.1 * np.sin(7 * scale_factor * xi) * np.cos(8 * xi))
            
            # Adaptive conditioning with dynamic exponent and chaotic scaling
            condition = 1.0 + 0.4 * np.abs(xi) * (1 + 0.3 * np.sin(0.2 * i)) * np.exp(-0.1 * np.abs(xi))
            
            # Recursive fractal component with exponential decay and chaotic coupling
            fractal_component = 0.0
            for k in range(1, min(6, self.dim - i + 1)):
                if i + k < self.dim:
                    fractal_component += (0.15 * np.sin(2**k * xi) * np.cos(3**k * x[i+k]) / 
                                        (k**1.7 * (1 + 0.1 * np.abs(xi))))
            
            result += condition * harmonic + fractal_component
            
        # Enhanced cross-dimensional coupling with dynamic chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended scope for more complex coupling
                # Dynamic coupling strength with chaotic modulation
                coupling_strength = (1 + 0.3 * np.sin(0.4 * (i + j))) * \
                                  (1 + 0.2 * np.cos(0.6 * i)) * \
                                  (1 + 0.2 * np.sin(0.5 * j)) * \
                                  np.exp(-0.03 * np.abs(i - j))
                
                # Fractal coupling with multi-scale interaction and chaotic modulation
                cross_coupling += coupling_strength * \
                                np.sin(x[i] * x[j]) * \
                                np.exp(-0.08 * (x[i]**2 + x[j]**2)) * \
                                (1 + 0.1 * np.sin(3 * (x[i] + x[j])) + 
                                 0.05 * np.cos(5 * (x[i] - x[j])))
        
        # Multi-scale periodicity with chaotic frequency modulation
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency pattern with recursive scaling
            freq = 1.0 + 0.6 * np.sin(0.15 * i) + 0.4 * np.sin(0.25 * i**2) + \
                   0.2 * np.sin(0.3 * i**3)
            periodicity += freq * np.sin(freq * xi) * np.cos(2 * freq * xi) * \
                          np.exp(-0.02 * np.abs(xi))
            
        # Combine components with chaotic weights
        result = 0.7 * result + 0.4 * cross_coupling + 0.5 * periodicity
        
        # Enhanced penalty for distance from origin with chaotic scaling and fractal exponents
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic-like penalty with varying fractal exponents
            exponent = 2.0 + 0.6 * np.sin(0.4 * i) + 0.3 * np.cos(0.3 * i**1.5)
            if xi >= 0:
                penalty += 0.2 * xi**exponent
            else:
                penalty += 0.25 * np.abs(xi)**(exponent + 0.7)
                
        result += penalty
        
        # Add chaotic noise term to increase multimodality
        chaos_noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaos_noise += 0.1 * np.sin(10 * xi) * np.cos(15 * xi) * \
                          np.exp(-0.05 * xi**2) * (1 + 0.1 * np.sin(0.5 * i))
        result += chaos_noise
        
        return result