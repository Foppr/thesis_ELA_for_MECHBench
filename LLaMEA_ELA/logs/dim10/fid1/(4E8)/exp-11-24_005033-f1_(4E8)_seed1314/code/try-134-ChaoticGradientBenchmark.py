import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with time-varying parameters
        chaotic_factor = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Time-varying chaotic map (logistic-like)
            chaotic_value = self.a * xi * (1 - xi) + self.b * np.sin(self.c * i)
            chaotic_factor += chaotic_value**2
            
        # Multi-modal harmonic structure
        harmonic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Combine multiple sine/cosine waves with varying frequencies
            freqs = [1, 2, 3, 4, 5]
            wave_sum = 0.0
            for k, freq in enumerate(freqs):
                wave_sum += np.sin(freq * xi) * np.cos(freq * xi) * (k + 1)
            
            # Adaptive conditioning based on position and dimension
            condition = 1.0 + 0.3 * np.sin(0.2 * i) * np.abs(xi) + 0.1 * np.cos(0.1 * xi**2)
            
            harmonic_component += condition * wave_sum
            
        # Cross-dimensional coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength
                coupling_strength = 0.4 * (1 + np.sin(0.2 * (i + j)))
                distance = np.abs(x[i] - x[j])
                
                # Time-varying coupling with chaotic modulation
                coupling += coupling_strength * np.sin(distance) * np.exp(-0.2 * distance**2)
                
        # Asymmetric basin structure with fractal-like features
        asymmetry = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Fractal-like asymmetry with recursive structure
            asym_factor = 0.3 * np.sin(xi**2) * np.cos(0.5 * xi) + 0.1 * np.sin(3 * xi)
            asymmetry += asym_factor
            
        # Penalty term for distance from origin with chaotic scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Chaotic penalty with varying exponents
            exponent = 2.0 + 0.5 * np.sin(0.3 * i)
            if xi >= 0:
                penalty += 0.1 * xi**exponent
            else:
                penalty += 0.15 * np.abs(xi)**(exponent + 0.2)
                
        # Combine all components
        result = 0.7 * harmonic_component + 0.2 * coupling + 0.1 * asymmetry + 0.3 * chaotic_factor + penalty
        
        # Final scaling to ensure good fitness range
        result *= 1.5
        
        return result