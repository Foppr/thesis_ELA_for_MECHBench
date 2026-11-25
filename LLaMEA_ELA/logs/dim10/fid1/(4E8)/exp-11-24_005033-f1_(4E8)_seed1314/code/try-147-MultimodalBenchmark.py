import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like structure with chaotic recursion
        for i in range(self.dim):
            xi = x[i]
            
            # Base fractal component with chaotic scaling
            base = np.sin(xi) * np.cos(2 * xi) + 0.5 * np.sin(3 * xi) + 0.1 * np.sin(7 * xi)
            
            # Multi-scale harmonic oscillations with chaotic frequencies
            scale_factor = 1.0
            harmonic_sum = 0.0
            for k in range(1, 8):  # Up to 7 scales for increased complexity
                scale_factor *= 0.45
                freq = k * (1 + 0.2 * np.sin(0.3 * i))
                harmonic_sum += scale_factor * np.sin(freq * xi) * np.cos(freq * xi)
            
            # Enhanced adaptive conditioning with chaotic modulation
            condition = 1.0 + 0.4 * np.sin(0.5 * i + 0.1 * xi) * np.abs(xi) + 0.2 * np.cos(0.2 * xi + 0.3 * i)
            
            # Asymmetric basin structure with chaotic scaling
            asymmetry = 0.4 * np.sin(xi**2) * np.cos(0.7 * xi) + 0.1 * np.sin(4 * xi) + 0.05 * np.sin(9 * xi)
            
            result += condition * (base + harmonic_sum) + asymmetry
            
        # Enhanced cross-dimensional coupling with chaotic strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength with fractal scaling
                coupling_strength = 0.5 * (1 + np.cos(0.3 * (i + j) + 0.2 * np.sin(i * j)))
                distance = np.abs(x[i] - x[j])
                coupling += coupling_strength * np.sin(distance + 0.1 * np.sin(i + j)) * np.exp(-0.3 * distance**2)
                
        # Add enhanced fractal periodicity component with chaotic phases
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal periodic terms with varying phase shifts
            term = 0.0
            for k in range(1, 8):
                phase_shift = 0.1 * np.sin(0.2 * i + k)
                term += np.sin(k * xi + phase_shift) * np.cos(k * xi + phase_shift) / (k**1.6)
            periodicity += term
            
        # Combine all components with chaotic weights
        result = 0.6 * result + 0.3 * coupling + 0.25 * periodicity
        
        # Enhanced fractal penalty term for distance from origin with chaotic exponents
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic penalty with varying exponents and phase shifts
            if xi >= 0:
                exponent = 2.5 + 0.4 * np.sin(0.3 * i + 0.1 * xi)
                penalty += 0.2 * xi**exponent
            else:
                exponent = 3.5 + 0.2 * np.cos(0.2 * i + 0.1 * xi)
                penalty += 0.25 * np.abs(xi)**exponent
                
        result += penalty
        
        # Add chaotic noise component for increased difficulty
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(13 * x[i] + 0.5 * np.cos(7 * i)) * np.cos(11 * x[i])
        result += noise
        
        # Final scaling with chaotic factor
        chaos_factor = 1.2 + 0.1 * np.sin(0.4 * sum(x))
        result *= chaos_factor
        
        return result